
const desktopOffset = 200;
const mobileOffset = 88;

/**
 * Applies smooth scrolling with an offset for anchor links.
 */
function handleAnchorClick(e) {
    const targetId = e.target.getAttribute('href');
    
    if (targetId && targetId.startsWith('#')) {
        e.preventDefault();

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const offset = window.innerWidth >= 768 ? desktopOffset : mobileOffset;
            const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;

            window.scrollTo({
                top: elementPosition - offset,
                behavior: 'smooth'
            });
        }
    }
}

/**
 * Uses event delegation to handle anchor clicks globally.
 */
function offsetAnchorLinks() {
    document.body.addEventListener('click', function(e) {
        if (e.target.tagName === 'A' && e.target.getAttribute('href').startsWith('#')) {
            handleAnchorClick(e);
        }
    });
}

/**
 * Adjusts the scroll position on page load if there's an anchor in the URL.
 */
function offsetScrollOnPageLoad() {
    if (window.location.hash) {
        const targetId = window.location.hash;
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            // Run this after the page content is fully loaded
            const offset = window.innerWidth >= 768 ? desktopOffset : mobileOffset;
            const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;

            window.scrollTo({
                top: elementPosition - offset,
                behavior: 'smooth'
            });
        }
    }
}

// Call the functions after DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    offsetAnchorLinks();
    offsetScrollOnPageLoad();
});

