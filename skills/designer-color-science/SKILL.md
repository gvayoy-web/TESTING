---
name: designer-color-science
description: "Diseña paletas por objetivos perceptuales, contrastes y reproducción web/impresión."
---

# Diseñador v3 — Color Science

**Activación:** Diseña paletas por objetivos perceptuales, contrastes y reproducción web/impresión.

## Procedimiento
1. Identifica entorno (sRGB en web, CMYK/ICC en impresión cuando el proveedor lo indique, HDR/ACES en 3D).
2. Crea roles semánticos y no solo muestras: foreground/background, primario, secondary, warning, accent, border.
3. Calcula y compara luminancia/contraste sin confiar solo en la estética; valida estados hover/disabled/error.
4. Define degradados y sombras en un espacio de color apropiado, comprueba grises y baja saturación.
5. Documenta conversiones como aproximadas hasta pruebas de color del proveedor.

## Entregable
Tokens de color, porcentajes recomendados, equivalencias de entrega y muestras.

## Puerta de calidad
Accesibilidad, coherencia de valores, diferencia de estados y límites del gamut.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-design-quality-gates.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
