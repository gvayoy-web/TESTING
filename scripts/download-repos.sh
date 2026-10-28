#!/usr/bin/env bash
set -uo pipefail
# Diseñador v2: solo clone sin instalar ni ejecutar terceros
DEST="${1:-$HOME/disenador-v2-originales}"
command -v git >/dev/null || { echo "Necesitas git" >&2; exit 1; }
mkdir -p "$DEST"
repos=(
  'anthropics/skills'
  'nextlevelbuilder/ui-ux-pro-max-skill'
  'pbakaus/impeccable'
  'MengTo/Skills'
  'freshtechbro/claudedesignskills'
  'greensock/gsap-skills'
  'claudekit/frontend-design-pro-demo'
  'bergside/awesome-design-skills'
  'vercel-labs/agent-skills'
  'vercel-labs/web-interface-guidelines'
  'shadcn-ui/ui'
  'radix-ui/primitives'
  'tailwindlabs/tailwindcss'
  'DavidHDev/react-bits'
  'magicuidesign/magicui'
  'ibelick/motion-primitives'
  'darkroomengineering/lenis'
  'motiondivision/motion'
  'pmndrs/react-three-fiber'
  'pmndrs/drei'
  'pmndrs/postprocessing'
  'emilkowalski/skills'
  'Leonxlnx/taste-skill'
  'CloudAI-X/threejs-skills'
  'wshobson/agents'
  'coreyhaines31/marketingskills'
  'microsoft/playwright'
  'dequelabs/axe-core'
  'GoogleChrome/lighthouse'
  'lucide-icons/lucide'
)
for repo in "${repos[@]}"; do
  target="$DEST/${repo//\//__}"
  if [[ -e "$target" ]]; then echo "SKIP existente: $repo"; continue; fi
  git clone --depth 1 --filter=blob:none "https://github.com/$repo.git" "$target" || echo "ERROR: $repo" >&2
done
echo "Fuentes descargadas en: $DEST"
echo "Revisa licencia de cada proyecto antes de copiar o redistribuir. Sin npm/postinstall."
