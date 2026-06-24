# SLKone AI Repositioning — Site Review & Page-by-Page Plan

**Status:** Draft for team review · Internal · Companion to `AI-Positioning.md` (the "what/why") and `VOICE-AND-TONE.md` (the "how it sounds").
**Scope:** Homepage, Services (8 pages + 26 sub-services), Industries (6 pages + 19 sub-industries), plus shared components and net-new pages. **No page copy is changed yet** — this is the review and the plan for what changes and why.

How to read the AI-touch column: **Heavy / Medium / Light** per the rubric in `AI-Positioning.md` §7. Light is a deliberate choice, not a gap — we do not force-fit AI onto relationship- and judgment-led work.

---

## Part A — Current-state review

### The headline
The site today is a well-built, classic management-consulting site. Its voice is already strong on the two things we most need (implementation and measurable outcomes), and the **bridge metaphor is already the spine**. What it does **not** do is say anything about AI — except in one corner (the Digital Strategy / Data cluster). So this is less a rebuild than a **focused evolution**: thread AI as the accelerant through pages where it's true, strengthen the embedded-delivery voice where it's soft, and leave the relationship-led pages largely alone.

### Homepage (`index.md` + `_data/homepage.yml` + `_layouts/home.html`)
- **Hero:** "Bridge strategy to measurable success." Strong, on-brand, no AI.
- **What sets SLKone apart** (6 icon points): Data-Backed Decisiveness · Beyond Advice to Action · Cross-Industry Insights · Aligned Success · Versatile Expertise ("from coding to process redesign") · Results-Driven Partnership. Already implies "consultants who can code" and embedded delivery.
- **Approach** ("Bridging Complexity to Clarity") + service cards pulled from `_services`.
- **Data Driven Approach** (4 steps: Strategic Analysis → Data-Backed Planning → Practical Execution → Ongoing Improvement). The natural home for the "weeks into hours" story.
- **Testimonials** — one is perfect proof for the new position: *"keeping the group small, we were able to adapt and move fast."*
- Join-team and Contact CTAs.

### Services (`services.md` + `_services/*`)
Eight services, consistent structure (intro → approach → impact metrics → why-SLKone → CTA). Implementation voice is **strong** on Operational Excellence and M&A, **soft/advisory** on Strategy, Org Design, Corp Finance, New Business Support. AI appears only in the Digital Strategy + Data cluster and the `genai-readiness` / `automation` / `predictive-model-development` sub-services.

### Industries (`industries.md` + `_industries/*`)
Six industries, shared structure (intro → landscape → approach → why-SLKone → CTA), sub-industries render as anchored sections. AI is essentially absent as a term; the strongest existing hooks are "data-driven" / "advanced analytics," plus three sub-industries that already say "AI" outright (Technology Providers, Industrial Services, Specialty Retail).

### Assets to preserve (do not break these while repositioning)
- The bridge metaphor and "measurable success."
- Quantified outcome ranges (e.g., "20-30% EBITDA," "30-40% defect reduction").
- The embedded/"extension of your team" voice and the "We don't just X—we Y" device.
- The deep `_case-study` library — our proof.

### Gap summary
1. **AI is missing** everywhere except the Digital/Data cluster.
2. **The speed/cost dimension** ("weeks into hours") is nowhere, despite strong outcome metrics to attach it to.
3. **The embedded-delivery differentiator is implicit**, not named, on the softer pages.
4. **No front-door offer** (no "Phase Zero" discovery, no AI-readiness hook).
5. **Several data-quality defects** exist independent of AI (see Part G) — fix them in the same pass.

---

## Part B — Plan at a glance (AI-touch by area)

