# Arquitectura Layered Scroll v4

Un capítulo narrativo es una unidad de **distancia scroll**, no una animación que secuestra la rueda del ratón. Componer con planos independientes: (A) ambiente, (B) atmósfera/partículas opcionales, (C) objeto/sujeto, (D) titular, (E) interfaz narrativa. 5 capas es un máximo orientativo, no un requisito.

## Handoff entre escenas

`0–20%` establecer mundo y foco → `20–55%` transformación → `55–80%` revelación → `80–100%` entregar atención a la siguiente escena. Un capítulo nuevo debe comenzar sobre el mismo eje o explicar la discontinuidad visual. El scroll permite avance y retroceso deterministas.

## CSS sticky vs GSAP

**CSS sticky:** etapa `.chapter {height:260svh}` y `.stage {position:sticky;top:0;height:100svh}`. No JS si una composición estática/etapas CSS es suficiente. Para varios elementos con progreso continuo, rAF throttled usando `getBoundingClientRect` una vez por capítulo.

**GSAP:** un único ScrollTrigger por secuencia si se necesita pin compartido + scrub + timeline. Animar hijos del contenedor fijado, no el propio pin. `ease:'none'` en animaciones ligadas al desplazamiento; marcar desde y hasta. Usar `gsap.context`/`useGSAP`, cleanup. Llamar refresh tras fuentes o imágenes que cambian layout. Evitar doble pin CSS/GSAP.

**WebGL/R3F:** calcular cámara, luces y posición de objeto a partir del mismo progreso; limitar raster/texture y pausar offscreen. No crear WebGL cuando CSS/SVG cumple.

## QA

1. Inicio/medio/final de cada capítulo + scroll hacia atrás.
2. Contenido útil sin JS y con movimiento reducido; `position:sticky` eliminado en reduced motion cuando hace un recorrido demasiado largo.
3. 320, 375, 768, 1024, 1440; título no cortado; pointer/touch sin scroll-lock.
4. Foco del teclado visible, navegación y enlaces dentro de escenas.
5. Nada de scroll-jacking, auto-scroll, overscroll inventado ni loop visual eterno.
6. FPS/paint y CLS medidos si hay herramientas; declarar si no se midieron.
7. Capas puramente decorativas `pointer-events:none;aria-hidden=true`.

El demo offline usa DOM + CSS + JS sin dependencias. Para una web real, sustituye decoraciones por assets con licencia y evita recrear fotografías con CSS.
