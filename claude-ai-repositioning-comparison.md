# Comparison: `claude/ai-repositioning-pages`

## Executive Take

Do not merge this branch as-is.

Rachit/Claude's branch has useful strategy work and several reusable implementation ideas, but it conflicts with the latest positioning decisions in important ways:

- It makes a paid business value assessment the public front door and primary CTA.
- It does not rename `GenAI Readiness`; the page still leads with GenAI, LLM deployment, and chatbot development.
- It underplays Bridge as owned proof.
- It mixes marketing/content changes with Ruby/Gemfile build changes.
- It spreads broad copy rewrites across 77 files before the core positioning is settled.

The right move is to cherry-pick ideas, not merge the branch wholesale.

## What The Branch Gets Right

### 1. Business-First AI Framing

The strongest part of the branch is the internal positioning line:

> "We are a business firm that uses AI, not an AI firm."

That is directionally useful. It prevents the site from sounding like an AI vendor and keeps operations, finance, revenue, cost, and implementation at the center.

The branch also introduces a strong AI copy test:

- name the business outcome;
- name the operating mechanism;
- name proof or soften the claim;
- say what the client owns afterward;
- be honest where judgment beats the model.

This is worth keeping. It is probably the most useful artifact in the branch.

### 2. It Protects Vendor Neutrality

The branch repeatedly says SLKone is vendor- and model-neutral. That fits the market position better than sounding tied to any one model, vendor, or AI stack.

Useful language:

> "We pick the right tool for the problem, build one when it helps, or recommend none."

That should survive into the final site copy.

### 3. It Emphasizes Ownership

The branch does a good job saying clients own what SLKone builds:

- model;
- dashboard;
- workflow;
- process;
- playbook;
- operating cadence;
- know-how.

This matters because it differentiates SLKone from both strategy-only consultants and software vendors.

### 4. The "How We Work" Page Is Directionally Strong

The new `how-we-work.md` page is worth adapting.

What works:

- small embedded team;
- same people from start to finish;
- no deck-and-leave model;
- practical build capacity;
- client keeps the tools and routines.

What needs revision:

- It currently points back to Business Value Assessment as the default public step.
- It should include Bridge as owned proof of how SLKone has changed its own delivery model.
- It should better cover decision support, not only execution after strategy.

### 5. The Proof Include Is Useful

The new `_includes/proof-cases.html` and layout hooks are useful because they let service and industry pages surface relevant case studies directly.

This aligns with the workshop theme: the pitch needs proof.

However, the implementation is basic. It matches case studies by path substring and only renders existing case cards. It is a good starting point, but not a full proof system.

## Main Conflicts With Current Direction

### 1. Business Value Assessment Is Viable, But Needs Better Placement

The branch creates `business-value-assessment.md`, adds it to the main nav CTA, and routes many page CTAs to it.

Examples:

- `_data/header-navigation.yml` adds `Business Value Assessment` as the header CTA.
- `_data/homepage.yml` points the hero CTA to `/business-value-assessment`.
- `business-value-assessment.md` publicly describes the assessment and says the fee is credited toward the engagement.

The page itself is useful and may be worth keeping as a public cold lead-gen opportunity. The issue is not that it exists. The issue is whether it becomes the dominant first impression before the broader SLKone positioning is clear.

Better distinction:

> Business Value Assessment can be a public lead-gen page and a sendable sales page, but it should support the firm positioning rather than replace it.

Recommendation:

- Keep and adapt `business-value-assessment.md`.
- It can be public and indexable if the team wants a cold lead-gen path.
- Consider using it as a secondary CTA rather than the only homepage hero CTA.
- If it appears in top nav, label and route it carefully so it reads as a useful entry point, not the whole offer.
- Pair it with sales collateral: one-pager, deck module, proposal language, and post-call follow-up.
- Public CTAs can mix direct and softer prompts: "Start with a Business Value Assessment," "Talk to SLKone," "Discuss a business priority," "See relevant proof."

### 2. GenAI Readiness Is Not Actually Fixed

The branch keeps the page title as `GenAI Readiness` and keeps focus areas such as:

- GenAI Training
- LLM Deployment
- Chatbot Development
- GenAI Strategy Development
- Use Case Identification

This directly conflicts with the current direction:

> GenAI Readiness absolutely needs to be renamed.

Recommendation:

- Rename visible title to `AI Enablement`.
- Keep the existing URL temporarily if link stability matters, but change the page title, card title, metadata, and page copy now.
- Replace the current focus areas with:
  - Workflow Selection and Value Sizing
  - AI Governance and Controls
  - MCP Tooling and System Integrations
  - Skills and Agent Automation
  - Use-Case Testing
  - Build / Buy / Route Decisions

### 3. Bridge Is Missing As Proof

The branch talks about build capability, ownership, and internal capacity, but it does not use Bridge as a proof point.

That leaves a major proof asset on the table.

Current direction:

> Bridge is proof of what SLKone can build and how SLKone works.

