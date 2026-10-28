# Contrato de movimiento V4

Para cada animación declara: **qué explica** (estado/continuidad/jerarquía/imagen de marca), objetivo, elemento de entrada, salida, distancia, tipo de interpolación, control de usuario, versión móvil/reduced-motion, coste.

- Un momento protagonista por experiencia; microinteracciones subordinadas.
- Para scrub por scroll, progreso `0..1`, sin delays basados en tiempo y normalmente ease lineal.
- Para botón, 100–200ms; modal/overlay, 150–350ms; transición narrativa, distancia del scroll, sin bloquear acciones.
- Limitar sombras, blur y filtros a regiones controladas; `will-change` dinámico solo cuando sea necesario, no globalmente.
- GSAP y CSS nativo no deben animar `transform` del mismo elemento a la vez.
