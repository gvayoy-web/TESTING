---
name: designer-implementation-strategy
description: "Elegir arquitectura frontend y organizar cambios incrementales para entregar interfaces completas sin romper el proyecto."
---

# Estrategia de implementación

Inspecciona stack, dependencias y rutas: HTML/CSS/JS, Vite, React, Next.js, Astro u otro. Preferir el stack existente; migrar framework requiere razón tangible.

1. Divide cambios: tokens/themes → layout → components → interactions → motion/3D → content/accessibility → tests.
2. Usa arquitectura de componentes con propiedad clara; no generes una sola página monstruosa ni sobreabstraigas elementos de uso único.
3. Elige CSS variables y design tokens; responsive mobile-first con grid, `clamp()` y container queries cuando ayuden.
4. Componentes deben cubrir normal, hover, focus, pressed, disabled, loading, empty, error y success cuando corresponda.
5. Importa 3D/dinámicas de forma diferida y conserva la experiencia útil sin JavaScript/Canvas si es posible.
6. Al editar repos: preserva package manager lockfile, rutas, configuración, keys y variables. Añade tests y notas de migración.

Entrega archivos editados, dependencias realmente instaladas, pasos para ejecutar y resultados reales.
