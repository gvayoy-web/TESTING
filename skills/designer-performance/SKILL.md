---
name: designer-performance
description: "Optimizar sitios visuales con Three.js, GSAP, CSS y assets sin sacrificar FPS, LCP, INP y accesibilidad."
---

# Rendimiento visual y estabilidad

- Presupuesto: rendimiento móvil primero. Evitar boot 3D que bloquea contenido principal.
- Core Web Vitals: LCP, INP, CLS. Medir antes/después usando datos de laboratorio/real si están disponibles.
- Modelos 3D: comprimir GLB, reducir draw calls, geometría instanciada, textura razonable, ajustar DPR, pausar fuera de viewport.
- ScrollTrigger: refrescar al modificar DOM, evitar layout thrash, usar transform en lugar de margen/top por frame.
- R3F: evitar state updates cada frame, lazy load de Canvas, dispose y frameloop demand según interacción.
- CSS: sombras múltiples pesadas/blur a gran escala y backdrop-filter necesitan prueba en móvil; usar degradación.
- Tipografía: preload sólo tipografía crítica, font-display fallback adecuado, dimensión de elementos para evitar CLS.
- `loading="lazy"` sólo bajo el pliegue; priorizar hero image si es LCP.
- Accesibilidad: entorno debe funcionar sin WebGL, sin motion, con reducción de datos y zoom.
- QA: auditar scroll smoothness, memory leaks en navegación, resize y perfil de batería de portátil.

Entregar lista priorizada por beneficio esperado, coste y riesgo, no prometer FPS sin medir.
