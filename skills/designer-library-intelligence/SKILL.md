---
name: designer-library-intelligence
description: "Consultar repositorios externos de UI, motion y 3D, determinar sus licencias/compatibilidad y recomendar la alternativa mínima eficaz."
---

# Inteligencia de repositorios

Usa `references/repositorios-v2.md` como lista curada, NO como librería instalada. Cuando el usuario pida nuevos recursos, investiga vigencia, licencia, mantenimiento, API, performance y compatibilidad antes de adoptar.

**Reglas**: prioriza docs oficiales/repositorios, valida versión del framework y el método de import, verifica paquetes npm contra el sitio oficial. Evita copiar licencias restrictivas dentro de plugins o redistribuir componentes que lo prohíban. Nunca instales dependencias sin permiso del entorno y revisión razonable.

**Score /100**: ajuste a necesidad (30), facilidad/compatibilidad (20), accesibilidad (15), mantenimiento/seguridad (15), rendimiento (15), licencia (5). No informes puntajes como medición objetiva; son juicio de ingeniería.

Forma salida: recurso, motivo, coste técnico, alternativa nativa y riesgo, más enlace oficial.
