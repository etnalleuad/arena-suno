from pathlib import Path
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from html import escape
import re

ROOT = Path('/home/user')
source = ROOT / 'suno_v6_studio_dark_2026-09-11.md'
text = source.read_text()
md = MarkdownIt('commonmark', {'html': False}).enable('table')
soup = BeautifulSoup(md.render(text), 'html.parser')
soup.h1.decompose()
nav = []
block = 0
labels = {
  1: 'Тексты и вокал',
  2: 'Style и саунд-дизайн',
  3: 'Studio: дорожки, MIDI, FX',
}
for h in soup.find_all(['h2','h3']):
    if h.name == 'h2':
        block += 1
        h['id'] = f'block-{block}'
        nav.append(f'<a class="nav-block" href="#block-{block}"><span>0{block}</span>{labels[block]}</a>')
    else:
        title = h.get_text(' ', strip=True)
        match = re.match(r'(\d+)\.(\d+)\.', title)
        slug = 'section-' + '-'.join(match.groups()) if match else 'section-' + str(len(nav))
        h['id'] = slug
        nav.append(f'<a class="nav-section" href="#{slug}">{escape(title)}</a>')
bank = soup.find('h3', id='section-3-5')
if bank:
    for el in bank.find_next_siblings():
        if el.name == 'h3':
            break
        if el.name == 'h4':
            key = el.get_text(' ', strip=True).split(' — ')[0]
            if re.fullmatch(r'[A-Z_]+',key):
                el['id']='track-'+key.lower()
for i, pre in enumerate(soup.find_all('pre')):
    pre['id'] = f'code-{i}'
    wrap = soup.new_tag('div', attrs={'class':'code-wrap'})
    pre.wrap(wrap)
    btn = soup.new_tag('button', attrs={'class':'copy', 'type':'button','data-code':f'code-{i}', 'aria-label':'Копировать пример'})
    btn.string = 'Копировать'
    wrap.insert(0,btn)
for table in soup.find_all('table'):
    wrap = soup.new_tag('div', attrs={'class':'table-wrap', 'role':'region', 'tabindex':'0', 'aria-label':'Таблица — можно прокрутить по горизонтали'})
    table.wrap(wrap)
for a in soup.find_all('a', href=True):
    if a['href'].startswith('http'):
        a['target'] = '_blank'
        a['rel'] = 'noopener noreferrer'
        a['title'] = a['href']
        if a.get_text(strip=True).isdigit():
            a['class'] = ['citation']

