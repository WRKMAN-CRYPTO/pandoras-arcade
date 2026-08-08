from pathlib import Path
import base64,zlib,re
parts=[Path(f'staging/vc{i}.txt').read_text().strip() for i in range(5)]
game=zlib.decompress(base64.b64decode(''.join(parts))).decode()
required=['<title>VAULT//CHOIR</title>','vaultChoirCodexV1',"S.lastTech&&S.lastTech.type!=='chorus'","const rank={ember:0,veil:1,root:2,echo:3,glass:4}"]
for marker in required:
    if marker not in game: raise SystemExit('missing game marker: '+marker)
Path('games/wip/index.html').write_text(game)
p=Path('index.html')
s=p.read_text()
zone='<section class="wipZone"><div class="wipLabel">WORK IN PROGRESS</div><div class="wipHint">One-shot build. No patches. Learn it or be learned by it.</div><button class="cabinet wipCab" data-game="games/wip/index.html" data-title="WIP // VAULT//CHOIR"><div class="body"></div><div class="marquee">WIP//<br>VAULT CHOIR</div><div class="bezel"><div class="screen"><div class="attract"><div class="symbol">◈</div><small>PAIR • READ • BREAK RULES</small><div class="coin">ONE SHOT BUILD</div></div></div></div><div class="deck"><span class="stick"></span><span class="buttons"><i></i><i></i><i></i></span></div><div class="door"></div><div class="plaque">CURRENT WORKING GAME</div></button></section>'
s2,n=re.subn(r'<section class="wipZone">.*?</section>',zone,s,count=1,flags=re.S)
if n!=1: raise SystemExit('WIP zone not found exactly once')
p.write_text(s2)
