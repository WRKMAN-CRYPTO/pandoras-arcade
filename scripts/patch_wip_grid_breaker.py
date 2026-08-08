from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace('data-title="WIP // VEIL//GEAR"','data-title="WIP // GRID//BREAKER"',1)
s=s.replace('WIP//<br>VEIL GEAR','WIP//<br>GRID BREAKER',1)
s=s.replace('<div class="symbol">⚙</div><small>HUMANOID FRAME • RESONANCE DRIVE</small>','<div class="symbol">✕</div><small>DECOMPOSE • CHARGE • COMBINE</small>',1)
p.write_text(s)
