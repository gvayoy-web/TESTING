# Visual DNA — familias de estilo y falsas equivalencias

Guía **bajo demanda**. Para referencias con imágenes, observa la pieza antes de clasificar. El nombre del estilo es una hipótesis; la forma, materialidad, ritmo y tipografía son evidencias.

| Familia | Señales distintivas | No confundir con |
|---|---|---|
| Claymorphism | Formas mullidas/puffy, radios muy amplios, colores suaves o sólidos, volumen amable y doble sombra | Neumorphism: relieve tonal, no piezas de arcilla |
| Neumorphism | Componentes del mismo tono del fondo, luces/sombras exteriores e interiores sutiles, sensación de molde | Glass: transparencia y contenido detrás |
| Glassmorphism | Transparencia, blur real del fondo, bordes translúcidos, luz especular | Tarjeta blanca opaca con sombra |
| Skeuomorphism | Imitación de objetos y materiales físicos reales, controles análogos, textura y profundidad funcional | Una única textura como decoración |
| Neo-brutalism | Bordes negros, sombras desplazadas duras, tipografía pesada, bloques contrastados | Dark UI minimal con tarjetas |
| Brutalism/editorial experimental | Jerarquía cruda, tipografía protagonista, ruptura intencional de la retícula, alto contraste | Layout mal alineado por error |
| Swiss/editorial | Retícula disciplinada, contraste tipográfico, jerarquía en blanco, espacio negativo, lectura consciente | Minimalismo genérico sin sistema |
| Minimalismo | Pocos elementos, funciones claras, espacio negativo, paleta contenida | Interfaz sin contenido suficiente |
| Maximalismo | Alta densidad organizada, ornamentos, capas, lenguaje visual abundante | Ruido visual sin estructura |
| Bento | Bloques modulares de tamaños contrastados en rejilla, agrupación temática | Toda cuadrícula de tarjetas iguales |
| Y2K/chrome | Superficies glossy, metal líquido, iridiscencia, tipografías retro-futuristas, destellos | Simple gradiente oscuro/neón |
| Retro/pixel/riso | Formas históricas intencionales, pixel grid o trama de impresión, paletas limitadas, textura de reproducción | Compresión de imagen accidental |
| 3D product/immersive | Perspectiva espacial, iluminación volumétrica y parallax real, cámara/objetos con profundidad | Sombras CSS o botón levantado |
| Material/enterprise | Sistemas tipográficos y de componentes explícitos, jerarquías de densidad, estados coherentes | Un estilo puramente decorativo |
| Organic/biomorphic | Contornos irregulares, curvas fluidas, asimetría natural, composiciones orgánicas | Una forma circular suelta |

## Clasificación en tres observaciones
1. **Geometría:** bordes, radios, grid, ocupación del espacio.
2. **Superficie:** transparencia, relieve, material, sombra, textura.
3. **Tipografía/ritmo:** pesos, escala, proporción, tono, animación.

Si las tres coinciden, confianza alta. Si dos, media; si una, baja. No se calculan probabilidades estadísticas. «Visualmente es X» no implica que fue implementado con tecnología X. Para escoger el estilo más conveniente: evalúa audiencia, tarea y restricciones, no solo similitud.

### Falsos positivos habituales
- Blur decorativo no equivale a glassmorphism si no hay transparencia sobre elementos posteriores.
- «3D» y «Three.js» no son sinónimos; Three.js puede dibujar formas planas y el CSS puede simular volumen.
- Una paleta pastel no basta para diagnosticar claymorphism.
- Una retícula Bento no es por sí sola un sistema de diseño.
- El mismo producto puede usar composición editorial y acentos clay; jerarquiza las capas en lugar de listar todo como dominante.
