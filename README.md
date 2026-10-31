# Reed: evidence for one result on coding agents

**New here?** Start with [What is Reed? Explained simply](WHAT-IS-REED.md). [This repository, explained simply](EVIDENCE-EXPLAINED.md) covers what each file is and how to check the results yourself.

**The result:**
- **gpt-6-astra (OpenAI), run in our agent harness on 638 real pull requests,** passes all of a task's hidden checks on **68.5 %** of tasks when given Reed's behaviour record of the change. Without it, the figure is **40.3 %**.
  - That is **+28.2 points** (95 % CI +24.4 to +32.0; paired McNemar exact p 6.5 × 10⁻⁴³).
  - This was the experiment's internally pre-registered primary test.
- **claude-fable-5-1 (Anthropic),** in the same harness, on the same tasks and checks: **42.3 % → 71.9 %**, +29.6 points (95 % CI +25.7 to +33.5).
- **Examples written by a model from the task description alone did not help:** −1.9 points (95 % CI −5.1 to +1.4), on 375 of these tasks (pre-registered). Examples drawn from the record did help: +27.2 points over the description-written ones.

**"Hidden"** means the agent never saw those checks. The examples shown to the agent never include them.

Every number in the results table is recomputed from the per-task outcomes in `data/` by `python3 verify.py`, which uses only the Python standard library. The stricter whole-task scores in the notes come from our records and are not in `data/`.

## Results

| experiment | agent (in our harness) | tasks | comparison | result | status |
|---|---|---|---|---|---|
| E180b | gpt-6-astra | 638 | with the record vs. without | **40.3 % → 68.5 %**, +28.2 pts [+24.4, +32.0]; 192 tasks gained, 12 lost; p 6.5e-43 | internally pre-registered primary (bar: ≥ +10 pts at p < 0.01; prediction +20) |
| E180 | claude-fable-5-1 | the same 638 | the same | **42.3 % → 71.9 %**, +29.6 pts [+25.7, +33.5]; 202 gained, 13 lost; p 9.4e-45 | this comparison was computed after the run (see the notes) |
| E181 | claude-fable-5-1 | 375 of the 638 | examples written from the task description vs. none | **−1.9 pts** [−5.1, +1.4]; 16 gained, 23 lost; p 0.34 | internally pre-registered; this test failed its bar |
| E181 | claude-fable-5-1 | 375 | examples from the record vs. examples written from the task description | **+27.2 pts** [+22.3, +32.1]; 109 gained, 7 lost; p 1.2e-24 | internally pre-registered |
| E181 | claude-fable-5-1 | 375 | examples from the record vs. none | **+25.3 pts** [+20.5, +30.2]; 102 gained, 7 lost | derived from the same arms, not a separate registered test |

**Notes:**
- **Order:** E180 (Anthropic's agent) came first. Its registered measure was a stricter whole-task score: 27.6 % → 63.0 %. The hidden-check comparison above was computed from the same attempts after its read. E180b was then registered, as a test of whether the effect holds for another vendor's agent, before any of its attempts ran. On the stricter score, gpt-6-astra went from 30.1 % to 61.6 %.
- **E181's 375 tasks** are every task of the 638 that met its pre-registered eligibility rule.
- **The examples drawn from the record** come from the same behaviour record as the hidden checks, but never include them. So E181 shows that the record's executed behaviour helps where a description of the task does not. It does not separate that from "examples close to the checks help".
- **Each task got one attempt per condition.** Intervals are Wald 95 % intervals for a paired difference.
- **Not claimed:** generality beyond these agents, harness and tasks; anything about training; novelty.

## Verify
```
python3 verify.py   # prints each recomputed number and exits 0 only if all match the values our readers reported
```
- `data/e180b_outcomes.csv` has one row per task. Each cell is 1 if that attempt passed all hidden checks, else 0, for each agent with and without the record.
- `data/e181_outcomes.csv` has the same for the three E181 conditions.
- **Task identities are withheld.** Each task appears only as a salted SHA-256 commitment with its own secret salt. A single task can therefore be opened later without exposing the others. See `COMMITMENTS.md`.

## What is withheld
This repository shows results, not methods. It does not contain:
- how behaviour records are built, represented or shown to an agent;
- the harness, tools or prompts;
- the task list, the environments, or the hidden checks themselves;
- the code.

**The limit on "pre-registered":** the pre-registration documents and result write-ups are committed to by hash in `COMMITMENTS.md`. The hashes fix their content, but their registration times come from our own version history and are not externally timestamped. That makes the label "internally pre-registered".

**An audit we can offer, under an appropriate agreement:**
- a public randomness beacon picks a sample of tasks;
- we open those tasks' identities, their hidden checks and both conditions' patches;
- the reviewer re-grades them independently.
