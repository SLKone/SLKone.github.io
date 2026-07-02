# SLKone Growth Data Foundation

This plan turns the website, referral activity, future paid media, and CRM pipeline into one reportable operating dataset. The first phase is data quality: tagging, tracking, lead capture, and storage before media spend.

## 1. UTM Parameter Standards

Every external campaign link should use the same naming convention so traffic can be traced to the source that created it.

| Parameter | Required | Standard | Example |
| --- | --- | --- | --- |
| `utm_source` | Yes | Platform, partner, or sender in lowercase kebab case | `linkedin`, `google`, `amalgam-capital`, `partner-name` |
| `utm_medium` | Yes | Channel type | `organic-social`, `paid-search`, `email`, `referral`, `event` |
| `utm_campaign` | Yes | Initiative or campaign name | `pe-value-creation-q3-2026` |
| `utm_content` | Recommended | Creative, post, CTA, or placement | `case-study-card`, `partner-email-link` |
| `utm_term` | Paid search only | Keyword or audience label | `private-equity-consulting` |
| `utm_id` | Recommended | Stable campaign ID shared with ad/CRM data | `2026-q3-pe-vc` |

Rules:
- Use lowercase kebab case.
- Do not use spaces, dates with slashes, or partner initials that will be unclear later.
- Keep campaign names stable across channels when they support the same initiative.
- Preserve UTMs on handoff links from partner emails, event follow-ups, QR codes, and future paid campaigns.

## 2. GA4 Event Tracking Through Google Tag Manager

The site now exposes a `dataLayer` foundation for Google Tag Manager. Once the GTM container ID is added in `_config.yml`, configure GA4 tags around these events:

| Event | Trigger | Primary parameters |
| --- | --- | --- |
| `site_context` | Every page load | `site_name`, `page_title`, `page_path`, `page_collection` |
| `page_view_enriched` | DOM ready | `page_path`, `first_touch_source`, `last_touch_source` |
| `lead_form_submit` | Contact form submit | `form_name`, `form_type`, `page_path` |
| `contact_intent_click` | Contact, email, or phone link click | `link_url`, `link_text`, `page_path` |
| `content_download_click` | PDF/document/file link click | `link_url`, `link_text`, `page_path` |
| `scroll_depth` | 25%, 50%, 75%, 90% scroll | `percent_scrolled`, `page_path` |
| `engaged_time` | 30, 60, 120 seconds on page | `seconds`, `page_path` |

Recommended GA4 conversions:
- `lead_form_submit`
- High-intent `contact_intent_click`
- Selected `content_download_click` events for case studies, articles, or gated assets if gating is added later

## 3. BigQuery Data Warehouse

Connect GA4 to BigQuery export before investing in media. This makes the raw event stream a durable company asset outside GA4's reporting UI.

Minimum datasets:
- `ga4_events`: native GA4 export tables.
- `crm_leads`: lead records from the CRM.
- `campaign_costs`: future paid media cost and impression/click data.
- `campaign_taxonomy`: canonical UTM/campaign naming lookup table.

Minimum modeled views:
- `web_sessions_by_source`
- `lead_attribution_first_touch`
- `lead_attribution_last_touch`
- `content_engagement_by_account_or_domain`
- `pipeline_by_source_medium_campaign`

## 4. CRM Lead Capture

The contact form now stores first-touch and last-touch attribution fields as hidden inputs before submission. The CRM should map those fields onto lead/contact records.

Fields to create or map:
- First-touch source, medium, campaign, content, term, campaign ID
- First-touch landing page, referrer, capture timestamp
- Last-touch source, medium, campaign, content, term, campaign ID
- Last-touch landing page, referrer, capture timestamp
- Current page and current path
- Lead source category: website, event, partner referral, warm intro, direct outreach
- Deal status, owner, notes, next step, qualified status

Operational rule: warm intros and event leads should still be entered into the CRM with source and relationship context, even when the website was not the first touch.

## 5. Unifying Layer And Reporting

Use BigQuery as the unifying layer, then build Looker dashboards on top.

Leadership dashboard:
- Inbound leads by source, medium, and campaign
- Qualified opportunities by source
- Pipeline created by relationship source versus website source
- Case study/article engagement before form submission
- Referral partner and event activity
- Website pages that precede contact intent

Marketing/BD operating dashboard:
- UTM compliance
- Broken or untagged campaign traffic
- Contact form submissions and contact intent clicks
- Content downloads and engagement depth
- Campaign cost, clicks, leads, qualified leads, and pipeline once media begins

## Phasing

1. Data foundation: GTM, GA4 events, UTM standards, contact attribution, CRM field mapping, BigQuery export.
2. Reporting: Looker dashboards for leadership and BD operating review.
3. SEO/GEO optimization: use the baseline data to prioritize content and technical search work.
4. Media investment: only begin meaningful paid spend once attribution, conversion tracking, and reporting are trusted.

## External Setup Checklist

- Create or confirm the Google Tag Manager container.
- Add the production GTM container ID to `google_tag_manager_id` in `_config.yml`.
- Create GA4 tags and conversion events in GTM.
- Link GA4 to BigQuery with daily export enabled.
- Create CRM fields for first-touch and last-touch attribution.
- Map Web3Forms submissions into the CRM or replace Web3Forms with a CRM-native form endpoint.
- Build the first Looker dashboard against BigQuery after events and lead records are flowing.
