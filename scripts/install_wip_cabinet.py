from pathlib import Path

# Build the current WIP from the stable VEIL//GEAR cabinet, then apply the humanoid mech art pass.
src = Path('games/veil-gear/index.html')
wip = Path('games/wip/index.html')
wip.parent.mkdir(parents=True, exist_ok=True)
text = src.read_text(encoding='utf-8')

old = """ x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;\n x.fillStyle=S.mode==='skirmish'?'#7998b8':'#b08b67';x.beginPath();x.moveTo(0,-18);x.lineTo(12,12);x.lineTo(0,7);x.lineTo(-12,12);x.closePath();x.fill();\n x.fillStyle=S.mode==='skirmish'?'#7fd7ff':'#ffb06a';x.fillRect(-3,-8,6,11);x.restore();"""
new = """ x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;\n const mechPrimary=S.mode==='skirmish'?'#93a8c4':'#b79a72';\n const mechSecondary=S.mode==='skirmish'?'#5f7397':'#6e573d';\n const mechAccent=S.mode==='skirmish'?'#7fd7ff':'#ffb06a';\n const mechTrim=S.mode==='skirmish'?'#dce8f7':'#ead7b5';\n const bob=Math.sin(performance.now()*0.008)*1.5;x.translate(0,bob);\n x.globalAlpha*=0.55;x.fillStyle='#05070d';x.beginPath();x.ellipse(0,20,18,6,0,0,Math.PI*2);x.fill();x.globalAlpha/=0.55;\n x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-20,-10);x.lineTo(-10,-18);x.lineTo(-8,-2);x.closePath();x.fill();x.beginPath();x.moveTo(20,-10);x.lineTo(10,-18);x.lineTo(8,-2);x.closePath();x.fill();\n x.fillStyle=mechSecondary;x.fillRect(-12,6,8,14);x.fillRect(4,6,8,14);x.fillStyle=mechAccent;x.fillRect(-11,18,6,4);x.fillRect(5,18,6,4);\n x.fillStyle=mechPrimary;x.fillRect(-10,-1,7,10);x.fillRect(3,-1,7,10);x.fillStyle=mechSecondary;x.fillRect(-7,-4,14,6);\n x.fillStyle=mechPrimary;x.beginPath();x.moveTo(0,-24);x.lineTo(14,-14);x.lineTo(11,4);x.lineTo(0,10);x.lineTo(-11,4);x.lineTo(-14,-14);x.closePath();x.fill();\n x.fillStyle=mechTrim;x.fillRect(-10,-14,20,7);x.fillStyle=mechAccent;x.fillRect(-3,-12,6,10);x.fillRect(-8,-4,5,4);x.fillRect(3,-4,5,4);\n x.fillStyle=mechPrimary;x.fillRect(-18,-16,8,8);x.fillRect(10,-16,8,8);x.fillStyle=mechSecondary;x.fillRect(-18,-9,6,16);x.fillRect(12,-9,6,16);\n if(S.mode==='gear'){x.fillStyle=mechPrimary;x.fillRect(14,-4,11,8);x.fillStyle=mechAccent;x.fillRect(22,-2,6,4)}else{x.fillStyle=mechAccent;x.fillRect(-17,5,4,6);x.fillRect(13,5,4,6)}\n x.fillStyle=mechPrimary;x.fillRect(-6,-28,12,8);x.fillStyle=mechTrim;x.fillRect(-4,-30,8,4);x.fillStyle=mechAccent;x.fillRect(-4,-25,8,3);\n x.fillStyle=mechTrim;x.fillRect(-11,9,6,4);x.fillRect(5,9,6,4);\n if(S.mode==='skirmish'){x.strokeStyle='rgba(127,215,255,.65)';x.lineWidth=1.5;x.beginPath();x.moveTo(-15,-12);x.lineTo(-22,-3);x.moveTo(15,-12);x.lineTo(22,-3);x.stroke()}else{x.fillStyle='rgba(255,176,106,.55)';x.fillRect(-3,12,6,7);x.fillRect(-1,-20,2,5)}\n x.restore();"""
if old not in text:
    raise SystemExit('player art block not found')
text = text.replace(old, new)
text = text.replace('Drag to steer • Frame leads your fingertip • Autoguns fire','Drag to steer • Frame leads your fingertip • WIP humanoid frame')
text = text.replace('<title>VEIL//GEAR</title>', '<title>VEIL//GEAR — WIP</title>')
wip.write_text(text, encoding='utf-8')

# Patch the arcade launcher with an always-on-top WIP cabinet.
p = Path('index.html')
arcade = p.read_text(encoding='utf-8')

css_anchor = ".c5{--m1:#786d49;--m2:#1b2435;--g:#e7c56c;--sg:rgba(127,215,255,.24);--stick:#7fd7ff;--btn:#d99a62}"
wip_css = css_anchor + ".wipZone{position:relative;z-index:3;max-width:820px;margin:12px auto 0;padding:0 16px 6px;text-align:center}.wipLabel{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#ffd86b;margin:0 0 7px;text-shadow:0 0 10px #ffd86b55}.wipHint{font-size:9px;color:#9c90a7;margin:-2px 0 9px}.wipCab{display:block;width:min(100%,360px);margin:0 auto;min-height:376px}.wipCab .body{background:repeating-linear-gradient(135deg,rgba(255,216,107,.075) 0 12px,transparent 12px 24px),linear-gradient(90deg,#171318,#3b3020 48%,#100e11);border-color:#ffd86b2b}.wipCab:before{content:'CURRENT BUILD';position:absolute;z-index:5;left:50%;top:72px;transform:translateX(-50%);padding:3px 8px;border-radius:999px;background:#ffd86b;color:#241b08;font-size:8px;font-weight:1000;letter-spacing:.12em;box-shadow:0 0 12px #ffd86b66}.wipCab .marquee{height:82px}.wipCab .bezel{top:98px;height:164px}.wipCab .deck{top:273px}.wipCab .door{top:340px}.wipCab{--m1:#9a792f;--m2:#332719;--g:#ffd86b;--sg:rgba(127,215,255,.22);--stick:#7fd7ff;--btn:#ff9b63}@media(max-width:560px){.wipCab{min-height:362px}.wipCab .bezel{height:151px}.wipCab .deck{top:260px}.wipCab .door{top:325px}}"
if css_anchor not in arcade:
    raise SystemExit('c5 css anchor not found')
arcade = arcade.replace(css_anchor, wip_css, 1)

html_anchor = '<section class="cabinets">'
wip_html = '''<section class="wipZone"><div class="wipLabel">WORK IN PROGRESS</div><div class="wipHint">The active build lives here until it graduates to the main floor.</div><button class="cabinet wipCab" data-game="games/wip/index.html" data-title="WIP // VEIL//GEAR"><div class="body"></div><div class="marquee">WIP//<br>VEIL GEAR</div><div class="bezel"><div class="screen"><div class="attract"><div class="symbol">⚙</div><small>HUMANOID FRAME • RESONANCE DRIVE</small><div class="coin">PLAYTEST BUILD</div></div></div></div><div class="deck"><span class="stick"></span><span class="buttons"><i></i><i></i><i></i></span></div><div class="door"></div><div class="plaque">CURRENT WORKING GAME</div></button></section>'''
if 'data-game="games/wip/index.html"' not in arcade:
    if html_anchor not in arcade:
        raise SystemExit('cabinet section anchor not found')
    arcade = arcade.replace(html_anchor, wip_html + html_anchor, 1)

p.write_text(arcade, encoding='utf-8')