Recommendation:

- Treat Bridge as owned proof, not as the main offer.
- Best early uses:
  - sales demo;
  - proof slide;
  - controlled website module;
  - "Built by SLKone, used by SLKone" story.
- What Bridge proves:
  - MCP tooling;
  - AI-enabled delivery loops;
  - knowledge capture;
  - communications and workshop synthesis;
  - document workflows;
  - governed internal automation;
  - practical agent/tool integration.

### 4. The Branch Overcorrects Away From AI

The "business firm that uses AI, not an AI firm" frame is good, but the branch sometimes turns that into a rule that AI should never lead.

That is too rigid.

For firm-level pages, AI probably should not be the headline. But for an AI Enablement page, Bridge proof module, or AI-specific sales path, AI can and should be explicit. The issue is not whether AI appears early. The issue is whether AI is tied to a real workflow, governance model, and business outcome.

Better rule:

> AI can lead when the buyer is already in an AI-specific context. Everywhere else, lead with the business problem and use AI as the accelerant or build capability.

### 5. It Repeats The "Clients Already Know" Bias In Places

The branch is better than the earlier "decision has been made" framing, but it still leans heavily into "decision to done" and "strategy only matters once it is done."

That is strong, but incomplete.

SLKone also helps clients:

- clarify the decision;
- diagnose the operating problem;
- size the value;
- pick the right path;
- align leaders;
- decide what should not be done.

Recommendation:

- Keep "From Decision to Done" as one motif.
- Broaden the overall arc to: decide, align, build, execute, prove.

### 6. It Mixes Content Work With Build-Environment Churn

The branch changes `Gemfile` and `Gemfile.lock` to handle Ruby 3.4 default gem changes.

Those changes may be valid, but they should not be bundled with a positioning/content branch. They add review noise and deployment risk.

Recommendation:

- Split Ruby/build fixes into a separate PR.
- Review them independently by running the Jekyll build in the target environment.

### 7. It Changes Too Much At Once

The branch touches 77 files.

That includes:

- homepage;
- nav;
- services;
- sub-services;
- industries;
- sub-industries;
- layouts;
- new pages;
- CSS;
- Gemfile/Gemfile.lock.

This is too wide for the current stage. The positioning is still being refined. A broad rewrite now increases the chance of carrying wrong decisions into dozens of pages.

Recommendation:

- Start with homepage, services landing, Digital Strategy and Technology, AI Enablement, Data and Advanced Analytics, Private Equity, and proof modules.
- Roll the new pattern into the rest only after the core pages feel right.

## Specific Keep / Change / Drop

### Keep

- `AI-Positioning.md` concept of "business firm that uses AI, not an AI firm."
- AI copy test: outcome, mechanism, proof, ownership, honesty.
- Vendor-neutrality.
- "You own what we build."
- `how-we-work.md` as a concept.
- `_includes/proof-cases.html` as a starting point.
- Proof cases on Data and Advanced Analytics.
- Many of the Data and Advanced Analytics copy improvements.

### Change

- Keep and improve `Business Value Assessment` as a public lead-gen / sales landing page.
- Decide whether homepage should point to BVA as primary or secondary CTA. Recommendation: secondary until the homepage has established the broader firm position.
- Change `GenAI Readiness` to `AI Enablement`.
- Add governance, MCP tooling, skills, agents, and automation to AI Enablement.
- Add Bridge as owned proof.
- Change "decision to done" to a broader "decide, align, build, execute, prove" arc.
- Make the proof system richer than case-card reuse.

### Drop

- Treating BVA as the entire positioning rather than one conversion path.
- "GenAI Training," "LLM Deployment," and "Chatbot Development" as headline focus areas.
- Broad sitewide copy rewrites before core positioning is approved.
- Ruby/Gemfile changes from the marketing branch.

## Suggested Path Forward

1. Do not merge `claude/ai-repositioning-pages` wholesale.
2. Cherry-pick the internal strategy ideas into our planning docs:
   - business-first AI frame;
   - AI copy test;
   - vendor-neutrality;
   - client owns what we build.
3. Build a cleaner implementation branch from current `master`.
4. First implementation scope:
   - homepage copy;
   - services landing;
   - Digital Strategy and Technology;
   - renamed AI Enablement page;
   - Data and Advanced Analytics;
   - Private Equity;
   - How We Work;
   - proof-case include;
   - Bridge proof module.
5. Keep Business Value Assessment as a public lead-gen and sales asset, but make sure the homepage first explains why SLKone is necessary.
6. Split Ruby/build fixes into their own branch if still needed.

## Bottom Line

Claude's branch is a good rough draft, but it is not aligned enough with the current positioning decisions.

Its best contribution is discipline: business first, AI must earn its sentence, vendor-neutral, client owns what we build. Its biggest mistakes are letting Business Value Assessment carry too much of the positioning, failing to rename GenAI Readiness, and leaving Bridge out of the proof system.

Use it as source material. Do not use it as the implementation plan.
