#!/usr/bin/env bash
set -euo pipefail
# Opcional: descarga de fuentes ORIGINALES a un directorio local.
# Revisa el código y las licencias de cada repositorio antes de ejecutar sus scripts.
DEST="${1:-$HOME/disenador-originales}"
mkdir -p "$DEST"
for REPO in   anthropics/skills   nextlevelbuilder/ui-ux-pro-max-skill   pbakaus/impeccable   MengTo/Skills   freshtechbro/claudedesignskills   greensock/gsap-skills   claudekit/frontend-design-pro-demo   bergside/awesome-design-skills; do
  NAME="${REPO##*/}"
  TARGET="$DEST/$(printf '%s' "$REPO" | tr '/' '_')"
  if [ -d "$TARGET/.git" ]; then echo "Already present: $REPO"; else git clone --depth 1 "https://github.com/$REPO.git" "$TARGET"; fi
done
echo "Fuentes descargadas en $DEST. Revisa licencias y dependencias."
