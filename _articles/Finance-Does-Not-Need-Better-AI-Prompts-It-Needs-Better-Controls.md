---
layout: post
title: "The Iceberg Under the Prompt: AI Controls That Actually Matter for Finance"
authors: [Adit Shukla]
tags: [AI Enablement, Finance, Generative AI, Governance]
background_image: /assets/images/posts/Finance-AI-Controls.png
subtitle: "The prompt is only the visible part. Context, iteration, validation, and human judgment determine whether the work holds up."
date: 2026-07-15
permalink: /articles/The-Iceberg-Under-the-Prompt/
redirect_from:
  - /articles/Finance-Does-Not-Need-Better-AI-Prompts-It-Needs-Better-Controls/
---

Give an AI tool a budget-versus-actual workbook and ask it to explain the largest variances. Within seconds, it can produce something that looks remarkably close to an executive-ready finance summary.

Now ask yourself three questions:

- Did it use the right month?
- Did its numbers reconcile to the workbook?
- Did it find evidence for the explanations, or did it simply invent plausible reasons?

**If you cannot answer those questions, you do not have an analysis. You have a convincing draft.**

That distinction matters because language models are unusually good at sounding finished. A missing input does not always produce a visible blank. An unsupported conclusion does not arrive highlighted in red. The tool will often try to complete the assignment with whatever context it has.

Finance professionals have seen this problem before. It is why we reconcile accounts, separate preparers from reviewers, document assumptions, investigate exceptions, and require approval before consequential actions.

We tend to discuss AI mistakes as prompting problems. Many of them are really management and control problems. Four habits make the difference.

#### 1. Start With Why, Not Just What

*Analyze this workbook* is a task, but it is not much of an assignment.

Before the tool begins, you should be able to answer:

- What should the analysis help someone understand?
- Who is reading it?
- What decision will they make?
- Which period matters?
- What counts as material?
- Which sources are authoritative?

**Task-only prompt:**

> Analyze this budget-versus-actual workbook.

**Decision-oriented prompt:**

> Prepare the CFO to decide whether June expense variances require corrective action. Use the approved budget-versus-actual workbook. Treat variances above $100,000 as material. Separate what the workbook shows from your interpretation, and identify any missing explanations.

The second version is not better because it contains special prompting language. It is better because it explains **why the work exists**.

The first prompt gives the tool a *what*: analyze the workbook. The second gives it a *why*: help the CFO decide whether corrective action is needed. Once the why is clear, the tool can make better choices about relevance, materiality, evidence, and format. If you provide only the what, it has to fill in the why with assumptions.

**But won't this take longer?**

That was my first reaction. If every assignment requires a long, carefully engineered prompt, the process starts to sound like more work than it saves.

The good news is that you do not have to write the entire prompt yourself. Start with what you know, especially the purpose of the work, and let the conversation expose the rest:

1. State what you need and why you need it.
2. Ask the tool what context, sources, or success criteria are missing.
3. Answer its questions and correct any assumptions.
4. Ask it to restate the assignment before it begins.

In practice, we rarely know everything the AI needs when we begin. That is fine. *Instead of trying to write a perfect prompt, ask the tool to help expose what is missing.*

**Interview prompt:**

> Do not perform the analysis yet. Ask me what you need to know about the audience, decision, reporting period, materiality, approved sources, and required output. Then restate the assignment before beginning.

This changes prompting from a writing exercise into a briefing process. **Let the tool participate in shaping the brief, but do not let it quietly decide what the brief means.**

Yes, this takes longer than typing one sentence and pressing Enter. The relevant question is whether the *whole assignment* takes longer. A few rounds of briefing can still be much faster than doing the analysis manually, and they are usually faster than untangling a polished answer to the wrong question.

**Choose your poison: spend a little longer explaining the work up front, or spend much longer checking, correcting, and rebuilding it later.**

#### 2. Make Failure Visible

Imagine giving an AI tool five departmental files and asking it to prepare a consolidated report. Four departments are represented. Marketing is missing.

The impressive result is not a completed five-department report. The impressive result is for the tool to stop and say that it cannot complete the assignment.

That behavior does not happen reliably because we asked it to *be accurate*. We have to define what should be checked and what should happen when a check fails.

For finance work, that often means instructions such as:

- Confirm the reporting period and version before analyzing anything.
- Reconcile totals to the source.
- Identify the supporting source for material conclusions.
- Separate facts, management explanations, assumptions, and inferences.
- Do not fill gaps with estimated or invented information.
- Stop and report an exception if a required input is missing.

These are not all the same kind of instruction:

