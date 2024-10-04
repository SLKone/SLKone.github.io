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
<section id="linkedin">
    <div id="white-linkedin-bg" class="bg-white overflow-hidden mx-auto relative z-[-1] flex flex-col items-center justify-center" style="width: 1584px; height: 396px;">
        <canvas
            class="windmap-canvas absolute w-screen h-full left-0 z-0"
            data-num-streamlines="15"
            data-num-animated="0"
            data-num-colors="1"
            data-opacity="0.3"
            data-opacity-dark="0.75"
            data-scale="0.00015"
        ></canvas>
        <h2 class="text-4xl font-display text-currant">Bridge strategy to measurable success.</h2>
        <img src="{{ '/assets/images/logo_light.svg' }}" alt="{{ site.title }}" class="h-12 w-auto">
    </div>
    <button class="download-png bg-emerald dark:bg-forest text-white dark:text-currant text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 dark:hover:bg-forest-500" data-target="white-linkedin-bg">
        Download as PNG
    </button>

</section>