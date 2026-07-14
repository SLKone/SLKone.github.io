-- Source -> content -> Bridge lead outcome starter model.
-- Replace the project/dataset names with the final BigQuery export and Bridge mirror tables.

with ga4_events as (
  select
    event_date,
    timestamp_micros(event_timestamp) as event_at,
    user_pseudo_id,
    event_name,
    (select value.string_value from unnest(event_params) where key = 'page_location') as page_location,
    (select value.string_value from unnest(event_params) where key = 'page_path') as page_path,
    (select value.string_value from unnest(event_params) where key = 'link_text') as link_text,
    (select value.string_value from unnest(event_params) where key = 'form_name') as form_name,
    traffic_source.source as session_source,
    traffic_source.medium as session_medium,
    traffic_source.name as session_campaign
  from `slkone-501222.analytics_366012577.events_*`
  where _table_suffix >= format_date('%Y%m%d', date_sub(current_date(), interval 90 day))
),

lead_events as (
  select
    user_pseudo_id,
    min(event_at) as lead_event_at,
    array_agg(page_path ignore nulls order by event_at desc limit 1)[safe_offset(0)] as lead_page_path,
    array_agg(form_name ignore nulls order by event_at desc limit 1)[safe_offset(0)] as form_name,
    array_agg(session_source ignore nulls order by event_at desc limit 1)[safe_offset(0)] as last_source,
    array_agg(session_medium ignore nulls order by event_at desc limit 1)[safe_offset(0)] as last_medium,
    array_agg(session_campaign ignore nulls order by event_at desc limit 1)[safe_offset(0)] as last_campaign
  from ga4_events
  where event_name = 'lead_form_submit'
  group by user_pseudo_id
),

content_path as (
  select
    user_pseudo_id,
    array_agg(struct(event_at, event_name, page_path, link_text) order by event_at limit 25) as pre_lead_touchpoints
  from ga4_events
  where event_name in ('page_view_enriched', 'content_download_click', 'contact_intent_click', 'scroll_depth', 'engaged_time')
  group by user_pseudo_id
),

bridge_leads as (
  select
    id as bridge_lead_id,
    name as bridge_lead_name,
    created_at as bridge_created_at,
    stage_label as bridge_stage,
    result_label as bridge_result,
    cast(metadata.website_attribution.last_touch.params.utm_source as string) as bridge_utm_source,
    cast(metadata.website_attribution.last_touch.params.utm_medium as string) as bridge_utm_medium,
    cast(metadata.website_attribution.last_touch.params.utm_campaign as string) as bridge_utm_campaign,
    cast(metadata.website_contact.email as string) as lead_email_domain
  from `slkone-501222.bridge_reporting.leads`
)

select
  le.lead_event_at,
  le.lead_page_path,
  coalesce(bl.bridge_utm_source, le.last_source) as source,
  coalesce(bl.bridge_utm_medium, le.last_medium) as medium,
  coalesce(bl.bridge_utm_campaign, le.last_campaign) as campaign,
  le.form_name,
  bl.bridge_lead_id,
  bl.bridge_lead_name,
  bl.bridge_stage,
  bl.bridge_result,
  cp.pre_lead_touchpoints
from lead_events le
left join content_path cp using (user_pseudo_id)
left join bridge_leads bl
  on bl.bridge_created_at between timestamp_sub(le.lead_event_at, interval 1 hour)
     and timestamp_add(le.lead_event_at, interval 24 hour);
