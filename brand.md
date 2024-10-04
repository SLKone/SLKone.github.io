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
            const range = document.createRange();
            range.selectNodeContents(element);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            document.execCommand('copy');
            alert(`Copied: ${element.innerHTML}`);
        } else {
            alert('Element not found');
        }
    }
</script>
<section id="logo-downloads" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Logo Files</h2>
    <p class="mb-8 text-xl">Download the logo files for use anywhere you need the SLKone logo.</p>
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
    <p class="mb-8 text-xl">Use the color palette to select the color you want to use. The color name, hex value, rgb value, and hsl value are all linked to the color. Click on the color to copy the value to your clipboard.</p>
    <div class="grid grid-cols-1 gap-8">
        {% assign colors = site.data.colors.colors %}
        {% for color in colors %}
            <div class="flex items-center">
                {% assign color_name = color.color %}
                {% for shade in color.shades %}
                    <div class="text-center">
                        <div class="bg-{{ color_name | downcase }}-{{ shade.shade }} w-full h-20 block cursor-pointer mb-2" onclick="copyToClipboard('{{ color_name }}-{{ shade.shade }}-hex')"></div>
                        <span class="ml-2 text-sm block">{{ color_name | upcase }}-{{ shade.shade }}</span>
                        <a href="#" class="ml-2 text-sm block" onclick="copyToClipboard('{{ color_name }}-{{ shade.shade }}-hex')">#<span id="{{ color_name }}-{{ shade.shade }}-hex">{{ shade.hex }}</span></a> 
                        <a href="#" class="ml-2 text-sm block" onclick="copyToClipboard('{{ color_name }}-{{ shade.shade }}-rgb')">RGB(<span id="{{ color_name }}-{{ shade.shade }}-rgb">{{ shade.rgb }}</span>)</a> 
                        <a href="#" class="ml-2 text-sm block" onclick="copyToClipboard('{{ color_name }}-{{ shade.shade }}-hsl')">HSL(<span id="{{ color_name }}-{{ shade.shade }}-hsl">{{ shade.hsl }}</span>)</a>
                    </div>
                {% endfor %}
            </div>
        {% endfor %}
    </div>
</section>

<section id="email-signatures" class="py-20 container mx-auto max-w-7xl">
    <h2 class="text-4xl mb-12 font-display">Email Signatures</h2>
    <div class="flex flex-col mb-8">
        <h3 class="text-xl mb-4">Update the signature based on your information and then paste into the signature editor in outlook </h3>
        <div class="grid grid-cols-2 gap-8">
            <div>
                <label for="first-name" class="block">First Name:</label>
                <input type="text" id="first-name" class="border p-2 w-full text-currant" placeholder="First Name" oninput="updateSignature()">
            </div>
            <div>
                <label for="last-name" class="block">Last Name:</label>
                <input type="text" id="last-name" class="border p-2 w-full text-currant" placeholder="Last Name" oninput="updateSignature()">
            </div>
            <div>
                <label for="position" class="block">Position:</label>
                <input type="text" id="position" class="border p-2 w-full text-currant" placeholder="Position" oninput="updateSignature()">
            </div>
            <div>
                <label for="email" class="block">Email:</label>
                <input type="email" id="email" class="border p-2 w-full text-currant" value="email@slkone.com" oninput="updateSignature()" required>
            </div>
            <div>
                <label for="phone" class="block">Phone:</label>
                <input type="text" id="phone" class="border p-2 w-full text-currant" placeholder="(XXX) XXX-XXXX" oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\d{3})(\d)/, '($1) $2').replace(/(\d{3})(\d{4})$/, '$1-$2'); updateSignature();">
            </div>
        </div>
    </div>
    <div class="grid grid-cols-2 gap-8">
        <div class="mb-4">
            <div id="with-logo" class="bg-white p-8 rounded-xl">
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
            <button class="bg-emerald text-white p-2 rounded mt-4" onclick="copyToClipboard('with-logo')">Copy Signature with Logo HTML</button>
        </div>
        <div class="mb-4">
            <div id="without-logo" class="bg-white p-8 rounded-xl">
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
            <button class="bg-emerald text-white p-2 rounded mt-4" onclick="copyToClipboard('without-logo')">Copy Signature without Logo HTML</button>
        </div>
    </div>
    <script>
        function updateSignature() {
            const firstName = document.getElementById('first-name').value;
            const lastName = document.getElementById('last-name').value;
            const position = document.getElementById('position').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;

            document.getElementById('with-logo-name').innerText = `${firstName} ${lastName}`;
            document.getElementById('with-logo-position').innerText = `${position} | SLKone, LLC`;
            document.getElementById('with-logo-phone').innerText = phone || '(XXX) XXX-XXXX';
            document.getElementById('with-logo-email').innerText = email || 'email@slkone.com';

            document.getElementById('without-logo-name').innerText = `${firstName} ${lastName}`;
            document.getElementById('without-logo-position').innerText = `${position} | SLKone, LLC`;
            document.getElementById('without-logo-phone').innerText = phone || '(XXX) XXX-XXXX';
            document.getElementById('without-logo-email').innerText = email || 'email@slkone.com';
        }
    </script>
