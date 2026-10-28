---
name: designer-postprocessing
description: "Aplicar bloom, SSAO, profundidad de campo, ruido, LUT y postprocesado 3D de forma selectiva y barata."
---

# Postprocesado con criterio

Fuentes: https://github.com/pmndrs/postprocessing y `CloudAI-X/threejs-skills` (threejs-postprocessing).

- Define objetivo de un solo efecto antes de crear EffectComposer.
- Un único pipeline compartido; evita varios render passes duplicados. Selecciona bloom selectivo en lugar de bloom global si la legibilidad lo pide.
- Asegura color space y tone mapping consistentes con el renderer. Revisa alpha/compositing cuando el canvas es transparente.
- En móvil, prioriza escenas sin DOF/SSAO; evalúa la calidad percibida vs ms reales de GPU, no presupongas 60 fps.
- Ajusta tamaño a DPR acotado y redimensiona el composer. Libera render targets al desmontar.
- No sacrifiques texto y CTA por glow/film grain, y usa fallback estático si WebGL falla.

Antes/después: capturas comparables y reporte de GPU/CPU si se dispone de instrumentos.
