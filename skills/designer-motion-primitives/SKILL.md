---
name: designer-motion-primitives
description: "Diseñar animaciones componentes con Motion y Motion Primitives, foco en feedback, layout transitions y reduced motion."
---

# Motion Primitives

Inspiración y componentes: https://github.com/ibelick/motion-primitives, biblioteca MIT; Motion runtime: https://github.com/motiondivision/motion.

**Sistema**:
- Clasifica la transición: entrada, feedback, continuidad de layout, navegación, causa/efecto, despedida.
- Define tokens: `--duration-fast: 140ms`, `--duration-base: 240ms`, `--duration-slow: 450ms` y easing acordado con marca; son puntos de partida, no valores universales.
- Usa Motion para interacciones React y cambios de layout, CSS para estados simples, GSAP para secuencias complejas; no animes el mismo nodo desde dos motores.
- Mueve `transform` y `opacity` preferentemente, evita animar `top/left/width` de grandes zonas continuamente.
- Revisa semántica, foco después de modal/ruta, detención offscreen y respeto a `prefers-reduced-motion`.

Se entrega una matriz componente→animación→gatillo→duración→fallback y se prueba la ida y vuelta.
