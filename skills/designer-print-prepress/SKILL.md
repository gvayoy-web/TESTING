---
name: designer-print-prepress
description: "Prepara piezas para impresión, con sangrado, perfiles, tipografías y control preflight."
---

# Diseñador v3 — Print Prepress

**Activación:** Prepara piezas para impresión, con sangrado, perfiles, tipografías y control preflight.

## Procedimiento
1. Solicita o infiere de documentos existentes tamaño final, número de caras, papel, método y especificación de la imprenta.
2. Configura bleed (frecuentemente 3 mm, pero prevalece requisito del impresor) y zona segura distinta del sangrado.
3. Revisa perfiles ICC, RGB/CMYK, rich black y overprint solo con perfil y proceso conocidos; evita conversiones improvisadas.
4. Comprueba resolución efectiva de bitmaps según tamaño final (300 ppp es referencia común, no regla absoluta).
5. Incrusta o contornea fuentes según contrato; prepara PDF/X solo con herramienta y preset válidos.
6. Entrega ficha de impresión y prueba visual, sin declarar imprenta-ready si no se verificaron separaciones/color.

## Entregable
Archivo final para imprenta cuando sea técnicamente posible + ficha de preflight.

## Puerta de calidad
No recortar información crítica; fuente adecuada; bleed, tamaño final, transparencia y perfil revisados.

## Coordinación
Selecciona el soporte correcto, sigue el orquestador `designer-universal-autopilot` para tareas compuestas y aplica las reglas de atribución, edición autorizada y pruebas reales. Para detalles operativos consulta `references/v3-print-production.md` de la raíz del plugin. No afirmes haber ejecutado una herramienta ausente; entrega fuentes editables y resultados concretos cuando el entorno lo permita.
