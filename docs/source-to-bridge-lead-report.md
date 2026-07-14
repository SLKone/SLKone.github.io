# Source To Bridge Lead Outcome Report

Purpose: give leadership one first dashboard that connects acquisition source, content consumed, and Bridge lead outcome.

## Data Sources

- GA4 BigQuery export: `slkone-501222.analytics_366012577.events_*`
- Bridge reporting mirror: `slkone-501222.bridge_reporting.leads`
- UTM registry: `_data/utm_registry.yml`

## Looker Explores

Primary explore: `source_to_bridge_lead_outcome`

Core dimensions:
- Lead event date
- Source
- Medium
- Campaign
- Lead page path
- Form name
- Bridge lead stage
- Bridge lead result
- Pre-lead touchpoints

Core measures:
- Website lead form submissions
- Bridge leads created
- Qualified Bridge leads
- Opportunity / active lead count
- Source-to-lead conversion rate
- Lead-to-qualified rate

## First Dashboard Tiles

- Leads by source / medium / campaign
- Bridge qualified leads by source
- Contact page submissions by landing page
- Content viewed before lead submission
- UTM compliance exceptions
- Unmatched GA4 lead events without Bridge lead
- Bridge leads without usable UTM attribution

## Matching Logic

Initial matching is timestamp-based because GA4 does not expose submitted email addresses by default. Once the Bridge intake endpoint stores a generated `website_submission_id`, use that ID as the durable join key between the GA4 event metadata and Bridge lead metadata.

## Operational Review

Review weekly until the flow stabilizes:
- Confirm new campaign links exist in `_data/utm_registry.yml`.
- Check that `lead_form_submit` appears in GA4 and BigQuery.
- Confirm each real form submission created or updated a Bridge lead.
- Resolve unmatched records before interpreting source performance.
