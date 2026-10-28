---
name: designer-gsap
description: "Implementar microinteracciones, timelines, easing, stagger y animación GSAP en React y HTML, con cleanup."
---

# GSAP en producto web

GSAP es una herramienta para comunicar cambios de estado y transiciones narrativas.

## Principios
- Usa `gsap.to`, `.from`, `.fromTo` para estados; timelines para secuencias. Favorecer `transform` y `opacity` sobre top/left/layout.
- En React scoped contexts con `gsap.context()` o `useGSAP()` (si disponible), revertir al desmontar; no dejar dobles triggers.
- GSAP en scroll es otro skill (`designer-scroll`). Animación de interfaz nunca debe bloquear el CTA.
- Easing: expo/power para UI refinada; elastic/bounce sólo para clay lúdico y con moderación.
- Duración 150–300ms para interacción y 400–900ms para revelación, según complejidad.
- `matchMedia` y `prefers-reduced-motion` para desactivar traslaciones largas, zoom exagerado o animaciones repetitivas.
- Testear anchos estrechos y text overflow durante animaciones.

Estructura: establecer propiedades iniciales, animar, revertir en cleanups, controlar acciones activables repetidas.

Fuente: GSAP oficial greensock/gsap-skills/gsap-core. Comprobar API instalada antes de usar extensiones.
