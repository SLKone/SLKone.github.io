# SLKone Repositioning: Site Review and Page Plan

**Status:** Draft for team review. Internal. Companion to `AI-Positioning.md` (the what and why) and `VOICE-AND-TONE.md` (the voice).
**Scope:** Homepage, Services (8 pages plus 26 sub-services), Industries (6 pages plus 19 sub-industries), shared components, and net-new pages.
**Voice rules (on top of VOICE-AND-TONE):** business first, AI as a supporting tool that never opens a sentence, vendor-neutral, no em dashes, go easy on "senior."

The AI-touch column is Heavy, Medium, or Light per `AI-Positioning.md` section 7. Light is deliberate. We do not force AI onto relationship- and judgment-led work.

## Part A: Current-State Review

The site today is a well-built, classic management-consulting site. Its voice already nails the two things we most need, implementation and measurable outcomes, and the bridge metaphor is already the brand spine. What it never mentions is AI, except in the Digital Strategy and Data cluster. So this is a focused rethread, not a rebuild, and the goal is to position SLKone as a business firm that uses AI, not as another AI firm.

- **Homepage** (`index.md`, `_data/homepage.yml`, `_layouts/home.html`): hero, "What sets SLKone apart" (6 points), an approach section with service cards, a "Data Driven Approach" (4 steps), testimonials, and contact. One testimonial is ready-made proof for the operator buyer: "keeping the group small, we were able to adapt and move fast."
- **Services** (`services.md`, `_services/*`): eight services, consistent structure (intro, approach, impact metrics, why-SLKone, CTA). Implementation voice is strong on Operational Excellence and M&A, softer elsewhere.
- **Industries** (`industries.md`, `_industries/*`): six industries, shared structure; sub-industries render as anchored sections.

**Assets to protect:** the bridge metaphor, the quantified outcome ranges, the embedded delivery voice, and the deep `_case-study` library (our proof).

**The gap:** AI is absent outside the Digital and Data cluster; the talent-and-capacity reason we are needed is unstated; vendor-neutrality is unstated; and several content and metadata defects exist independent of AI (Part I).

## Part B: Plan at a Glance

Two axes per page: AI-touch (how much AI changes the work) and lead buyer (outcome buyer, operator buyer, or both). They are independent.

| Area | AI-touch | Lead buyer | Direction |
| --- | --- | --- | --- |
| Homepage | Medium | Both | Business-first; bridge from decision to result; talent-and-capacity gap; AI as a tool |
| Services landing | Medium | Both | We implement; AI where it moves the business, proven methods elsewhere |
| Industries landing | Light to Medium | Both | Deep sector expertise; fit the tool to the problem; honest when not AI |
| Digital Strategy and Technology | Heavy | Outcome plus IT | Applied automation and AI, vendor-neutral, you own what we build |
| Data and Advanced Analytics | Heavy | Outcome plus IT | Models and analytics that drive the business; fill the empty metrics |
| Operational Excellence | Medium | Operator | Throughput, cost, quality; AI accelerates the analysis |
| Corporate Finance and Revenue Mgmt | Medium | Outcome | Forecasting and pricing analytics; capital judgment stays advisory |
| New Business Support | Medium | Operator | Stand up the operation and the right tooling together |
| Org Design and Alignment | Light to Medium | Operator | Process strand medium; structure, role, talent light |
| Strategy Operationalization | Light | Outcome | Faster execution; lead with the decision |
| Mergers and Acquisitions | Light | Operator | Quiet diligence acceleration; protect the trust-led message |
| Private Equity | Heavy | Deal team plus operating partner | Value creation; talent gap; vendor-neutral; capability stays |
| Technology | Heavy | Outcome plus IT | An operating partner fluent in the tools the sector expects |
| Retail and Consumer Goods | Medium to Heavy | Outcome | Forecasting, pricing, inventory; brand judgment human |
| Manufacturing | Medium | Operator | Predictive maintenance and quality; capital cycles set the pace |
| Energy and Resources | Medium | Operator | Asset and production optimization; safety- and regulation-led |
| Healthcare | Medium (split) | Operator | Data-rich segments only; compliance- and privacy-led overall |

