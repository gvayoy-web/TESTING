# Contratos técnicos de artefactos

| Medio | Fuente editable prioritaria | Export usual | QA mínima |
|---|---|---|---|
| Logo | SVG / curvas editables / archivo de editor | SVG + PNG transparente + 1 tinta | vista 16/32 px, viewBox, contraste, mono |
| Iconos | SVG por icono, grid y token | SVG, sprite si se solicita | trazo, optical center, aria-label |
| Ilustración | SVG/capas raster editables | SVG/PNG/WebP | composición, trazos, bordes |
| Poster/flyer | diseño editable con medidas y fuentes | PDF de impresión/PDF visualización y PNG | sangrado, zona segura, tipografías, resolución |
| Packaging | dieline real + diseño editable | PDF por capa / mockup | medidas exactas, plegado, zonas legales |
| Social | fuente de composición | PNG/WebP/MP4 por relación | safe zones, legibilidad, copy |
| Web | repositorio fuente/componentes | build, sitio o screenshots | 320-1440, teclado, contraste, rendimiento |
| Gráficos | datos tabulares + código | SVG/PNG/HTML | ejes, unidades, exactitud |
| 3D | .blend / escena fuente o mallas | GLB/GLTF, FBX/OBJ o renders | escala, normals, UV, compatibilidad |
| Motion/video | proyecto editable, animatic | MP4/WebM + captions | duración, FPS, clips, derechos de música |
| Presentación | PPTX/Google Slides editable | PDF para compartir | overflow, fuentes, referencias |

## Política de entregables
- Nombre `proyecto-pieza-formato-vXX.ext`, master separado de outputs y pruebas.
- Archivo solo se declara creado si existe en el entorno; enlaces de sandbox solo tras comprobar.
- No confundir PDF de pantalla con PDF/X profesional; PNG no equivale a vector.
- Vincular licencias y procedencia, especialmente fotos, fuentes y modelos.
- Si el usuario pide modificación de archivo, preservar original o crear una versión de respaldo; documentar cambios.
- Si el usuario requiere varios tamaños, generar derivados desde un master único, no reescalar logos raster.
