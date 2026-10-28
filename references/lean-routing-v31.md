# Lean routing — selección de habilidades y coste contextual

**Regla:** leer el archivo pequeño que resuelve la tarea; escalar solo ante un vacío real. El coordinador `skills/disenador/SKILL.md` permanece breve. Evitar cargar el catálogo entero de 67 estilos o los 58 repositorios por defecto.

| Pedido | Ruta mínima | Escalar cuando |
|---|---|---|
| «¿Qué estilo es este?» con imagen | `designer-visual-mind` y, si es ambiguo, `visual-dna-v31.md` | Si pide replicarlo, cargar el especialista del medio |
| «Quiero claymorphism» | `designer-clay` | Si hay diseño nuevo completo, `designer-design-system` |
| «Haz logo vectorial» | `designer-logo-design` + `designer-vector-svg` | Branding completo: `designer-branding` |
| «Rediseña mi landing» | `designer-autopilot` + `designer-style-lab` | Código complejo: `designer-implementation-strategy` |
| «Crea hero 3D» | `designer-threejs` o `designer-r3f` | GLSL personalizado: `designer-shaders` |
| «Haz poster para imprimir» | `designer-editorial-poster` + `designer-print-prepress` | Si es fotográfico: `designer-image-retouch` |
| «Crea motion graphic» | `designer-motion-graphics` | Video completo: `designer-video-pipeline` |
| «Corrige botones» | `designer-component-library` | Defecto sistémico: `designer-design-tokens` |
| «QA de toda web» | `designer-audit` + `designer-a11y` | Si hay repositorio y tests, `designer-playwright` |

## Contexto
- Inspeccionar 1 manifest/README relevante y rutas afectadas, no copiar todo el repo al chat.
- Usar búsqueda por filename/símbolo y extraer trozos pertinentes; no abrir cientos de módulos sin evidencia.
- Reusar material ya inspeccionado en el turno; actualizarlo solo si hay cambios.
- No convertir 5 fases en 5 resúmenes. Ejecutar y contar resultados.
- Si algo falta, una pregunta indispensable (cuando es realmente imposible) o supuesto pequeño y reversible.

## Criterio de parada
Al cumplir el objetivo, pasar los checks proporcionales al riesgo y producir el entregable. No agregar efectos, repos, frameworks ni refactorizaciones como regalo. Escalar solo cuando un bug, inaccesibilidad, requisitos del usuario o pruebas lo exijan.
