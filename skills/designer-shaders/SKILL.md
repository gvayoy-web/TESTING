---
name: designer-shaders
description: "Construir shaders GLSL y efectos de material en Three.js con degradación visual, límites GPU y códigos de color correctos."
---

# Three.js Shaders & Materiales

Fuente técnica externa: https://github.com/CloudAI-X/threejs-skills/tree/main/skills/threejs-shaders. Valida versión de Three.js/TSL; los ejemplos upstream pueden apuntar a revisiones distintas del proyecto.

1. Define función visual: onda, refracción, gelatina, metal/vidrio, distorsión de imagen, gradiente o partículas. El shader debe comunicar materialidad y marca.
2. Elige MeshStandard/PhysicalMaterial antes de ShaderMaterial. Si necesita custom shader, define uniforms explícitos, vertex/fragment, geometría y variable tiempo controlada por delta clock.
3. Usa color management correcto (`SRGBColorSpace`, tone mapping, renderer config acorde a versión); evita colores lavados entre CSS y WebGL.
4. Limita loops en fragment, texturas gigantes, overdraw y blend innecesario. Prueba DPR, tamaño de canvas y clipping.
5. Incluye prueba sin WebGL/reduced-motion: imagen, poster SVG/CSS o video opcional ligero. Nunca ocultes CTA textual dentro de WebGL.
6. Define pausa al salir de viewport, limpieza de geometrías/materiales/texturas y comportamiento ante pérdida de WebGL context.

Salida: hipótesis visual, escena, uniforms/documentación, fallback, medición si el entorno la permite.
