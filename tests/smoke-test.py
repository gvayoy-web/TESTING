#!/usr/bin/env python3
"""Simple no-network packaging and SVG tests for Diseñador v3."""
from pathlib import Path
import subprocess, tempfile, sys, json, yaml
root=Path(__file__).resolve().parents[1]
for path in root.glob('skills/*/SKILL.md'):
    t=path.read_text(encoding='utf-8')
    assert t.startswith('---\n')
    fm=yaml.safe_load(t.split('---',2)[1])
    assert fm['name']==path.parent.name and fm['description']
assert len(list(root.glob('skills/*/SKILL.md')))==76
x=json.loads((root/'plugin.json').read_text())
assert x['name']=='disenador' and x['version']=='3.0.0'
check=str(root/'scripts/svg-preflight.py')
assert subprocess.run([sys.executable,check,str(root/'examples/brand-board.example.svg')],capture_output=True).returncode==0
with tempfile.TemporaryDirectory() as folder:
    bad=Path(folder)/'bad.svg'
    bad.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4 4"><script>alert(1)</script></svg>')
    assert subprocess.run([sys.executable,check,str(bad)],capture_output=True).returncode!=0
    good=Path(folder)/'generated.svg'
    ret=subprocess.run([sys.executable,str(root/'scripts/brand-board.py'),str(root/'examples/brand-brief.example.json'),'-o',str(good)],capture_output=True,text=True)
    assert ret.returncode==0,ret.stderr
    assert subprocess.run([sys.executable,check,str(good)],capture_output=True).returncode==0
print('Diseñador v3 smoke-tests passed: manifest, 76 skill headers, generated SVG, malicious SVG rejection.')
