---
name: designer-magic-ui
description: "Diseñar secciones animadas y adaptar Magic UI en proyectos React/Next.js sin saturación ni pérdida de accesibilidad."
---

# Magic UI — efectos para secciones

Fuente: https://github.com/magicuidesign/magicui; skill original `skills/magic-ui/SKILL.md`.
1. Verifica React/Next, Tailwind, estructura shadcn y versión antes de intentar instalar.
2. Selecciona por intención: aparición sutil para comunicar jerarquía; light/glow para CTAs; marquee solo para contenido secundario no esencial; globe/3D solo si conecta con el mensaje.
3. La instalación usa la CLI documentada del registro shadcn, por ejemplo `npx shadcn@latest add @magicui/magic-card`, **solo** cuando usuario y entorno autorizan dependencias. Verifica nombre exacto antes de usarlo.
4. Revisa ids de componentes, CSS, reduced motion, foco de enlaces, semántica, responsive, hidratación SSR y carga de fuentes.
5. Nunca dependas de animación para leer el contenido. Combina como máximo una familia de efectos por sección.

Entrega: cambios reales o código autocontenido, dependencias y validación.
