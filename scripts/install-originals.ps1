# Downloads the full upstream GitHub repositories locally (not into ChatGPT).
param([string]$Destination = (Join-Path $HOME 'disenador-originales'))
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$repos = @(
  'anthropics/skills',
  'nextlevelbuilder/ui-ux-pro-max-skill',
  'pbakaus/impeccable',
  'MengTo/Skills',
  'freshtechbro/claudedesignskills',
  'greensock/gsap-skills',
  'claudekit/frontend-design-pro-demo',
  'bergside/awesome-design-skills'
)
foreach ($repo in $repos) {
  $folder = Join-Path $Destination ($repo.Replace('/', '_'))
  if (Test-Path (Join-Path $folder '.git')) { Write-Host "Ya descargado: $repo"; continue }
  & git clone --depth 1 "https://github.com/$repo.git" $folder
  if ($LASTEXITCODE -ne 0) { throw "git clone falló para $repo" }
}
Write-Host "Fuentes originales descargadas: $Destination. Lee sus licencias antes de usarlas."
