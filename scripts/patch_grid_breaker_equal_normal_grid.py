from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
old="if(S.boss){xs=edge(weights(A),gx,gw);ys=edge(weights(B),gy,gh)}else{xs=edge(A,gx,gw);ys=edge(B,gy,gh)}"
new="if(S.boss){xs=edge(weights(A),gx,gw);ys=edge(weights(B),gy,gh)}else{xs=edge(A.map(()=>1),gx,gw);ys=edge(B.map(()=>1),gy,gh)}"
if old not in s:
    raise SystemExit('target grid geometry block not found')
s=s.replace(old,new,1)
p.write_text(s)
