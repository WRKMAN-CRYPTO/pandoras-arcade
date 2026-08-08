from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
marker='/* EQUAL BOSS GRID PASS V1 */'
if marker in s:
    raise SystemExit(0)
old="const weights=arr=>arr.map(v=>S.boss?Math.max(1,String(Math.round(v)).length):v), edge=(vals,start,size)=>{let out=[start],sum=vals.reduce((a,b)=>a+b,0),acc=0;for(const v of vals){acc+=v;out.push(start+size*(acc/sum))}return out};\n if(S.boss){xs=edge(weights(A),gx,gw);ys=edge(weights(B),gy,gh)}else{xs=edge(A.map(()=>1),gx,gw);ys=edge(B.map(()=>1),gy,gh)}"
new="const edge=(vals,start,size)=>{let out=[start],sum=vals.reduce((a,b)=>a+b,0),acc=0;for(const v of vals){acc+=v;out.push(start+size*(acc/sum))}return out};\n xs=edge(A.map(()=>1),gx,gw);ys=edge(B.map(()=>1),gy,gh)"
if old not in s:
    raise SystemExit('equal boss grid target not found')
s=s.replace(old,new,1)
s=s.replace('</style>',marker+'\n</style>',1)
p.write_text(s)
