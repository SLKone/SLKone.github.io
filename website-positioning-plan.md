# SLKone Website Positioning Plan

## Source Signal

This plan translates the Management Workshop positioning and branding discussions into website changes for this Jekyll site.

Primary workshop conclusions:

- SLKone is an AI-enabled delivery firm, not an AI company.
- The strongest message is the full arc from decision clarity to measurable execution.
- Some clients already know what needs to happen and need help making it real. Others need SLKone to clarify the decision, align the organization, and define the practical path before execution can move.
- AI should appear early, but as an accelerant for embedded delivery, not as the headline product.
- Bridge is a proof point of what SLKone can build and how SLKone works. Use it carefully: as evidence of AI-enabled delivery capability, not as the product SLKone is selling.
- The pitch needs proof: named case studies, concrete artifacts, and visible examples of how SLKone changes work.

Workshop language to preserve internally:

> Most of our clients already know what needs to happen. The decision's been made. What's missing is the connection between that and it actually happening.
>
> That's the gap we close. We embed - small team, deep in the work, aligned on your actual priorities. We get to know how the business really operates, figure out where the leverage is, and then we move. We use AI the way we once used Excel, except it compresses weeks into hours. Your team can't move at that speed without outside help.
>
> We're not an AI company. We're a delivery firm that uses AI better than anyone else. Our clients don't pay for decks. They pay because things actually change.

## Messaging Architecture

### Primary Position

SLKone helps leadership teams make the right call, align the business, and turn priority decisions into measurable results.

Use this on the homepage and services entry points. It is broader and more durable than an AI-first headline, while still making room for AI as the current acceleration wedge.

### Supporting Points

- Embedded delivery: small teams working deep in the client's operating reality.
- AI-enabled speed: compress analysis, synthesis, and iteration cycles without turning SLKone into an AI vendor.
- Business outcomes: revenue growth, cost reduction, cycle-time reduction, better execution discipline.
- Proof over promise: case studies, concrete artifacts, Bridge, and named delivery examples should carry the pitch.

### Words To Use

- "decision clarity"
- "alignment to action"
- "execution gap"
- "decision to result"
- "embedded team"
- "AI-enabled delivery"
- "owned proof"
- "built to change the work"
- "measurable revenue and cost outcomes"
- "faster operating rhythm"
- "proof, not decks"

### Words To Avoid

- "AI company"
- "GenAI transformation" as the main offer
- "platform" when it makes SLKone sound like a software vendor instead of an implementation-led consulting firm
- "tool adoption" without business outcome
- generic "digital transformation" language that could describe any consulting firm

## Recommended Site Changes

### 1. Homepage

Files:

- `_data/homepage.yml`
- `_layouts/home.html` only if a new proof section is needed

Change the hero from broad consulting language to the new execution-gap position.

Recommended hero copy:

```yaml
hero:
  title: "Make the right call. Make the change real."
  description: "SLKone embeds with your team to clarify priorities, align the business, and turn high-stakes decisions into measurable revenue, cost, and cycle-time outcomes. We use AI the way strong operators use any practical tool: to understand the work faster, find leverage sooner, and help changes actually land."
  cta_text: "See how we work"
  cta_link: "/services"
```

Replace "What sets SLKone apart" points with workshop-aligned points:

- Embedded where the work happens
- AI-enabled, outcome-led
- Small teams, senior judgment
- From strategy to operating rhythm
- Proof through delivery artifacts
- Built around measurable change

Add a short proof band below the hero or before services:

> We are not an AI company. We are a delivery firm that uses AI to move faster inside real business problems.

Use this as a positioning link into services and case studies.

### 2. Services Page

File:

- `services.md`

Reframe the services page around the operating promise rather than the catalog.

Recommended subtitle:

> Leadership teams rarely need another abstract recommendation. They need the right decision, a practical path, and the operating capacity to make change real. SLKone works inside that gap.

Recommended big paragraph:

> We combine management consulting, operating experience, analytics, and AI-enabled delivery to move from diagnosis to implementation quickly. The service lines below are not isolated offerings; they are the lenses we use to help clients grow revenue, reduce cost, shorten cycle times, and sustain the change after we leave.

### 3. Digital Strategy and Technology

Files:

- `_services/Digital-Strategy-and-Technology.md`
- `_sub-services/genai-readiness.md`
- `_sub-services/automation.md`

Current copy is tool-forward. Reframe it as AI-enabled workflow improvement.

Priority change:

- Rename "GenAI Readiness" to "AI Enablement." This should be a visible title/card change, not just a copy refresh.
- If avoiding URL churn, keep the existing URL temporarily but change the visible title, metadata, and copy now. Plan a later redirect if the filename/slug changes.
- A Business Value Assessment page can be useful as a public cold lead-gen path and a sendable sales page. It should support the broader SLKone positioning rather than become the whole offer.

