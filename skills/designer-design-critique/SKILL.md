---
name: designer-design-critique
description: "Critica diseños por jerarquía, especificidad, carga cognitiva, estados y heurísticas; produce hallazgos reales priorizados sin inventar pruebas."
---

# Crítica independiente y accionable

Separar **A. juicio de diseño** y **B. evidencia técnica** para evitar anclaje: si no hay subagentes, haz las dos evaluaciones secuencialmente.

A. ¿El diseño pertenece a este producto? Analiza composición, copy, identidad, lectura, foco, descubribilidad, tono, moment-to-moment, puntos de fricción y estética.
B. Si el runtime lo permite: render, resize, teclado, touch, consola, accesibilidad, CSS computado, contraste y performance. Una captura no prueba el comportamiento táctil real.

Hallazgos `[P0–P3] título · ubicación · prueba/razón · impacto · corrección mínima`; distingue hechos observados de gusto subjetivo. Selecciona 3–5 cambios principales, no 50 sugerencias. No inventes métricas Lighthouse ni puntuación visual objetiva.

Si solo hay código no ejecutable, marca «revisión estática; no inspección visual». La revisión no cambia archivos salvo autorización.
