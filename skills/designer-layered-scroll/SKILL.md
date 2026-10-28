---
name: designer-layered-scroll
description: "Implementa transiciones de scroll por capas: depth planes, escenas sticky/pinned, parallax, texto, objetos y fondos con handoffs suaves y fallback."
---

# Layered Scroll Engine — Arquitectura ejecutable

Objetivo: una coreografía por capítulos con **background → ambiente → sujeto → tipografía → interfaz**, cada capa con un rol y velocidades/entradas intencionales. Primero escribe 3–5 beats del storyboard. Que la transición narre algo: materia→forma→producto, problema→solución, plano→volumen.

## Decisión técnica
1. CSS `position: sticky` + progresión `scroll()` / `view()` cuando sea suficiente; JS rAF para control de progreso compartido y soporte extendido.
2. GSAP ScrollTrigger si el proyecto ya tiene GSAP o requiere pin/timelines sincronizadas, scrub, reversa y secuencias complejas.
3. React/R3F solo si hay escena tridimensional real. Para scroll de texto y fotos, CSS/GSAP suele ser mejor.
4. Lenis es OPCIONAL; nunca lo instales solo para sumar una sensación de suavidad. No secuestres scroll nativo.

## Pipeline
- `.chapter` aporta distancia real de scroll sin scroll-jacking; `.stage` sticky (o `pin` de GSAP) muestra el escenario.
- Un único `progress∈[0,1]` por capítulo gobierna **5 capas máximas por defecto**.
- Define keyframes por fase: `0–0.2` establecer, `0.2–0.55` transformación, `0.55–0.8` revelación, `0.8–1` entrega a la siguiente sección.
- Una capa visual dominante cambia por transición; limita filtros costosos; no hagas 100 toggles ni renders por fotograma.
- Mantén enlaces, copy y controles legibles; no transformes el contenedor fijado, solo hijos.
- Para móvil simplifica a 2–3 capas, acorta pinning, evita horizontal fake scroll cuando interfiere con touch.
- `prefers-reduced-motion`: mostrar escenas estáticas o transiciones cortas sin parallax ni pin prolongado.
- `img` con dimensiones, fuente responsive y precarga del primer visual únicamente. No uses overlays sobre texto hasta ocultarlo.

## GSAP
```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);
const context = gsap.context(() => {
  const mm = gsap.matchMedia();
  mm.add('(min-width: 768px) and (prefers-reduced-motion: no-preference)', () => {
    const tl = gsap.timeline({scrollTrigger:{trigger:'.chapter',pin:'.stage',start:'top top',end:'+=180%',scrub:0.6,invalidateOnRefresh:true}});
    tl.fromTo('.subject', {yPercent:35,autoAlpha:0}, {yPercent:0,autoAlpha:1,duration:1,ease:'none'})
      .to('.foreground',{yPercent:-18,scale:1.12,duration:1,ease:'none'},0)
      .fromTo('.headline',{autoAlpha:0,y:32},{autoAlpha:1,y:0,duration:0.7,ease:'none'},0.35);
  });
});
// Cuando el componente se desmonta: context.revert();
```
No pegar este snippet sin adaptar selectores; no fijar `.stage` a la vez con CSS sticky y GSAP pin en el mismo modo.

Código offline funcional: `examples/layered-scroll-v4.html`. Plantillas y decisiones: `references/v4-layered-scroll.md`.
