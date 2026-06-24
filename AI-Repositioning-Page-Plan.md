# SLKone AI Repositioning — Site Review and Page Plan

**Status:** Draft for team review · Internal · Companion to `AI-Positioning.md` (the what/why) and `VOICE-AND-TONE.md` (the voice).
**Scope:** Homepage, Services (8 pages + 26 sub-services), Industries (6 pages + 19 sub-industries), shared components, and net-new pages. **No page copy is changed yet.**

AI-touch column = Heavy / Medium / Light per `AI-Positioning.md` §8. Light is deliberate; we do not force-fit AI onto relationship- and judgment-led work.

---

## Part A — Current-State Review

**The headline.** The site is a well-built, classic management-consulting site. Its voice already nails the two things we most need (implementation and measurable outcomes), and the bridge metaphor is already the brand's spine. What it never mentions is AI, except in the Digital Strategy and Data cluster. So this is a rethreading of about three things, not a rebuild.

**Homepage** (`index.md` + `_data/homepage.yml` + `_layouts/home.html`)
- Hero: "Bridge strategy to measurable success." On-brand, no AI.
- "What sets SLKone apart" (6 points): Data-Backed Decisiveness · Beyond Advice to Action · Cross-Industry Insights · Aligned Success · Versatile Expertise ("from coding to process redesign") · Results-Driven Partnership. Already implies consultants-who-can-code and embedded delivery.
- Approach ("Bridging Complexity to Clarity") + service cards from `_services`.
- "Data Driven Approach" (4 steps). The 4-step block already describes the method step by step, so it's the one place that can show time compression without a separate explainer.
- Testimonials. One is ready-made proof for the operator buyer: *"keeping the group small, we were able to adapt and move fast."*

**Services** (`services.md` + `_services/*`). Eight services, consistent structure (intro → approach → impact metrics → why-SLKone → CTA). Implementation voice is strong on Operational Excellence and M&A, softer on Strategy, Org Design, Corporate Finance, New Business Support. AI shows up only in the Digital/Data cluster and the `genai-readiness` / `automation` / `predictive-model-development` sub-services.

**Industries** (`industries.md` + `_industries/*`). Six industries, shared structure (intro → landscape → approach → why-SLKone → CTA); sub-industries render as anchored sections. AI is essentially absent as a term; the existing hooks are "data-driven" / "advanced analytics," plus three sub-industries that already say "AI" (Technology Providers, Industrial Services, Specialty Retail).

**Assets to protect:** the bridge metaphor; the quantified outcome ranges; the embedded/"extension of your team" voice; the deep `_case-study` library (our proof).

**The gap:** (1) AI is missing outside the Digital/Data cluster; (2) the speed and cost dimension is nowhere, despite strong metrics to attach it to; (3) the embedded differentiator is implied, not specified; (4) there's no front-door offer; (5) several content and metadata defects exist independent of AI (Part I).

---

## Part B — Plan at a Glance

Two axes per page: **AI-touch** (how much AI changes the work) and **lead buyer** (who the page must convert — ROI buyer / Operator buyer / Both via the two-door pattern in Part J). They are independent: a Heavy page aimed only at the ROI buyer will repel the operator.

| Area | AI-touch | Lead buyer | Direction |
|---|---|---|---|
| Homepage | Medium | Both | Bridge spans decision→done; AI as accelerant in the approach block; free + paid CTA |
| Services landing | Medium | Both | Umbrella: "we ship the change, and AI is how we ship it faster" |
| Industries landing | Light-Med | Both | Add the speed frame; keep cross-sector |
| Digital Strategy & Technology | Heavy | ROI + IT | The AI flagship service page |
| Data & Advanced Analytics | Heavy | ROI + IT | Core AI/ML/GenAI; also fill empty metrics |
| Operational Excellence | Medium | Operator | AI accelerates process/throughput; keep on-time/on-cost/on-quality core |
| Corporate Finance & Revenue Mgmt | Medium | ROI | Forecasting/pricing analytics; capital judgment stays advisory |
| New Business Support | Medium | Operator | Greenfield: stand up process and its tooling together, in weeks |
| Org Design & Alignment | Light-Med | Operator | Process strand medium; structure/role/talent light |
| Strategy Operationalization | Light | ROI | Faster KPI/scenario execution; lead with the decision |
| Mergers & Acquisitions | Light | Operator | Quiet diligence acceleration; protect the trust-led message |
| Private Equity | Heavy | Deal team + Operating partner | Diligence and value creation at speed — our strongest AI story |
| Technology | Heavy | ROI + IT | AI-fluent partner the audience expects |
| Retail & Consumer Goods | Med-Heavy | ROI | Forecasting/personalization/pricing; brand judgment human |
| Manufacturing | Medium | Operator | Predictive maintenance/quality; capital cycles set the pace |
| Energy & Resources | Medium | Operator | Asset/production optimization; safety- and regulation-led |
| Healthcare | Medium (split) | Operator | Data-rich segments only; compliance- and privacy-led overall |

