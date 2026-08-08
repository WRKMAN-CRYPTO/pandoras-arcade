from pathlib import Path

p=Path('games/wip/index.html')
s=p.read_text()
s=s.replace("const lean=-0.18;","const lean=0.18;",1)
s=s.replace("x.rotate(lean);x.translate(0,bob-2);","x.rotate(lean);x.translate(2,bob-4);",1)
s=s.replace("WIP lean humanoid frame","Humanoid Gear v4 • forward charge pose",1)
p.write_text(s)
