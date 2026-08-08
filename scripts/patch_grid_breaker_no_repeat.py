from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
old="function makeProblem(){let pool=[[23,14],[32,18],[41,26],[43,25],[56,32],[67,24],[72,35],[84,16],[39,47],[58,43]];let p=pool[Math.min(pool.length-1,Math.floor((S.node-1)/2))];if(S.node>pool.length*2)p=[20+Math.floor(Math.random()*7)*10+Math.ceil(Math.random()*9),10+Math.floor(Math.random()*4)*10+Math.ceil(Math.random()*9)];S.a=p[0];S.b=p[1];let A=splitNum(S.a),B=splitNum(S.b);"
new="function makeProblem(){let pool=[[23,14],[32,18],[41,26],[43,25],[56,32],[67,24],[72,35],[84,16],[39,47],[58,43]];let p;if(S.node<=pool.length){p=pool[S.node-1]}else{let tries=0,key='';do{p=[20+Math.floor(Math.random()*7)*10+Math.ceil(Math.random()*9),10+Math.floor(Math.random()*4)*10+Math.ceil(Math.random()*9)];key=[...p].sort((a,b)=>a-b).join('x');tries++}while(key===S.prevProblemKey&&tries<40)}S.a=p[0];S.b=p[1];S.prevProblemKey=[S.a,S.b].sort((a,b)=>a-b).join('x');let A=splitNum(S.a),B=splitNum(S.b);"
if old not in s: raise SystemExit('target makeProblem block not found')
s=s.replace(old,new,1)
p.write_text(s)