---

## Part C — Global and Shared Elements

High-leverage because they propagate; do these first.

| Element | File(s) | AI-touch | What changes | Why |
|---|---|---|---|---|
| Hero | `_data/homepage.yml` (hero) | Medium | Keep "Bridge strategy to measurable success." Evolve the description to name decision→done and AI as accelerant. Replace the dead-end "Cross The Bridge → /services" with a real next step offering both a free and a paid door. | Bridge is the spine; the hero should move someone, not teach a metaphor. |
| "What sets SLKone apart" | `_data/homepage.yml` (unique_points) | Medium | Recast "Data-Backed Decisiveness" to include AI acceleration; make one point the specific embedded mechanics (small, senior, no rotation). | Names the moat and the accelerant without a rewrite. |
| Approach blurb | `_data/homepage.yml` (approach) | Light-Med | Retire "Bridging Complexity to Clarity" (abstract) for a decision→done line; add one sentence on AI-accelerated delivery. | Clarity isn't what we sell; shipped work is. |
| "Data Driven Approach" (4 steps) | `_data/homepage.yml` | Med-Heavy | Add one AI sentence to the two steps where it changes the work (Planning, Execution) and nowhere else; this block carries the "weeks into hours" example. | It already describes the method, so it can show time compression in place. |
| Why-Choose include | `_includes/why-choose-slkone.html` | Light | Make an "AI-enabled, implementation-led" point available for reuse. | One edit, broad reach. |
| In-house IT/data block | new reusable include | Light | One line for every Heavy page: *we build with your data and IT team; you own the system when we leave.* | Defuses the silent deal-killer (`Positioning` §4). |
| Contact CTAs | `_includes/contact-card.html`; `_data/homepage.yml` | Light | Replace the single reused block with per-page CTAs and a `data-cta-id` for events. Contact becomes the fallback, not the co-primary (see Part G). | One generic CTA across pages is the same defect as the duplicated Corp-Finance CTA. |
| Header nav | `_data/header-navigation.yml` | Light | Surface the Five Whys diagnostic and Phase Zero once they exist. | Make the front doors findable. |
| Services landing | `services.md` | Medium | Lead with the buyer's problem; umbrella line "we ship the change, and AI is how we ship it faster." | Sets the frame for 8 service pages without the contentless "solving problems, enabled by AI." |
| Industries landing | `industries.md` | Light-Med | Add the AI-accelerant/speed frame; keep cross-sector. | Sets the frame for 6 industry pages. |

---

## Part D — Services

### Top-Level Services (8)

