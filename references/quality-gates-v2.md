# Quality Gates — criterio de salida

| Gate | Prueba | Éxito | Qué reportar |
|---|---|---|---|
| G0 Código | build/lint/typecheck | sin error bloqueante | comando, resultado real |
| G1 Función | CTA, menú, rutas, formularios | tarea primaria completada | ruta/interacción |
| G2 Visual | 320/375/768/1024/1440 | jerarquía y sin recorte involuntario | screenshots si existen |
| G3 Accesibilidad | teclado, foco, contraste, reduced motion | problemas severos corregidos | herramientas/manual |
| G4 Motion | animaciones reversibles/no bloquean | sin jank significativo visible | prueba real o NOT RUN |
| G5 3D | WebGL supported/unsupported | contenido y CTA no dependen del Canvas | fallback |
| G6 Calidad | errors/loading/empty | feedback y estados completos | caso de prueba |
| G7 Performance | CWV y tamaño de assets | sin regresión no justificada | instrumento y datos |
| G8 Seguridad | secretos, deps, enlaces, contenido externo | ningún hallazgo crítico conocido | verificación realizada |
| G9 Release | rama/commit/deploy solicitados | artefactos reales y links válidos | SHA/URL solo si comprobados |

Regla: un Gate NOT RUN no es PASS. Riesgos críticos que no se hayan corregido se explican; no declarar "production ready" sin pruebas. Si el usuario demanda creatividad radical, conservar función y accesibilidad.
