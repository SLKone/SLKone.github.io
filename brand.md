---
layout: brand
title: The SLKone Brand
sitemap: false
---
<section id="toc" class="container mx-auto max-w-7xl py-20">
    <h2 class="text-4xl mb-12 font-display">SLKone Brand Assets</h2>
    <ul class="prose dark:prose-invert">
        <li><a href="#logo-downloads">Logo Files</a></li>
        <li><a href="#color-palette">Color Palette</a></li>
        <li><a href="#email-signatures">Email Signatures</a></li>
        <li><a href="#linkedin">LinkedIn Banners</a></li>
    </ul>
</section>
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
<script>
    function copyToClipboard(targetId) {
        const element = document.getElementById(targetId);
        if (element) {
            const text = element.innerText; // Get inner text content
            navigator.clipboard.writeText(text).then(() => {
                alert(`Copied: ${text}`);
            });
        } else {
            alert('Element not found');
        }
    }
</script>
<section id="logo-downloads" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Logo Files</h2>
    <div class="grid grid-cols-2 gap-8">
        {% assign logos = "Primary Lock up – Primary,Primary Lock up – Dark Green,Primary Lock up – Light Green,Primary Lock up – Black,Primary Lock up – White,Mark - Black,Mark – White,Mark – Dark Green,Mark – Light Green,Vertical Lockup – Black,Vertical Lockup – Dark Green,Vertical Lockup – Light Green,Vertical Lockup – Primary,Vertical Lockup – White" | split: "," %}
        {% for logo in logos %}
        <div class="mb-8 bg-slate-100 dark:bg-currant-300 p-8 rounded-xl text-center">
            <img src="{{ '/assets/images/logo/svg/' | append: logo | append: '.svg' }}" alt="{{ logo }}" class="h-32 w-auto mx-auto">
            <h3 class="py-4 text-xl">{{ logo }}</h3>
            <div>
            Download: <a class="text-emerald dark:text-forest" href="{{ '/assets/images/logo/svg/' | append: logo | append: '.svg' }}">SVG</a> | <a class="text-emerald dark:text-forest" href="{{ '/assets/images/logo/png/' | append: logo | append: '.png' }}">PNG</a>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
<section id="color-palette" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Color Palette</h2>
    <div class="grid grid-cols-1 gap-8">
        {% assign colors = site.data.colors %}
        {% for color in colors %}
            <div class="flex items-center p-4 cursor-pointer">
                {% assign color_name = color[0] %}
                {% for shade in color %}
                    <div class="flex items-center mr-4">
                        <div class="bg-{{ color_name | downcase }}-{{ shade.shade }} text-black p-8 rounded-xl"></div>
                        <span class="ml-2">{{ color_name | capitalize }} {{ shade.shade }}: </span>
                        <button id="{{ color_name | capitalize }}-{{ shade.shade }}-hex" class="ml-2" onclick="copyToClipboard('{{ color_name | capitalize }}-{{ shade.shade }}-hex')">{{ shade.hex }}</button> 
                        <button id="{{ color_name | capitalize }}-{{ shade.shade }}-rgb" class="ml-2" onclick="copyToClipboard('{{ color_name | capitalize }}-{{ shade.shade }}-rgb')">{{ shade.rgb }}</button> 
                        <button id="{{ color_name | capitalize }}-{{ shade.shade }}-hsl" class="ml-2" onclick="copyToClipboard('{{ color_name | capitalize }}-{{ shade.shade }}-hsl')">{{ shade.hsl }}</button>
                    </div>
                {% endfor %}
            </div>
        {% endfor %}
    </div>
</section>

