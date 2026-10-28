---
name: designer-mask-transitions
description: "Crea revelaciones de capas con clip-path, máscaras, compositing y cambios de profundidad sin cortar contenido ni romper rendimiento."
---

# Máscaras / Oclusión / Handoffs

Usar máscara cuando explique la transición (corte arquitectónico, revelado de producto, cambio de soporte), no solo porque sea vistosa.

1. Preferir un elemento o pseudo-elemento de máscara aislado para evitar alterar layout del contenido.
2. `clip-path: inset()` / `circle()` si la geometría es simple; `mask-image` con fallbacks si necesita materialidad. Para bordes orgánicos exige máscara alfa real, no círculos aproximados sobre personas.
3. Animar variables de capa o transforms/opacity. `clip-path` y `filter` pueden requerir repintado: medir en el dispositivo objetivo.
4. Nunca ocultar focos y botones ni impedir que enlaces reciban eventos; `pointer-events:none` para capas puramente decorativas.
5. En reduced-motion usar imagen final estática y transiciones por color/opacidad; garantizar semántica y lectura aun sin JS.

Patrón: background base + overlay recortado + sujeto + título. Los estados al 0% y 100% deben ser composiciones completas, no pantallas vacías.
