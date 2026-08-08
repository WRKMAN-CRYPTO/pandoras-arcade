from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
marker='/* CHOICE TILE PASS V1 */'
if marker in s:
    raise SystemExit(0)
old_css=".choice{width:100%;min-height:70px;text-align:left;margin-top:8px;padding:13px 16px;border:2px solid #6a523e;background:linear-gradient(#403027,#2b2019);color:#fff4da;font:900 16px ui-monospace,monospace;box-shadow:inset 0 0 0 2px #1b130f,inset 0 -4px 0 #221813,0 3px 0 #0d0908}.choice b{display:block;font-size:18px;line-height:1.1}.choice span{display:block;color:#e2cba7;font-size:13px;line-height:1.3;margin-top:6px}"
new_css=".choice{width:100%;min-height:78px;display:flex;align-items:center;justify-content:center;text-align:center;margin-top:8px;padding:12px 14px;border:2px solid #6a523e;background:linear-gradient(#403027,#2b2019);color:#fff4da;font:1000 21px/1.2 ui-monospace,monospace;letter-spacing:.01em;box-shadow:inset 0 0 0 2px #1b130f,inset 0 -4px 0 #221813,0 3px 0 #0d0908}.choice b,.choice span{display:inline;font:inherit;color:inherit;margin:0}"
if old_css not in s:
    raise SystemExit('choice css target not found')
s=s.replace(old_css,new_css,1)
old_js="function showChoices(title,sub,choices){document.getElementById('mt').textContent=title;document.getElementById('ms').textContent=sub;let l=document.getElementById('ml');l.innerHTML='';choices.forEach(c=>{let b=document.createElement('button');b.className='choice';b.innerHTML='<b>'+c.label+'</b><span>'+c.desc+'</span>';b.onclick=()=>{document.getElementById('modal').classList.remove('on');c.fn()};l.appendChild(b)});document.getElementById('modal').classList.add('on')}"
new_js="function showChoices(title,sub,choices){document.getElementById('mt').textContent=title;document.getElementById('ms').textContent=sub;let l=document.getElementById('ml');l.innerHTML='';choices.forEach(c=>{let b=document.createElement('button');b.className='choice';b.textContent=c.desc+' = '+c.label;b.onclick=()=>{document.getElementById('modal').classList.remove('on');c.fn()};l.appendChild(b)});document.getElementById('modal').classList.add('on')}"
if old_js not in s:
    raise SystemExit('showChoices target not found')
s=s.replace(old_js,new_js,1)
s=s.replace('</style>',marker+'\n</style>',1)
p.write_text(s)