| Area | AI-touch | One-line direction |
|---|---|---|
| Homepage | Medium | Evolve the bridge to span decision→done; AI as accelerant in the "approach" section; add discovery CTA |
| Services landing | Medium | Introduce the umbrella: "solving problems, enabled by AI"; "not an AI company" |
| Industries landing | Light-Med | Add the speed/AI-accelerant frame; keep cross-sector |
| Digital Strategy & Technology | **Heavy** | The AI flagship service page |
| Data & Advanced Analytics | **Heavy** | Core AI/ML/GenAI; also fix empty metrics |
| Operational Excellence | Medium | AI accelerates process/throughput; keep on-time/on-cost/on-quality core |
| Corporate Finance & Revenue Mgmt | Medium | Forecasting/pricing analytics; capital judgment stays advisory |
| New Business Support | Medium | "AI-native from day one" greenfield story |
| Org Design & Alignment | Light-Med | Process strand medium; structure/role/talent light |
| Strategy Operationalization | Light | Faster KPI/scenario execution; lead with the decision |
| Mergers & Acquisitions | Light | Quiet diligence acceleration; protect the trust-led message |
| Private Equity | **Heavy** | Diligence/value-creation at speed — our strongest AI story |
| Technology | **Heavy** | AI-fluent partner expected by the audience |
| Retail & Consumer Goods | Med-Heavy | Forecasting/personalization/pricing; brand judgment human |
| Manufacturing | Medium | Predictive maintenance/quality; physical/capital cycles set pace |
| Energy & Resources | Medium | Asset/production optimization; safety- and regulation-led |
| Healthcare | Medium | Data-rich segments only; compliance/privacy-led overall |

---

## Part C — Global & shared elements

These propagate across many pages, so they're high-leverage and should go first.

| Element | File(s) | AI-touch | What changes | Why |
|---|---|---|---|---|
| Hero | `_data/homepage.yml` (hero) | Medium | Keep "Bridge strategy to measurable success"; evolve the description to name decision→done and AI as accelerant. Add a secondary CTA to the discovery offer. | Bridge is the spine; AI earns the second sentence, not the headline (Positioning §4.3). |
| "What sets SLKone apart" | `_data/homepage.yml` (unique_points) | Medium | Recast "Data-Backed Decisiveness" to include AI acceleration; make one point explicitly "Embedded delivery"; keep "Versatile Expertise / from coding to process redesign." | Names the embedded moat + AI accelerant without a rewrite. |
| Approach + service cards | `_data/homepage.yml` (approach); `_includes/service-card.html` | Light-Med | Add one line on AI-accelerated delivery to the approach blurb; cards inherit from `_services` edits. | Single source of truth — update services, cards follow. |
| "Data Driven Approach" (4 steps) | `_data/homepage.yml` (data_driven_approach) | Med-Heavy | Thread AI through the steps (AI-accelerated modeling in Planning; AI-built tooling in Execution); this is where "weeks into hours" lives. | The most natural place to *show* the method without hype. |
| Why-Choose component | `_includes/why-choose-slkone.html` | Light | Ensure an "AI-enabled, implementation-led" point is available for reuse. | Reused across pages; one edit, broad reach. |
| Contact CTAs | `_includes/contact-card.html`; `_data/homepage.yml` (contact) | Light | Offer the discovery session as the primary next step alongside "Contact." | Converts AI-curious buyers into the Phase Zero funnel (Positioning §8). |
| Header nav | `_data/header-navigation.yml` | Light | Consider surfacing the discovery offer / AI-readiness diagnostic in nav once those pages exist. | Make the front-door offer findable. |
| Services landing | `services.md` | Medium | Add umbrella framing ("solving problems, enabled by AI"), the "not an AI company" line, and lead with the client problem. | Sets the frame for all 8 service pages. |
| Industries landing | `industries.md` | Light-Med | Add the AI-accelerant/speed frame; keep "cross-sector insights." | Sets the frame for all 6 industry pages. |

---

## Part D — Services

### Top-level services (8)

