from pathlib import Path
p=Path('games/veil-gear/index.html')
text=p.read_text()
text=text.replace("note:'Plate halves GEAR damage until fractured by BURST.'","note:'Plate halves GEAR damage until a GEAR Drive-release fractures it.'")
text=text.replace("note:'Veil reduces SKIRMISH tagging. BURST fractures it.'","note:'Veil reduces SKIRMISH tagging. A GEAR Drive-release can fracture it.'")
text=text.replace("learn('plate','Plate halves heavy GEAR damage until BURST fractures it.')","learn('plate','Plate halves heavy GEAR damage until a GEAR Drive-release fractures it.')")
old="if(e.fract&&has('fracture'))d*=1.25;\n e.hp-=d;"
new="if(s.echo&&s.type==='g'){e.fract=Math.max(e.fract,1.8);e.adapt=null;fl('DRIVE FRACTURE',e.x,e.y-40,'#c9a2ff');learn('fracture','A GEAR Drive-release fractures defenses and clears adaptive resistance.')}\n if(e.fract&&has('fracture'))d*=1.25;\n e.hp-=d;"
if old not in text: raise SystemExit('damage hook not found')
text=text.replace(old,new)
oldgraze="if(has('graze')&&S.chain%8===0)S.hp=Math.min(S.mhp,S.hp+1);learn('graze','Grazing bullets builds Resonance without taking damage.')"
newgraze="if(has('graze')&&S.chain%8===0)S.hp=Math.min(S.mhp,S.hp+1);if(has('grazeTag')&&S.chain%3===0&&S.enemies.length){let n=S.enemies.reduce((a,e)=>Math.hypot(e.x-player.x,e.y-player.y)<Math.hypot(a.x-player.x,a.y-player.y)?e:a,S.enemies[0]);n.tag=Math.min(8,n.tag+1);fl('+TAG',n.x,n.y-30,'#7fd7ff')}learn('graze','Grazing bullets builds Resonance without taking damage.')"
if oldgraze not in text: raise SystemExit('graze relic hook not found')
text=text.replace(oldgraze,newgraze)
p.write_text(text)
