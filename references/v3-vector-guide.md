# SVG y arte vectorial — reglas de producción

SVG es vector editable, no un canvas con JPEG embebido. Requisitos:
- `viewBox` estable + `width`/`height` apropiados; grupos y IDs únicos cuando haya símbolos o gradientes.
- Usar `stroke-linecap`, `stroke-linejoin`, `fill-rule` explícitos cuando afecten aspecto.
- No incrustar JavaScript ni XML entities arbitrarias; no cargar imágenes/fonts de dominios no verificados.
- Elementos `<text>` pueden depender de tipografía externa; para imprenta considera contornear con herramientas adecuadas y conservar la fuente editable aparte.
- No deformar el `viewBox`; exportar con proporción conservada.
- Para iconografía, comprobar legibilidad a 16, 20, 24, 32 y 64 px y evitar trazos muy finos.
- Ejecutar `python scripts/svg-preflight.py ejemplo.svg`; revisar manualmente la forma renderizada.

### Repos de referencia
svgdotjs/svg.js, fabricjs/fabric.js, paperjs/paper.js, konvajs/konva, opentypejs/opentype.js, svg/svgo, rough-stuff/rough, iconify/iconify. Código de terceros requiere licencia y revisión; el plugin no lo instala automáticamente.
