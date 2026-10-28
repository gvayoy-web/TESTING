---
name: designer-ui-hardening
description: "Endurece diseños y experiencias contra estados límite, fallos de carga, localización, foco y errores sin añadir complejidad innecesaria."
---

# Hardening de UI

- Flujos completos: loading, empty, slow, offline, failed, denied, success, disabled, long copy, small viewport.
- Contratos: navegación y CTA funcionan aun si animación/3D no carga; controles semánticos y foco restaurable.
- Adaptación: formatos internacionales, strings largos, preferencias de movimiento, zoom, cambio de tema.
- Animaciones: cleanup en unmount, ScrollTrigger refresh solo tras reflow real, ningún estado invisible al fallar JS, no fijación infinita.
- Medir los efectos reales de la corrección en tests, snapshots y navegación; no crear abstracciones sin uso.
- Reportar qué caminos se comprobaron y cuáles no.
