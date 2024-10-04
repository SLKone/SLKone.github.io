---
layout: brand
title: The SLKone Brand
sitemap: false
---
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('download-png')) {
        const targetId = event.target.getAttribute('data-target');
        const div = document.getElementById(targetId);
        
        if (div) {
            html2canvas(div).then(canvas => {
                const link = document.createElement('a');
                link.download = `${targetId}-image.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
            });
        }
    }
});
</script>
<section id="logo-downloads" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Download Logo Variants</h2>
    <div class="grid grid-cols-2 gap-8 prose dark:prose-invert">
        {% assign logos = "Mark - Black,Mark – White,Mark – Dark Green,Mark – Light Green,Primary Lock up – Black,Primary Lock up – Dark Green,Primary Lock up – Light Green,Primary Lock up – Primary,Primary Lock up – White,Vertical Lockup – Black,Vertical Lockup – Dark Green,Vertical Lockup – Light Green,Vertical Lockup – Primary,Vertical Lockup – White" | split: "," %}
        {% for logo in logos %}
        <div class="mb-8 bg-slate-100 dark:bg-currant-300 p-8 rounded-xl">
            <h3 class="text-2xl font-display">{{ logo }}</h3>
            <img src="{{ '/assets/images/logo/svg/' | append: logo | append: '.svg' }}" alt="{{ logo }}" class="h-32 w-auto">
            <div class="mt-2">
                <a href="{{ '/assets/images/logo/svg/' | append: logo | append: '.svg' }}">Download SVG</a>
                <a href="{{ '/assets/images/logo/png/' | append: logo | append: '.png' }}">Download PNG</a>
                <a href="{{ '/assets/images/logo/jpg/' | append: logo | append: '.jpg' }}">Download JPG</a>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
<section id="linkedin" class="flex flex-col justify-center items-center py-20">
    <h2 class="text-4xl mb-12 font-display">LinkedIn Banners</h2>
    <div class="mb-8 w-full flex justify-center">
        <form id="banner-text-form" class="flex flex-col items-center w-1/2">
            <label for="banner-text" class="mb-2 text-lg">Update Banner Text:</label>
            <input 
                type="text" 
                id="banner-text" 
                name="banner-text" 
                class="w-full p-2 border border-gray-300 rounded" 
                placeholder="Enter new banner text"
            >
        </form>
    </div>
    <div class="mb-8" style="width: 1584px; height: 396px;">
        <div id="white-linkedin-bg" class="bg-white overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right w-[1584px] h-[396px]" style="width: 1584px; height: 396px;">
            <canvas
                class="windmap-canvas absolute w-screen h-full left-0 z-0"
                data-num-streamlines="100"
                data-num-animated="0"
                data-num-colors="3"
                data-opacity="0.3"
                data-scale="0.00015"
            ></canvas>
            <h2 class="linkedin-banner-text text-5xl font-display text-currant mr-16 z-10 ml-[400px] text-right" style="text-align:right">Bridge strategy to measurable success</h2>
            <img src="{{ '/assets/images/logo_light.svg' }}" alt="{{ site.title }}" class="h-32 w-auto z-10 ">
        </div>
    </div>
    <button class="download-png bg-emerald dark:bg-forest text-white dark:text-currant text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 dark:hover:bg-forest-500 mb-8" data-target="white-linkedin-bg">
        Download as PNG
    </button>
    <div class="mb-8" style="width: 1584px; height: 396px;">
        <div id="currant-linkedin-bg" class="bg-currant overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right w-[1584px] h-[396px]" style="width: 1584px; height: 396px;">
            <canvas
                class="windmap-canvas absolute w-screen h-full left-0 z-0"
                data-num-streamlines="100"
                data-num-animated="0"
                data-num-colors="3"
                data-opacity="0.75"
                data-scale="0.00015"
            ></canvas>
            <h2 class="linkedin-banner-text text-5xl font-display text-white mr-16 z-10 ml-[400px] text-right" style="text-align:right">Bridge strategy to measurable success</h2>
            <img src="{{ '/assets/images/logo_dark.svg' }}" alt="{{ site.title }}" class="h-32 w-auto z-10 ">
        </div>
    </div>
    <button class="download-png bg-emerald dark:bg-forest text-white dark:text-currant text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 dark:hover:bg-forest-500 mb-8" data-target="currant-linkedin-bg">
        Download as PNG
    </button>
    <script>
        document.getElementById('banner-text').addEventListener('input', function(event) {
            const newText = event.target.value;
            const bannerTexts = document.querySelectorAll('.linkedin-banner-text');
            bannerTexts.forEach(function(h2) {
                h2.textContent = newText;
            });
        });
    </script>
</section>

