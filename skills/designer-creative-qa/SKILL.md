---
name: designer-creative-qa
description: "Audita calidad visual profesional en gráficos, SVG, impresión, 3D, web y video."
---

# Diseñador v3 — Creative Qa

**Activación:** Audita calidad visual profesional en gráficos, SVG, impresión, 3D, web y video.

## Procedimiento
1. Determina primero el medio y selecciona sus gates técnicos específicos.
2. Revisa mensaje, jerarquía, consistencia, detalle, ortografía y calidad percibida.
3. En vectores valida XML/viewBox/seguridad y en imprenta dimensiones/perfiles/sangrado.
4. En 3D revisa malla, materiales, luces, export y vista móvil; en video fps/timing/textos.
5. Corrige defectos críticos; registra qué pruebas se ejecutaron y qué no se pudo verificar.

## Entregable
Reporte QA con severidad P0–P3, evidencias, correcciones y pendientes honestos.

## Puerta de calidad
Nada marcado como final sin comprobación del medio; no inventar Lighthouse, Blender o print specs.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-design-quality-gates.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
