---
name: designer-debug
description: "Localizar bugs visuales de CSS, responsive, scroll, React hydration, canvas y JavaScript, corregir y evitar regresiones."
---

# Debug UI profundo

1. Reproduce: URL/ruta, viewport, dispositivo, evento y diferencia esperada-real. Usa logs reales si están disponibles.
2. Localiza por capas: DOM/CSS -> layout/stacking/overflow -> eventos/estado -> dependencias/motion -> WebGL/GPUs -> red/SSR.
3. Corrige causa raíz. Antipatrones: z-index infinito, `overflow: hidden` sobre todo el sitio, `height:100vh` ignorando barras móviles, inicios múltiples de RAF, fuentes que cambian medidas tras `ScrollTrigger`.
4. Pasa smoke tests en rutas relacionadas, móvil, teclado, zoom y reduced motion.
5. No cambies diseño general cuando el bug sea local ni elimines funciones sin consultar su uso.

Informe: problema reproducido, archivo/línea, causa verificada, modificación, prueba de regresión.
