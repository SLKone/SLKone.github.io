# Article image system

SLKone article artwork should feel like part of the same visual family as the service pages while giving each article one distinct visual idea.

## Visual language

- Square, abstract editorial artwork with a strong silhouette that survives `background-size: cover` at both hero and card sizes.
- Visible canvas grain, dry-brush texture, layered paint, restrained geometric lines, and occasional circular accents.
- Deep navy, dark currant, forest green, muted sage, warm cream, dusty peach, and sparing ochre accents.
- One metaphor per article, expressed through motion, balance, convergence, structure, or contrast.
- No embedded text, numbers, logos, watermarks, dashboards, stock-photo scenes, glossy 3D rendering, or generic corporate vector art.
- Prefer nonfigurative abstraction. Use people only when the article is specifically a profile or interview and a portrait is more useful than an abstract metaphor.

## Production specification

- Source canvas: square, at least 1254 by 1254 pixels.
- Site asset: WebP at quality 90.
- Filename: preserve the article image basename and append `-v2.webp`.
- Keep the original image in place during the rollout so every replacement is reversible.
- Update only the article's `background_image` frontmatter after the replacement passes review.

## Base generation prompt

Use case: `stylized-concept`

Asset type: square editorial hero image for an SLKone consulting article.

Style/medium: sophisticated abstract mixed-media painting with visible dry-brush strokes, subtle canvas grain, restrained geometric linework, and small circular accents; premium management-consulting editorial art consistent with SLKone service-page artwork.

Composition: square, bold composition, strong silhouette, readable when center-cropped and at card-thumbnail size, edge-to-edge artwork.

Palette: deep navy, dark currant, forest green, muted sage, warm cream, dusty peach, and one restrained ochre accent.

Constraints: no text, letters, numbers, logos, watermark, charts, dashboard, photorealism, generic corporate vector art, glossy 3D rendering, neon colors, clutter, or tiny details.

Add an article-specific `Primary request`, `Subject`, and `Mood`. State literal imagery to avoid when the metaphor could be interpreted too directly.

## Rollout order

1. New and recently updated articles.
2. Low-resolution or visibly stock-photo hero images.
3. High-value topic clusters such as AI, finance, strategy, operations, and process intelligence.
4. Evergreen archive content.
5. Interviews and book reviews, which may need a separate portrait or cover-image treatment.

## Review checklist

- The metaphor is relevant without becoming literal or clichéd.
- The image reads at small card size and in the center-cropped hero.
- The title remains legible with the site's existing dark overlay.
- No accidental text, pseudo-letters, numbers, faces, or brand marks appear.
- The piece is related to the service artwork without duplicating an existing composition.
- The WebP exists at the frontmatter path and the production Jekyll build succeeds.

Track accepted replacements in `_data/article_image_rollout.yml`.
