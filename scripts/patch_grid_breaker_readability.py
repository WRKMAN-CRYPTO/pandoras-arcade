from pathlib import Path
p=Path('games/wip/index.html')
s=p.read_text()
marker='/* READABILITY PASS V1 */'
if marker in s:
    raise SystemExit(0)
repls={
"#hint{position:absolute;left:8px;right:8px;bottom:8px;text-align:center;font-size:9px;":"#hint{position:absolute;left:8px;right:8px;bottom:8px;text-align:center;font-size:11px;line-height:1.35;",
".term{min-height:68px;border:2px solid #735840;background:linear-gradient(#403027,#2a1f19);color:var(--ink);font:900 11px ui-monospace,monospace;padding:8px;text-align:left;":".term{min-height:72px;border:2px solid #735840;background:linear-gradient(#403027,#2a1f19);color:var(--ink);font:900 13px ui-monospace,monospace;padding:10px;text-align:left;",
".term small{display:block;color:var(--muted);font-size:8px;margin-top:4px}.term strong{font-size:16px;color:#fff1cf}":".term small{display:block;color:#ddc9aa;font-size:11px;line-height:1.3;margin-top:6px}.term strong{font-size:19px;color:#fff1cf}",
".card h1,.card h2{margin:0 0 8px;color:#4b301f}.small{font-size:10px;color:#563d2d;line-height:1.55}":".card h1,.card h2{margin:0 0 10px;color:#4b301f}.card h2{font-size:22px;line-height:1.1}.small{font-size:12px;color:#4e3527;line-height:1.5}",
".bigbtn{width:100%;margin-top:10px;padding:12px;border:2px solid #6d553a;background:linear-gradient(#8a6b46,#61472f);color:#fff4da;font:1000 10px ui-monospace,monospace;":".bigbtn{width:100%;margin-top:10px;padding:14px;border:2px solid #6d553a;background:linear-gradient(#8a6b46,#61472f);color:#fff4da;font:1000 13px ui-monospace,monospace;",
".choice{width:100%;text-align:left;margin-top:7px;padding:10px;border:2px solid #6a523e;background:linear-gradient(#403027,#2b2019);color:#fff4da;font:900 10px ui-monospace,monospace;":".choice{width:100%;min-height:70px;text-align:left;margin-top:8px;padding:13px 16px;border:2px solid #6a523e;background:linear-gradient(#403027,#2b2019);color:#fff4da;font:900 16px ui-monospace,monospace;",
".choice span{display:block;color:#ceb999;font-size:9px;margin-top:4px}":".choice b{display:block;font-size:18px;line-height:1.1}.choice span{display:block;color:#e2cba7;font-size:13px;line-height:1.3;margin-top:6px}",
"#bossTag{display:none;position:absolute;z-index:3;left:50%;top:36px;transform:translateX(-50%);padding:3px 7px;background:#2a160f;border:2px solid #aa8241;color:#ffd98b;font-size:8px;":"#bossTag{display:none;position:absolute;z-index:3;left:50%;top:36px;transform:translateX(-50%);padding:4px 8px;background:#2a160f;border:2px solid #aa8241;color:#ffe4a8;font-size:10px;",
"#app.boss #board .term{min-height:62px;padding:7px;text-align:center}#app.boss #board .term strong{font-size:13px}#app.boss #board .term small{font-size:7px;line-height:1.25}":"#app.boss #board .term{min-height:70px;padding:9px 6px;text-align:center}#app.boss #board .term strong{font-size:16px}#app.boss #board .term small{font-size:10px;line-height:1.25}",
"x.textAlign='center';x.font='900 9px monospace';x.fillStyle=pal[3];x.fillText(S.boss?'ARCHON OF HUNDREDS':ENEMY_NAMES[kind],cx,cy-(S.boss?58:49));\n x.font='900 11px monospace';":"x.textAlign='center';x.font='900 '+(S.boss?'12':'11')+'px monospace';x.fillStyle=pal[3];x.fillText(S.boss?'ARCHON OF HUNDREDS':ENEMY_NAMES[kind],cx,cy-(S.boss?58:49));\n x.font='900 '+(S.boss?'14':'13')+'px monospace';",
"x.fillStyle=charged?'#fff0cc':'#c6ad88';x.font='900 '+(S.boss?'8':'9')+'px monospace';x.textAlign='center';x.fillText(S.parts[i][0]+'×'+S.parts[i][1],r.x+r.w/2,r.y+r.h/2-3);x.fillText(charged?String(S.parts[i][0]*S.parts[i][1]):'?',r.x+r.w/2,r.y+r.h/2+10)":"x.fillStyle=charged?'#fff7df':'#ead7b7';x.font='900 '+(S.boss?'11':'12')+'px monospace';x.textAlign='center';x.fillText(S.parts[i][0]+'×'+S.parts[i][1],r.x+r.w/2,r.y+r.h/2-5);x.font='900 '+(S.boss?'13':'14')+'px monospace';x.fillText(charged?String(S.parts[i][0]*S.parts[i][1]):'?',r.x+r.w/2,r.y+r.h/2+12)",
"x.fillStyle=S.boss?'#f4d59b':'#cfe8ff';x.font='900 9px monospace';":"x.fillStyle=S.boss?'#ffe2a6':'#e9f5ff';x.font='900 '+(S.boss?'11':'12')+'px monospace';"
}
for old,new in repls.items():
    if old not in s:
        raise SystemExit('missing target: '+old[:80])
    s=s.replace(old,new,1)
s=s.replace('</style>',marker+'\n</style>',1)
p.write_text(s)
