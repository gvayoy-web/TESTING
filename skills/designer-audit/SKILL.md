---
name: designer-audit
description: "Auditar interfaz, diseño, QA, accesibilidad, usabilidad, copy, estados, microinteracciones y coherencia visual."
---

# Auditoría impecable y QA de diseño

No confundir percepción de calidad con cantidad de animaciones. Revisar diseño real renderizado; sin navegador declarar los controles NO verificados, nunca fingir pruebas.

## Checklist por prioridad
P0: contenido inaccesible, botones bloqueados, errores de navegación, overflow severo, formularios rotos, estado de carga perpetuo, textos recortados.
P1: jerarquía débil, textos poco legibles, móvil lento, contraste, foco invisible, CTA ambiguo, 3D impide entrada, animación sin salida.
P2: microcopy, ritmos tipográficos, consistencia de radios/sombras, timing, imágenes degradadas, contenido placeholder.

## Review
1. Auditar 320px, 375px, 768px, 1024px, 1440px; comprobar también landscape y 200% zoom.
2. Navegación teclado completa y elementos interactivos con foco visible. Touch targets adecuados.
3. `prefers-reduced-motion` y alternative static art.
4. Accesibilidad de formularios, labels, errores, estados de carga y anuncios dinámicos cuando corresponda.
5. Revisar tamaño/timing de overlays, stacking context, safe areas en móvil, CLS por fuentes/imágenes.
6. Medir rendimiento si herramientas disponibles; diferenciar observado versus supuesto.
7. Clasificar hallazgos con impacto, evidencia y cambio exacto; arreglar P0/P1 antes de efectos decorativos.

Inspiración metodológica: Impeccable de pbakaus, pautas WAI/WCAG, web interface guidelines. Esta adaptación NO ejecuta su launcher o sus binarios.
