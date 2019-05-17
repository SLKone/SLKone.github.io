---
layout: collections
title: "SLKone's Expertise"
subtitle: "Our Expertise and Industries of Focus"
intro: "We have a range of experience building and implementing solutions within a variety of service areas."
heroimage: "expertise.jpg"
permalink: "/expertise/"
---

<div id="leadership-and-strategy" class="service-line">
<h4>Leadership and Strategy</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'leadership-and-strategy' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>

<div id="Operational-Excellence-and-Execution" class="service-line">
<h4>Operational Excellence and Execution</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Operational-Excellence-and-Execution' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>

<div id="Organization-and-Human-Capital" class="service-line">
<h4>Organization and Human Capital</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Organization-and-Human-Capital' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>

<div id="Revenue-and-Sales" class="service-line">
<h4>Revenue and Sales</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Revenue-and-Sales' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>
<div id="Data-Analytics-and-Decision-Science" class="service-line">
<h4>Data Analytics and Decision Science</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Data-Analytics-and-Decision-Science' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>
<div id="Information-Technology-and-Digital-Strategy" class="service-line">
<h4>Information Technology and Digital Strategy</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Information-Technology-and-Digital-Strategy' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>
<div id="Oversight-and-Event-Driven-Expertise" class="service-line">
<h4>Oversight and Event-Driven Expertise</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Oversight-and-Event-Driven-Expertise' %}
    {% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>
<div id="Finance-and-Accounting" class="service-line">
<h4>Finance and Accounting</h4>
<ul>
  {% for service in site.services %}
	  {% if service.categories contains 'Finance-and-Accounting' %}
		{% include service-list.html %}
     {% endif %}
  {% endfor %}
</ul>
</div>