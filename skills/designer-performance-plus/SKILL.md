---
name: designer-performance-plus
description: "Optimizar Core Web Vitals, render 3D, bundle de dependencias y scroll sin inventar métricas."
---

# Performance & Core Web Vitals

Fuentes: https://github.com/GoogleChrome/lighthouse, https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices y https://github.com/CloudAI-X/threejs-skills.

- Detecta stack y genera perfil base ANTES de cambiarlo si Lighthouse/devtools disponibles; no inventes mediciones. Observa LCP, INP, CLS, imágenes, tamaño JS, requests, render blocking y CPU/main thread.
- Target orientativos para buena experiencia: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 en datos de campo; laboratorio y datos reales son distintos.
- Prioriza eliminar waterfalls y JS innecesario; carga diferida de escenas 3D o efectos decorativos después de contenido principal. Fonts `font-display`, tamaños de imágenes conocidos y fuentes limitadas.
- Render 3D: limitar DPR, draw calls, overdraw, texturas, postFX, pausar offscreen, fallback sin WebGL.
- Animaciones: transform/opacity; preferir una única raf loop; cleanup de observers y de listener. No habilites scroll smoothing solo para lucir suave.
- Al final compara resultado con baseline y explica limitaciones de medición.
