---
name: designer-3d-lighting-render
description: "Define iluminación cinematográfica y pipeline de render 3D coherente entre escenas y productos."
---

# Diseñador v3 — 3D Lighting Render

**Activación:** Define iluminación cinematográfica y pipeline de render 3D coherente entre escenas y productos.

## Procedimiento
1. Selecciona motor disponible: Eevee/Cycles/Three.js/WebGPU sin fingir compatibilidad.
2. Construye key/fill/rim o HDRI apropiado, controla sombras/contacto y balance de blancos.
3. Fija cámara, lente, resolución, fondo, alpha y dirección narrativa.
4. Renderiza pruebas de bajo coste y ajusta composición antes de alta calidad.
5. Entrega passes/AOV solo cuando hagan falta y revisa transparencias, bordes y tonemapping.

## Entregable
Render en formato solicitado y setup documentado si existe motor.

## Puerta de calidad
Luz coherente, ausencia de noise/aliasing excesivo, color y proporciones controlados.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-3d-production.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