| Service | File | AI-touch | What changes | Why |
|---|---|---|---|---|
| Digital Strategy & Technology | `_services/Digital-Strategy-and-Technology.md` | **Heavy** | Lead the rewrite here: AI/GenAI/automation as implementation-grade enablement; parent of `automation` + `genai-readiness`. Add an impact-metrics block (currently missing). | Already the most tech-forward page; the natural AI flagship. |
| Data & Advanced Analytics | `_services/data-advanced-analytics.md` | **Heavy** | Lead with AI/ML/GenAI as native capability; **fill the empty impact-metrics block**. | Core AI/ML territory; parent of predictive-model-development + data-enrichment. |
| Operational Excellence | `_services/operational-excellence.md` | Medium | Layer AI as accelerant on analytics/bottleneck detection; keep the on-time/on-cost/on-quality + "5x ROI" core intact. | Strong implementation voice already; don't overwrite it. |
| Corporate Finance & Revenue Mgmt | `_services/corporate-finance-revenue-management.md` | Medium | Weight AI toward forecasting/pricing/spend analytics sub-services; keep capital-allocation as judgment-led. | Analytics is AI-amenable; capital strategy is advisory. |
| New Business Support | `_services/new-business-support.md` | Medium | Add an "AI-native from day one" greenfield narrative (lean teams, AI-built processes = "weeks into hours"); add impact metrics. | Greenfield is a clean AI story; audience is early-stage, keep it outcome-led. |
| Org Design & Alignment | `_services/organizational-design-and-alignment.md` | Light-Med | Medium touch on the process-design strand only; keep structure/role/talent copy human. | Split nature — don't force AI onto org/people work. |
| Strategy Operationalization | `_services/strategy.md` | Light | Light nod to AI-accelerated execution (faster KPI tracking, scenario modeling); lead with the decision/outcome. | Strategy direction and risk are advisory/leadership-led. |
| Mergers & Acquisitions | `_services/Mergers-and-Acquisitions.md` | Light | A targeted nod to AI-accelerated diligence/data-room analysis only; protect the trust- and people-led message. | Relationship/judgment-led; over-claiming undercuts trust. |

### Sub-services (26) — by parent

