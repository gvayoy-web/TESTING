---
name: designer-figma-canva-interop
description: "Integra flujos de diseño entre Figma, Canva, SVG, documentación y código según conectores disponibles."
---

# Diseñador v3 — Figma Canva Interop

**Activación:** Integra flujos de diseño entre Figma, Canva, SVG, documentación y código según conectores disponibles.

## Procedimiento
1. Comprueba qué app/conector está instalado y qué permisos tiene; nunca asumas acceso.
2. Conserva editabilidad usando componentes/variables/layers cuando la herramienta lo soporte.
3. Sincroniza paleta, tipografía y naming entre artefactos; evita rasterizar vectores innecesariamente.
4. Respeta el archivo de origen y crea versiones para handoff; no sobrescribas diseños de terceros sin permiso.
5. Si no hay acceso al app, entrega SVG/JSON/archivos compatibles con pasos concretos de importación.

## Entregable
Archivos interoperables y guía de transferencia; edición directa si el conector lo permite.

## Puerta de calidad
No inventar acciones en apps; revisar tipografías/layers antes/después de importación.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-tool-routing.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
