#!/usr/bin/env python3
"""Offline, no-dependency editable SVG brand sample generator. Uses safe XML escaping."""
import argparse, json, re, math
from pathlib import Path
from xml.sax.saxutils import escape

def color(s):
    if not re.fullmatch(r'#[0-9A-Fa-f]{6}',s): raise ValueError(f'invalid color: {s}')
    return s.upper()
def lum(s):
    a=[int(s[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in a]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def contrast(a,b):
    a,b=sorted((lum(a),lum(b)),reverse=True)
    return (a+.05)/(b+.05)
def txt(s):return escape(str(s), {'"':'&quot;', "'":'&apos;'})
def main():
    p=argparse.ArgumentParser();p.add_argument('config');p.add_argument('-o','--output',required=True);a=p.parse_args()
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    brand=str(cfg.get('brand','MARCA'))[:60]; tag=str(cfg.get('tagline',''))[:100]
    mono=str(cfg.get('monogram','')).strip()[:3] or ''.join(s[0] for s in brand.split()[:2]).upper()
    cols={k:color(v) for k,v in cfg.get('colors',{}).items()}
    ink=cols.get('ink','#17212C'); bg=cols.get('background','#FAF7F1'); accent=cols.get('accent','#F07D59'); secondary=cols.get('secondary','#86B7AC')
    text_color=ink if contrast(ink,bg)>=contrast('#FFFFFF',bg) else '#FFFFFF'
    swatches=list(cols.items())[:6] or [('ink',ink),('background',bg),('accent',accent),('secondary',secondary)]
    chunks=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc"><title id="title">Brand board: {txt(brand)}</title><desc id="desc">Editable vector board showing a simple monogram, type hierarchy and selected colors.</desc>',
        f'<rect width="1200" height="800" fill="{bg}"/>',f'<rect x="55" y="55" width="1090" height="690" rx="12" fill="none" stroke="{ink}" opacity="0.16"/>',
        f'<rect x="90" y="90" width="235" height="235" rx="56" fill="{accent}"/>',
        f'<text x="207" y="245" font-family="Arial,sans-serif" font-size="100" font-weight="bold" text-anchor="middle" fill="{ink}">{txt(mono)}</text>',
        f'<text x="365" y="182" font-family="Arial,sans-serif" font-size="68" font-weight="bold" fill="{ink}">{txt(brand)}</text>',
        f'<text x="368" y="228" font-family="Arial,sans-serif" font-size="26" fill="{ink}">{txt(tag)}</text>',
        f'<line x1="90" y1="375" x2="1110" y2="375" stroke="{ink}" opacity="0.25"/>',
        f'<text x="90" y="421" font-family="Arial,sans-serif" font-size="21" font-weight="bold" fill="{ink}">PALETA / COLOR SYSTEM</text>'
    ]
    for idx,(name,col) in enumerate(swatches):
        x=90+idx*174
        chunks.append(f'<rect x="{x}" y="453" width="152" height="138" rx="9" fill="{col}" stroke="{ink}" stroke-opacity="0.2"/>')
        chunks.append(f'<text x="{x}" y="625" font-family="Arial,sans-serif" font-size="19" font-weight="bold" fill="{ink}">{txt(name[:14])}</text>')
        chunks.append(f'<text x="{x}" y="653" font-family="monospace" font-size="16" fill="{ink}">{col}</text>')
    chunks.append(f'<text x="90" y="718" font-family="Arial,sans-serif" font-size="18" fill="{ink}">Editable SVG study — refine geometry and type before commercial approval.</text>')
    chunks.append('</svg>')
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text('\n'.join(chunks)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(Path(a.output).resolve()),'contrast_ink_bg':round(contrast(ink,bg),2),'swatches':len(swatches)},ensure_ascii=False))
if __name__=='__main__':main()
