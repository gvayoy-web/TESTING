---
name: designer-asset-pipeline
description: "Crear un pipeline fiable para GLB/glTF, compresión de modelos, texturas, carga progresiva y fallbacks 3D para web."
---

# Asset Pipeline 3D

1. Inventaria modelos `.glb/.gltf`, texturas, HDRI, licencias, unidades, puntos de origen y dirección de escena.
2. Para web: geometría razonable, LOD cuando se justifique, texturas adecuadas al dispositivo, compresión KTX2/Basis donde sea compatible, Draco/Meshopt según el pipeline y loaders disponibles.
3. Comprueba compatibilidad entre compresión y loaders. No conviertas archivos sin conservar originales/referencias.
4. Carga progresiva: skeleton o poster visible, progreso no bloqueante, fallback si canvas no se inicia. Evita loader de pantalla completa que impida navegar.
5. En R3F, reutiliza geometría y materiales donde sea posible, Suspense con fallback, cleanup al desmontar y preload solo para escena crítica.
6. Revisa licencia del modelo, derechos de textura/fotos y exportación desde Blender antes de publicar.

Entrega: manifiesto de assets con tamaño, uso, prioridad de carga y alternativa sin GPU.
