---
name: designer-r3f-advanced
description: "Arquitectura avanzada de React Three Fiber y Drei: componentes 3D, estado, instancing, interacción y calidad."
---

# R3F & Drei avanzado

Fuentes: https://github.com/pmndrs/react-three-fiber y https://github.com/pmndrs/drei.

- Divide escena por responsabilidades: Canvas/renderer, iluminación, cámara, modelo, interaction layer, UI HTML y recursos.
- Nunca guardes posiciones/rotaciones por frame en React state si puedes actualizar refs en `useFrame` sin rerender.
- Instancing para objetos repetidos, textura reducida y calidad adaptativa según capacidades reales; demand frameloop para escenas mayoritariamente estáticas.
- Usa helpers Drei cuando reducen código, no como excusa para capas excesivas de shaders/postFX.
- Coordina puntero/touch con scroll sin secuestrar gestos. Botones HTML reales para interacciones críticas, accesibles por teclado.
- Clean up de canvases, eventos, observers, geometrías, texturas y loaders; evita duplicación de contextos WebGL.
- Valida 375px, zoom, mobile low-power, tab order, SSR boundaries y fallbacks no WebGL.

Verifica bundle impact y render stats cuando el proyecto permite instrumentarlo.