<section id="email-signatures" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Email Signatures</h2>
    <div class="flex flex-col mb-8">
        <h3 class="text-xl mb-4">Email Signatures</h3>
        <div class="mb-4">
            <label for="first-name" class="block">First Name:</label>
            <input type="text" id="first-name" class="border p-2 w-full text-currant" placeholder="First Name" oninput="updateSignature()">
        </div>
        <div class="mb-4">
            <label for="last-name" class="block">Last Name:</label>
            <input type="text" id="last-name" class="border p-2 w-full text-currant" placeholder="Last Name" oninput="updateSignature()">
        </div>
        <div class="mb-4">
            <label for="position" class="block">Position:</label>
            <input type="text" id="position" class="border p-2 w-full text-currant" placeholder="Position" oninput="updateSignature()">
        </div>
        <div class="mb-4">
            <label for="email" class="block">Email:</label>
            <input type="email" id="email" class="border p-2 w-full text-currant" placeholder="Email" oninput="updateSignature()">
        </div>
        <div class="mb-4">
            <label for="phone" class="block">Phone:</label>
            <input type="text" id="phone" class="border p-2 w-full text-currant" placeholder="Phone Number" oninput="updateSignature()">
        </div>
        <button class="bg-emerald text-white p-2 rounded mt-4" onclick="copyToClipboard('with-logo')">Copy Signature with Logo HTML</button>
        <button class="bg-emerald text-white p-2 rounded mt-4" onclick="copyToClipboard('without-logo')">Copy Signature without Logo HTML</button>
    </div>
    <script>
        function updateSignatures() {
            const firstName = document.getElementById('first-name').value.trim();
            const lastName = document.getElementById('last-name').value.trim();
            const position = document.getElementById('position').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();

            if (firstName && lastName) {
                document.getElementById('with-logo-name').innerText = `${firstName} ${lastName}`;
                document.getElementById('without-logo-name').innerText = `${firstName} ${lastName}`;
            } else {
                document.getElementById('with-logo-name').innerText = 'First Last';
                document.getElementById('without-logo-name').innerText = 'First Last';
            }

            document.getElementById('with-logo-position').innerText = position ? `${position} | SLKone, LLC` : 'Title | SLKone, LLC';
            document.getElementById('without-logo-position').innerText = position ? `${position} | SLKone, LLC` : 'Title | SLKone, LLC';

            document.getElementById('with-logo-email').innerText = email || 'email@slkone.com';
            document.getElementById('without-logo-email').innerText = email || 'email@slkone.com';

            document.getElementById('with-logo-phone').innerText = phone || '(XXX) XXX-XXXX';
            document.getElementById('without-logo-phone').innerText = phone || '(XXX) XXX-XXXX';
        }
    </script>
    <div id="with-logo">
    <table id="email" width="340" cellspacing="0" cellpadding="0" border="0">
        <tr style="border:0;padding:0;">
            <td style="border:0;padding:0;">
                <table cellspacing="0" cellpadding="0" border="0">
                    <tr style="border:0;padding:0;">
                        <td valign="top" width="140" height="72" style="padding:0 24px 0 0; vertical-align: middle; border:0;">
                            <a href="http://slk.one" target="_blank"><img alt="SLKone" width="116" height="72px" style="margin-right: 24px;width:116px; height: 72px; vertical-align: middle;" src="https://slkone.com/assets/images/logo/email.png" /></a>
                        </td>
                        <td style="padding:0 15px 0 24px;vertical-align: top; border:0; border-left: 1px solid #5DBC5B;" valign="top">
                            <table cellspacing="0" cellpadding="0" border="0" style="line-height: 1.1;">
                                <tr style="border:0;padding:0;">
                                    <td style="border:0;padding:0;">
                                        <div id="with-logo-name" style="font: 15px arial, helvetica, sans-serif;color:#161A41;">First Last</div>
                                    </td>
                                </tr>
                                <tr style="border:0;padding:0;">
                                    <td style="padding: 4px 0 12px;border:0;">
                                        <div id="with-logo-position" style="font: 11px arial, helvetica, sans-serif;color:#161A41;">Title | SLKone, LLC</div>
                                    </td>
                                </tr>
                                <tr style="padding: 0;border:0;">
                                    <td style="border:0;padding:0;">
                                        <div id="with-logo-phone" style="color: #5DBC5B;border:0;padding:0;font: 11px arial, helvetica, sans-serif;text-decoration: none;">(XXX) XXX-XXXX</div>
                                    </td>
                                </tr>
                                <tr style="padding: 0;border:0;">
                                    <td style="border:0;padding:0;">
                                        <div id="with-logo-email" style="color: #5DBC5B;border:0;padding:0;font: 11px arial, helvetica, sans-serif;text-decoration: none;">email@slkone.com</div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</div>
<div id="without-logo">
    <table id="email" width="340" cellspacing="0" cellpadding="0" border="0">
        <tr style="border:0;padding:0;">
            <td style="border:0;padding:0;">
                <table cellspacing="0" cellpadding="0" border="0" style="line-height: 1.1;">
                    <tr style="border:0;padding:0;">
                        <td style="border:0;padding:0;">
                            <div id="without-logo-name" style="font: 15px arial, helvetica, sans-serif;color:#161A41;">First Last</div>
                        </td>
                    </tr>
                    <tr style="border:0;padding:0;">
                        <td style="padding: 4px 0 12px;border:0;">
                            <div id="without-logo-position" style="font: 11px arial, helvetica, sans-serif;color:#161A41;">Title | SLKone, LLC</div>
                        </td>
                    </tr>
                    <tr style="padding: 0;border:0;">
                        <td style="border:0;padding:0;">
                            <div id="without-logo-phone" style="color: #5DBC5B;border:0;padding:0;font: 11px arial, helvetica, sans-serif;text-decoration: none;">(XXX) XXX-XXXX</div>
                        </td>
                    </tr>
                    <tr style="padding: 0;border:0;">
                        <td style="border:0;padding:0;">
                            <div id="without-logo-email" style="color: #5DBC5B;border:0;padding:0;font: 11px arial, helvetica, sans-serif;text-decoration: none;">email@slkone.com</div>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</div>
</section>
<section id="linkedin" class="flex flex-col justify-center items-center py-20">
    <div class="container mx-auto max-w-7xl">
        <h2 class="text-4xl mb-12 font-display">LinkedIn Banners</h2>
        <div class="mb-8 w-full">
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
