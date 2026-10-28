---
name: designer-lenis
description: "Integrar smooth scrolling opcional con Lenis y sincronización con GSAP/ScrollTrigger sin romper accesibilidad o navegación."
---

# Lenis + scroll responsable

Fuente: https://github.com/darkroomengineering/lenis. Usar solo si el proyecto justifica suavizado del scroll; **el scroll nativo es la opción inicial**.

1. Comprueba si ya hay Lenis, Locomotive, CSS smooth, router scroll u otro sistema de animación. No dupliques controladores.
2. Si integras Lenis: una sola instancia, init en cliente, RAF sincronizado con GSAP donde corresponda; liberar en cleanup y recrear cuando cambien rutas/layout.
3. Verifica `position: sticky`, anclas, historial, hash links, teclado, rueda, trackpad, touch, nested scrolling y scroll restoration.
4. Desactivar suavizado para reduced-motion si puede resultar molesto; considera móviles de poca capacidad.
5. Usa ScrollTrigger.refresh después de cambios de fuentes/imágenes que alteren medidas, no continuamente cada frame.

Tests: anchor directo desde URL, teclado PageDown/Space/Home/End, scroll dentro de modal, back navigation y FPS real instrumentado si disponible.
