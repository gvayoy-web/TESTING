---
name: designer-scroll
description: "Implementar ScrollTrigger GSAP, parallax, pinning y scroll storytelling con sincronización estable y sin scroll-jacking."
---

# ScrollTrigger y storytelling

Utilizar sólo si la sección se comprende con movimiento. Contenido accesible sin JS permanece legible.

## Técnica
- Registrar ScrollTrigger una sola vez.
- `start`, `end`, `scrub` y `pin` explícitos, evitar fijar secciones enteras en móvil sin necesidad.
- Animar transform/opacity del contenido con GSAP timeline; refrescar tras imágenes, fuentes y cambios de layout.
- Crear triggers por ámbito, destruirlos durante unmount y route transitions.
- Respetar `prefers-reduced-motion` y condiciones de touch/coarse-pointer: movimiento reducido, interacción sin pin.
- No combinar múltiples smooth-scroll engines sin coordinar proxy y sus consecuencias; en la mayoría de sitios basta scroll nativo.
- Evitar disparos múltiples cuando React strict mode monta dos veces; asegurar limpieza.
- Animaciones secuenciales con indicadores visibles de continuidad, pero no ocultar enlaces/CTAs fuera de pantalla.

Fuente: GSAP/greensock `gsap-scrolltrigger`; verificar API y registrar plugin correctamente.

## Extensión V4
Para scroll por capas y cambios de escenas, aplicar `designer-layered-scroll` y `designer-scroll-storyboard`. Preferir sticky nativo o GSAP ScrollTrigger según stack. Demo `examples/layered-scroll-v4.html`; revisar `references/v4-layered-scroll.md`.
