---
name: designer-view-transitions
description: "Aplicar transiciones de navegación y continuidad visual con View Transitions API o React cuando esté soportado."
---

# View Transitions

Referencia: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions

- Detecta framework, router y soporte del navegador; elige native View Transitions si basta, no instales otra librería automáticamente.
- Selecciona dos a cuatro elementos persistentes a través de la navegación (thumbnail, hero label, card); evita transiciones masivas en todo el DOM.
- Protege foco y posición de scroll tras navegación, conserva la URL y back/forward. El cambio de página debe funcionar sin transición.
- Mantén ids de transición únicos, elimina colisiones entre elementos compartidos, limita duración y reduce movimiento.
- Si React/SSR: no animar markup no hidratado ni capturar estado de navegación inexistente; comprueba compatibilidad actual.
- QA real: entrada directa a URL, atrás/adelante, móvil, modo reduced motion, navegador sin API.