Recommended AI Enablement angle:

> We help teams identify where AI can improve real work, not where AI sounds interesting. Then we design the governance, build the MCP tools and integrations, and create the skills, agents, and automations needed to make the workflow actually improve.

AI Enablement should include:

- Workflow selection and value sizing
- AI governance, data boundaries, and operating controls
- MCP tool and system integration design
- Skills and agents for repeatable automation
- Practical build / buy / route decisions
- Implementation support tied to revenue, cost, speed, quality, or decision-making outcomes

### 4. Case Studies

Files:

- `_case-study/*.md`
- `case-studies.md`

The workshop repeatedly says the pitch is incomplete without proof. The site should surface 2-3 reference examples near the new positioning. Use approved or anonymized public-safe proof, not internal tool names.

Bridge proof strategy:

- Bridge is one of the strongest proof points because it shows SLKone can build the modern operating infrastructure it recommends: MCP tools, knowledge capture, communications/workshop synthesis, documents, workflow support, and AI-enabled delivery loops.
- Use Bridge in sales conversations and demos as owned proof of capability.
- On the public site, consider a controlled proof module such as "How we changed our own delivery model" or "Built by SLKone, used by SLKone" if leadership is comfortable naming it.
- Avoid positioning Bridge as a standalone product unless that becomes an explicit business decision.

AI and analytics proof points from the MCP knowledgebase / insights:

- Machine learning financial forecasting for a $10B oil and gas organization: 90%+ predictive accuracy at three months for a significant cost line item.
- PE-backed CRO post-merger integration across four sites: operating model, playbooks, data infrastructure, and seven AI automation opportunities identified.
- $100M SaaS ARR automation and KPI cleanup: supported a transaction at 16.6x EBITDA.
- $100M SaaS cloud-based FP&A implementation: first-ever budget process, sale at 13x EBITDA, >$700M total price.
- Senior care finance transformation: 6.3x higher liquidity than expected, collections forecast accuracy to +/-3%, RCM dashboard visibility.
- Behavioral health reimbursement intelligence: 20-30% rate increases across key CPT codes, moving from bottom 5% to market-competitive.

Add tags or intro language that makes these examples findable as "AI-enabled delivery" or "execution gap" proof, even where older cases used Power BI, analytics, or automation rather than GenAI.

### 5. Insights

Files:

- `_articles/*.md`
- `insights.md`

Recommended near-term article topics:

- "AI Is Not the Strategy. It Is the Speed Layer."
- "Why Most AI Work Fails Between the Board Mandate and the Operating Team"
- "From AI Interest to Operating Backlog"
- "The Difference Between AI Use Cases and AI Value"

These should support the new pitch without turning the homepage into a thought-leadership essay.

Do not publish paid discovery as a thought-leadership article. Use Business Value Assessment as a focused lead-gen / sales landing page instead.

### 6. Navigation

File:

- `_data/header-navigation.yml`

No immediate navigation change is required.

Possible later change:

- Add a top-level "AI-Enabled Delivery" page only after the message is proven on the homepage/services page.

Avoid adding a top-level AI nav item first. That would work against the workshop conclusion that SLKone is not an AI company.

## Implementation Sequence

1. Update homepage copy in `_data/homepage.yml`.
2. Update `services.md` subtitle and big paragraph.
3. Rewrite `_services/Digital-Strategy-and-Technology.md` to make AI a delivery accelerant.
4. Rename/rewrite `_sub-services/genai-readiness.md` around AI Enablement. Prefer visible rename immediately; handle URL migration carefully.
5. Add a proof band or curated case-study section on the homepage.
6. Tag or rewrite 2-3 existing case studies to support the new proof narrative.
7. Adapt the Business Value Assessment page as a public lead-gen and sales landing page. Use it as a secondary homepage CTA unless the team decides it should be the primary conversion path.
8. Build the site with `npm run build:css:prod` and `bundle exec jekyll build`.

## Open Decisions

- What is the final visible name: "AI Enablement" or "AI Readiness and Enablement"? Recommended answer: "AI Enablement."
- Which 2-3 named proof points are safe to publish?
- How should Business Value Assessment be exposed? Recommended answer: public lead-gen page plus one-page PDF, deck module, and proposal language; test as a secondary homepage CTA before making it the dominant nav/hero CTA.
- How should Bridge be used publicly? Recommended answer: controlled proof module or sales demo first; public naming only if it reinforces SLKone's delivery capability without making Bridge look like the main offer.
