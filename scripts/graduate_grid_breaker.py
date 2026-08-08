from pathlib import Path

root=Path('index.html')
wip=Path('games/wip/index.html')
perm=Path('games/grid-breaker/index.html')

html=root.read_text()
game=wip.read_text()
perm.parent.mkdir(parents=True, exist_ok=True)
perm.write_text(game)

# Dedicated cabinet palette.
if '.c6{' not in html:
    html=html.replace('.c5{--m1:#786d49;--m2:#1b2435;--g:#e7c56c;--sg:rgba(127,215,255,.24);--stick:#7fd7ff;--btn:#d99a62}',
        '.c5{--m1:#786d49;--m2:#1b2435;--g:#e7c56c;--sg:rgba(127,215,255,.24);--stick:#7fd7ff;--btn:#d99a62}.c6{--m1:#7a572d;--m2:#281911;--g:#f1c46a;--sg:rgba(241,196,106,.28);--stick:#83d4ff;--btn:#d46a87}')

cab='''<button class="cabinet c6" data-game="games/grid-breaker/index.html" data-title="GRID//BREAKER"><div class="body"></div><div class="marquee">GRID//<br>BREAKER</div><div class="bezel"><div class="screen"><div class="attract"><div class="symbol">✕</div><small>SPLIT • STRIKE • COMBINE</small><div class="coin">INSERT COIN</div></div></div></div><div class="deck"><span class="stick"></span><span class="buttons"><i></i><i></i><i></i></span></div><div class="door"></div><div class="plaque">Decomposition dungeon crawler</div></button>'''
if 'data-game="games/grid-breaker/index.html"' not in html:
    start=html.index('<section class="cabinets">')
    end=html.index('</section>',start)
    html=html[:end]+cab+html[end:]

# Graduation clears the WIP slot without changing launcher behavior.
start=html.index('<section class="wipZone">')
end=html.index('</section>',start)+len('</section>')
empty='''<section class="wipZone"><div class="wipLabel">WORK IN PROGRESS</div><div class="wipHint">No active build. The next experiment will appear here.</div></section>'''
html=html[:start]+empty+html[end:]

root.write_text(html)
