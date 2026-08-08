from pathlib import Path
p=Path('games/wip/index.html')
text=p.read_text()
old=""" x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;
 const mechPrimary=S.mode==='skirmish'?'#93a8c4':'#b79a72';
 const mechSecondary=S.mode==='skirmish'?'#5f7397':'#6e573d';
 const mechAccent=S.mode==='skirmish'?'#7fd7ff':'#ffb06a';
 const mechTrim=S.mode==='skirmish'?'#dce8f7':'#ead7b5';
 const bob=Math.sin(performance.now()*0.008)*1.5;x.translate(0,bob);
 x.globalAlpha*=0.55;x.fillStyle='#05070d';x.beginPath();x.ellipse(0,20,18,6,0,0,Math.PI*2);x.fill();x.globalAlpha/=0.55;
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-20,-10);x.lineTo(-10,-18);x.lineTo(-8,-2);x.closePath();x.fill();x.beginPath();x.moveTo(20,-10);x.lineTo(10,-18);x.lineTo(8,-2);x.closePath();x.fill();
 x.fillStyle=mechSecondary;x.fillRect(-12,6,8,14);x.fillRect(4,6,8,14);x.fillStyle=mechAccent;x.fillRect(-11,18,6,4);x.fillRect(5,18,6,4);
 x.fillStyle=mechPrimary;x.fillRect(-10,-1,7,10);x.fillRect(3,-1,7,10);x.fillStyle=mechSecondary;x.fillRect(-7,-4,14,6);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(0,-24);x.lineTo(14,-14);x.lineTo(11,4);x.lineTo(0,10);x.lineTo(-11,4);x.lineTo(-14,-14);x.closePath();x.fill();
 x.fillStyle=mechTrim;x.fillRect(-10,-14,20,7);x.fillStyle=mechAccent;x.fillRect(-3,-12,6,10);x.fillRect(-8,-4,5,4);x.fillRect(3,-4,5,4);
 x.fillStyle=mechPrimary;x.fillRect(-18,-16,8,8);x.fillRect(10,-16,8,8);x.fillStyle=mechSecondary;x.fillRect(-18,-9,6,16);x.fillRect(12,-9,6,16);
 if(S.mode==='gear'){x.fillStyle=mechPrimary;x.fillRect(14,-4,11,8);x.fillStyle=mechAccent;x.fillRect(22,-2,6,4)}else{x.fillStyle=mechAccent;x.fillRect(-17,5,4,6);x.fillRect(13,5,4,6)}
 x.fillStyle=mechPrimary;x.fillRect(-6,-28,12,8);x.fillStyle=mechTrim;x.fillRect(-4,-30,8,4);x.fillStyle=mechAccent;x.fillRect(-4,-25,8,3);
 x.fillStyle=mechTrim;x.fillRect(-11,9,6,4);x.fillRect(5,9,6,4);
 if(S.mode==='skirmish'){x.strokeStyle='rgba(127,215,255,.65)';x.lineWidth=1.5;x.beginPath();x.moveTo(-15,-12);x.lineTo(-22,-3);x.moveTo(15,-12);x.lineTo(22,-3);x.stroke()}else{x.fillStyle='rgba(255,176,106,.55)';x.fillRect(-3,12,6,7);x.fillRect(-1,-20,2,5)}
 x.restore();"""
new=""" x.save();x.translate(player.x,player.y);if(player.inv>0&&Math.floor(player.inv*20)%2===0)x.globalAlpha=.35;
 const mechPrimary=S.mode==='skirmish'?'#93a8c4':'#b79a72';
 const mechSecondary=S.mode==='skirmish'?'#5f7397':'#6e573d';
 const mechAccent=S.mode==='skirmish'?'#7fd7ff':'#ffb06a';
 const mechTrim=S.mode==='skirmish'?'#dce8f7':'#ead7b5';
 const bob=Math.sin(performance.now()*0.008)*1.5;x.translate(0,bob-2);
 x.globalAlpha*=0.52;x.fillStyle='#05070d';x.beginPath();x.ellipse(0,24,16,5,0,0,Math.PI*2);x.fill();x.globalAlpha/=0.52;
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-18,-12);x.lineTo(-9,-22);x.lineTo(-7,-7);x.closePath();x.fill();x.beginPath();x.moveTo(18,-12);x.lineTo(9,-22);x.lineTo(7,-7);x.closePath();x.fill();
 x.fillStyle=mechSecondary;x.beginPath();x.moveTo(-10,8);x.lineTo(-4,8);x.lineTo(-2,25);x.lineTo(-10,25);x.closePath();x.fill();x.beginPath();x.moveTo(4,8);x.lineTo(10,8);x.lineTo(10,25);x.lineTo(2,25);x.closePath();x.fill();
 x.fillStyle=mechTrim;x.fillRect(-10,24,9,3);x.fillRect(1,24,9,3);x.fillStyle=mechAccent;x.fillRect(-8,18,5,5);x.fillRect(3,18,5,5);
 x.fillStyle=mechPrimary;x.fillRect(-9,0,6,11);x.fillRect(3,0,6,11);x.fillStyle=mechSecondary;x.fillRect(-6,-3,12,6);x.fillRect(-3,-1,6,4);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(0,-31);x.lineTo(12,-20);x.lineTo(8,2);x.lineTo(0,11);x.lineTo(-8,2);x.lineTo(-12,-20);x.closePath();x.fill();
 x.fillStyle=mechTrim;x.fillRect(-8,-19,16,7);x.fillStyle=mechAccent;x.fillRect(-3,-16,6,11);x.fillRect(-7,-6,4,3);x.fillRect(3,-6,4,3);
 x.fillStyle=mechPrimary;x.beginPath();x.moveTo(-18,-18);x.lineTo(-8,-18);x.lineTo(-10,-10);x.lineTo(-19,-8);x.closePath();x.fill();x.beginPath();x.moveTo(18,-18);x.lineTo(8,-18);x.lineTo(10,-10);x.lineTo(19,-8);x.closePath();x.fill();
 x.fillStyle=mechSecondary;x.fillRect(-17,-9,5,20);x.fillRect(12,-9,5,20);x.fillStyle=mechTrim;x.fillRect(-17,10,5,5);x.fillRect(12,10,5,5);
 if(S.mode==='gear'){x.fillStyle=mechPrimary;x.fillRect(14,-4,12,8);x.fillStyle=mechAccent;x.fillRect(24,-2,7,4);x.fillStyle='rgba(255,176,106,.55)';x.fillRect(-2,13,4,9);x.fillRect(-1,-24,2,6)}else{x.fillStyle=mechAccent;x.fillRect(-16,12,3,5);x.fillRect(13,12,3,5);x.strokeStyle='rgba(127,215,255,.65)';x.lineWidth=1.5;x.beginPath();x.moveTo(-14,-14);x.lineTo(-20,-6);x.moveTo(14,-14);x.lineTo(20,-6);x.stroke()}
 x.fillStyle=mechSecondary;x.fillRect(-2,-27,4,4);x.fillStyle=mechPrimary;x.fillRect(-5,-35,10,8);x.fillStyle=mechTrim;x.fillRect(-3,-37,6,4);x.fillStyle=mechAccent;x.fillRect(-4,-31,8,3);
 x.fillStyle=mechTrim;x.fillRect(-9,11,5,4);x.fillRect(4,11,5,4);x.fillRect(-17,0,5,3);x.fillRect(12,0,5,3);
 x.restore();"""
if old not in text:
    raise SystemExit('current WIP mech block not found')
text=text.replace(old,new)
text=text.replace('WIP humanoid frame','WIP lean humanoid frame')
p.write_text(text)
