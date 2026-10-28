# Impeccable × Diseñador — Guía de integración V4

Origen contrastado: https://github.com/pbakaus/impeccable (Paul Bakaus; licencia Apache-2.0, NOTICE para terceros). Versión de referencia consultada en la rama main, skill `.agents/skills/impeccable/SKILL.md` con metadata 4.8.0 al preparar V4. Esta integración es una implementación original en español; no ejecuta `impeccable context`, `impeccable detect`, su motor Rust, ni sus hooks automáticamente.

## Conceptos trasladados

- Cuatro modos de superficie: Persuade / Operate / Read / Experience. Priorizar conversión, eficacia, comprensión o exploración respectivamente.
- Identidad estable: **refinar** conserva el lenguaje visual del proyecto; **rediseñar** lo sustituye conscientemente, conservando verdad, funciones, contenido y permisos.
- Intención editorial: composición específica a audiencia y producto, no layout genérico de cards de igual tamaño.
- Una secuencia hero/motion focal de autor; no animar todas las secciones por inercia.
- Autoridad visual con evidencia: leer DESIGN.md, PRODUCT.md si están, assets y código; si falta DESIGN.md, no asumir que es greenfield.
- La revisión del resultado debe **ver** el render a los tamaños de publicación, más pruebas de interacción; detectores, heurísticas y calificaciones no reemplazan juicio editorial.
- Calidad: contraste, jerarquía, legibilidad, densidad, estados, teclado, responsive, copy factual, archivos de tipografía y seguridad.

## Decisión creativa

| Estado | Resultado | Skills |
|---|---|---|
| Web nueva | mundo visual singular + implementación | `designer-impeccable`, `designer-experience-modes` |
| Pulir web | conservar sistema y mejorar precisión | `designer-art-direction-polish` |
| Auditar | hallazgos verificables | `designer-design-critique`, `designer-visual-regression` |
| Landing con coreografía | beats y scroll por capas | `designer-layered-scroll` |
| UI operativa | controles y datos sobre espectáculo | `designer-ui-hardening` |

No copiar el CLI ni atribuirle resultados al detector sin instalarlo. Para obtener el upstream: `git clone https://github.com/pbakaus/impeccable.git` y revisar `LICENSE` y `NOTICE.md`.
