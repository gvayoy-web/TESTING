---
name: designer-r3f
description: "Diseño e implementación de escenas React Three Fiber y Drei integradas con React, Next.js, Suspense y accesibilidad."
---

# React Three Fiber

Elegir R3F si el proyecto usa React/Next.js y requiere estado/escenas 3D, en lugar de montar Three.js imperativo paralelo.

## Procedimiento
- Verificar paquete `three`, `@react-three/fiber`, `@react-three/drei`, compatibilidad con versión de React.
- Configurar `<Canvas>` bajo frontera cliente en Next y controlar SSR; suspense con loading legible.
- Evitar re-render masivo por estado React en cada frame; usar `useFrame` con refs.
- `useGLTF` para modelos, preload sólo para elementos prioritarios, correcto cleanup de recursos.
- Cámara, sombras y Environment calibrados con prueba en móviles.
- Implementar fallback estático accesible para `Canvas`, dark/light consistency y `prefers-reduced-motion`.
- Para interacciones, tener alternativas DOM, y medir necesidades `frameloop="demand"` en escenas casi estáticas.

## Patrones
Hero 3D, configurador, escena scroll-driven, viewer de producto, portafolio animado. Prueba hardware de gama baja primero. Fuente temática: freshtechbro/claudedesignskills/react-three-fiber.