css = '''
.jump-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:25px}.jump-links a{font-size:11px;text-decoration:none;padding:6px 10px;border:1px solid #d1c9bb;border-radius:4px;color:#75543e;background:#fffdf6}.jump-links a:hover{background:#eee4d3}
:root{--ink:#242726;--muted:#68716d;--accent:#925034;--paper:#fffefa;--page:#f3f3ed;--line:#dedfd5;--nav:#202127;--navtext:#d7ded9;--code:#edf1eb;--soft:#e8eee5}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;color:var(--ink);background:var(--page);font-size:16px;line-height:1.72}button,input{font:inherit}a{color:var(--accent);text-underline-offset:3px}button{cursor:pointer}aside{position:fixed;inset:0 auto 0 0;width:278px;background:var(--nav);color:var(--navtext);display:flex;flex-direction:column;z-index:30} .brand{padding:27px 25px 20px;border-bottom:1px solid #3b443e}.brand small{font-size:10px;letter-spacing:2px;color:#9eafa1}.brand b{display:block;font-size:33px;line-height:1.3;letter-spacing:1px;color:#fff}.brand p{margin:5px 0 0;font-size:12px;color:#bac6bd}.stamp{display:inline-block;font-size:10px;letter-spacing:.5px;margin-top:17px;padding:4px 9px;border:1px solid #526455;border-radius:4px;color:#d2e1ce}nav{padding:10px 14px 24px;overflow:auto;scrollbar-width:thin;scrollbar-color:#55635a #202824}nav a{display:block;text-decoration:none;border-radius:5px;line-height:1.5}nav a:hover,nav a:focus-visible{background:#36453a;color:white}.nav-block{font-size:13px;font-weight:700;color:#f3f6f2;padding:12px 10px 7px;margin-top:9px}.nav-block span{font-size:11px;color:#e1a47d;display:inline-block;width:27px}.nav-section{font-size:11px;color:#bac6bd;padding:6px 10px 6px 16px}.nav-section.active{background:#344439;color:#fff} .sidebar-foot{padding:15px 25px;font-size:11px;color:#92a397;border-top:1px solid #3b443e}.shell{margin-left:278px} .toolbar{position:sticky;top:0;z-index:20;background:#f3f3edf5;backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:12px 36px;display:flex;gap:8px;align-items:center}.search-group{display:flex;align-items:center;max-width:580px;width:100%;border:1px solid #c9d1c5;border-radius:6px;background:#fffefa;padding:0 12px}.search-group svg{width:17px;height:17px;flex:none;color:#6b786d}.search-group input{width:100%;border:none;background:transparent;outline:none;padding:9px 10px;font-size:13px}.key{font-size:10px;white-space:nowrap;color:#758171}.tool{border:1px solid #c9d1c5;border-radius:5px;background:#fffefa;color:#49554b;font-size:12px;padding:8px 11px;white-space:nowrap}#count{font-size:11px;color:#64725f;min-width:55px;white-space:nowrap}.mobile-nav{display:none}.hero{max-width:1100px;margin:0 auto;padding:49px 60px 35px;border-bottom:1px solid var(--line)}.eyebrow{font-size:10px;letter-spacing:2.5px;font-weight:700;color:var(--accent)}h1{font-size:clamp(33px,4vw,48px);line-height:1.13;letter-spacing:-1.4px;margin:17px 0 20px;font-weight:750}.deck{font-size:17px;max-width:750px;color:#687168;line-height:1.6;margin:0}.metrics{display:flex;gap:30px;margin-top:28px;flex-wrap:wrap}.metrics div{border-left:2px solid #c8d2c1;padding-left:12px;font-size:11px;color:#6a7667}.metrics strong{display:block;font-size:19px;color:#293b2d;font-weight:650;line-height:1.4}.article{max-width:1100px;margin:0 auto;padding:25px 60px 70px;background:var(--paper)}.article>p:first-child{font-size:14px}.article>p:nth-child(2),.article>p:nth-child(3){font-size:13px;color:#596558}.article p{margin:15px 0}.article h2{font-size:25px;line-height:1.4;letter-spacing:-.5px;padding:24px 0 18px;margin:62px 0 24px;border-top:3px solid #71856a;border-bottom:1px solid var(--line);scroll-margin-top:100px}.article h3{font-size:21px;line-height:1.4;margin:42px 0 18px;letter-spacing:-.3px;scroll-margin-top:90px}.article h4{font-size:17px;line-height:1.5;margin:27px 0 11px}.article ul,.article ol{padding-left:24px}.article li{padding-left:3px;margin:7px 0}.article li>p{margin:8px 0}strong{font-weight:680}hr{height:1px;border:0;background:var(--line);margin:36px 0}.table-wrap{overflow-x:auto;margin:22px 0;border:1px solid var(--line);border-radius:6px}table{border-collapse:collapse;width:100%;font-size:12.5px;line-height:1.65}th,td{padding:13px 14px;vertical-align:top;text-align:left;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}th{background:#eaf0e5;color:#32482e;font-weight:680;font-size:11.5px}tr:last-child td{border-bottom:0}th:last-child,td:last-child{border-right:0}tbody tr:nth-child(even){background:#fafbf7}td:first-child{min-width:130px}td{min-width:135px}code{font-family:Consolas,SFMono-Regular,Menlo,monospace;font-size:.84em;background:#edf1e9;padding:2px 4px;border-radius:3px;overflow-wrap:anywhere}.code-wrap{position:relative;margin:21px 0}pre{background:var(--code);border-left:3px solid #8f9f80;border-radius:0 5px 5px 0;margin:0;padding:46px 20px 20px;white-space:pre-wrap;word-wrap:break-word;line-height:1.7;font-size:13px;overflow:auto}pre code{background:none;font-size:1em;padding:0;border-radius:0;overflow-wrap:anywhere}.copy{position:absolute;right:10px;top:8px;border:1px solid #bdcbb4;border-radius:4px;background:#f7f9f3;color:#54654c;font-size:10px;padding:3px 8px}.copy:hover{background:#dce7d4}.citation{font-size:10px;border:1px solid #d6ccb9;padding:1px 4px;border-radius:3px;text-decoration:none;vertical-align:super;color:#8c6448;white-space:nowrap}.citation:before{content:'↗ ';font-size:9px}mark{background:#ffe5a4;border-radius:2px;color:inherit}mark.current{background:#f4b76a;outline:2px solid #cc783a}.endnote{max-width:1100px;margin:auto;padding:25px 60px 40px;font-size:12px;color:#71806b;border-top:1px solid var(--line)}:focus-visible{outline:2px solid #b45b35;outline-offset:3px}.progress{height:2px;background:var(--accent);width:0;position:fixed;left:278px;top:0;z-index:80}#toast{position:fixed;bottom:20px;right:20px;background:#263a2a;color:white;border-radius:5px;padding:10px 17px;font-size:12px;z-index:100;opacity:0;transition:opacity .2s;pointer-events:none}#toast.visible{opacity:1}
@media(min-width:1650px){.hero,.article,.endnote{max-width:1180px;padding-left:75px;padding-right:75px}body{font-size:17px}table{font-size:13px}}
@media(max-width:1100px){aside{width:230px}.shell{margin-left:230px}.progress{left:230px}.hero,.article,.endnote{padding-left:32px;padding-right:32px}.toolbar{padding-left:24px;padding-right:24px}.key{display:none}.nav-section{font-size:10.5px}}
@media(max-width:800px){aside{display:none;width:278px;box-shadow:10px 0 40px #0004}aside.open{display:flex}.shell{margin-left:0}.progress{left:0}.mobile-nav{display:inline-block}.toolbar{padding:10px 15px}.hero{padding:34px 23px 28px}.article{padding:18px 23px 50px}.endnote{padding:20px 23px}.hero h1{font-size:34px}.article h2{font-size:21px}.article h3{font-size:19px}body{font-size:15px}.print,.key{display:none}.metrics{gap:17px}.metrics strong{font-size:17px}.article table{font-size:12px}th,td{padding:11px 12px}#count{min-width:30px;font-size:10px}.tool{padding:7px 9px}.search-group{padding:0 8px}.search-group input{padding-left:7px;min-width:0;font-size:12px}}
@media print{body{background:#fff;color:#000;font-size:10.5pt;line-height:1.55}aside,.toolbar,.copy,.progress,#toast{display:none!important}.shell{margin:0}.hero,.article,.endnote{max-width:none;padding:0;background:white}.hero{padding-bottom:20px}.hero h1{font-size:29pt}.deck{font-size:11pt}.metrics{margin-top:17px}.article h2{break-before:page;font-size:19pt;margin-top:0;padding-top:0;border-top:0}.article h3{font-size:14pt;break-after:avoid;margin-top:22px}.article h4{font-size:11pt;break-after:avoid}.article p,.article li{orphans:3;widows:3}.table-wrap{overflow:visible;border-radius:0}table{font-size:8.3pt}th,td{padding:7px;min-width:0!important}tr{break-inside:avoid}thead{display:table-header-group}pre{font-size:9pt;padding:12px;break-inside:avoid;background:#f2f5ed}a{color:#635441}.citation{font-size:7pt}.endnote{margin-top:20px}mark{background:none!important;outline:none!important}@page{size:A4;margin:17mm 14mm 18mm}}
'''
js = '''
const main=document.querySelector('.article');
const toast=document.getElementById('toast');
let toastTimer;
function notify(t){toast.textContent=t;toast.classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>toast.classList.remove('visible'),2200);}
document.querySelectorAll('.copy').forEach(btn=>btn.addEventListener('click',async()=>{const el=document.getElementById(btn.dataset.code);const text=el.querySelector('code').textContent;let copied=false;try{await navigator.clipboard.writeText(text);copied=true;}catch(e){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{copied=document.execCommand('copy');}catch(e){}t.remove();}if(copied){btn.textContent='Скопировано';setTimeout(()=>btn.textContent='Копировать',1600);notify('Текст примера скопирован');}else{const r=document.createRange();r.selectNodeContents(el);const s=window.getSelection();s.removeAllRanges();s.addRange(r);notify('Пример выделен — нажмите Ctrl+C / Cmd+C');}}));
const input=document.getElementById('search');let found=[],current=-1,timer;
function clearMarks(){main.querySelectorAll('mark').forEach(m=>m.replaceWith(document.createTextNode(m.textContent)));main.normalize();found=[];current=-1;}
function highlight(){clearMarks();const q=input.value.trim().toLowerCase();if(q.length<2){document.getElementById('count').textContent='';return;}const w=document.createTreeWalker(main,NodeFilter.SHOW_TEXT);const nodes=[];while(w.nextNode()){const n=w.currentNode;if(n.parentElement.closest('button,script,style'))continue;if(n.nodeValue.toLowerCase().includes(q))nodes.push(n);}for(const n of nodes){const v=n.nodeValue,low=v.toLowerCase();let pos=0,idx=low.indexOf(q);const f=document.createDocumentFragment();while(idx!==-1){f.append(document.createTextNode(v.slice(pos,idx)));const m=document.createElement('mark');m.textContent=v.slice(idx,idx+q.length);f.append(m);pos=idx+q.length;idx=low.indexOf(q,pos);}f.append(document.createTextNode(v.slice(pos)));n.replaceWith(f);}found=[...main.querySelectorAll('mark')];document.getElementById('count').textContent=found.length?'0 / '+found.length:'0';}
function moveMatch(delta=1){if(!found.length)return;if(current>=0)found[current].classList.remove('current');current=(current+delta+found.length)%found.length;found[current].classList.add('current');found[current].scrollIntoView({behavior:'smooth',block:'center'});document.getElementById('count').textContent=(current+1)+' / '+found.length;}
input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(highlight,180);});input.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();clearTimeout(timer);if(!found.length)highlight();moveMatch(e.shiftKey?-1:1);}if(e.key==='Escape'){input.value='';clearMarks();document.getElementById('count').textContent='';input.blur();}});document.getElementById('next').addEventListener('click',()=>moveMatch(1));document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();input.focus();input.select();}});
document.getElementById('menu').addEventListener('click',()=>document.querySelector('aside').classList.toggle('open'));document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{if(window.innerWidth<801)document.querySelector('aside').classList.remove('open');}));
document.addEventListener('click',e=>{if(window.innerWidth<801&&!e.target.closest('aside')&&!e.target.closest('#menu'))document.querySelector('aside').classList.remove('open');});
const headings=[...main.querySelectorAll('h3')];function progress(){const available=document.documentElement.scrollHeight-window.innerHeight;const frac=available?Math.min(1,window.scrollY/available):0;const offset=window.innerWidth<801?0:(window.innerWidth<=1100?230:278);document.querySelector('.progress').style.width=((window.innerWidth-offset)*frac)+'px';let selected;for(const h of headings){if(h.getBoundingClientRect().top<150)selected=h;}document.querySelectorAll('.nav-section').forEach(a=>a.classList.toggle('active',!!selected&&a.getAttribute('href')==='#'+selected.id));}window.addEventListener('scroll',progress,{passive:true});window.addEventListener('resize',progress);progress();
'''
count_sources=len(set(re.findall(r'\]\((https?://[^)]+)\)', text)))
html=f'''<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Практическая база знаний Suno: Lyrics Engineering, Style, Studio 2.0, Premier и выпущенное семейство v6. Обновлено 11 сентября 2026."><title>Suno v6 — Dark Production / Studio · 11.09.2026</title><style>{css}</style></head>
<body><div class="progress" aria-hidden="true"></div><aside><div class="brand"><small>DARK PRODUCTION / FIELD MANUAL</small><b>SUNO /</b><p>v6 / Studio 2.0 / Premier</p><span class="stamp">Обновлено · 11 сентября 2026</span></div><nav aria-label="Содержание">{''.join(nav)}</nav><div class="sidebar-foot">Официальные функции ≠ вероятностные приёмы. Проверяйте гипотезы, сохраняйте удачные дубли.</div></aside>
<div class="shell"><div class="toolbar"><button class="tool mobile-nav" id="menu" aria-label="Открыть содержание">☰</button><div class="search-group"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><input id="search" type="search" autocomplete="off" placeholder="Найти тег, функцию или приём…" aria-label="Поиск по базе знаний"><span class="key">Ctrl / ⌘ K</span></div><span id="count" aria-live="polite"></span><button class="tool" id="next" aria-label="Следующее совпадение" title="Следующее совпадение; в поле поиска — Enter">↓</button><button class="tool print" onclick="window.print()">Печать</button></div>
<header class="hero"><div class="eyebrow">DARK ART-POP · POST-PUNK · INDUSTRIAL TRIP-HOP</div><h1>Свой звук.<br>Под контролем.</h1><p class="deck">Русский вокал, отдельные дорожки, MIDI и электрический нерв. Свежая практика v6 — без фонка, рэпа и коммерческого dance-pop.</p><div class="metrics"><div><strong>03 блока</strong>единая производственная система</div><div><strong>11 part-промптов</strong>конкретные задания для дорожек</div><div><strong>{count_sources} источников</strong>официальные материалы и сообщества</div><div><strong>v6 / LIVE</strong>релиз 9 сентября 2026</div></div><div class="jump-links"><a href="#section-2-2">Max / Variety</a><a href="#section-3-5">Дорожки: готовые промпты</a><a href="#section-3-7">MIDI вместо угадывания</a><a href="#section-3-13">Три рабочих маршрута</a></div></header>
<main class="article">{soup}</main><footer class="endnote">Документальный ресерч · 11 сентября 2026. Страница самодостаточна: поиск, содержание и примеры работают без внешних библиотек. Ссылки на источники требуют доступа к сети. Для переноса в базу знаний используйте сопровождающий Markdown-файл.</footer></div><div id="toast" role="status"></div><script>{js}</script></body></html>'''
out=ROOT/'suno_v6_studio_dark_2026-09-11.html'
out.write_text(html)
print(out.name, out.stat().st_size, 'bytes')
print('H2:',len(soup.find_all('h2')),'H3:',len(soup.find_all('h3')),'tables:',len(soup.find_all('table')),'copyable examples:',len(soup.find_all('pre')))
assert len(soup.find_all('h2'))==3
assert len(soup.find_all('pre'))==45
assert not soup.find_all(['script','img','iframe'])
