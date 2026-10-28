---
name: designer-visual-regression
description: "Comprueba diseños renderizados en escritorio/móvil con capturas comparables, overflow, reduced motion y un informe verificable."
---

# Visual Regression Gate

1. Si existe Playwright/browser, abrir un servidor local del proyecto y capturar 320, 375, 768, 1024 y 1440px. Evitar capturas antes de fuentes e imágenes cargadas.
2. Recorrer inicio, mitad y fin de cada capítulo de scroll; también hacia atrás. Verificar que no haya flashes, saltos de layout o texto cortado.
3. Comprobar foco mediante teclado, menú, links, estados, scroll vertical nativo y reduced motion.
4. Comparar visuales significativas; una diferencia de píxeles no es por sí sola un bug. Priorizar regresiones de UX y legibilidad.
5. Reportar consola, errores JS, desbordes, rutas y limitaciones del entorno. No indicar «prueba real móvil» cuando solo se emuló un viewport.

Scripts de muestra: `tests/test_layered_scroll.py`; contrato `references/v4-qa-gates.md`.
