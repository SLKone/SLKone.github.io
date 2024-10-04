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
<section id="linkedin" class="flex flex-col justify-center items-center py-8">
    <h2 class="text-4xl mb-12 font-display">LinkedIn Backgrounds</h2>
    <div class="mb-8" style="width: 1584px; height: 396px;">
        <div id="white-linkedin-bg" class="bg-white overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right" style="width: 1584px; height: 396px;">
            <canvas
                class="windmap-canvas absolute w-screen h-full left-0 z-0"
                data-num-streamlines="100"
                data-num-animated="0"
                data-num-colors="3"
                data-opacity="0.3"
                data-scale="0.00015"
            ></canvas>
            <h2 class="text-6xl font-display text-currant mr-8 z-10 ml-[400px] text-right">Bridge strategy to measurable success</h2>
            <img src="{{ '/assets/images/logo_light.svg' }}" alt="{{ site.title }}" class="h-32 w-auto z-10 ">
        </div>
    </div>
    <button class="download-png bg-emerald dark:bg-forest text-white dark:text-currant text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 dark:hover:bg-forest-500 mb-8" data-target="white-linkedin-bg">
        Download as PNG
    </button>
    <div class="mb-8" style="width: 1584px; height: 396px;">
        <div id="currant-linkedin-bg" class="bg-currant overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right" style="width: 1584px; height: 396px;">
            <canvas
                class="windmap-canvas absolute w-screen h-full left-0 z-0"
                data-num-streamlines="100"
                data-num-animated="0"
                data-num-colors="3"
                data-opacity="0.3"
                data-scale="0.00015"
            ></canvas>
            <h2 class="text-6xl font-display text-white mr-8 z-10 ml-[400px] text-right">Bridge strategy to measurable success</h2>
            <img src="{{ '/assets/images/logo_dark.svg' }}" alt="{{ site.title }}" class="h-32 w-auto z-10 ">
        </div>
    </div>
    <button class="download-png bg-emerald dark:bg-forest text-white dark:text-currant text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 dark:hover:bg-forest-500 mb-8" data-target="currant-linkedin-bg">
        Download as PNG
    </button>
</section>