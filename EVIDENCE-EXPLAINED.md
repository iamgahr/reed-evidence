# This repository, explained simply

This page covers three things:
- what each file here is;
- what the words in the [README](README.md) mean;
- how you can check every number yourself, in about a minute.

For what Reed is, see [WHAT-IS-REED.md](WHAT-IS-REED.md).

## What's in this folder

| file | what it is |
|---|---|
| `README.md` | the results, with exact numbers |
| `WHAT-IS-REED.md` | what Reed is and how the experiments work, in plain words |
| `EVIDENCE-EXPLAINED.md` | this page |
| `data/e180b_outcomes.csv` | a spreadsheet with one row per task (638 rows). For each AI agent, with and without the record: **1** means the attempt passed every hidden check, **0** means it did not |
| `data/e181_outcomes.csv` | the same for the 375 tasks of the examples experiment, with three conditions |
| `verify.py` | a small program that recomputes the README's results table from the two spreadsheets |
| `COMMITMENTS.md` | fingerprints that lock in the private documents and the task names, without revealing them |

## Check it yourself

1. Download this repository: the green **Code** button, then **Download ZIP**, or `git clone`.
2. With Python 3 installed, open a terminal in the folder and run `python3 verify.py`.
3. It recomputes each result in the README's table and checks it against the value our analysis reported, which is written into the script. It ends with `ALL RECOMPUTED NUMBERS MATCH`.

The program uses only tools built into Python, so there is nothing to install and nothing hidden. You don't have to trust our summary: the program counts the 1s and 0s itself.

## The words in the README

**Task.** One real change to a real project, which the AI agent has to make.

**Hidden checks.** Like exam questions the student never saw. The agent never sees them while it works; they are used only to grade it.

**With the record / without the record.** Whether the agent could use part of Reed's behaviour record while it worked. The tasks, the agent and the hidden checks were the same.

**Paired.** The same tasks were attempted under both conditions, so the comparison is task by task, like with like.

**+28.2 points.** Percentage points: the plain difference between 68.5 % and 40.3 %.

**192 gained, 12 lost.**
- 192 tasks went from fail to pass with the record.
- 12 went from pass to fail.
- The rest came out the same both ways.

**95 % CI (confidence interval), e.g. +24.4 to +32.0.** The range the true improvement very likely lies in, allowing for the luck of which tasks happened to pass.

**p-value (McNemar exact test), e.g. 6.5 × 10⁻⁴³.** How surprising the result would be if the record made no difference at all.
- Of the 638 tasks, 204 changed between the two conditions.
- If the record did nothing, each of them would be as likely to go one way as the other, like a coin toss.
- Seeing 192 go one way and only 12 the other is like tossing a fair coin 204 times and getting 192 heads. That practically never happens.

**Pre-registered.** Before running the experiment, we wrote down what we would measure and what result would count as success. A few dated amendments followed, all before the results were read. It is like calling your shot before you take it. That stops anyone, including us, from picking whatever looks best afterwards.
- For OpenAI's agent the pass mark was at least +10 points, at p < 0.01. Our prediction was +20. The result was +28.2.
- We say "internally" pre-registered because the dates come from our own records, not from a public notary. `COMMITMENTS.md` holds the fingerprints of those documents.

**"Computed after the run."** For Anthropic's agent, this comparison was not the one written down in advance. It was calculated afterwards from the same attempts. That is why we then ran OpenAI's agent as a test written down in advance. It came out almost the same.

**Salted SHA-256 commitment.** Think of a sealed envelope with a fingerprint on the outside.
- SHA-256 turns any text into a long fingerprint. Change one letter and the fingerprint changes completely, and you can't work backwards from the fingerprint to the text.
- We publish the fingerprint now, so we can't swap the envelope's contents later.
- The **salt** is a secret random addition, different for every task. So nobody can find a task's name by guessing candidates, and opening one envelope reveals only that one task.

**Withheld.** The task list, how records are built, the tools and prompts, and the code. The results are public; the method is private.

## Why you can trust it, and how to go further

- **The raw outcomes are here.** Every task's 1s and 0s are in `data/`, and `verify.py` recomputes the results table from them. The stricter whole-task scores in the README's notes come from our records and are not in `data/`.
- **The main tests were fixed in advance.** They were written down before running, with a pass mark, and the documents are locked by fingerprint in `COMMITMENTS.md`.
- **An independent audit is on offer.**
  - A public source of randomness picks a sample of tasks.
  - We open those tasks: their names, their hidden checks, and the changes made in both conditions.
  - An outside reviewer re-grades them independently.
  - The [README](README.md) has the details.
