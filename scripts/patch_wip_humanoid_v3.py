from pathlib import Path

p=Path('games/wip/index.html')
s=p.read_text()
start=s.index(" x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;")
end=s.index(" x.restore();\n player.inv=Math.max(0,player.inv-1/60);", start)
new=""" x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;
 const mechPrimary=S.mode==='skirmish'?'#9fb4d2':'#c0a47a';
 const mechSecondary=S.mode==='skirmish'?'#546985':'#6b5438';
 const mechAccent=S.mode==='skirmish'?'#7fd7ff':'#ffb06a';
 const mechTrim=S.mode==='skirmish'?'#e8f1fb':'#f0dfbf';
 const lean=-0.18;
 const bob=Math.sin(performance.now()*0.008)*1.4;
 x.rotate(lean);x.translate(0,bob-2);
 x.globalAlpha*=0.48;x.fillStyle='#05070d';x.beginPath();x.ellipse(0,28,14,4,0,0,Math.PI*2);x.fill();x.globalAlpha/=0.48;
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-13,-20);x.lineTo(-8,-33);x.lineTo(-4,-17);x.closePath();x.fill();x.beginPath();x.moveTo(13,-20);x.lineTo(8,-33);x.lineTo(4,-17);x.closePath();x.fill();
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(-7,4);x.lineTo(-1,4);x.lineTo(0,16);x.lineTo(-5,17);x.lineTo(-9,11);x.closePath();x.fill();x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-5,17);x.lineTo(0,16);x.lineTo(2,31);x.lineTo(-4,33);x.lineTo(-8,23);x.closePath();x.fill();x.fillStyle=mechTrim;x.fillRect(-4,31,7,3);x.fillStyle=mechAccent;x.fillRect(-3,25,4,5);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(2,3);x.lineTo(8,4);x.lineTo(9,15);x.lineTo(5,16);x.lineTo(1,10);x.closePath();x.fill();x.fillStyle=mechSecondary;x.beginPath();x.moveTo(5,16);x.lineTo(9,15);x.lineTo(10,28);x.lineTo(5,29);x.lineTo(2,22);x.closePath();x.fill();x.fillStyle=mechTrim;x.fillRect(5,28,6,3);x.fillStyle=mechAccent;x.fillRect(6,23,4,4);
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-7,-2);x.lineTo(7,-2);x.lineTo(5,5);x.lineTo(-5,5);x.closePath();x.fill();x.fillStyle=mechTrim;x.fillRect(-3,0,6,2);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(0,-31);x.lineTo(10,-24);x.lineTo(11,-14);x.lineTo(8,-4);x.lineTo(4,2);x.lineTo(-4,2);x.lineTo(-8,-4);x.lineTo(-11,-14);x.lineTo(-10,-24);x.closePath();x.fill();x.fillStyle=mechTrim;x.beginPath();x.moveTo(-7,-20);x.lineTo(7,-20);x.lineTo(4,-9);x.lineTo(-4,-9);x.closePath();x.fill();x.fillStyle=mechAccent;x.fillRect(-3,-18,6,10);x.fillRect(-7,-8,4,3);x.fillRect(3,-8,4,3);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(-18,-22);x.lineTo(-9,-22);x.lineTo(-10,-14);x.lineTo(-19,-12);x.closePath();x.fill();x.beginPath();x.moveTo(18,-22);x.lineTo(9,-22);x.lineTo(10,-14);x.lineTo(19,-12);x.closePath();x.fill();
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-16,-13);x.lineTo(-11,-13);x.lineTo(-12,0);x.lineTo(-17,2);x.closePath();x.fill();x.beginPath();x.moveTo(-12,0);x.lineTo(-17,2);x.lineTo(-18,15);x.lineTo(-13,14);x.closePath();x.fill();x.fillStyle=mechTrim;x.fillRect(-18,14,5,4);
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(11,-13);x.lineTo(16,-13);x.lineTo(17,0);x.lineTo(12,1);x.closePath();x.fill();x.beginPath();x.moveTo(12,1);x.lineTo(17,0);x.lineTo(18,14);x.lineTo(13,15);x.closePath();x.fill();
 if(S.mode==='gear'){x.fillStyle=mechPrimary;x.beginPath();x.moveTo(16,-3);x.lineTo(29,-3);x.lineTo(31,5);x.lineTo(17,6);x.closePath();x.fill();x.fillStyle=mechAccent;x.fillRect(27,0,7,4);x.fillStyle='rgba(255,176,106,.45)';x.fillRect(-2,13,4,11)}else{x.fillStyle=mechAccent;x.fillRect(-17,18,3,5);x.fillRect(14,18,3,5);x.strokeStyle='rgba(127,215,255,.7)';x.lineWidth=1.4;x.beginPath();x.moveTo(-15,-18);x.lineTo(-21,-8);x.moveTo(15,-18);x.lineTo(21,-8);x.stroke()}
 x.fillStyle=mechSecondary;x.fillRect(-2,-31,4,4);x.fillStyle=mechPrimary;x.beginPath();x.moveTo(-5,-40);x.lineTo(5,-40);x.lineTo(6,-32);x.lineTo(0,-28);x.lineTo(-6,-32);x.closePath();x.fill();x.fillStyle=mechTrim;x.fillRect(-3,-42,6,4);x.fillStyle=mechAccent;x.fillRect(-4,-35,8,3);x.fillStyle=mechTrim;x.fillRect(-1,-46,2,4);x.fillRect(-8,-39,4,2);x.fillRect(4,-39,4,2);
 x.fillStyle=mechTrim;x.fillRect(-6,13,4,3);x.fillRect(5,12,4,3);x.fillRect(-16,1,4,3);x.fillRect(13,1,4,3);
 x.restore();
"""
s=s[:start]+new+s[end+len(" x.restore();\n"):]
s=s.replace('WIP humanoid frame','Humanoid Gear v3 • WIP')
p.write_text(s)
