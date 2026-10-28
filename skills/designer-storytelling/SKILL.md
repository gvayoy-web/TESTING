---
name: designer-storytelling
description: "Diseñar páginas narrativas cinematográficas basadas en scroll, secciones inmersivas y transiciones entre escenas."
---

# Storytelling digital

1. Escribe **6 escenas máximo** por defecto: gancho → problema → propuesta → evidencia → diferenciador → CTA. No conviertas scroll en videojuego sin motivo.
2. Cada escena debe funcionar como bloque estático para usuario con reduced-motion, tab keyboard y navegadores sin WebGL.
3. Usa scroll progress como orientación visible, no como obstáculo para hacer clic. No pinnear largos tramos en móvil.
4. Decide renderer según material: HTML/CSS/SVG para narrativas de texto y datos; GSAP ScrollTrigger para transiciones; Canvas/Three solo si agrega dimensiones imposibles con DOM.
5. Diseña transferencia de foco, navegación por anclas y CTA disponible incluso si el usuario salta las animaciones.
6. Prueba velocidad de scroll baja/alta, barra del navegador móvil, back navigation, cambios de viewport e imágenes tardías.

Resultado: storyboard por escena con objetivo, información, mecánica de motion, assets y fallback.