| Service | File | AI-touch | What changes | Why |
|---|---|---|---|---|
| Digital Strategy & Technology | `_services/Digital-Strategy-and-Technology.md` | Heavy | Lead the rewrite here: applied automation, RPA, GenAI adoption (not the generic "AI consulting"). Add an impact-metrics block. | Most tech-forward page; parent of `automation` + `genai-readiness`. |
| Data & Advanced Analytics | `_services/data-advanced-analytics.md` | Heavy | Lead with ML/predictive/GenAI as native capability; **fill the empty impact-metrics block.** | Core AI/ML territory; parent of predictive-model-development + data-enrichment. |
| Operational Excellence | `_services/operational-excellence.md` | Medium | Layer AI as accelerant on analytics and bottleneck detection; keep the on-time/on-cost/on-quality + "5x ROI" core. | Strong implementation voice already; the core terms are load-bearing for SEO too. |
| Corporate Finance & Revenue Mgmt | `_services/corporate-finance-revenue-management.md` | Medium | Weight AI to forecasting/pricing/spend analytics; keep capital allocation advisory. | Analytics is AI-amenable; capital strategy is judgment. |
| New Business Support | `_services/new-business-support.md` | Medium | Greenfield story: no legacy to unwind, so we stand up the process and its tooling together, in weeks. Add impact metrics. | Clean AI story; audience is early-stage, keep it outcome-led. |
| Org Design & Alignment | `_services/organizational-design-and-alignment.md` | Light-Med | Medium touch on the process-design strand only; keep structure/role/talent human. | Split nature; don't force AI onto org and people work. |
| Strategy Operationalization | `_services/strategy.md` | Light | Light nod to AI-accelerated execution (KPI tracking, scenario modeling); lead with the decision. | Strategy and risk are leadership-led. |
| Mergers & Acquisitions | `_services/Mergers-and-Acquisitions.md` | Light | A targeted nod to AI-accelerated diligence only; protect the trust- and people-led message. | Over-claiming undercuts the trust the work runs on. |

### Sub-Services (26), by Parent