⚡ = already AI-oriented today (refine, don't introduce).

| Sub-service | Parent | AI-touch | Note |
|---|---|---|---|
| GenAI Readiness ⚡ | Digital Strategy & Tech | **Heavy** | Flagship AI page (GenAI training, LLM deployment) — sharpen + add proof |
| Automation ⚡ | Digital Strategy & Tech | **Heavy** | Already "ML and AI smart workflows" + RPA |
| Technology Landscape | Digital Strategy & Tech | Medium | Surface AI/emerging-tech adoption; **fix placeholder text + dup `intro` key** |
| IT Roadmap | Digital Strategy & Tech | Light-Med | AI as a roadmap input; consolidate vs Technology Roadmap Development |
| Predictive Model Development ⚡ | Data & Adv. Analytics | **Heavy** | Core ML build work |
| Data Enrichment ⚡ | Data & Adv. Analytics | **Heavy** | LLM-based enrichment fits directly |
| Financial Analytics | Corp Finance & Rev Mgmt | Med-Heavy | "Predictive financial modeling" — analytics-heavy |
| Revenue Management | Corp Finance & Rev Mgmt | Medium | Pricing/forecasting models; strategy stays advisory |
| Cost Management | Corp Finance & Rev Mgmt | Medium | Spend analytics AI-fit; sourcing decisions judgment-led; **give it its own CTA** |
| Working Capital Management | Corp Finance & Rev Mgmt | Medium | Cash-flow forecasting; **give it its own CTA** |
| Performance Improvement | Operational Excellence | Medium | Analytics accelerates process work |
| SIOP | Operational Excellence | Med-Heavy | Demand forecasting is AI-fit |
| Supply Chain Network Optimization | Operational Excellence | Med-Heavy | Optimization/simulation = AI-fit |
| Process Design | Org Design & Alignment | Medium | Process mining + automation; consolidate vs Process Setup & Optimization |
| Operating Model Design | Org Design & Alignment | Light | Structural/leadership design |
| Organizational Structure Design | Org Design & Alignment | Light | Pure org/people judgment — **do not force AI** |
| Organizational Role Effectiveness | Org Design & Alignment | Light | Role/accountability judgment |
| Process Setup & Optimization | New Business Support | Medium | Greenfield processes AI-built; **fix mis-pointed permalink** |
| Technology Roadmap Development | New Business Support | Light-Med | Near-duplicate of IT Roadmap; **fix placeholder + dup `intro`** |
| Org Design & Talent Building | New Business Support | Light | Talent/people-led |
| Performance Management | Strategy Operationalization | Light-Med | Real-time measurement = mild dashboard hook |
| Risk Mitigation | Strategy Operationalization | Light-Med | Continuous risk-monitoring = mild anomaly hook |
| Change Management | Mergers & Acquisitions | Light | Human/adoption-led — AI feels tone-deaf here |
| Pre-Transaction Readiness | Mergers & Acquisitions | Light-Med | Diligence data analysis can be AI-accelerated |
| Post-Merger Integration | Mergers & Acquisitions | Light | Execution/people coordination |
| Exit Preparation & Readiness | Mergers & Acquisitions | Light | Advisory/value-narrative & relationship work |

---

## Part E — Industries

### Top-level industries (6)

| Industry | File | AI-touch | What changes | Why |
|---|---|---|---|---|
| Private Equity | `_industries/private-equity.md` | **Heavy** | Lead with diligence-at-speed, automated data-room/financial analysis, value-creation analytics, exit-prep acceleration — "weeks into hours" per deal. | Named key audience; sponsors are the channel; buyers care about speed/cost per deal. |
| Technology | `_industries/technology.md` | **Heavy** | AI-native product/eng/GTM workflows, analytics, automation; an AI-fluent partner. **Fix duplicate `order: 4` and the missing icon.** | Audience expects AI fluency; "we use AI like we used Excel" lands hardest here. |
| Retail & Consumer Goods | `_industries/retail-and-consumer-goods.md` | Med-Heavy | Demand forecasting, personalization/recommendation, inventory/pricing optimization; lead with margin/inventory/CX outcomes. | Data-rich ops; brand/merchandising judgment stays human. |
| Manufacturing | `_industries/manufacturing.md` | Medium | Predictive maintenance, demand forecasting, quality/defect detection, digital twins; lead with throughput/cost/OEE. | Real leverage, but capital cycles + legacy systems set the pace. |
| Energy & Resources | `_industries/energy-and-resources.md` | Medium | Asset/production optimization, predictive maintenance, ESG reporting; lead with cost/uptime/risk. **Thin (1 sub-industry) — consider expanding.** | Capital-, safety-, and regulation-led. |
| Healthcare | `_industries/healthcare.md` | Medium (split) | Apply AI to data-rich segments (health-tech, RCM automation, analytics); lead with operational/financial problems, not the tech. | Compliance-, privacy-, and relationship-led (HIPAA, patient trust). |

### Sub-industries (19)

| Sub-industry | Parent | AI-touch | Note |
|---|---|---|---|
| Pre-Transaction Readiness | Private Equity | **Heavy** | Data-room/diligence at speed — core PE win |
| Operational Due Diligence | Private Equity | **Heavy** | Rapid ops/financial pattern-finding on messy target data |
| Value Creation & Growth | Private Equity | **Heavy** | Analytics value levers + add-on screening |
| Exit Readiness | Private Equity | Med-Heavy | AI speeds EBITDA-quality analysis; narrative is human |
| Post-Merger Integration | Private Equity | Medium | AI accelerates synergy tracking; execution people-led |
| SaaS | Technology | **Heavy** | Churn prediction, unit-economics analytics — AI-native |
| Technology Providers ⚡ | Technology | **Heavy** | Already says "process automation and AI integration" |
| Health Tech | Healthcare | **Heavy** | Tech-first, data-rich; already "predictive modeling" |
| Pharma & Biotech | Healthcare | Med-Heavy | R&D/trial analytics strong; regulatory gating |
| Provider & Practice Mgmt | Healthcare | Medium | RCM/denials automation; care relationships human |
| Medical Devices & MedTech | Healthcare | Medium | Mfg + design analytics; heavy regulatory/quality |
| Industrial Services ⚡ | Manufacturing | Med-Heavy | Already "AI-powered diagnostics," IoT, predictive maintenance |
| Aerospace & Defense | Manufacturing | Medium | Predictive supply + digital twin; security/compliance-led |
| Discrete & Process Mfg | Manufacturing | Medium | Predictive quality/forecasting; legacy-bound ops |
| Building Products & Construction | Manufacturing | Medium | Forecasting/inventory; cyclical, labor- and project-led |
| Logistics & Distribution | Retail & Consumer Goods | Med-Heavy | Route optimization + predictive/real-time analytics |
| Specialty Retail ⚡ | Retail & Consumer Goods | Med-Heavy | Already "AI-driven recommendation systems" |
| Consumer Goods & Services | Retail & Consumer Goods | Medium | Trend/consumer-insight + supply analytics; brand human |
| Oil & Gas | Energy & Resources | Medium | "IoT and predictive analytics"; safety/regulation-led; **fix copy-paste why_choose + malformed subtitle** |

---

## Part F — Net-new pages & components (from the workshop)

These don't exist yet and directly support the go-to-market decisions from Sessions 2–3.

| New asset | What it is | Priority | Notes |
|---|---|---|---|
| **Phase Zero discovery offer** | A page describing the paid 1–2 day discovery sprint with a concrete "here's what we'll build and why" deliverable; primary CTA across the site. | **High** | The front-door offer (Two Toasters precedent, ~1-in-5 to 1-in-10 convert). The natural CTA for AI-curious buyers. |
| **"Five Whys for AI" readiness check** | A lightweight AI-readiness diagnostic / lead-capture hook. | Medium | Qualifies leads, anchors the discovery pitch. Keep it short and outcome-oriented. |
| **Proof / case-study surfacing** | Map existing `_case-study` entries to each repositioned service/industry; feature AI-relevant outcomes. | **High (gating)** | Positioning is jargon without proof. Don't ship AI claims ahead of named proof (Bernardo owns 2–3 within 30 days). |
| **"How we work" / so-what** | A one-page explanation of the embedded + AI method in practice (Andrew's S3 action). | Medium | The answer to "so what — how does this actually work here?" |

---

## Part G — Fix-while-we're-in-here (defects found during review)

Independent of AI; clean these up in the same editing pass.

- **Empty/missing impact metrics:** Data & Advanced Analytics has an impact block with no metrics; Digital Strategy and New Business Support have no impact block at all. Add defensible ranges.
- **Placeholder copy:** `_sub-services/technology-landscape.md` and `_sub-services/technology-roadmap-development.md` contain leftover `"[Introductory text from Siteplanning-SLKone.md…]"` and a **duplicate `intro:` key**.
- **Sort collision:** `_industries/technology.md` and `_industries/retail-and-consumer-goods.md` both use `order: 4`.
- **Missing icon:** Technology industry "Customer-Centric Innovation" approach point.
- **Oil & Gas:** malformed leading-quote in `subtitle`; unquoted bullets; a copy-pasted `why_choose` block that wrongly references "manufacturing technologies."
- **Duplicate CTA:** the Corp-Finance CTA is reused verbatim on Cost Management, Financial Analytics, and Working Capital.
- **Near-duplicate content:** IT Roadmap vs Technology Roadmap Development; Process Design vs Process Setup & Optimization — consolidate or clearly differentiate.
- **Placeholder icons** (`fa-chart-line` / `fa-check`) across industry approach blocks — replace with meaningful icons.

---

## Part H — Sequencing & guardrails

**Sequence (respecting the 6-9 month window and the proof dependency):**
1. **Foundation:** homepage hero + "Data Driven Approach" section, Services landing, Industries landing, shared includes (why-choose, contact CTA). Sets the frame everywhere.
2. **Lead pages (Heavy):** Digital Strategy & Technology, Data & Advanced Analytics, Private Equity, Technology + the Phase Zero discovery page. These carry the repositioning.
3. **Medium pages:** Operational Excellence, Corporate Finance, New Business Support, Manufacturing, Retail, Energy, Healthcare.
4. **Light pages (last, and lightly):** M&A, Strategy Operationalization, Org Structure/Role/Talent, Change Management, Exit, Operating Model.

**Guardrails:**
- **Proof gates AI.** No AI-accelerated claim ships ahead of a named outcome/case study. Where proof isn't ready, soften the claim (Positioning §6).
- **Don't force-fit (explicit Light list):** Change Management, Org Structure Design, Org Role Effectiveness, M&A cultural integration, Post-Merger Integration, Exit narrative, Operating Model Design. AI stays a quiet assist here; over-claiming reads as tone-deaf.
- **Every page follows the VOICE-AND-TONE arc:** Problem → Approach → Impact (with metrics) → Why SLKone. AI is the accelerant inside "Approach/Impact," never the opening line.
- **Mechanics:** "SLKone" one word; closed em dashes; metric ranges as "20-30%"; no banned filler (now including "AI-powered").
