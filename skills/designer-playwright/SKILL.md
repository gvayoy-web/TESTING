---
name: designer-playwright
description: "Ejecutar pruebas end-to-end de interfaz con Playwright: breakpoints, visual regression, teclado, rutas y errores JS."
---

# Playwright QA — pruebas que sí se ejecutan

Fuente: https://github.com/microsoft/playwright. Comprueba que Playwright y navegadores estén instalados antes de ejecutar.

**Matriz**: 320/375/768/1024/1440px; landing, menú, CTA, formulario, navegación, modal y estados de carga/error. Usa capturas consistentes con fuentes cargadas y animaciones desactivadas durante snapshots.

- Assert de links y rutas: sin 404, anchors, `target=_blank` seguro, CDN y fuentes si están accesibles.
- Assert responsive: sin `scrollWidth > innerWidth` excepto carruseles con overflow intencionado; clipping de titulares/botones; landmarks visibles.
- Interacciones: click/tap/teclado, Escape, volver atrás, focus trap, inputs error/success, enlaces y menú móvil.
- Console: registrar pageerror, requests fallidos, hydration mismatch y carga de imágenes.
- Tests visuales: capturas comparables y umbral definido; revisar diffs, no actualizar golden snapshots para esconder regresiones.
- Reportar lo que realmente pasó y los tests no disponibles; no inventar resultados.

Entrega una matriz Pass/Fail/Not Run y los fallos críticos P0-P2.
