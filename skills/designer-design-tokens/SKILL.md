---
name: designer-design-tokens
description: "Generar sistemas de tokens CSS interoperables para temas clay, glass, editorial, brutalista y 3D sin inconsistencias."
---

# Design Tokens inteligentes

Empieza por variables semánticas: --color-surface, --color-text, --color-action, --color-border, --radius-card, --shadow-card, --spacing-*, --motion-fast, --motion-ease. No uses valores de marca distintos en cada componente.

- Paletas: contraste, dark/light tokens independientes, coherencia entre canvas/WebGL y CSS.
- Type: familia para display y texto; escalas fluidas clamp con límites; longitud de línea; fuentes locales o provider licenciado.
- Layout: sistema de spacing 4/8 pt o escala propia, container max y breakpoints según contenido, no arbitrarios.
- Motion: una curva y 3 velocidades base, reducidas en `prefers-reduced-motion`.
- Estados: focus visible y feedback perceptible en todas las variantes.

Acompaña tokens con demo de botón, card, hero y form. Usa plantillas CSS en `assets/tokens/` como base editable, no como identidad definitiva.
