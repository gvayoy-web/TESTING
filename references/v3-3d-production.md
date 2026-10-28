# Producción 3D de estudio

## Pipeline
Brief y referencias → blockout → modelado → UV/topología → PBR/shaders → iluminación/cámara → render/test → export/optimización → validación.

## Formatos
- .blend: fuente editable si Blender disponible.
- glTF/GLB: transferencia a web, con texturas/materiales limitados al estándar soportado.
- OBJ: geometría y UV más simple; no supone PBR ni rigging completo.
- FBX: flujo dependiente de DCC y exportador instalado.
- PNG con alpha: imagen de render, no modelo tridimensional.

## Pruebas 3D
1. Escala y unidades explícitas, pivote en lugar lógico, ejes documentados.
2. Normales correctas y ausencia de caras invertidas/non-manifold para impresión.
3. UV sin texturas ausentes; uso correcto de color space de mapas.
4. Mallas por distancia, reducción de polígonos, compresión de textura, backface y draw calls.
5. Iluminación comprobada en fondo claro y oscuro si la marca lo requiere.
6. Verificar GLB con validador glTF si se tiene disponible; no declarar validación sin ejecutarla.
7. Para móvil: poster de fallback, loader y reduced motion.

## Script opcional
`scripts/blender-product-studio.py` crea una escena de ejemplo editable con Blender si está instalado. No implica que se ejecutó un render dentro de ChatGPT.
