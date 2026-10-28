---
name: designer-react-bits
description: "Integrar selectivamente React Bits para títulos animados, efectos visuales, partículas, backgrounds y tarjetas con rendimiento controlado."
---

# React Bits experto

Fuente externa: https://github.com/DavidHDev/react-bits. El repositorio actual publica componentes JS/TS en estilos CSS y Tailwind; revisa términos MIT + Commons Clause antes de redistribuir. No afirmes que los componentes se incluyeron sin instalarlos.

**Aplicación**:
- Elige objetivo (titular, feedback, ambiente, interacción); selecciona un efecto por bloque visual, dos como máximo en primer viewport.
- Examina adaptador React, dependencia del componente, CSS y variantes TS/JS y CSS/Tailwind. No pegues nombres de exports sin verificarlos en el proyecto o docs.
- Desactiva movimiento si `prefers-reduced-motion`; evita cursor following en touch; conserva texto HTML indexable y selección/copiar cuando sea posible.
- Para fondos GPU/Canvas, limita DPR y animación fuera de viewport, comprueba on unmount y ofrece degradación CSS estática.
- Evita partículas detrás de párrafos largos y efectos que muevan CTAs; mide sensibilidad visual y costo de rendering.

Test: móvil lento, evento hover/touch, hydration en SSR, tab order y assets. Entrega component path, dependencia y fallback.
