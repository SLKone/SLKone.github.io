---
layout: brand
title: The SLKone Brand
sitemap: false
---
<section id="linkedin">
    <div aria-label="download-target" class="bg-white overflow-hidden mx-auto relative" style="width: 1584px; height: 396px;">
        <canvas
            class="windmap-canvas absolute w-screen h-full left-0 z-[-1]"
            data-num-streamlines="15"
            data-num-animated="0"
            data-num-colors="1"
            data-opacity="0.3"
            data-opacity-dark="0.75"
            data-scale="0.00015"
        ></canvas>
    </div>
    <button id="download-png" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600" aria-controls="download-target">
        Download as PNG
    </button>
    <script>
    document.getElementById('download-png').addEventListener('click', function() {
        const div = document.querySelector('[aria-label="download-target"]');
        html2canvas(div).then(canvas => {
            const link = document.createElement('a');
            link.download = 'div-image.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
        });
    });
    </script>
</section>