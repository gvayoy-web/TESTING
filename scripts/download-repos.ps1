# Diseñador v2 - clona fuentes originales sin ejecutarlas
# Requiere Git y acceso a GitHub. No instala npm ni ejecuta scripts de terceros.
param([string]$Destination = (Join-Path $HOME 'disenador-v2-originales'))
$ErrorActionPreference='Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Necesitas Git instalado' }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$repos = @(
  'anthropics/skills',
  'nextlevelbuilder/ui-ux-pro-max-skill',
  'pbakaus/impeccable',
  'MengTo/Skills',
  'freshtechbro/claudedesignskills',
  'greensock/gsap-skills',
  'claudekit/frontend-design-pro-demo',
  'bergside/awesome-design-skills',
  'vercel-labs/agent-skills',
  'vercel-labs/web-interface-guidelines',
  'shadcn-ui/ui',
  'radix-ui/primitives',
  'tailwindlabs/tailwindcss',
  'DavidHDev/react-bits',
  'magicuidesign/magicui',
  'ibelick/motion-primitives',
  'darkroomengineering/lenis',
  'motiondivision/motion',
  'pmndrs/react-three-fiber',
  'pmndrs/drei',
  'pmndrs/postprocessing',
  'emilkowalski/skills',
  'Leonxlnx/taste-skill',
  'CloudAI-X/threejs-skills',
  'wshobson/agents',
  'coreyhaines31/marketingskills',
  'microsoft/playwright',
  'dequelabs/axe-core',
  'GoogleChrome/lighthouse',
  'lucide-icons/lucide'
)
foreach ($repo in $repos) {
  $target=Join-Path $Destination ($repo.Replace('/','__'))
  if (Test-Path $target) { Write-Host "SKIP existente: $repo"; continue }
  & git clone --depth 1 --filter=blob:none "https://github.com/$repo.git" $target
  if ($LASTEXITCODE -ne 0) { Write-Warning "Falló descarga: $repo" }
}
Write-Host "Fuentes descargadas en: $Destination"
Write-Host "REVISAR LICENCIAS antes de copiar o redistribuir; este script no ejecuta código ajeno."
