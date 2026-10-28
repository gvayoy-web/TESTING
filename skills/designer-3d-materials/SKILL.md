---
name: designer-3d-materials
description: "Crea materiales PBR, clay, metal, vidrio, textiles y texturas de modelos 3D."
---

# Diseñador v3 — 3D Materials

**Activación:** Crea materiales PBR, clay, metal, vidrio, textiles y texturas de modelos 3D.

## Procedimiento
1. Escoge referencia física y narrativa de material antes de configurar shaders.
2. Define base color, roughness, metalness, normal, AO y mapas cuando existan; no mezcles mapas sin convención.
3. Comprueba consistencia color space (sRGB para basecolor, linear para mapas de datos).
4. Genera UV o triplanar según complejidad, verifica seams y repeticiones.
5. Cuida costo de shaders y usa LOD/fallback donde proceda.

## Entregable
Preset/material documentado, mapas con rutas relativas, vistas de prueba y variantes.

## Puerta de calidad
Material legible con luz neutra, energía plausible, sin texturas rotas ni dependencias remotas.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-3d-production.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