- **Writing constraint:** *Keep the summary under 200 words.* This shapes the output.
- **Control:** *Reconcile the total to the source workbook.* This tests the output.
- **Permission boundary:** *Do not load the file into the system without approval.* This limits the tool's authority.
- **Stop condition:** *If the reconciliation fails, stop.* This determines whether the work proceeds.

That may sound like semantics, but the differences become important as AI moves beyond writing text and begins using spreadsheets, systems, and other tools. A writing preference is not a control. A control is not a permission boundary. None of them matter much if a failed check can be ignored.

**Ask it to check its work. Then check it yourself.**

AI can be instructed to reconcile a total, list its assumptions, trace a conclusion to a source, or critique its own answer. Those inline checks are useful, and we should ask for them. But they are not a substitute for independent human review. The same tool that produced an answer can carry the same misunderstood instruction, missing context, or unsupported assumption into its review of that answer.

Before relying on an AI-assisted finance output, a person should still:

- Confirm that the correct source, period, version, entity, and department were used.
- Spot-check calculations against the underlying data.
- Trace material conclusions back to actual evidence.
- Challenge assumptions and investigate missing inputs.
- Decide whether the result is appropriate for its intended use.

Validation is also feedback on the assignment itself. If the tool selected the wrong month, ignored a material exception, or answered a different question than the one you intended, ask what the brief failed to establish. The problem may not be the wording of one instruction. It may be that the purpose, source hierarchy, materiality threshold, or definition of success was never made clear.

**Inline validation is a useful control aid, not approval or accountability. Your goal is not to prevent every error; it is to make important errors easier to detect before someone acts on them.**

#### 3. Know When to Throw the Conversation Away

AI conversations accumulate context. That is usually helpful until it is not.

If the wrong reporting period enters the discussion, later answers may continue building on it. If the tool misunderstands the assignment and then performs several calculations, creates a spreadsheet, and writes a summary, each new step makes the original mistake more expensive to unwind.

People often respond by adding more corrections:

> - Ignore the earlier month.
> - Use the revised file instead.
> - Do not use the assumption from the first analysis.
> - Keep the format, but change the audience and objective.

Eventually, the conversation contains the original assignment, several abandoned versions, and a collection of instructions explaining which instructions no longer apply.

At that point, starting over is usually faster.

It is useful to separate two kinds of conversations:

- **Exploration conversation:** Brainstorm, challenge assumptions, identify missing information, and develop the assignment. Keep this work mostly textual and inexpensive.
- **Execution conversation:** Once the brief is stable, move a clean, self-contained prompt and the approved source material into a fresh conversation. Generate the analysis or artifact there, then run a deliberate review.

Continue an existing conversation when the objective and sources remain sound. Start fresh when:

- The audience or objective changes.
- A foundational assumption was wrong.
- The wrong source, version, or reporting period entered the work.
- Corrections are beginning to pile up.

**A new conversation is cheap. A polished artifact built on contaminated context is not.**

#### 4. Manage the Workflow, Not Just the Prompt

A good prompt can improve one person's output. It does not create a dependable finance process.

The larger opportunity is to decide where AI belongs in the work:

- Where can it reduce manual effort?
- Which sources may it use?
- What must it reconcile?
- When should it stop?
- What still requires human judgment?
- Who approves the result?
- How will you know whether the new approach is actually faster or better?

Those questions are less exciting than a dramatic AI demo. They are also where most of the value will be won or lost.

The most promising use cases are often ordinary, recurring activities:

- Drafting variance commentary.
- Reviewing data quality.
- Preparing reconciliations.
- Organizing forecast inputs.
- Performing a first pass through supporting documents.

These processes have identifiable inputs, reviewers, exceptions, and measures of quality. Turn one into a dependable workflow and you should be able to point to concrete operating assets:

- A reusable assignment brief built around the decision.
- An approved-source list with clear period, version, entity, and scope rules.
- A validation checklist covering reconciliations, evidence, and materiality.
- An exception report that makes missing inputs and failed checks visible.
- A named human reviewer and an explicit approval boundary.
- Measures for total cycle time, rework, accuracy, and decision usefulness.

That is the difference between a prompt that happens to work and a process the finance team can run repeatedly.

Finance teams already know how to manage work where accuracy matters. We do not need to abandon that discipline to use AI. We need to extend it: brief the work around the decision, define the checks before execution, limit what the tool can do without approval, and make failure visible.

**The teams that do this well will get more than better AI-generated content. They will build faster, more reliable ways of working—and they will know whether the speed advantage survives the full assignment.**

If your team has recurring finance work that consumes time but cannot tolerate unchecked output, treat it as a workflow-design problem rather than a prompt-writing exercise. SLKone works with finance and leadership teams to define the decision, map the sources, build the controls, implement the workflow, and measure whether it reduces cycle time and rework without weakening decision quality. [Discuss the workflow with SLKone](/contact).
