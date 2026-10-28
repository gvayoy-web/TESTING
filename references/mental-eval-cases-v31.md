# Casos de aceptación de la mente visual (evaluación manual)

Estas pruebas no son benchmarks de ahorro de tokens. Son escenarios para comprobar el enrutamiento y la calibración.

1. Brief: «Botones pastel inflados, esquinas redondas, dos sombras suaves, aspecto plastilina». Esperado: claymorphism, alta; no cargar Three.js.
2. Brief: «Tarjetas del mismo color que el fondo, casi sin contraste, relieve por luces y sombras». Esperado: neumorphism, alta; advertir contraste si requiere interacción.
3. Brief: «Paneles translúcidos con backdrop blur y contenido detrás». Esperado: glassmorphism, alta; atención a legibilidad.
4. Brief: «Titulares gigantes, rejilla tipográfica rigurosa, mucho espacio blanco». Esperado: editorial/swiss, media-alta según contexto; no brutalism automático.
5. Brief: «Brillos cromados, gradientes iridiscentes, tipografía retrofuturista». Esperado: Y2K/chrome, alta; no Three.js obligatorio.
6. Brief: «Quiero una landing minimalista» (sin referencia). Esperado: decisión de diseño, NO reconocimiento visual demostrado; sin confianza alta injustificada.
7. Brief: «Haz un logo SVG simple»; esperado: especialista de logo+SVG; no cargar 3D ni motion.
8. Brief: «Tengo captura de una web; ¿qué estilo es?» sin captura accesible. Esperado: declarar falta de imagen y no inventar evidencias.
9. Brief: «Actualiza color de un botón y déjalo accesible». Esperado: cambio mínimo, revisión de contraste, sin cambios de framework.
10. Brief: «Rediseña web completa con 3D» y repo real. Esperado: seleccionar stack existente, plan interno conciso, implementar, testear, fallback móvil.
11. Brief: «Haz todo en un prompt». Esperado: ejecución real de todas las fases permitidas, no exigir pasos arbitrarios ni prometer trabajo en segundo plano.
12. Brief: «Explícame todo con máximo detalle». Esperado: no imponer respuesta breve; respetar la instrucción expresa.
