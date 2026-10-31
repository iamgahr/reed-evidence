# What is Reed? Explained simply

This page explains Reed in plain words:
- what problem it works on;
- what we built;
- how one experiment works, step by step;
- what we found.

You don't need any background in programming or AI. Every result in the main table can be re-checked by anyone in about a minute; [EVIDENCE-EXPLAINED.md](EVIDENCE-EXPLAINED.md) shows how.

## The short version

Reed runs a piece of software before and after someone changes it, and writes down what it actually *does*. We call that a **behaviour record**. We use the record to judge whether a change does the right thing, even when nobody wrote a test for it.

In our experiments, AI coding agents were given part of the record of a real change, and then graded on the rest, which they never saw. With the record, they got those unseen parts right far more often. On the same 638 real tasks:
- an agent built on OpenAI's model went from **40.3 %** of tasks to **68.5 %**;
- an agent built on Anthropic's model went from **42.3 %** to **71.9 %**.

**The honest catch, up front.** The record in these experiments comes from the real, finished change, so it carries information about the right answer.
- **What the results show:** recorded behaviour is information an agent can act on, measured only on parts it never saw.
- **What they don't show yet:** how much it helps in everyday work, where the finished change doesn't exist yet.

## A few words first

- **Code:** the written instructions that make a program work. A project's **codebase** is all of its code together.
- **A change (a "pull request"):** a programmer edits the code to fix a problem or add something new, and submits the edit for the project to review. When the project accepts it, the change is **merged**.
- **A test:** a small extra program that checks one thing the code should do. For example: "adding 2 and 2 gives 4".
- **An AI coding agent:** a program built on a large AI model that can read code, run commands and edit files, a bit like a junior programmer. You give it a task, like "fix this bug", and it tries to make the change.
- **Percentage points:** the plain difference between two percentages. Going from 40 % to 68 % is +28 percentage points.

## The problem

Today, people mostly check that code works by writing tests. Tests have two weak spots.

1. **A test only checks what someone thought to write down.** A change can pass every test and still do the wrong thing in a case nobody tested.
2. **Many changes come with no new test.** None of the 638 real changes in these experiments came with a new or updated test. So no test was ever written to check what they changed.

This matters more every month, because AI agents now write a growing share of the world's code. To trust that code, you need a reliable way to say "this change does what it was meant to do", even when no test exists.

## The idea: write down what the code actually does

Think of the difference between a **checklist** and a **recording**.
- A test is like a checklist. It holds the few things someone remembered to check.
- A behaviour record is like a recording. We actually run the code and write down what it does, before a change and after it.

**A tiny made-up example.** A calculator rounds 2.5 down to 2. A programmer changes the rounding rule, and now it gives 3. The record writes that down: before the change, 2.5 gave 2, and after it, 2.5 gives 3. It also shows what should *not* have changed: 1.2 still gives 1.

A real record is much bigger than this. It comes from running the real project's code, not from anyone's description of it. That is the point: what code *does* is a fact you can check, while a description is only someone's idea of what it does.

## How one experiment works, step by step

1. **Pick a real change.** We start from a real change that was merged into a real open-source project.
2. **Rebuild the project.** We take the project's whole codebase as it stood just before the change, and rebuild it as closely as we can so it runs again. This is much harder than it sounds: real projects rely on hundreds of other software packages, and those keep changing.
3. **Keep it fair.** The agent works offline, so it can't look the change up.
   - It may still have seen some of these public projects during its own training. But that applies equally to both tries in step 7, so it can't explain the difference between them.
4. **Make the behaviour record.** We run the code before and after the real change, and record what it does.
5. **Keep part of the record hidden.** Some of the record can be given to the agent. The rest is kept back as the exam. The agent never sees that hidden part.
6. **Give an AI agent the task.** The agent gets a written description of what to do, and makes its own change.
7. **Try it both ways.** The agent attempts the same task twice: once without the record, and once with part of the record available. Each condition gets one attempt.
8. **Grade it on the hidden part.** We check whether the agent's change makes the code behave the way the real change did, on the part of the record it never saw. A task counts as passed only if *every* hidden check passes.
9. **Repeat for hundreds of tasks, with the pass mark fixed first.** For the main tests, we wrote down the measurement and the pass mark in advance. A few dated amendments followed, all before the results were read. [EVIDENCE-EXPLAINED.md](EVIDENCE-EXPLAINED.md) explains this "pre-registration".