## Part C: Global and Shared Elements

High-leverage because they propagate. Do these first. (Homepage, Services landing, and Industries landing are done as the exemplar set.)

| Element | File(s) | What changes |
| --- | --- | --- |
| Hero | `_data/homepage.yml` | Business-first hero; the right tools, including AI; results on the bottom line. Done. |
| "What sets SLKone apart" | `_data/homepage.yml` | Data point reads "the right tools"; the embedded point reads "the same people start to finish." Done. |
| Approach | `_data/homepage.yml` | "From Decision to Done," with the talent-and-capacity gap. Done. |
| Data Driven Approach (4 steps) | `_data/homepage.yml` | The right tools at each step; AI where it sharpens the work. Done. |
| In-house team note | new reusable include | One line for Heavy pages: we work with your team and leave the capability behind. |
| Contact CTA | `_includes/contact-card.html`, `_data/homepage.yml` | Per-page CTAs with a `data-cta-id`; contact is the fallback, not the co-primary. |
| Services landing | `services.md` | We implement; AI where it moves the business; SEO `description` added. Done. |
| Industries landing | `industries.md` | Fit the tool to the problem; honest when not AI; SEO `description` added. Done. |

## Part D: Services

### Top-level services (8)

| Service | File | AI-touch | What changes |
| --- | --- | --- | --- |
| Digital Strategy and Technology | `_services/Digital-Strategy-and-Technology.md` | Heavy | Lead here: applied automation and AI, vendor-neutral. Add an impact-metrics block. |
| Data and Advanced Analytics | `_services/data-advanced-analytics.md` | Heavy | Models and analytics that drive the business. Fill the empty impact-metrics block. |
| Operational Excellence | `_services/operational-excellence.md` | Medium | AI accelerates the analysis; keep the on-time, on-cost, on-quality core. |
| Corporate Finance and Revenue Mgmt | `_services/corporate-finance-revenue-management.md` | Medium | Forecasting and pricing analytics; capital allocation stays advisory. |
| New Business Support | `_services/new-business-support.md` | Medium | Stand up the operation and its tooling together. Add impact metrics. |
| Org Design and Alignment | `_services/organizational-design-and-alignment.md` | Light to Medium | Medium on the process strand only; keep structure, role, talent human. |
| Strategy Operationalization | `_services/strategy.md` | Light | Light note on faster execution; lead with the decision. |
| Mergers and Acquisitions | `_services/Mergers-and-Acquisitions.md` | Light | A targeted note on diligence acceleration only; protect the trust-led message. |

### Sub-services (26)

Apply the same treatment by parent service. Lead with the business problem; name AI only where it genuinely changes the work. Already AI-oriented and to refine, not introduce: `genai-readiness`, `automation`, `predictive-model-development`, `data-enrichment`. Keep Light: `organizational-structure-design`, `organizational-role-effectiveness`, `operating-model-design`, `change-management`, `post-merger-integration`, `exit-preparation-readiness`, `organizational-design-and-talent-building`.

## Part E: Industries

### Top-level industries (6)

| Industry | File | AI-touch | What changes |
| --- | --- | --- | --- |
| Private Equity | `_industries/private-equity.md` | Heavy | Deal team vs operating partner; the talent gap; vendor-neutral; capability stays. Done. |
| Technology | `_industries/technology.md` | Heavy | An operating partner fluent in the sector's tools. Fix the duplicate `order: 4` and the missing icon. |
| Retail and Consumer Goods | `_industries/retail-and-consumer-goods.md` | Medium to Heavy | Forecasting, pricing, inventory; brand judgment stays human. |
| Manufacturing | `_industries/manufacturing.md` | Medium | Predictive maintenance and quality; capital cycles set the pace. |
| Energy and Resources | `_industries/energy-and-resources.md` | Medium | Asset and production optimization; safety- and regulation-led. Thin (1 sub-industry). |
| Healthcare | `_industries/healthcare.md` | Medium (split) | Data-rich segments only; lead with operational and financial problems. |

