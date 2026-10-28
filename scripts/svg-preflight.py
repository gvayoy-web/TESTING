#!/usr/bin/env python3
"""SVG safety/structure check: not a substitute for human render QA."""
import argparse, json, re, sys, xml.etree.ElementTree as ET
from pathlib import Path

def scan(path):
  result={'file':str(path),'errors':[],'warnings':[],'dimensions':{}}
  b=Path(path).read_bytes()
  if len(b)>10*1024*1024: result['warnings'].append('SVG exceeds 10 MiB.')
  if re.search(br'<!DOCTYPE|<!ENTITY',b,re.I): result['errors'].append('DOCTYPE/entity declaration is forbidden in this workflow.')
  try:root=ET.fromstring(b)
  except ET.ParseError as e:result['errors'].append('XML parse error: '+str(e));return result
  if root.tag.split('}')[-1]!='svg':result['errors'].append('Root element must be SVG.')
  vb=root.get('viewBox')
  if not vb:result['errors'].append('Missing viewBox; may not scale correctly.')
  else:
    try:
      n=[float(x) for x in re.split(r'[\s,]+',vb.strip())]
      if len(n)!=4 or n[2]<=0 or n[3]<=0:raise ValueError
      result['dimensions']['viewBox']=n
    except ValueError:result['errors'].append('Invalid viewBox.')
  for a in ('width','height'):
    if root.get(a):result['dimensions'][a]=root.get(a)
    else:result['warnings'].append('No explicit '+a+'; SVG can still be valid but output sizing may vary.')
  ids=set()
  for el in root.iter():
    tag=el.tag.split('}')[-1].lower()
    if tag in ('script','foreignobject'):
      result['errors'].append('Unsafe/unsupported element: '+tag)
    id=el.get('id')
    if id in ids:result['errors'].append('Duplicate SVG id: '+id)
    if id:ids.add(id)
    for k,v in el.attrib.items():
      name=k.split('}')[-1].lower();value=v.strip()
      if name.startswith('on') and len(name)>2:
        result['errors'].append('Inline event handler: '+name)
      if name in ('href','src') and (re.match(r'^(?:https?:|javascript:|data:|file:|//)',value,re.I)):
        result['errors'].append('External/embedded resource: '+name)
      if 'url(' in value.lower() and re.search(r'url\(\s*[\"\']?(?:https?:|data:|file:|//)',value,re.I):
        result['errors'].append('Potential remote resource in CSS attribute.')
  if '<style' in b.decode('utf-8','replace').lower():result['warnings'].append('CSS style elements need manual review for external @import and CSS URLs.')
  return result

def main():
  p=argparse.ArgumentParser();p.add_argument('svg',nargs='+');a=p.parse_args()
  results=[scan(x) for x in a.svg]
  print(json.dumps(results,ensure_ascii=False,indent=2))
  sys.exit(1 if any(r['errors'] for r in results) else 0)
if __name__=='__main__':main()
