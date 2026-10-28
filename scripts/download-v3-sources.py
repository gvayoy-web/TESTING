#!/usr/bin/env python3
"""Opt-in GitHub source clone, explicit single repository or category, no script execution."""
from pathlib import Path
import argparse, json, subprocess, sys
REPOS={
 'vector':['svgdotjs/svg.js','fabricjs/fabric.js','paperjs/paper.js','konvajs/konva','svg/svgo','rough-stuff/rough'],
 'type':['opentypejs/opentype.js','fontsource/fontsource','fonttools/fonttools','google/fonts'],
 'raster':['lovell/sharp','scikit-image/scikit-image','Kozea/CairoSVG'],
 'design':['penpot/penpot','excalidraw/excalidraw','tldraw/tldraw','iconify/iconify','xyflow/xyflow'],
 'creative':['processing/p5.js'],
 '3d':['blender/blender','KhronosGroupArchives/glTF-Sample-Models','KhronosGroup/glTF-Blender-IO','donmccurdy/glTF-Transform','google/model-viewer','KhronosGroup/glTF-Validator'],
 'motion':['remotion-dev/remotion','motion-canvas/motion-canvas','ManimCommunity/manim']}
p=argparse.ArgumentParser();p.add_argument('--list',action='store_true');p.add_argument('--category',choices=sorted(REPOS));p.add_argument('--repo',help='Exact owner/name from curated list');p.add_argument('--dest',default='disenador-sources');p.add_argument('--clone',action='store_true',help='Explicitly opt in to git clone (may download huge repos)');args=p.parse_args()
selected=[args.repo] if args.repo else REPOS[args.category] if args.category else sorted(set(r for v in REPOS.values() for r in v))
valid=set(r for v in REPOS.values() for r in v)
if any(x not in valid for x in selected):raise SystemExit('Repository must be from the curated list.')
if args.list or not args.clone:
 for category,rs in REPOS.items():
  print(category+': '+', '.join(rs))
 if not args.clone: print('No downloads made. Use --clone --repo owner/name or --clone --category NAME.');sys.exit(0)
dest=Path(args.dest);dest.mkdir(parents=True,exist_ok=True)
for repo in selected:
 folder=dest/repo.replace('/','__')
 if folder.exists():print('Already exists:',folder);continue
 print('Cloning',repo)
 subprocess.run(['git','clone','--depth','1',f'https://github.com/{repo}.git',str(folder)],check=True)
print('Verify license/permissions, do not run arbitrary scripts without review.')