⚡ = already AI-oriented today (refine, don't introduce).

| Sub-service | Parent | AI-touch | Note |
|---|---|---|---|
| GenAI Readiness ⚡ | Digital Strategy & Tech | Heavy | Owns "generative AI adoption/training" intent; sharpen + add proof |
| Automation ⚡ | Digital Strategy & Tech | Heavy | Already ML/AI smart workflows + RPA |
| Technology Landscape | Digital Strategy & Tech | Medium | **Fix placeholder text + duplicate `intro` key** |
| IT Roadmap | Digital Strategy & Tech | Light-Med | Consolidate vs Technology Roadmap Development (301 the loser) |
| Predictive Model Development ⚡ | Data & Adv. Analytics | Heavy | Core ML build work |
| Data Enrichment ⚡ | Data & Adv. Analytics | Heavy | LLM-based enrichment fits directly |
| Financial Analytics | Corp Finance & Rev Mgmt | Med-Heavy | "Predictive financial modeling" |
| Revenue Management | Corp Finance & Rev Mgmt | Medium | Pricing/forecasting; strategy advisory |
| Cost Management | Corp Finance & Rev Mgmt | Medium | Spend analytics; **give it its own CTA** |
| Working Capital Management | Corp Finance & Rev Mgmt | Medium | Cash-flow forecasting; **give it its own CTA** |
| Performance Improvement | Operational Excellence | Medium | Analytics accelerates process work |
| SIOP | Operational Excellence | Med-Heavy | Demand forecasting; "SIOP as a service" is also a search term |
| Supply Chain Network Optimization | Operational Excellence | Med-Heavy | Optimization/simulation |
| Process Design | Org Design & Alignment | Medium | Process mining + automation; consolidate vs Process Setup & Optimization |
| Operating Model Design | Org Design & Alignment | Light | Structural/leadership design |
| Organizational Structure Design | Org Design & Alignment | Light | Org/people judgment — do not force AI |
| Organizational Role Effectiveness | Org Design & Alignment | Light | Role/accountability judgment |
| Process Setup & Optimization | New Business Support | Medium | Greenfield processes; **fix mis-pointed permalink** |
| Technology Roadmap Development | New Business Support | Light-Med | **Fix placeholder + duplicate `intro`**; consolidate vs IT Roadmap |
| Org Design & Talent Building | New Business Support | Light | Talent/people-led |
| Performance Management | Strategy Operationalization | Light-Med | Real-time measurement = mild dashboard hook |
| Risk Mitigation | Strategy Operationalization | Light-Med | Continuous monitoring = mild anomaly hook |
| Change Management | Mergers & Acquisitions | Light | Adoption-led; AND reassure the workforce (AI does the grunt analysis, people keep the judgment) |
| Pre-Transaction Readiness | Mergers & Acquisitions | Light-Med | Diligence data analysis can be AI-accelerated |
| Post-Merger Integration | Mergers & Acquisitions | Light | Execution/people coordination |
| Exit Preparation & Readiness | Mergers & Acquisitions | Light | Advisory/value-narrative work |

---

## Part E — Industries

### Top-Level Industries (6)

| Industry | File | AI-touch | What changes | Why |
|---|---|---|---|---|
| Private Equity | `_industries/private-equity.md` | Heavy | Split the page's two buyers explicitly: **deal team** (diligence on messy target data in days) and **operating partner** (a repeatable value-creation playbook across the portfolio). Make Phase Zero the dominant CTA. **Fix the duplicate `order: 4`.** | Key channel; one sponsor refers many portcos. The two PE buyers want different lead lines. |
| Technology | `_industries/technology.md` | Heavy | AI-native product/eng/GTM workflows; SaaS unit economics and churn. **Fix the missing icon and the `order: 4` collision.** | Audience expects AI fluency. |
| Retail & Consumer Goods | `_industries/retail-and-consumer-goods.md` | Med-Heavy | Demand forecasting, personalization, inventory/pricing; lead with margin/inventory/CX outcomes. | Data-rich ops; brand judgment stays human. |
| Manufacturing | `_industries/manufacturing.md` | Medium | Predictive maintenance, demand forecasting, quality detection; lead with throughput/cost/OEE. | Real leverage, but capital cycles and legacy systems set the pace. |
| Energy & Resources | `_industries/energy-and-resources.md` | Medium | Asset/production optimization, predictive maintenance, ESG reporting. Thin (1 sub-industry) — consider expanding. | Capital-, safety-, and regulation-led. |
| Healthcare | `_industries/healthcare.md` | Medium (split) | Apply AI to data-rich segments (health-tech, RCM automation); lead with operational and financial problems. | Compliance-, privacy-, and relationship-led (HIPAA, patient trust). |

### Sub-Industries (19)

| Sub-industry | Parent | AI-touch | Note |
|---|---|---|---|
| Pre-Transaction Readiness | Private Equity | Heavy | Data-room/diligence at speed (deal-team buyer) |
| Operational Due Diligence | Private Equity | Heavy | Rapid ops/financial pattern-finding on target data |
| Value Creation & Growth | Private Equity | Heavy | Value levers + add-on screening (operating-partner buyer) |
| Exit Readiness | Private Equity | Med-Heavy | AI speeds EBITDA-quality analysis; narrative is human |
| Post-Merger Integration | Private Equity | Medium | AI accelerates synergy tracking; execution people-led |
| SaaS | Technology | Heavy | Churn prediction, unit-economics analytics |
| Technology Providers ⚡ | Technology | Heavy | Already "process automation and AI integration" |
| Health Tech | Healthcare | Heavy | Tech-first, data-rich; already "predictive modeling" |
| Pharma & Biotech | Healthcare | Med-Heavy | R&D/trial analytics; regulatory gating |
| Provider & Practice Mgmt | Healthcare | Medium | RCM/denials automation; care relationships human |
| Medical Devices & MedTech | Healthcare | Medium | Mfg + design analytics; heavy regulatory/quality |
| Industrial Services ⚡ | Manufacturing | Med-Heavy | Already "AI-powered diagnostics," IoT, predictive maintenance |
| Aerospace & Defense | Manufacturing | Medium | Predictive supply + digital twin; security/compliance-led |
| Discrete & Process Mfg | Manufacturing | Medium | Predictive quality/forecasting; legacy-bound ops |
| Building Products & Construction | Manufacturing | Medium | Forecasting/inventory; cyclical, project-led |
| Logistics & Distribution | Retail & Consumer Goods | Med-Heavy | Route optimization + real-time analytics |
| Specialty Retail ⚡ | Retail & Consumer Goods | Med-Heavy | Already "AI-driven recommendation systems" |
| Consumer Goods & Services | Retail & Consumer Goods | Medium | Trend/consumer-insight + supply analytics; brand human |
| Oil & Gas | Energy & Resources | Medium | "IoT and predictive analytics"; **fix copy-paste why_choose + malformed subtitle** |

---

## Part F — Net-New Pages and Components

| New asset | What it is | Priority | Notes |
|---|---|---|---|
| **Phase Zero** discovery offer | A paid 1-2 day sprint ending in a concrete "here's what we'll build and why" deliverable. | High | Build it as a **closing page**, not a description: fixed scope and duration, price (credited toward the engagement if you proceed), the **named senior people who show up**, a **redacted sample deliverable**, and a **keep-the-plan guarantee**. The operator buyer won't pay without these. SEO slug `/services/ai-discovery` (see Part H). |
| **Five Whys for AI** readiness check | A short, free diagnostic and lead capture. | High | The cold-traffic front door; feeds Phase Zero. Slug `/ai-readiness`. Owns the "AI readiness assessment" intent. |
| **Proof / case-study surfacing** | Map existing `_case-study` entries to each repositioned page; feature AI-relevant outcomes. | High (gating) | Positioning is jargon without proof. Don't ship AI claims ahead of named proof (owner: 2-3 case studies in 30 days). |
| **"How we work" page** | One page on the embedded + AI method in practice. | High (ship with Phase Zero) | Carries the operator buyer's "who and how" proof; re-prioritized from Medium because it gates skeptic conversion. |
| **PE portfolio one-pager** | A sponsor-forwardable "what we do for your portfolio companies" page/PDF. | High | Serves the actual PE channel motion (sponsor → portfolio CEO), which currently has no asset. |
| **Existing-client AI re-pitch** | A path/motion to take the AI story to the current book. | Medium | Warmest pipeline and the fastest source of the proof we owe. |

---

## Part G — CTA and Conversion Funnel

**The error to avoid:** a paid offer cannot be the cold-traffic CTA. At a 1-in-5 to 1-in-10 conversion-to-engagement rate, Phase Zero is a warm-buyer mechanism. Cold traffic gets a **free** rung first. Contact is the fallback, never the co-primary.

**The ladder (free → paid), by temperature and buyer:**

| Temperature | ROI buyer | Operator buyer |
|---|---|---|
| Cold (just landed) | Five Whys diagnostic (a board-ready readiness read) | Proof — a case study or the "How we work" page |
| Warm (read a page) | Phase Zero ("a 2-day plan for what AI changes in [function]") | Phase Zero framed as scoping ("exactly what we'd build and why, before you commit") |
| Hot (on the offer page) | Book Phase Zero | Book Phase Zero, emphasizing who shows up and the sample deliverable |

**In-voice CTA copy** (button + supporting line; no "Click here," closed em dashes):

| Page | Button | Supporting line |
|---|---|---|
| Hero | See What We'd Build First | "The decision's made. We're the bridge to it actually happening. Start with a two-day plan, or see where your readiness stands." |
| Service page | Scope It in Two Days | "We implement alongside your team. Phase Zero gives you a concrete plan for what we'd build and why, before you commit." |
| Industry page | Pressure-Test Your [Industry] Plan | "See the outcome we delivered, then map your version in a two-day Phase Zero." (secondary link to the matched case study) |
| Phase Zero | Book Your Phase Zero | "Two days. A senior team, not a sales rep. You leave with exactly what we'd build, why, and what it's worth, whether or not you go further." |
| Five Whys | Run the Five Whys | "Five questions, ten minutes. A candid read on where AI moves your numbers, and where it won't. No deck, no pitch." |
| Proof (secondary) | See How It Played Out | "Keeping the group small, they adapted and moved fast. Read what changed, and the numbers behind it." |

**One primary CTA per page**, plus one inline secondary (usually the matched case study). Don't stack buttons.

**Measurement (instrument from day one):** `phase_zero_booking_submitted`, `five_whys_completed`, `contact_form_submitted` as macro events; `cta_click` with `{cta_id, page_type, buyer_variant}` and views of the Phase Zero sample-deliverable and "who shows up" blocks as diagnostics. Tag the PE-sponsor channel as a source on every macro event.

---

## Part H — SEO

**Search intent.** The buyers don't search "AI consulting" (unwinnable head term, mixed intent, off-position). They search the business problem plus their context. Prioritize buyer and function long-tail where we already hold case-study proof: "PE portfolio value creation," "operational due diligence," "AI in M&A due diligence," "FP&A automation," "demand forecasting consulting," "predictive maintenance consulting," "revenue cycle automation."

**Protect core-term equity.** Keep "operational excellence," "post-merger integration," "FP&A," "management consulting," and "supply chain optimization" in each page's title tag, H1, and first paragraph. AI enters the subtitle, a body section, and the metadata — never by displacing the core term. This is also why the Light pages stay light: forcing AI there spends H2s on the wrong keyword.

**Net-new pages take the pure-AI intent.** Let `/services/ai-discovery` (Phase Zero) and `/ai-readiness` (Five Whys) absorb "AI discovery / pilot / readiness assessment," so the established pages don't chase it. Use intent-bearing slugs, not the brand coinages "Phase Zero" / "Five Whys," which have no search volume; keep the coined names as on-page H1.

**Resolve cannibalization.** One owner per query: Five Whys = "AI readiness assessment"; Phase Zero = "AI discovery / pilot"; GenAI Readiness sub-service = "generative AI adoption/training." Consolidate the near-duplicate sub-services (IT Roadmap vs Technology Roadmap Development; Process Design vs Process Setup & Optimization) to one canonical URL each, with a 301.

**The libraries are a topical-authority engine, not decoration.** ~70 case studies and ~50 articles already map to high-intent queries ("SIOP as a service," "ML financial forecasting," "ARR automation," "process mining"). The ML/automation/process-mining case studies are our AI proof and our AI long-tail at once. Build hub-and-spoke: each Heavy page links to its proof; "How we work" is the hub.

**Technical (precedes AI copy):** `jekyll-seo-tag` reads a `description` key for meta descriptions, and our pages set `subtitle`/`intro` instead — so every service and industry page currently ships with **no meta description.** Add a `description` (≤155 chars) to every page, and template one across the case-study library. Preserve every existing `redirect_from` on any consolidation, and add new redirects in `redirect_from` to match the dominant pattern.

---

## Part I — Fix-While-We're-In-Here (Defects)

Independent of AI; clean these up in the same pass.

- **No meta descriptions sitewide** — add a `description` key to every page front-matter (highest-ROI, zero-risk SEO fix).
- **Empty/missing impact metrics** — Data & Advanced Analytics has an empty impact block; Digital Strategy and New Business Support have none. Source real ranges from past engagements (don't invent).
- **Placeholder copy** — `_sub-services/technology-landscape.md` and `_sub-services/technology-roadmap-development.md` contain leftover `"[Introductory text from Siteplanning…]"` and a **duplicate `intro` key** (YAML keeps only one, so content may be silently missing).
- **Sort collision** — Technology and Retail both use `order: 4`.
- **Missing icon** — Technology "Customer-Centric Innovation" approach point.
- **Oil & Gas** — malformed `subtitle` quote and a copy-pasted `why_choose` block that references "manufacturing technologies."
- **Duplicate CTA** — the Corp-Finance CTA is reused verbatim on Cost Management, Financial Analytics, and Working Capital.
- **Placeholder icons** — `fa-chart-line` / `fa-check` across industry approach blocks.

---

## Part J — Sequencing and Guardrails

**Sequence** (respecting the 6-9 month window and the proof dependency):
1. **Foundation:** homepage hero + "Data Driven Approach" block, Services landing, Industries landing, shared includes (why-choose, IT/data block, contact CTA), and the sitewide `description` fix.
2. **Lead pages (Heavy):** Digital Strategy & Technology, Data & Advanced Analytics, Private Equity, Technology, plus Phase Zero, Five Whys, and "How we work."
3. **Medium pages:** Operational Excellence, Corporate Finance, New Business Support, Manufacturing, Retail, Energy, Healthcare.
4. **Light pages (last, lightly):** M&A, Strategy Operationalization, Org Structure/Role/Talent, Change Management, Exit, Operating Model.

**Guardrails:**
- **Two-door pattern on every Heavy page:** open with the problem, then one path to the ROI (metrics, Phase Zero) and one to the method ("How we work," the embedded mechanics, proof). Serves both buyers without whiplash.
- **Proof gates AI.** No AI-accelerated claim ships ahead of a named outcome. Where proof isn't ready, soften the claim.
- **Don't force-fit (the Light list):** Change Management, Org Structure Design, Org Role Effectiveness, M&A cultural integration, Post-Merger Integration, Exit, Operating Model Design. AI stays back-office and out of the headline.
- **Every page follows the voice arc:** Problem → Approach → Impact (with metrics) → Why SLKone. AI lives inside Approach/Impact.
- **Mechanics:** "SLKone" one word; closed em dashes; ranges as "20-30%"; no banned filler (now including "AI-powered" and AI superlatives).
