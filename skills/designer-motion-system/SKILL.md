---
name: designer-motion-system
description: "Diseñar motion language consistente y decidir entre CSS, Motion, GSAP, Rive y Lottie usando presupuesto de movimiento."
---

# Arquitectura del movimiento

Antes de elegir biblioteca responde: ¿qué comunica la transición?, ¿la controla el usuario?, ¿ocurre una vez o en bucle?, ¿qué pasa si no hay animación?

**Motor**: CSS para hover/open/press; Motion para React/interpolación/layout; GSAP para timelines complejos/ScrollTrigger; Rive/Lottie para vector interactivo o ilustración exportada; Three.js para geometría WebGL. No mezcles timeline GSAP con CSS transition sobre las mismas propiedades.

**Tokens**: fast 120–180 ms; normal 200–320 ms; expressive 400–700 ms cuando realmente convenga. Preferir easings definidos por producto y `transform`+`opacity`. Limitar loops continuos e intensidad de parallax.

**Motion QA**: secuencias reversibles, foco nunca perdido, animaciones cancelables, zero-motion fallback, teclado y GPU budget. Para scroll no bloquear desplazamiento natural ni usar `preventDefault` para capturar el usuario; cuidado con scroll-jacking y elementos fijos ocultando CTAs.

Referencia: `designer-gsap`, `designer-scroll`, `designer-motion-primitives` y `designer-lenis`.
