#!/usr/bin/env node
// Diseñador v2 — heuristic static UI scan; NEVER claim WCAG or QA conformance based on this.
import fs from 'node:fs';
import path from 'node:path';
const root=path.resolve(process.argv[2] || process.cwd());
const ignored=new Set(['node_modules','.git','.next','dist','build','coverage','.turbo','.vercel','.output','vendor']);
const allowed=/\.(html|jsx|tsx|css|scss|vue|svelte)$/i;
const files=[];
function walk(dir,depth=0){if(depth>12||files.length>2500)return;for(const entry of fs.readdirSync(dir,{withFileTypes:true})){if(ignored.has(entry.name)||entry.name.startsWith('.'))continue;const f=path.join(dir,entry.name);if(entry.isDirectory())walk(f,depth+1);else if(allowed.test(entry.name)){files.push(f);}}}
walk(root);
const issues=[];
const report=(file,code,detail)=>issues.push({file:path.relative(root,file),code,detail});
let styles=0,hasReducedMotion=false,hasViewport=false;
for(const file of files){
 const src=fs.readFileSync(file,'utf8');
 if(/@media\s*\(prefers-reduced-motion\s*:\s*reduce\s*\)/.test(src))hasReducedMotion=true;
 if(/<meta\s+[^>]*name=['"]viewport['"]/.test(src))hasViewport=true;
 if(/\.(?:css|scss)$/i.test(file)){styles++;if(/scroll-behavior\s*:\s*smooth/.test(src))report(file,'CHECK_SCROLL','CSS smooth scrolling: comprobar reduced motion y compatibilidad');}
 if(/<img\b(?![^>]*\balt\s*=)[^>]*>/gims.test(src))report(file,'IMG_ALT','Posibles <img> sin alt; revisar manualmente');
 if(/target\s*=\s*['"]_blank['"]/.test(src)&&!/rel\s*=\s*['"][^'"]*noopener/.test(src))report(file,'CHECK_EXTERNAL_LINK','Comprobar rel/noopener en enlaces externos');
 if(/outline\s*:\s*(?:none|0\s*;)/.test(src))report(file,'FOCUS','outline desactivado: confirmar alternativa :focus-visible');
 if(/dangerouslySetInnerHTML/.test(src))report(file,'RISK_HTML','HTML inyectado: verificar sanitización');
 if(/<canvas\b/.test(src)&&!/(aria-label|role=['"]img|fallback|noscript)/i.test(src))report(file,'CANVAS_FALLBACK','Revisar semántica y fallback de canvas');
}
if(styles&&!hasReducedMotion)issues.push({file:'(proyecto)',code:'REDUCED_MOTION',detail:'No se encontró media query de reduced motion; comprobar archivos fuera del alcance del escáner'});
if(files.some(f=>/\.html$/.test(f))&&!hasViewport)issues.push({file:'(proyecto)',code:'VIEWPORT',detail:'No se detectó viewport meta; revisar plantillas HTML'});
console.log(JSON.stringify({tool:'disenador-v2/audit-ui',root,files:files.length,heuristicOnly:true,notAFullAudit:true,issues},null,2));
// Exit 0: these are heuristic warnings, not independently verified failures.
