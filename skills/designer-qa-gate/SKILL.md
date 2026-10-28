---
name: designer-qa-gate
description: "Control de calidad final antes de afirmar una web lista para producción, con severidades y evidencia objetiva."
---

# QA Gate de publicación

Aplicar `references/quality-gates-v2.md`. Definir P0 bloquea release (crash, enlaces esenciales rotos, pérdida de datos); P1 impide uso de tarea principal (CTA inaccesible, modal imposible de cerrar, clipping serio); P2 polish (easing leve, espacio irregular); P3 detalle estético opcional.

**Condiciones**:
- Build/lint/typecheck cuando exista toolchain y permiso, tests de rutas y enlaces críticos.
- 320, 375, 768, 1024, 1440; navegadores disponibles, mobile touch, zoom 200%, teclado, reduced-motion, fallback sin WebGL.
- Performance real instrumentada o señalar "no medido". Sin claims de 100/100 Lighthouse sin reporte.
- Cambios acotados y git diff inspeccionado antes de deploy. Env variables no expuestas. Compatibilidad con deploy actual.
- Pruebas de scroll, loaders, CTA, hero, formularios, footer, persistencia cuando aplique.

Al finalizar emitir tabla breve: check, resultado real, evidencia/limitación. Si hay P0/P1, no declares listo.