(function () {
  const attributionKey = 'slkone_attribution_v1';
  const trackingParams = [
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_term',
    'utm_content',
    'utm_id',
    'gclid',
    'fbclid',
    'msclkid',
    'li_fat_id'
  ];

  function getUrlParams() {
    const searchParams = new URLSearchParams(window.location.search);
    return trackingParams.reduce((params, key) => {
      const value = searchParams.get(key);
      if (value) {
        params[key] = value;
      }
      return params;
    }, {});
  }

  function getStoredAttribution() {
    try {
      return JSON.parse(window.localStorage.getItem(attributionKey)) || {};
    } catch (error) {
      return {};
    }
  }

  function saveAttribution(attribution) {
    try {
      window.localStorage.setItem(attributionKey, JSON.stringify(attribution));
    } catch (error) {
      // Storage can be unavailable in private browsing modes.
    }
  }

  function hasTrackingParams(params) {
    return Object.keys(params).length > 0;
  }

  function buildTouch(params) {
    return {
      captured_at: new Date().toISOString(),
      landing_page: window.location.href,
      landing_path: window.location.pathname,
      referrer: document.referrer || '',
      params
    };
  }

  function captureAttribution() {
    const params = getUrlParams();
    const stored = getStoredAttribution();
    const shouldUpdateLastTouch = hasTrackingParams(params) || !stored.last_touch;
    const attribution = {
      first_touch: stored.first_touch || buildTouch(params),
      last_touch: shouldUpdateLastTouch ? buildTouch(params) : stored.last_touch,
      current_page: window.location.href,
      current_path: window.location.pathname
    };

    saveAttribution(attribution);
    return attribution;
  }

  function pushDataLayer(eventName, payload) {
    window.dataLayer = window.dataLayer || [];
    const eventPayload = Object.assign({ event: eventName }, payload || {});
    window.dataLayer.push(eventPayload);

    if (window.slkoneAnalyticsUsesDirectGtag && typeof window.gtag === 'function' && eventName !== 'site_context') {
      const gtagPayload = Object.assign({}, eventPayload);
      delete gtagPayload.event;
      window.gtag('event', eventName, gtagPayload);
    }
  }

  function flattenParams(prefix, touch) {
    const params = {};
    trackingParams.forEach((key) => {
      params[`${prefix}_${key}`] = touch && touch.params ? touch.params[key] || '' : '';
    });
    params[`${prefix}_landing_page`] = touch ? touch.landing_page || '' : '';
    params[`${prefix}_landing_path`] = touch ? touch.landing_path || '' : '';
    params[`${prefix}_referrer`] = touch ? touch.referrer || '' : '';
    params[`${prefix}_captured_at`] = touch ? touch.captured_at || '' : '';
    return params;
  }

  function addHiddenInput(form, name, value) {
    let input = form.querySelector(`input[type="hidden"][name="${name}"]`);
    if (!input) {
      input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      form.appendChild(input);
    }
    input.value = value || '';
  }

  function hydrateLeadForms(attribution) {
    const values = Object.assign(
      {},
      flattenParams('first_touch', attribution.first_touch),
      flattenParams('last_touch', attribution.last_touch),
      {
        current_page: attribution.current_page || window.location.href,
        current_path: attribution.current_path || window.location.pathname
      }
    );

    document.querySelectorAll('form[data-analytics-form="lead_capture"]').forEach((form) => {
      Object.keys(values).forEach((name) => addHiddenInput(form, name, values[name]));
    });
  }

  function trackFormSubmissions() {
    document.querySelectorAll('form[data-analytics-form]').forEach((form) => {
      form.addEventListener('submit', () => {
        pushDataLayer('lead_form_submit', {
          form_name: form.dataset.formName || 'unknown',
          form_type: form.dataset.analyticsForm || 'form',
          page_path: window.location.pathname
        });
      });
    });
  }

  function trackClicks() {
    document.body.addEventListener('click', (event) => {
      const link = event.target.closest('a[href]');
      if (!link) {
        return;
      }

      const href = link.getAttribute('href');
      const linkText = link.textContent.trim().slice(0, 120);
      const isDownload = /(\.pdf|\.docx?|\.xlsx?|\.pptx?|\.csv)(\?|#|$)/i.test(href) || href.includes('/files/');
      const isContactIntent = href.startsWith('mailto:') || href.startsWith('tel:') || href.includes('/contact');

      if (isDownload) {
        pushDataLayer('content_download_click', {
          link_url: link.href,
          link_text: linkText,
          page_path: window.location.pathname
        });
      }

      if (isContactIntent) {
        pushDataLayer('contact_intent_click', {
          link_url: link.href,
          link_text: linkText,
          page_path: window.location.pathname
        });
      }
    });
  }

  function trackEngagement() {
    const scrollDepths = [25, 50, 75, 90];
    const trackedDepths = new Set();
    const trackedTimers = new Set();

    window.addEventListener('scroll', () => {
      const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (scrollableHeight <= 0) {
        return;
      }

      const depth = Math.round((window.scrollY / scrollableHeight) * 100);
      scrollDepths.forEach((threshold) => {
        if (depth >= threshold && !trackedDepths.has(threshold)) {
          trackedDepths.add(threshold);
          pushDataLayer('scroll_depth', {
            percent_scrolled: threshold,
            page_path: window.location.pathname
          });
        }
      });
    }, { passive: true });

    [30, 60, 120].forEach((seconds) => {
      window.setTimeout(() => {
        if (!trackedTimers.has(seconds)) {
          trackedTimers.add(seconds);
          pushDataLayer('engaged_time', {
            seconds,
            page_path: window.location.pathname
          });
        }
      }, seconds * 1000);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    const attribution = captureAttribution();
    hydrateLeadForms(attribution);
    trackFormSubmissions();
    trackClicks();
    trackEngagement();

    pushDataLayer('page_view_enriched', {
      page_path: window.location.pathname,
      first_touch_source: attribution.first_touch && attribution.first_touch.params ? attribution.first_touch.params.utm_source || '' : '',
      last_touch_source: attribution.last_touch && attribution.last_touch.params ? attribution.last_touch.params.utm_source || '' : ''
    });
  });
})();


// Toggle mobile menu
function toggleMobileMenu() {
    const menu = document.getElementById('mobile-navigation');
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    const header = document.getElementById('header'); // Get the header element

    menu.classList.toggle('hidden');
    menuIcon.classList.toggle('hidden');
    closeIcon.classList.toggle('hidden');

    // Lock body scroll when menu is open
    if (!menu.classList.contains('hidden')) {
        document.body.style.overflow = 'hidden'; // Lock body scroll
        header.classList.add("shadow-lg", "bg-white", "dark:bg-currant");
    } else {
        document.body.style.overflow = ''; // Unlock body scroll
        // Only remove classes if the scroll position is above the threshold
        if (window.scrollY <= topThreshold) {
            header.classList.remove("shadow-lg", "bg-white", "dark:bg-currant");
        }
    }
    
    // Ensure the menu can still scroll
    menu.style.overflowY = 'auto'; // Allow vertical scrolling in the menu
}

// Scroll add shadow to header
const topThreshold = 10;

window.addEventListener("scroll", () => {
  const header = document.getElementById('header');
  if (window.scrollY > topThreshold) {
    header.classList.add("shadow-lg", "bg-white", "dark:bg-currant");
  } else {
    header.classList.remove("shadow-lg", "bg-white", "dark:bg-currant");
  }
});

// Windmap visualization
class WindMapVisualization {
    constructor(canvas) {
      this.canvas = canvas;
      this.ctx = canvas.getContext('2d');
      this.staticCanvas = document.createElement('canvas');
      this.staticCtx = this.staticCanvas.getContext('2d');

      this.animatedStreamlines = [];
      this.animationFrame = null;
      this.isVisible = true;
      this.width = 0;
      this.height = 0;
      this.pixelRatio = 1;
      this.renderHandle = null;
      this.resizeFrame = null;

      this.isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      this.readParameters();

      this.simplex = new SimplexNoise();
      this.grid = new Uint8Array(0);
      this.gridWidth = 0;
      this.gridHeight = 0;
      this.allStreamlines = [];

      this.init();

      if (window.matchMedia) {
        const colorScheme = window.matchMedia('(prefers-color-scheme: dark)');
        const handleColorSchemeChange = e => {
          this.isDarkMode = e.matches;
          this.readParameters();
          this.scheduleRender();
        };

        if (colorScheme.addEventListener) {
          colorScheme.addEventListener('change', handleColorSchemeChange);
        } else if (colorScheme.addListener) {
          colorScheme.addListener(handleColorSchemeChange);
        }
      }
    }
  
    readParameters() {
      const dataset = this.canvas.dataset;
      const modeSuffix = this.isDarkMode ? 'Dark' : 'Light';
      const getParam = (paramName, defaultValue) => {
        const modeParam = dataset[`${paramName}${modeSuffix}`];
        if (modeParam !== undefined) {
          return modeParam;
        }
        const generalParam = dataset[paramName];
        return generalParam !== undefined ? generalParam : defaultValue;
      };

      this.animate = getParam('animate', 'true') !== 'false';
      this.numStreamlines = parseInt(getParam('numStreamlines', '150'), 10);
      this.numAnimated = parseInt(getParam('numAnimated', '5'), 10);
      this.numColors = parseInt(getParam('numColors', '3'), 10);
  
      const colorsParam = getParam('colors', null);
      this.colorValues = colorsParam
        ? colorsParam.split(';').map(color => color.trim())
        : [
            'rgb(0, 101, 72)',    // emerald
            'rgb(55, 123, 191)',  // navy
            'rgb(249, 166, 24)',  // tangerine
            'rgb(255, 213, 74)',  // mustard
            'rgb(242, 149, 106)', // sand
            'rgb(239, 81, 39)',   // cinnabar
            'rgb(193, 77, 108)',  // blush
            'rgb(247, 39, 143)',  // coral
            'rgb(130, 7, 118)',   // plum
          ];
  
      this.scale = parseFloat(getParam('scale', '0.00015'));
      this.backgroundColor = 'rgba(0, 0, 0, 0)';

      const dataOpacity = getParam('opacity', null);
      if (dataOpacity !== null) {
        this.streamlineOpacity = parseFloat(dataOpacity);
        if (isNaN(this.streamlineOpacity) || this.streamlineOpacity < 0 || this.streamlineOpacity > 1) {
          console.warn(`Invalid opacity value: ${dataOpacity}. Using default value.`);
          this.streamlineOpacity = this.isDarkMode ? 0.8 : 0.4;
        }
      } else {
        this.streamlineOpacity = this.isDarkMode ? 0.8 : 0.4;
      }

      const dataSpeed = getParam('speed', null);
      if (dataSpeed !== null) {
        this.speed = parseFloat(dataSpeed);
        if (isNaN(this.speed) || this.speed <= 0) {
          console.warn(`Invalid speed value: ${dataSpeed}. Using default speed.`);
          this.speed = 0.004;
        }
      } else {
        this.speed = 0.004;
      }

      this.streamlineParams = {
        stepSize: 4,
        maxLength: 1100,
        dSep: 8,
        gridResolution: 70,
      };

      this.MIN_STREAMLINE_LENGTH = 6;
      this.selectedColors = this.getRandomColors(this.colorValues, this.numColors);
    }
  
    getRandomColors(palette, numColors) {
      const validColors = palette.filter(color => {
        const s = new Option().style;
        s.color = color;
        if (s.color === '') {
          console.warn(`Invalid color skipped: ${color}`);
          return false;
        }
        return true;
      });
  
      if (validColors.length < numColors) {
        console.warn(`Requested ${numColors} colors, but only ${validColors.length} are valid. Using available colors.`);
      }

      return this.selectRandomItems(validColors, numColors);
    }
  
    init() {
      this.resizeCanvas();

      window.addEventListener('resize', () => {
        if (this.resizeFrame) {
          cancelAnimationFrame(this.resizeFrame);
        }

        this.resizeFrame = requestAnimationFrame(() => this.resizeCanvas());
      }, { passive: true });

      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.stopAnimation();
        } else if (this.isVisible) {
          this.startAnimation();
        }
      });

      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(entries => {
          const entry = entries[0];
          this.isVisible = entry.isIntersecting;

          if (this.isVisible) {
            this.startAnimation();
          } else {
            this.stopAnimation();
          }
        }, { rootMargin: '200px' });

        observer.observe(this.canvas);
      }
    }
  
    resizeCanvas() {
      const width = Math.round(this.canvas.clientWidth);
      const height = Math.round(this.canvas.clientHeight);

      if (!width || !height || (width === this.width && height === this.height)) {
        return;
      }

      this.width = width;
      this.height = height;
      this.pixelRatio = Math.min(window.devicePixelRatio || 1, 1.5);

      const backingWidth = Math.ceil(width * this.pixelRatio);
      const backingHeight = Math.ceil(height * this.pixelRatio);

      this.canvas.width = backingWidth;
      this.canvas.height = backingHeight;
      this.staticCanvas.width = backingWidth;
      this.staticCanvas.height = backingHeight;

      this.ctx.setTransform(this.pixelRatio, 0, 0, this.pixelRatio, 0, 0);
      this.staticCtx.setTransform(this.pixelRatio, 0, 0, this.pixelRatio, 0, 0);
      this.scheduleRender();
    }

    scheduleRender() {
      if (this.renderHandle) {
        if ('cancelIdleCallback' in window) {
          cancelIdleCallback(this.renderHandle);
        } else {
          clearTimeout(this.renderHandle);
        }
      }

      const render = () => {
        this.renderHandle = null;
        this.renderWindMap();
      };

      if ('requestIdleCallback' in window) {
        this.renderHandle = requestIdleCallback(render, { timeout: 300 });
      } else {
        this.renderHandle = setTimeout(render, 16);
      }
    }

    clearCanvas(ctx) {
      ctx.clearRect(0, 0, this.width, this.height);
    }

    renderWindMap() {
      this.clearCanvas(this.staticCtx);
  
      this.initializeGrid();
      this.allStreamlines = [];
      this.generateStreamlines();
  
      const selectedStreamlines = this.selectRandomStreamlines(this.allStreamlines, this.numStreamlines);
      this.drawStreamlines(this.staticCtx, selectedStreamlines);

      if (this.animate) {
        this.animatedStreamlines = this.selectRandomStreamlines(this.allStreamlines, this.numAnimated).map(streamline => ({
          streamline,
          progress: Math.random(),
          speed: this.speed * (0.75 + Math.random() * 0.5),
          color: this.selectedColors[Math.floor(Math.random() * this.selectedColors.length)],
        }));

        this.startAnimation();
      } else {
        this.animatedStreamlines = [];
        this.paintStaticCanvas();
      }
    }
  
    initializeGrid() {
      this.gridWidth = Math.ceil(this.width / this.streamlineParams.dSep);
      this.gridHeight = Math.ceil(this.height / this.streamlineParams.dSep);
      this.grid = new Uint8Array(this.gridWidth * this.gridHeight);
    }

    gridIndex(x, y) {
      const i = Math.floor(x / this.streamlineParams.dSep);
      const j = Math.floor(y / this.streamlineParams.dSep);

      if (i < 0 || i >= this.gridWidth || j < 0 || j >= this.gridHeight) {
        return -1;
      }

      return j * this.gridWidth + i;
    }
  
    isFarFromStreamlines(x, y) {
      const index = this.gridIndex(x, y);
      return index >= 0 && this.grid[index] < 2;
    }
  
    markPointOnGrid(x, y) {
      const index = this.gridIndex(x, y);
      if (index >= 0 && this.grid[index] < 255) {
        this.grid[index] += 1;
      }
    }
  
    getVector(x, y) {
      const scale = this.scale;
      const angle = this.simplex.noise2D(x * scale, y * scale) * Math.PI * 2;
      return {
        x: Math.cos(angle),
        y: Math.sin(angle),
      };
    }
  
    computeStreamline(x0, y0) {
      const streamline = [];
      let x = x0;
      let y = y0;
  
      streamline.push({ x, y });
      this.markPointOnGrid(x, y);
  
      for (let i = 1; i < this.streamlineParams.maxLength; i++) {
        const vector = this.getVector(x, y);
  
        x += vector.x * this.streamlineParams.stepSize;
        y += vector.y * this.streamlineParams.stepSize;
  
        if (x < 0 || x > this.width || y < 0 || y > this.height) {
          break;
        }
  
        if (!this.isFarFromStreamlines(x, y)) {
          break;
        }

        streamline.push({ x, y });
        this.markPointOnGrid(x, y);
      }
  
      return streamline;
    }
  
    generateStreamlines() {
      const seeds = [];
      const spacing = this.streamlineParams.gridResolution;
  
      for (let x = spacing / 2; x < this.width; x += spacing) {
        for (let y = spacing / 2; y < this.height; y += spacing) {
          seeds.push({
            x: x + (Math.random() - 0.5) * spacing * 0.5,
            y: y + (Math.random() - 0.5) * spacing * 0.5,
          });
        }
      }
  
      for (const seed of this.selectRandomItems(seeds, seeds.length)) {
        if (this.isFarFromStreamlines(seed.x, seed.y)) {
          const streamline = this.computeStreamline(seed.x, seed.y);
          if (streamline.length >= this.MIN_STREAMLINE_LENGTH) {
            this.allStreamlines.push(streamline);
          }
        }
      }
    }
  
    drawStreamlines(ctx, selectedStreamlines) {
      ctx.save();
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      selectedStreamlines.forEach(streamline => {
        if (streamline.length >= this.MIN_STREAMLINE_LENGTH) {
          const color = this.selectedColors[Math.floor(Math.random() * this.selectedColors.length)];
          const lineWidth = 0.45 + Math.random() * 1.25;

          ctx.strokeStyle = color;
  
          for (let i = 1; i < streamline.length; i++) {
            const start = streamline[i - 1];
            const end = streamline[i];
            const t = i / (streamline.length - 1);
            const fadeLength = 0.16;
            let opacity = 1;

            if (t < fadeLength) {
              opacity = t / fadeLength;
            } else if (t > 1 - fadeLength) {
              opacity = (1 - t) / fadeLength;
            }

            ctx.globalAlpha = opacity * this.streamlineOpacity;
            ctx.lineWidth = lineWidth * (0.8 + opacity * 0.2);
  
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
          }
        }
      });

      ctx.restore();
    }

    selectRandomItems(items, numToSelect) {
      const selected = items.slice();
      const count = Math.min(Math.max(numToSelect, 0), selected.length);

      for (let i = 0; i < count; i++) {
        const randomIndex = i + Math.floor(Math.random() * (selected.length - i));
        const current = selected[i];
        selected[i] = selected[randomIndex];
        selected[randomIndex] = current;
      }

      return selected.slice(0, count);
    }

    selectRandomStreamlines(streamlines, numToSelect) {
      return this.selectRandomItems(streamlines, numToSelect);
    }
  
    drawAnimatedStreamline(ctx, animatedStreamline) {
      const streamline = animatedStreamline.streamline;
      const progress = animatedStreamline.progress;
      const windowSize = 0.16;
      const color = animatedStreamline.color;
  
      if (streamline.length >= this.MIN_STREAMLINE_LENGTH) {
        ctx.save();
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.lineWidth = 1.3;
        ctx.strokeStyle = color;
  
        for (let i = 1; i < streamline.length; i++) {
          const start = streamline[i - 1];
          const end = streamline[i];
          const t = i / (streamline.length - 1);
          let distance = Math.abs(t - progress);

          if (distance > 0.5) {
            distance = 1 - distance;
          }

          const opacity = distance < windowSize / 2 ? 1 - (distance / (windowSize / 2)) : 0;
  
          if (opacity > 0) {
            ctx.globalAlpha = opacity * this.streamlineOpacity;
  
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
          }
        }

        ctx.restore();
      }
    }

    paintStaticCanvas() {
      this.clearCanvas(this.ctx);
      this.ctx.drawImage(this.staticCanvas, 0, 0, this.width, this.height);
    }

    startAnimation() {
      if (!this.animate || !this.isVisible || document.hidden || this.animationFrame || !this.animatedStreamlines.length) {
        if (!this.animate || !this.animatedStreamlines.length) {
          this.paintStaticCanvas();
        }
        return;
      }

      const animationLoop = () => {
        this.paintStaticCanvas();

        this.animatedStreamlines.forEach(animatedStreamline => {
          animatedStreamline.progress += animatedStreamline.speed;
          if (animatedStreamline.progress > 1) {
            animatedStreamline.progress -= 1;
          }

          this.drawAnimatedStreamline(this.ctx, animatedStreamline);
        });

        this.animationFrame = requestAnimationFrame(animationLoop);
      };

      this.animationFrame = requestAnimationFrame(animationLoop);
    }

    stopAnimation() {
      if (this.animationFrame) {
        cancelAnimationFrame(this.animationFrame);
        this.animationFrame = null;
      }
    }
  }
  
  // Initialize the visualization for each canvas element with class 'windmap-canvas'
  document.querySelectorAll('.windmap-canvas').forEach(canvas => {
    new WindMapVisualization(canvas);
  });
  
