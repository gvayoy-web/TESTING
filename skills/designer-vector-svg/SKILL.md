---
name: designer-vector-svg
description: "Crea, transforma y audita archivos vectoriales SVG editables, seguros y reutilizables."
---

# Diseñador v3 — Vector Svg

**Activación:** Crea, transforma y audita archivos vectoriales SVG editables, seguros y reutilizables.

## Procedimiento
1. Define unidades, viewBox, grosor mínimo, métodos de unión y uso de stroke vs fill.
2. Organiza grupos semánticos, IDs únicos, referencias internas y orden de capas; para producción mantén curvas sencillas.
3. Si un bitmap debe convertirse a vector, traza formas con fidelidad; no prometas vectorización perfecta automática.
4. Conserva texto editable cuando el cliente necesita editarlo; ofrece contornos solo para imprenta o cuando se solicite.
5. Valida SVG con scripts/svg-preflight.py; exporta PNG/PDF únicamente cuando el convertidor esté disponible y sin alterar proporciones.

## Entregable
SVG editable y fuentes/referencias de sus variantes, con viewBox y pruebas.

## Puerta de calidad
Sin scripts embebidos ni URLs externas no aprobadas; IDs únicos; escala y relación de aspecto correctas.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-vector-guide.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
