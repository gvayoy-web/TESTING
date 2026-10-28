# Fuentes externas curadas — Diseñador v2

**30 repositorios verificados en GitHub**, 8 de v1 y 22 incorporados al catálogo de v2.

La relación siguiente es una **biblioteca de referencia**, no significa que su código completo esté incluido en ChatGPT. `scripts/download-repos.*` clona fuentes originales en un equipo con Git e internet. Consulta licencias y versiones antes de adoptar o redistribuir.

| Repositorio | Especialidad | Ruta/skill recomendado | Estado |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | Dirección visual y frontend | `frontend-design` | fuente previa |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Sistema de inteligencia UX/UI | `ui-ux-pro-max` | fuente previa |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Pulido UI de nivel producción | `impeccable` | fuente previa |
| [MengTo/Skills](https://github.com/MengTo/Skills) | Experiencias WebGL, GSAP y landings | `agent-skills/3d` | fuente previa |
| [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | React Three Fiber y animación | `react-three-fiber` | fuente previa |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | Motion GSAP oficial | `gsap-core, gsap-scrolltrigger` | fuente previa |
| [claudekit/frontend-design-pro-demo](https://github.com/claudekit/frontend-design-pro-demo) | Dirección visual y fotografía | `frontend-design-pro` | fuente previa |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 67 estilos, claymorphism y diseño | `claymorphism` | fuente previa |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Buenas prácticas React, UX y transiciones | `web-design-guidelines, react-best-practices` | NUEVO |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Checklist de interfaz web | `command.md` | NUEVO |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Componentes React editables | `ui components` | NUEVO |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | Primitives accesibles | `radix` | NUEVO |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | Utility CSS y sistema de tokens | `tailwind` | NUEVO |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | 215+ componentes animados React | `react bits` | NUEVO; MIT + Commons Clause |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Componentes y hero animados | `magic-ui` | NUEVO |
| [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) | Componentes animados Motion + Tailwind | `motion-primitives` | NUEVO |
| [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | Smooth scrolling accesible | `lenis` | NUEVO |
| [motiondivision/motion](https://github.com/motiondivision/motion) | Animaciones React y JS | `motion` | NUEVO |
| [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) | React renderer de Three.js | `r3f` | NUEVO |
| [pmndrs/drei](https://github.com/pmndrs/drei) | Utilidades y helpers para R3F | `drei` | NUEVO |
| [pmndrs/postprocessing](https://github.com/pmndrs/postprocessing) | PostFX para Three.js | `postprocessing` | NUEVO |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Diseño de interacción y animaciones | `emil-design-eng` | NUEVO |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Criterio visual anti-plantilla | `taste-skill` | NUEVO |
| [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills) | 13 especializaciones Three.js | `threejs-shaders, threejs-performance` | NUEVO |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills de ingeniería y diseño | `interaction-design` | NUEVO |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Copywriting, conversión y funnels | `copywriting, cro` | NUEVO |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Testing end-to-end y visual | `playwright` | NUEVO |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | Análisis automático accesibilidad | `axe-core` | NUEVO |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | Auditoría de rendimiento web | `lighthouse` | NUEVO |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | Iconografía vectorial consistente | `lucide` | NUEVO |

## Estrategia de integración
1. Los 39 módulos de `skills/` son guías operativas originales de Diseñador; sus conocimientos integran selectivamente ideas respaldadas por los proyectos, sin copiar textos completos.
2. Los repositorios de JavaScript (React Bits, Tailwind, Lenis, Magic UI, R3F, etc.) se importan como dependencias del proyecto web **solo después** de verificar stack y compatibilidad.
3. GitHub original no significa instalación automática ni permiso para ejecutar scripts. Ningún repositorio se clona en la cuenta ChatGPT al guardar este plugin.
4. `react-bits` incluye términos MIT + Commons Clause; revisa sus condiciones si redistribuyes componentes. El resto requiere consultar su licencia actual.
5. Para versiones exactas y APIs nuevas, inspecciona documentación actualizada en repositorios o package manager en el momento de uso.

## Buenas referencias adicionales
- https://www.skills.sh/ — ecosistema de Skills.
- https://web.dev/ — rendimiento y Core Web Vitals.
- https://www.w3.org/WAI/ — accesibilidad.
- https://developer.mozilla.org/ — CSS, Web APIs, HTML y JavaScript.
- https://threejs.org/docs/ — documentación oficial Three.js.
- https://gsap.com/docs/v3/ — documentación oficial GSAP.
