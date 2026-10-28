# Matriz de tecnología — elegir lo mínimo suficiente

| Necesidad | Primera solución | Elección especializada | Evitar si... |
|---|---|---|---|
| Hover o pressing | CSS transitions | Motion Primitives | basta con CSS |
| Enter/reveal | CSS + IntersectionObserver | GSAP/Motion | afecta lectura o SEO |
| React layout animation | CSS View Transitions API | Motion | hidratar complejidad innecesaria |
| Scroll narrativo | HTML/CSS sticky | GSAP ScrollTrigger | obliga a secuestrar scroll |
| Smooth scroll | Nativo | Lenis integrado en un loop | móvil modesto, reduced motion |
| Títulos vistosos | CSS typography | React Bits | contenido vital depende del canvas |
| Componentes formulario | HTML, Radix | shadcn/ui | mezclas de primitives duplicadas |
| Secciones glam | CSS | Magic UI | saturación efectos, high JS |
| Forma 3D decorativa | CSS / SVG | Three.js Vanilla | rendimiento o licencia insuficiente |
| Mundo 3D React | imagen / CSS | React Three Fiber + Drei | no hay React o varias canvas |
| Material artesanal | MeshPhysicalMaterial | custom GLSL/TSL | compatibilidad incierta |
| PostFX | ninguna | pmndrs/postprocessing | GPU modesta |
| Iconografía | emoji/svg simple | Lucide | el set crea complejidad |
| Auditoría visual | inspección y checklist | Playwright screenshots | no hay browser autorizado |
| Accesibilidad | teclado + semántica | axe-core | crees que automatización sustituye persona |
| Perf | Network / Devtools | Lighthouse | sin línea base medible |

## Dependencias y deuda
- Identifica framework, versión, bundle size e imports antes de instalar.
- Usa una solución principal por necesidad. No dupliques raf loops, engines y animaciones sobre el mismo selector.
- Prioriza contenido HTML/ARIA y estados funcionales; 3D y motion se cargan progresivamente.
- Si no está disponible instalar o ejecutar, prepara fuente/autorización y no atribuyas pruebas imaginarias.
