---
name: designer-clay
description: "Diseñar e implementar claymorphism: superficies puffy, sombras internas y externas, relieve colorido, accesibilidad y performance."
---

# Claymorphism utilizable en producción

Diseñar superficies como arcilla/blando juguete: formas redondeadas, iluminación coherente, volumen "puffy", materiales mates y sombras internas/externas. Juguetón NO significa infantil obligatorio.

## Tokens de referencia
```css
:root {
  --clay-bg:#f5efff; --clay-panel:#efe7ff; --clay-accent:#8a64e8;
  --clay-ink:#292044; --clay-radius:28px;
  --clay-raised: 12px 14px 28px rgba(95,67,142,.18), -7px -8px 17px rgba(255,255,255,.9), inset 2px 3px 6px rgba(255,255,255,.75), inset -3px -4px 8px rgba(133,100,189,.13);
  --clay-pressed:inset 6px 7px 12px rgba(95,67,142,.18), inset -4px -4px 10px rgba(255,255,255,.65);
}
.clay-card{border-radius:var(--clay-radius);background:var(--clay-panel);box-shadow:var(--clay-raised);color:var(--clay-ink);}
.clay-button{background:var(--clay-accent);border:2px solid transparent;border-radius:999px;color:white;box-shadow:var(--clay-raised);transition:transform .2s ease,box-shadow .2s ease;}
.clay-button:hover{transform:translateY(-2px)}
.clay-button:active{transform:translateY(1px);box-shadow:var(--clay-pressed)}
.clay-button:focus-visible{outline:3px solid #21214d;outline-offset:4px}
@media(prefers-reduced-motion:reduce){.clay-button{transition:none}}
```

## Calidad
- Usa las 3D-like sombras por componente, NO filters caros en cada pixel. Evita sombras sin fuente de luz consistente.
- Permite radio entre 18 y 40px en elementos clay, pero no contamine navegación y tablas donde la geometría convencional ayuda.
- Preserva estados interactivos explícitos; las sombras no sustituyen labels.
- En modo oscuro ajustar paneles y sombras por separado: no invertir filtros.
- Evitar neumorfismo blanco-sobre-blanco de bajo contraste.
- Para un hero 3D clay verdadero, Three.js MeshPhysicalMaterial/StandardMaterial con roughness alto, geometría suavizada e iluminación de área aproximada.

Fuente de estilo: bergside/awesome-design-skills/skills/claymorphism/SKILL.md (MIT). Consulta source antes de afirmar exactitud con nuevas versiones.
