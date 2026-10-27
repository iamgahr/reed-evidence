#!/usr/bin/env python3
"""Recompute every number in README.md from the per-task outcomes in data/, with the Python standard library only.

    python3 verify.py

Each row is one task (a real pull request). Each cell is 1 if that attempt passed all of the task's hidden checks,
and 0 otherwise. The comparisons are paired by task: McNemar's exact two-sided test on the discordant pairs, and a
Wald 95 % interval for the paired difference. The script exits 0 only if every recomputed count and p-value equals
the value our experiment readers reported when each experiment was read.
"""
import csv, math, sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
FAILED = []


def mcnemar(b, c):
    """Exact two-sided McNemar: the binomial(b + c, 1/2) tail at min(b, c), doubled, at most 1."""
    n = b + c
    return 1.0 if n == 0 else min(1.0, 2 * sum(math.comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)


def paired(rows, treated, control):
    pairs = [(int(r[treated]), int(r[control])) for r in rows]
    n = len(pairs)
    b = sum(1 for t, c in pairs if t and not c)
    c = sum(1 for t, c in pairs if c and not t)
    d = (b - c) / n
    se = math.sqrt(max(b + c - (b - c) ** 2 / n, 0.0)) / n
    return {"n": n, "treated": sum(t for t, _ in pairs), "control": sum(c for _, c in pairs), "gained": b, "lost": c,
            "d": d, "lo": d - 1.96 * se, "hi": d + 1.96 * se, "p": mcnemar(b, c)}


def check(label, got, want, rel=False):
    ok = abs(got / want - 1.0) <= 0.001 if rel else got == want
    if not ok:
        FAILED.append(label)
    print(f"    {'ok ' if ok else 'BAD'} {label}: {got:.4g} (reported {want})" if rel else f"    {'ok ' if ok else 'BAD'} {label}: {got} (reported {want})")


def load(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


def show(title, r):
    print(f"  {title}\n    {r['control'] / r['n']:.1%} -> {r['treated'] / r['n']:.1%} of {r['n']} tasks: {r['d'] * 100:+.1f} points "
          f"[95 % CI {r['lo'] * 100:+.1f}, {r['hi'] * 100:+.1f}], {r['gained']} gained / {r['lost']} lost, McNemar exact p {r['p']:.2g}")


rows = load("e180b_outcomes.csv")
print("E180b and E180: with the record vs. without, all hidden checks passed (paired by task)")
for title, model, want in [
    ("gpt-6-astra in our agent harness (E180b; internally pre-registered primary)", "gpt_6_astra", dict(n=638, treated=437, control=257, gained=192, lost=12, p=6.466e-43)),
    ("claude-fable-5-1 in our agent harness (E180; this comparison computed after the run)", "claude_fable_5_1", dict(n=638, treated=459, control=270, gained=202, lost=13, p=9.438e-45)),
]:
    r = paired(rows, model + "_with_record", model + "_without_record")
    show(title, r)
    for k in ("n", "treated", "control", "gained", "lost"):
        check(k, r[k], want[k])
    check("McNemar p", r["p"], want["p"], rel=True)

rows = load("e181_outcomes.csv")
print("\nE181: claude-fable-5-1 in our agent harness; examples shown to the agent (paired by task)")
for title, (t, c), want in [
    ("examples written by a model from the task description alone vs. no examples", ("examples_written_from_description", "no_examples"), dict(n=375, gained=16, lost=23, p=0.3368)),
    ("examples from the record vs. examples written from the task description", ("examples_from_record", "examples_written_from_description"), dict(n=375, gained=109, lost=7, p=1.198e-24)),
    ("examples from the record vs. no examples", ("examples_from_record", "no_examples"), dict(n=375, gained=None, lost=None, p=None)),
]:
    r = paired(rows, t, c)
    show(title, r)
    for k in ("n", "gained", "lost"):
        if want[k] is not None:
            check(k, r[k], want[k])
    if want["p"] is not None:
        check("McNemar p", r["p"], want["p"], rel=True)

print("\nALL RECOMPUTED NUMBERS MATCH" if not FAILED else f"\nMISMATCH: {FAILED}")
sys.exit(1 if FAILED else 0)