</section>
<section id="linkedin" class="flex flex-col justify-center items-center py-20">
    <div class="container mx-auto max-w-7xl">
        <h2 class="text-4xl mb-12 font-display">LinkedIn Banners</h2>
        <div class="mb-8 w-full">
            <form id="banner-text-form" class="w-1/2">
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
        <div class="mb-8">
            <label for="background-selector" class="mb-2 text-lg">Select Background:</label>
            <select id="background-selector" class="w-full p-2 border border-gray-300 rounded">
                <option value="white" data-logo="{{ '/assets/images/logo/png/Primary Lock up – Primary.png' }}" data-text-color="text-currant">White</option>
                <option value="currant" data-logo="{{ '/assets/images/logo/png/Primary Lock up – Light Green.png' }}" data-text-color="text-white">Currant</option>
            </select>
        </div>
    </div>
    <div class="mb-8" style="width: 1584px; height: 396px;">
        <div id="linkedin-bg" class="bg-white overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right w-[1584px] h-[396px]">
            <canvas
                class="windmap-canvas absolute w-screen h-full left-0 z-0"
                data-num-streamlines="100"
                data-num-animated="0"
                data-num-colors="3"
                data-opacity="0.3"
                data-scale="0.00015"
            ></canvas>
            <h2 id="linkedin-banner-text" class="linkedin-banner-text text-currant mr-16 z-10 ml-[400px] text-right absolute mr-[256px]" style="text-align:right">Bridge strategy to measurable success</h2>
            <img id="linkedin-logo" src="{{ '/assets/images/logo/png/Primary Lock up – Primary.png' }}" alt="{{ site.title }}" class="h-32 w-auto z-10 absolute">
        </div>
    </div>
    <button class="download-png bg-emerald text-white text-2xl transition-all p-4 rounded-full px-8 duration-300 hover:bg-emerald-500 mb-8" data-target="linkedin-bg">
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

        document.getElementById('background-selector').addEventListener('change', function(event) {
            const selectedOption = event.target.options[event.target.selectedIndex];
            const bgColor = selectedOption.value;
            const logoSrc = selectedOption.getAttribute('data-logo');
            const textColorClass = selectedOption.getAttribute('data-text-color');

            const linkedinBg = document.getElementById('linkedin-bg');
            linkedinBg.className = `overflow-hidden relative z-[-1] flex flex-row items-center justify-end p-16 text-right w-[1584px] h-[396px] bg-${bgColor}`;

            const linkedinLogo = document.getElementById('linkedin-logo');
            linkedinLogo.src = logoSrc;

            const linkedinBannerText = document.getElementById('linkedin-banner-text');
            linkedinBannerText.className = `linkedin-banner-text ${textColorClass} mr-16 z-10 ml-[400px] text-right absolute mr-[256px]`;
        });
    </script>
</section>
