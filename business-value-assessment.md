---
layout: default
title: Business Value Assessment
subtitle: "A focused way to identify where value is available, what it would take to capture it, and whether the next phase is worth pursuing."
permalink: /business-value-assessment
background_image: "/assets/images/backgrounds/strategy.webp"
color: "tangerine"
redirect_from:
  - /restart/
  - /restart
---

<section class="relative overflow-hidden min-h-[64dvh] flex items-center bg-currant text-white">
  <canvas
    class="windmap-canvas absolute inset-0 w-full h-full z-0"
    data-num-streamlines="90"
    data-num-animated="14"
    data-num-colors="3"
    data-opacity="0.28"
    data-opacity-dark="0.6"
    data-scale="0.00015"
  ></canvas>
  <div class="absolute inset-0 z-10 bg-gradient-to-b from-currant/70 via-currant/80 to-currant"></div>
  <div class="container relative z-20 mx-auto px-8 max-w-7xl py-24 lg:py-32">
    <p class="text-sm uppercase font-bold text-forest mb-5">Value Assessment</p>
    <h1 class="text-5xl lg:text-7xl font-display max-w-5xl mb-8">Find the credible path to measurable value.</h1>
    <p class="text-xl md:text-2xl max-w-3xl">{{ page.subtitle }}</p>
    <div class="mt-12 grid md:grid-cols-3 gap-px bg-white/20 max-w-5xl">
      <div class="bg-currant/70 backdrop-blur-sm p-6">
        <p class="text-sm font-bold text-forest mb-3">Decision</p>
        <p>Where is the value, and is it worth pursuing?</p>
      </div>
      <div class="bg-currant/70 backdrop-blur-sm p-6">
        <p class="text-sm font-bold text-forest mb-3">Work</p>
        <p>Interviews, data review, operating-model assessment, sizing, and sequencing.</p>
      </div>
      <div class="bg-currant/70 backdrop-blur-sm p-6">
        <p class="text-sm font-bold text-forest mb-3">Output</p>
        <p>A practical recommendation on what to do next, what to build, and what proof should matter.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-20">
  <div class="container mx-auto px-8 max-w-7xl">
    <div class="grid md:grid-cols-2 gap-12">
      <div class="md:text-xl">
        <h2 class="text-4xl font-display mb-6">When It Helps</h2>
        <p class="mb-6">A Business Value Assessment is useful when leadership sees opportunity but needs sharper facts, clearer tradeoffs, and a practical path before committing to a larger effort.</p>
        <p>It is also a useful entry point when a team wants to test whether AI, analytics, automation, operating model changes, pricing, process improvement, or value creation work can produce measurable impact.</p>
      </div>
      <div class="rounded-xl bg-slate-50 dark:bg-currant-500 p-8">
        <h3 class="text-3xl font-display mb-6">Typical Questions</h3>
        <ul class="space-y-4">
          <li>Where is the most credible value pool?</li>
          <li>What decisions need to be made before work begins?</li>
          <li>What data, process, system, or organizational constraints matter?</li>
          <li>Which initiatives should be prioritized, sequenced, or stopped?</li>
          <li>What would a next phase need to prove?</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="py-20 bg-slate-50 dark:bg-currant-500">
  <div class="container mx-auto px-8 max-w-7xl">
    <h2 class="text-4xl font-display mb-12">What the Assessment Produces</h2>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="rounded-xl bg-white dark:bg-currant p-8">
        <h3 class="text-2xl font-display mb-3">Value Hypothesis</h3>
        <p>A clear view of the likely value pools, evidence quality, assumptions, and expected business impact.</p>
      </div>
      <div class="rounded-xl bg-white dark:bg-currant p-8">
        <h3 class="text-2xl font-display mb-3">Execution Path</h3>
        <p>A practical plan for the work required, including owners, dependencies, operating cadence, and likely constraints.</p>
      </div>
      <div class="rounded-xl bg-white dark:bg-currant p-8">
        <h3 class="text-2xl font-display mb-3">Decision Recommendation</h3>
        <p>A recommendation on whether to proceed, where to focus first, and what proof a next phase should produce.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-20">
  <div class="container mx-auto px-8 max-w-7xl">
    <div class="max-w-prose md:text-xl">
      <h2 class="text-4xl font-display mb-6">How We Run It</h2>
      <p class="mb-6">We keep the assessment practical: targeted interviews, working sessions, data and artifact review, operating-model assessment, opportunity sizing, and a direct readout with leadership.</p>
      <p>The output is designed to help the team decide what to do next. Sometimes that means launching a larger implementation effort. Sometimes it means narrowing the scope, changing sequencing, or deciding not to proceed.</p>
    </div>
  </div>
</section>

{% include proof-cases.html
  title="Relevant Proof"
  description="Examples of value identification, analytics, transaction support, and operating improvement."
  cases=site.data.homepage.proof.case_studies
%}

{% include contact-card.html
  background_image=site.data.homepage.contact.background-image
  title="Want a sharper view of the opportunity?"
  description="Use a Business Value Assessment to clarify where value exists, what it would take to capture it, and whether the next phase is worth pursuing."
  cta_link="/contact"
  cta_text="Request an Assessment"
%}
