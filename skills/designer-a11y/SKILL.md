---
name: designer-a11y
description: "Auditar y corregir accesibilidad WCAG 2.2: teclado, foco, semántica, contraste, movimiento, formularios y canvas."
---

# Accesibilidad de diseño avanzada

- Audita WCAG 2.2 AA como objetivo general, sin garantizar conformidad sin pruebas completas.
- DOM: landmarks, `h1` único por página cuando tenga sentido, jerarquía de headings, etiquetas, textos alternativos, tabla con headers y vínculos inequívocos.
- Interacción: todos los controles por teclado, foco visible no obstruido, tab sequence lógico, focus management en modals, Escape y retorno de foco.
- Legibilidad: textos normales con contraste suficiente (referencia 4.5:1), texto grande 3:1, componentes perceptibles, zoom 200%, reflow 320 CSS px, targets adecuados.
- Motion: `prefers-reduced-motion`; autoplay/loops controlables; parallax discretos; no flashes.
- Canvas: proporciona alternativa textual y controles equivalentes, mensajes de error y contenido crítico fuera de WebGL.
- Tests: axe-core automatizado como apoyo, pero verificación manual imprescindible; registra problema, criterio, archivo, severidad, solución y evidencia de retest.

No declares accesibilidad total por una simple pasada de axe.
