# Diseñador V4 — Impeccable Craft × Layered Scroll

Versión: **4.0.0**. Mismo plugin privado `disenador`, nuevas especialidades y ejemplos ejecutables.

## Novedades

1. **Impeccable craft**: modos Persuade/Operate/Read/Experience, dirección de arte específica, preservar o reemplazar identidad según el alcance.
2. **Transiciones de scroll por capas**: fondo, objetos, titulares, máscaras y handoffs mediante un mismo progreso `0..1`.
3. **Storyboard y motion contract**: cada escena tiene propósito, cadencia y salida clara; no se acumulan efectos inútiles.
4. **QA visual**: crítica de diseño separada de prueba técnica; validar render en responsive, reduced-motion, scroll bidireccional y contenido.
5. **Demo offline**: `examples/layered-scroll-v4.html`, se abre con doble clic sin instalar dependencias. Para escenas reales sustituir geometría demo por assets propios.

## Workflow

Pedido de usuario → `designer-visual-mind` (solo con referencias) → `designer-lean-mind` → `designer-impeccable` → `designer-layered-scroll` (cuando aplica) → render → QA → entrega.

Para scroll por capas comenzar con `designer-layered-scroll` y `designer-scroll-storyboard`. Para crítica `designer-design-critique` y `designer-visual-regression`.

## Fuentes y límites

Basado en principios estudiados en [Impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus, Apache-2.0) y en [GSAP ScrollTrigger](https://github.com/greensock/gsap-skills). **No** incorpora ni ejecuta el CLI, binarios, hooks ni detectores propios de Impeccable. No incluye código upstream completo; el contenido nuevo son instrucciones originales y demo de Diseñador.

Los skills anteriores se conservan. Un skill no instala automáticamente GSAP, Blender, Figma ni WebGL. El demo offline usa JavaScript nativo.

Para ejecutar pruebas de demo: `pytest -q tests/test_layered_scroll.py` si Python + Playwright + Chromium están disponibles.

## Exportación a GitHub

El código del plugin y sus 89 skills se publicaron en este repositorio; los dos PNG binarios del paquete privado no se reproducen en esta exportación de texto. `assets/icon.svg` sustituye el icono PNG en los manifiestos. Para conservar exactamente todos los recursos, utiliza el ZIP original de Diseñador V4.
