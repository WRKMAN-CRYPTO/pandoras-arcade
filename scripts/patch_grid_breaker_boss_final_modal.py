from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
marker='/* BOSS FINAL MODAL PASS V1 */'
if marker in s:
    raise SystemExit(0)
css_old=".choice{width:100%;min-height:78px;display:flex;align-items:center;justify-content:center;text-align:center;margin-top:8px;padding:12px 14px;border:2px solid #6a523e;background:linear-gradient(#403027,#2b2019);color:#fff4da;font:1000 21px/1.2 ui-monospace,monospace;letter-spacing:.01em;box-shadow:inset 0 0 0 2px #1b130f,inset 0 -4px 0 #221813,0 3px 0 #0d0908}.choice b,.choice span{display:inline;font:inherit;color:inherit;margin:0}"
css_new=css_old+".modal.bossfinish .card{padding:12px}.modal.bossfinish .card h2{font-size:20px;margin-bottom:7px}.modal.bossfinish #ms{font-size:13px;line-height:1.35;text-align:center;font-weight:900;color:#4b301f;margin:2px 4px 8px}.modal.bossfinish .choice{min-height:58px;margin-top:7px;padding:8px 12px;font-size:24px}.modal.bossfinish .bigbtn{margin-top:8px;padding:11px;font-size:14px}"
if css_old not in s:
    raise SystemExit('choice css target not found')
s=s.replace(css_old,css_new,1)
show_old="function showChoices(title,sub,choices){document.getElementById('mt').textContent=title;document.getElementById('ms').textContent=sub;let l=document.getElementById('ml');l.innerHTML='';choices.forEach(c=>{let b=document.createElement('button');b.className='choice';b.textContent=c.desc+' = '+c.label;b.onclick=()=>{document.getElementById('modal').classList.remove('on');c.fn()};l.appendChild(b)});document.getElementById('modal').classList.add('on')}"
show_new="function showChoices(title,sub,choices){let m=document.getElementById('modal'),bossFinish=title==='FINISH THE BOSS';document.getElementById('mt').textContent=title;document.getElementById('ms').textContent=sub;m.classList.toggle('bossfinish',bossFinish);let l=document.getElementById('ml');l.innerHTML='';choices.forEach(c=>{let b=document.createElement('button');b.className='choice';b.textContent=bossFinish?c.label:(c.desc+' = '+c.label);b.onclick=()=>{m.classList.remove('on','bossfinish');c.fn()};l.appendChild(b)});m.classList.add('on')}"
if show_old not in s:
    raise SystemExit('showChoices target not found')
s=s.replace(show_old,show_new,1)
combine_old="showChoices(S.boss?'FINISH THE BOSS':'COMBINE THE GRID',expr+' = ?',arr)}"
combine_new="showChoices(S.boss?'FINISH THE BOSS':'COMBINE THE GRID',(S.boss?vals.join(' + '):expr)+' = ?',arr)}"
if combine_old not in s:
    raise SystemExit('combine target not found')
s=s.replace(combine_old,combine_new,1)
close_old="document.getElementById('close').onclick=()=>document.getElementById('modal').classList.remove('on');"
close_new="document.getElementById('close').onclick=()=>document.getElementById('modal').classList.remove('on','bossfinish');"
if close_old not in s:
    raise SystemExit('close target not found')
s=s.replace(close_old,close_new,1)
s=s.replace('</style>',marker+'\n</style>',1)
p.write_text(s)
