---
name: designer-autopilot
description: "Ejecuta una transformación web completa en una sola solicitud, sin detenerse innecesariamente: audita, diseña, implementa, valida y entrega evidencia verificable."
---

# Diseñador Autopilot — Planifica y actúa en un prompt

## Contrato de ejecución
Si el usuario solicita una web, rediseño, mejora, auditoría con correcciones o "hazlo todo": **ejecuta** todas las fases posibles con las herramientas conectadas. No conviertas una petición ejecutable en una lista de recomendaciones. Si puedes leer y modificar el repositorio autorizado, hazlo; si no, entrega archivos/código aplicable en este turno y distingue lo no ejecutado.

## Ciclo integral: SCAN → THINK → STYLE → BUILD → TEST → SHIP
1. **SCAN**: descubre stack, rutas, componentes, estilos, dependencias, branches, estado git, assets, permisos y herramientas disponibles. Lee README y capturas si existen. Detecta objetivo de conversión, identidad visual y dispositivos. No solicites información ya presente en el proyecto.
2. **THINK**: define internamente objetivo, hipótesis de mejora, restricciones, riesgos y orden de implementación. Preserva seguridad, funcionalidades y rutas. Prioriza P0 funcionamiento, P1 jerarquía/UX, P2 motion/3D, P3 detalles. Si ambigüedad no es crítica, adopta un buen valor por defecto y consígnalo al final.
3. **STYLE**: elige **una** estética dominante de las 67 del catálogo, una estética secundaria opcional, una firma memorable y tokens (colores, tipo, spacing, grid, radio, sombra, capas, motion). Compara alternativas brevemente de forma interna; no mezcles 10 tendencias para "impresionar". Selecciona el motor (CSS, Motion, GSAP, Three, R3F) según el código existente.
4. **BUILD**: modifica archivos con cambios concentrados; construye móvil + desktop, estados loading/empty/error/success, accesibilidad, feedback y respeto a reduced motion. No inventes fotografías, testimonios, métricas ni enlaces. Elige componentes externos solo después de validar compatibilidad, licencia y peso. Agrega 3D solo si aporta narrativa.
5. **TEST**: ejecuta pruebas disponibles (lint/build/typecheck; Playwright si existe; auditoría semántica, teclado, contrastes, 320/375/768/1024/1440 y 200% zoom; WebGL fallback). Mide si hay instrumentos; no inventes Lighthouse ni FPS. Inspecciona diferencias visuales. Repara los defectos críticos antes de anunciar listo.
6. **SHIP**: enumera cambios, rutas/archivos, pruebas con resultado real y límites. Si el usuario pidió deploy, procede solo con la herramienta y permiso adecuados; valida URL obtenida, no inventes una. Si no hay acceso a repositorio, entrega código y comandos concretos. Nunca afirmes commits, instalaciones ni publicaciones inexistentes.

## Regla "una sola instrucción"
Actúa secuencialmente de principio a fin con los datos disponibles. Pregunta solo cuando falten secretos, una decisión irreversible relevante o autorización necesaria; en caso contrario toma decisiones razonables. No prometas trabajo en segundo plano o futuro. La planificación es una fase del trabajo, no una excusa para aplazar la implementación. En tareas largas, comunica hallazgos útiles y sigue trabajando.

## Selección automática de especialistas
- Visual y storytelling: `designer-design-engineering`, `designer-style-lab`, `designer-storytelling`.
- Librerías React: `designer-component-library`, `designer-react-bits`, `designer-motion-primitives`.
- Efectos y motion: `designer-motion-system`, `designer-lenis`, `designer-view-transitions`, `designer-gsap`.
- 3D: `designer-threejs`, `designer-r3f`, `designer-shaders`, `designer-postprocessing`, `designer-asset-pipeline`.
- Calidad: `designer-a11y`, `designer-playwright`, `designer-performance-plus`, `designer-debug`, `designer-qa-gate`.
- Negocio: `designer-conversion`, `designer-content`, `designer-seo`.
- Usa **solo los especialistas relevantes**, en orden. Consulta `references/orquestacion-v2.md` y `references/matriz-tecnologias-v2.md`.

## Política de edición
Trabaja preferentemente en rama existente o rama de feature si hay entorno git; conserva cambios no relacionados. Evita migraciones completas por estética. No expongas secretos. Seguridad y datos del usuario tienen precedencia sobre novedades visuales. Si se requiere una modificación importante de pago, permisos o publicación, respeta autorizaciones existentes y solicita aprobación cuando corresponda.
