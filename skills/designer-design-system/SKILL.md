---
name: designer-design-system
description: "Generar sistemas de diseño completos con tokens, colores, tipografía, espaciado, componentes y estados responsivos."
---

# Design system primero

Genera tokens semánticos en CSS variables, no hex codes repetidos. Define los siguientes grupos:
1. Color: backgrounds, surfaces, borders, text, muted, primary, success, warning, danger; claro/oscuro.
2. Typography: display, h1–h4, body, small, mono; escalas clamp, line-height, tracking.
3. Layout: contenedor 1200–1440px, paddings fluidos, grid 12 columnas desktop, 4 columnas móvil.
4. Radius & depth: 0/8/16/24/32 (ajusta al estilo), sombra xsmall/small/medium/layered; z-index semánticos.
5. Motion: 120–180ms microestado, 240–400ms revelación, 500–800ms storytelling SOLO si aporta; easing coherente.
6. Componentes: button, input, modal, navbar, pricing, card, feedback, skeleton, toast. Estados hover, focus-visible, active, disabled, error, loading.
7. Sistemas claros/oscuros independientes (no sólo `filter:invert`).
8. Accesibilidad: labels, contraste, zoom, posición de foco, modo de movimiento reducido y entrada por teclado.
9. Imágenes: tamaños adecuados, descripciones, lazy loading por debajo del pliegue.

Entregables: tabla de tokens, CSS/Tailwind configuration si aplica, componentes y mini estilo-guía; no exportes un sistema incompleto bajo la etiqueta production-ready.