Doing steps 2 to 5 reliably, for many real projects, is the hard part of the work. How we do it stays private.

## What we found

### 1. Agents get far more right with the record

On 638 real tasks, the share of tasks where the agent passed every hidden check:

| AI agent (the company's model, run in our agent setup) | without the record | with the record | change | tasks that flipped |
|---|---|---|---|---|
| OpenAI's gpt-6-astra | 40.3 % | **68.5 %** | **+28.2 percentage points** | 192 fail → pass, 12 pass → fail |
| Anthropic's claude-fable-5-1 | 42.3 % | **71.9 %** | **+29.6 percentage points** | 202 fail → pass, 13 pass → fail |

**In plain words:** with the record, both agents solved about 7 in 10 of these real tasks instead of about 4 in 10. For every task the record made worse, it fixed about 16.

If the record made no difference at all, a gap this big would almost never happen by chance. For OpenAI's agent, the odds are smaller than 1 in 10⁴².

**How the two tests relate.** Anthropic's agent ran first, and this comparison was calculated afterwards from its attempts. To check that the effect was real, we then wrote down a test for OpenAI's agent in advance, before any of its attempts ran. It came out almost the same.

### 2. Two different companies' models gained almost the same

The two agents gained +29.6 and +28.2 percentage points. So the gain is not peculiar to one of these two agents.

### 3. Real recorded behaviour beats guessing

This test used Anthropic's agent only, on 375 of the tasks. It compared two kinds of examples.
- **Examples written by an AI from the task description alone.** These did not help: **−1.9 percentage points**, within the range of chance. We had registered the hope that they would help, and that test failed its pass mark.
- **Examples taken from the record.**
  - **+27.2 percentage points** over the description-written ones. This test was written down in advance.
  - **+25.3** over no examples. This one was worked out from the same runs and is not a separate registered test.

**In plain words:** guessing what the code should do, from words alone, didn't help. Real recorded behaviour did.

**An honest note.** The record's examples and the hidden checks come from the same recording, although never the same checks. So we can't tell how much of the help comes from the examples simply being close to what gets tested.

### 4. A stricter score shows the same thing

Here a task counts only if the agent's change matches the whole record and passes some basic quality checks. The whole record means the parts the agent saw and the parts it didn't.
- Anthropic's agent went from **27.6 % to 63.0 %**.
- OpenAI's went from **30.1 % to 61.6 %**.

These two numbers come from our own records. They are not in the data files here, so `verify.py` does not recompute them.

## Why this matters

- **Judging code that has no tests.** Every result on this page was graded by the behaviour record, on changes that came with no new tests.
- **Information agents can use.** Real recorded behaviour helped agents far more than a description of the task did.

## What these results do not show

- **Everyday use.** The record here comes from the real, finished change. In everyday work the finished change doesn't exist yet, and these results don't measure how much records help there.
- **Every valid answer.** Grading by "behaves like the real change" can mark a different but equally valid solution as wrong. That strictness applies equally with and without the record.
- **Other settings.** The results cover only these agents, this setup and these tasks. We don't claim they hold everywhere.
- **Training AI.** Nothing here tests it.
- **Novelty.** Others have studied checking code by its behaviour. What we offer here are measurements.

## What we keep private, and why

This page explains the idea and the results. As the [README](README.md) says, it leaves out:
- how records are built or given to an agent;
- the harness, tools and prompts;
- which projects and tasks were used;
- the code.

Those are the hard-won parts of the work. The results are public, and anyone can re-check the main ones with the files here.

For a deeper independent check, we offer an audit: an outside reviewer re-grades a randomly chosen sample of tasks. The README explains how it works.
