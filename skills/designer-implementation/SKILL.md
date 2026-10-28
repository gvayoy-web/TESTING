---
name: designer-implementation
description: "Convertir propuestas de diseño premium en código limpio, seguro, responsive, semántico y reutilizable."
---

# Implementación frontend responsable

1. Inspeccionar código y stack antes de intervenir; trabajar en rama si la sesión tiene Git. No desplegar ni tocar producción sin autorización explícita.
2. Si existe un design system, reutilizar tokens y componentes; añadir solo los necesarios.
3. Secciones HTML semánticas, h1 único cuando sea apropiado, headings jerárquicos, botones para acciones y enlaces para navegación.
4. Estilizar responsive sin dependencias innecesarias; usar clamp()/CSS Grid/flex.
5. Estado de carga, error, hover, focus-visible, disabled, reduced motion. Pruebas en teclado, touch y baja potencia.
6. Animaciones con cleanup; 3D con fallback; assets y modelos con fuentes/licencias verificadas.
7. Incluir README de diseño: tokens, fuentes de assets, límites de rendimiento y formas de probar.
8. Si no se dispone del repositorio ni de una herramienta para ejecutar el código, entregar parche conceptual o código y declarar qué no se verificó.
