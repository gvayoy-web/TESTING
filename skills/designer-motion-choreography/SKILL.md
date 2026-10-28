---
name: designer-motion-choreography
description: "Diseña movimiento con motivos, ritmos, dirección, velocidades y una secuencia focal sin animaciones repetidas ni jank."
---

# Coreografía de movimiento

Define **tesis de motion**: (1) momento protagonista, (2) continuidad, (3) feedback, (4) presupuesto.

- `100–150ms` interacción inmediata; `150–300ms` estado; `300–500ms` navegación; `500–800ms` intro focal justificada. Scroll scrub no usa duración cronológica fija: depende de distancia.
- Usa curvas de desaceleración naturales; CSS `cubic-bezier(.16,1,.3,1)` para entradas. En scrub GSAP usa `ease:'none'` para correspondencia espacial.
- El único acento cinético puede ser corte de escala, cambio de máscara o desplazamiento de cámara; no parallax, blur, flashes y partículas simultáneas.
- Mantén gestos táctiles, reversa y teclado. No desplazar el contenido fuera de vista hasta que JS lo active.
- R3F/Three.js solo para geometría real; `requestAnimationFrame` o shader con demanda condicionada al capítulo visible cuando sea posible.
- Auditoría: fps/long tasks, layouts, GPU, pruebas touch, reducción de movimiento, focus, CLS.