### Sub-industries (19)

Same treatment by parent industry. Heaviest AI leverage: Pre-Transaction Readiness, Operational Due Diligence, Value Creation and Growth (PE); SaaS, Technology Providers (Tech); Health Tech (Healthcare). Already say "AI" and need refining, not introducing: Technology Providers, Industrial Services, Specialty Retail.

## Part F: Net-New Pages and Components

| New asset | What it is | Priority |
| --- | --- | --- |
| Business value assessment | A focused, paid engagement on one part of the business or one portfolio company that finds where the value is and how we would capture it. A business diagnostic, not an AI exercise. The primary CTA for warm buyers. | High |
| Proof and case-study surfacing | Map existing `_case-study` entries to each repositioned page and feature the relevant outcomes. Proof gates the AI claims. | High (gating) |
| How we work | One page on the embedded model: how a small team works alongside yours, the same people start to finish, and what stays behind. Carries the operator buyer's "who and how." | High |
| PE portfolio one-pager | A sponsor-forwardable page on what we do for portfolio companies, for the referral motion. | High |
| Existing-client motion | A path to bring the story to the current book, the warmest pipeline and the fastest source of proof. | Medium |

## Part G: CTA and Conversion

Cold traffic gets a free rung first (proof, or the How we work page). The paid business value assessment is the primary CTA for warm and hot traffic. Contact is the fallback, never the co-primary. One primary CTA per page plus one inline secondary (usually the matched case study). Instrument the macro events (assessment requested, contact submitted) and tag the PE channel as a source.

## Part H: SEO

- The site currently ships no meta descriptions on service and industry pages. `jekyll-seo-tag` reads a `description` key, and the pages set `subtitle` and `intro` instead. Add a `description` (max 155 characters) to every page. Done for the four exemplar pages; roll out to the rest.
- Keep core terms in the title, H1, and first paragraph: "operational excellence," "post-merger integration," "FP&A," "management consulting," "supply chain optimization." Let AI sit in the body, not the head terms.
- Net-new pages take the AI and assessment intent with intent-bearing slugs (for example `/services/business-value-assessment`), not internal coinages.
- Treat the roughly 70 case studies and 50 articles as a topical-authority engine. Link each Heavy page to its proof.

## Part I: Fix While We Are In Here (defects)

Independent of AI. Clean up in the same pass.

- Missing meta descriptions sitewide (see Part H).
- Empty or missing impact metrics: Data and Advanced Analytics has an empty block; Digital Strategy and New Business Support have none. Source real ranges; do not invent.
- Placeholder copy and a duplicate `intro` key in `_sub-services/technology-landscape.md` and `_sub-services/technology-roadmap-development.md`.
- Technology and Retail both use `order: 4`.
- Technology "Customer-Centric Innovation" approach point is missing its icon.
- Oil and Gas has a malformed subtitle and a copy-pasted `why_choose` block referencing "manufacturing technologies."
- The Corp-Finance CTA is reused verbatim on Cost Management, Financial Analytics, and Working Capital.
- Placeholder icons (`fa-chart-line`, `fa-check`) across industry approach blocks.

## Part J: Sequencing and Guardrails

**Sequence:**
1. Foundation and exemplars: homepage, Services landing, Industries landing, Private Equity. Done.
2. Remaining Heavy pages: Digital Strategy and Technology, Data and Advanced Analytics, the Technology industry page, plus the business value assessment and How we work pages.
3. Medium pages: Operational Excellence, Corporate Finance, New Business Support, Manufacturing, Retail, Energy, Healthcare.
4. Light pages last and lightly: M&A, Strategy Operationalization, Org Structure, Role, and Talent, Change Management, Exit, Operating Model.

**Guardrails:**
- Business first. AI never opens a sentence or a headline.
- Vendor-neutral. Name when AI is not the answer. You own what we build.
- Proof gates AI. Soften any claim we cannot back with a named outcome.
- Do not force AI onto the Light list.
- No em dashes. Go easy on "senior." No banned filler.
- Every page follows the arc: problem, approach, impact (with metrics), why SLKone.
