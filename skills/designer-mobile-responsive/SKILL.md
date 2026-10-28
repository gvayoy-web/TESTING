---
name: designer-mobile-responsive
description: "Diseñar mobile-first con densidad adecuada, reflow y performance en equipos modestos."
---

# Responsive de verdad

Diseña primeros 320/375 px: navegación accesible, tamaño de texto, CTA, menú, cards legibles, formularios y safe areas.
- Usa `minmax`, CSS grid/flex, `clamp()` y container queries cuando la composición cambie por contenedor, no solo viewport.
- Evita fixed widths de headings, alturas rígidas, 100vh sin contemplar UI del navegador, hover-only y diálogos más grandes que la pantalla.
- Verifica imágenes `object-fit`, recortes deliberados, assets adaptativos, fuentes cargadas sin CLS y rutas reales.
- Considera conexiones lentas y GPU modesta; desactiva postFX en mobile cuando no aporta valor.
- Revisa zoom 200%, landscape, teclado virtual, dynamic viewport, `prefers-reduced-motion` y contraste en outdoor.

Entrega capturas/test matrix o indica qué pruebas no se pudieron realizar.
