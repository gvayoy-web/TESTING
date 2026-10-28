---
name: designer-component-library
description: "Elegir shadcn/ui, Radix, Magic UI, Motion Primitives o React Bits según la función, el stack y las necesidades de accesibilidad."
---

# Selector de bibliotecas UI

1. Detecta framework, Tailwind version, package manager, preferencias de estilo, bundle y estado de dependencias.
2. **Radix UI**: primitives de interacción compleja y accesible; dialog, menu, popover, tabs y combobox con estados, teclado y ARIA. **shadcn/ui**: componentes editables en el propio proyecto para UX estable. **Magic UI**: decoraciones animadas selectivas. **React Bits**: textos, fondos y efectos listos para personalizar. **Motion Primitives**: microinteracciones y transiciones con Motion.
3. Elige una biblioteca principal por capa. No mezcles dos implementaciones de la misma primitive; no rompas semántica por apariencia. Aísla wrappers y theme tokens para portabilidad.
4. Copia únicamente componentes permitidos por licencia y siguiendo documentación actual. Los componentes ajenos no están empaquetados en Diseñador.
5. Inspecciona dependencias y árbol de importación; no instales 5 bibliotecas por un botón. Prefiere CSS para efectos simples; verifica SSR/hidratación.
6. Ejecuta pruebas de teclado, screen reader, touch 44px, estados abierto/cerrado, focus trap, `prefers-reduced-motion`.

Consulta enlaces de origen en `references/repositorios-v2.md`. Produce lista de componentes adoptados, imports reales, dependencias, estados y riesgos de compatibilidad.
