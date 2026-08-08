from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
for marker in ('function shuffled(a){','const ENEMY_NAMES='):
    while s.count(marker)>1:
        a=s.index(marker)
        b=s.index(marker,a+1)
        s=s[:a]+s[b:]
p.write_text(s)
