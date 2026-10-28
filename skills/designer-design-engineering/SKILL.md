---
name: designer-design-engineering
description: "Pulir dirección artística, tipografía, detalle visual y movimiento con criterio de ingeniería de diseño antes de implementar."
---

# Design Engineering

Audita jerarquía y ritmo: cada página debe tener tensión visual deliberada, alineaciones coherentes, blancos útiles y variaciones medibles. Evita cards repetidas, gradientes estándar y saturación de componentes animados.

**Secuencia de refinamiento**:
- Lectura: propuesta de valor, sección activa y CTA visibles en 5 segundos; título parte en líneas elegantes; wrapping consciente.
- Tipografía: tamaño fluido `clamp()`, tracking óptico, números tabulares donde aplique, longitud de línea de lectura moderada.
- Composición: grids intencionadas (12 columnas desktop, 4 móvil cuando convenga), asimetría controlada, densidad por sección, alineación óptica de iconos y botones.
- Percepción táctil: hover/focus/press distintos, estado deshabilitado visible, border/shadow coherentes, transiciones justificadas y no automáticas.
- Identidad: usa una firma (material 3D, gráfica editorial, tipografía experimental), no cinco.
- QA de detalle: clipping de texto, legibilidad sobre texturas, cursor target, contrastes, stroke, safe areas, formas de input, modo sin JS.

Revisar contra `references/quality-gates-v2.md`; entregar cambios comprobables, no adjetivos vacíos. Inspírate en los trabajos de Emil Kowalski, Impeccable y Taste Skill sin copiar material externo automáticamente.
