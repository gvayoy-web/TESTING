---
name: designer-threejs
description: "Implementar Three.js real: cámaras, luces, shaders, interacción, modelos, render eficiente y fallback sin WebGL."
---

# Three.js — escena con propósito

Usa Three.js cuando el resultado demande geometría real, cámaras, texturas, modelos GLB, partículas o shaders personalizados. Si solo se desea profundidad, CSS 3D/SVG puede ser suficiente.

## Arquitectura
- Crear `Scene`, cámara `PerspectiveCamera`/`OrthographicCamera`, `WebGLRenderer`, luces y meshes; manejar DPR dinámico y resize.
- Comprobar WebGL antes de montar. Separar contenido HTML semántico del canvas; texto y CTA deben existir en DOM.
- Animación dependiente del tiempo (delta), no de frames; detener loop en background y liberar recursos al desmontar.
- Models glTF/GLB comprimidos, `GLTFLoader`, compresión si corresponde, placeholder/skeleton e indicador si la carga demora.
- Evitar disparar modelos o draw calls masivos en smartphones. Medir CPU/GPU antes de combinar postprocesado, bloom, parallax y partículas.
- Interacción: raycasting sólo cuando haga falta; respetar touch y keyboard, ofrecer alternativa de control.
- Para material clay: roughness ~0.65–0.9 (ajustable), iluminación suave, sombras limitadas, color aproximado a tokens de marca.
- Fallback de imagen/SVG si WebGL está deshabilitado, conexión lenta o prefers-reduced-motion.

## QA
Comprobar renderer disposal (geometries, materials, textures), eventos, devicePixelRatio, context loss, resize, navegación interna, bfcache, intersección de pantalla y tiempo de primer render útil.

Base temática: MengTo Skills/Three.js y docs oficiales de threejs.org. No inventar APIs; verificar versiones de dependencias al escribir código.
