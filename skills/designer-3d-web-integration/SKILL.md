---
name: designer-3d-web-integration
description: "Adapta modelos GLB y escenas de Blender a Three.js/R3F con interactividad usable."
---

# Diseñador v3 — 3D Web Integration

**Activación:** Adapta modelos GLB y escenas de Blender a Three.js/R3F con interactividad usable.

## Procedimiento
1. Optimiza modelo (mesh/texture/draco/meshopt según compatibilidad), aplica nombres semánticos y pivotes.
2. Valida glTF con herramientas cuando existan; mide bytes, calls, tris y textura.
3. Incluye loader/skeleton accesible y poster estático de respaldo.
4. Diseña orbit/hover/scroll como affordance, no scroll-jacking; agrega pausa y reduced-motion.
5. Comprueba compatibilidad en móvil y WebGL perdido con fallback claro.

## Entregable
Sección 3D integrada con assets optimizados y resultados de prueba.

## Puerta de calidad
Carga progresiva, FPS real si se midió, estabilidad y control accesible.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-3d-production.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
