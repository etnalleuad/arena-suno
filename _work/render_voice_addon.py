from pathlib import Path
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from html import escape
import re,json,hashlib,zipfile,csv,subprocess
P=Path('/home/user/VOICE_ADDON_2026-09-12')
kb=(P/'07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt').read_text()
md=MarkdownIt('commonmark',{'html':False}).enable('table')
soup=BeautifulSoup(md.render(kb),'html.parser')
if soup.h1:soup.h1.decompose()
nav=[]
for h in soup.find_all('h2'):
 title=h.get_text(' ',strip=True)
 m=re.match(r'7\.(\d+)\.',title)
 if m:
  sid='section-'+m.group(1);h['id']=sid
  nav.append('<a href="#'+sid+'">'+escape(title)+'</a>')
for t in soup.find_all('table'):
 t.wrap(soup.new_tag('div',attrs={'class':'table-wrap'}))
for a in soup.find_all('a',href=True):
 if a['href'].startswith('http'):
  a['target']='_blank';a['rel']='noopener noreferrer';a['title']=a['href']
  if a.get_text(strip=True).isdigit():a['class']=['citation']
patch=(P/'GEM_INSTRUCTIONS_APPEND.txt').read_text()
full=(P/'GEM_INSTRUCTIONS_FULL_V2.txt').read_text()
first=(P/'FIRST_VOICE_MESSAGE.txt').read_text()
css='''
:root{--ink:#232827;--muted:#68726a;--green:#516943;--accent:#956241;--paper:#fffef9;--bg:#f0f2e9;--line:#d9dfd0}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;font:15px/1.72 Inter,Segoe UI,Arial,sans-serif;background:var(--bg);color:var(--ink)}a{color:var(--green);text-underline-offset:3px}header{background:#212a24;color:#f7f8ee;padding:42px max(24px,calc((100vw - 1160px)/2));border-bottom:4px solid #bdca8d}.eyebrow{font-size:10px;color:#c6d4ad;letter-spacing:2px}h1{font-size:clamp(31px,4vw,46px);line-height:1.15;letter-spacing:-1.4px;margin:16px 0 20px;max-width:850px}header p{max-width:860px;color:#bcc9b7}.badges{display:flex;gap:10px;flex-wrap:wrap;font-size:11px}.badges span{border:1px solid #56664b;padding:4px 9px;border-radius:3px}.shell{max-width:1220px;margin:auto;padding:25px 26px 55px}.top-grid{display:grid;grid-template-columns:1fr 1fr;gap:17px}.card{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:23px;margin-bottom:20px}h2{font-size:23px;line-height:1.4;margin:0 0 16px;letter-spacing:-.3px}h3{font-size:17px;line-height:1.4;margin:24px 0 10px}p{margin:13px 0}.label{font-size:11px;letter-spacing:1px;color:#7c886e;text-transform:uppercase}.big{font-size:32px;font-weight:700;line-height:1.25;margin:8px 0;color:#425838}.muted{font-size:13px;color:var(--muted)}.button{display:inline-block;border:1px solid #445e37;background:#445e37;color:#fff;text-decoration:none;padding:9px 14px;border-radius:4px;font-size:12px;font-weight:600;margin:7px 6px 7px 0}.copy{font:12px Inter,Segoe UI,Arial,sans-serif;border:1px solid #bacba7;background:#edf4e3;color:#415d31;padding:8px 12px;border-radius:4px;cursor:pointer;margin:7px 5px 7px 0}.notice{background:#f3ead8;border-left:3px solid #ab8252;padding:14px 17px;margin:18px 0;font-size:13px}.flow{display:flex;flex-wrap:wrap;gap:7px;align-items:center;font-size:12px;margin:18px 0}.flow b{padding:6px 9px;background:#edf1e4;border:1px solid #d2debf;border-radius:4px}.flow i{font-style:normal;color:#7e8c71}.layout{display:grid;grid-template-columns:236px minmax(0,1fr);gap:24px;align-items:start}.toc{position:sticky;top:18px;max-height:92vh;overflow:auto;background:#e6eddc;border:1px solid #d1dcc3;border-radius:6px;padding:13px 10px}.toc strong{display:block;font-size:12px;padding:4px 8px 10px;color:#495f3b}.toc a{display:block;font-size:11px;line-height:1.55;padding:7px 8px;border-radius:4px;text-decoration:none;color:#4f6341}.toc a:hover{background:#d6e3c6}.article{background:var(--paper);border:1px solid var(--line);border-radius:7px;padding:27px 31px;min-width:0}.article h2{border-top:2px solid #aabf94;padding-top:22px;margin:37px 0 17px;scroll-margin-top:25px}.article h2:first-of-type{margin-top:25px}.article h3{margin-top:28px}.article ul,.article ol{padding-left:23px}.article li{margin:6px 0}.table-wrap{overflow:auto;margin:20px 0}table{border-collapse:collapse;width:100%;font-size:12px;line-height:1.65}th,td{padding:10px;border:1px solid #d9dfd0;text-align:left;vertical-align:top;min-width:115px}th{background:#eaf1df;color:#475f37;font-size:11px}tr:nth-child(even){background:#f7f9f1}code{font:12px/1.6 Consolas,Menlo,monospace;padding:2px 4px;border-radius:3px;background:#edf2e5;color:#4f6340;overflow-wrap:anywhere}pre{font:12px/1.65 Consolas,Menlo,monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#edf2e5;border-left:3px solid #9fb887;padding:14px;max-height:420px;overflow:auto}pre code{background:none;padding:0}details{border:1px solid #d7e0cc;border-radius:5px;padding:10px 13px;margin:12px 0}summary{cursor:pointer;font-size:13px;font-weight:600}.citation{font-size:10px;vertical-align:super;text-decoration:none;padding:1px 4px;border:1px solid #d3dabe;border-radius:3px}.citation:before{content:'↗ ';font-size:9px}.foot{font-size:12px;color:#717d65;margin-top:20px}.toast{position:fixed;bottom:20px;right:20px;background:#304b27;color:#fff;padding:11px 16px;border-radius:4px;font-size:12px;opacity:0;pointer-events:none;z-index:20}.toast.show{opacity:1}[hidden]{display:none!important}:focus-visible{outline:2px solid #a17a3c;outline-offset:3px}@media(max-width:950px){.layout{grid-template-columns:1fr}.toc{position:static;max-height:none;display:grid;grid-template-columns:1fr 1fr}.toc strong{grid-column:1/-1}.top-grid{grid-template-columns:1fr}}@media(max-width:600px){.shell{padding:19px 15px}.article{padding:21px 18px}.toc{display:block}.card{padding:19px}body{font-size:14px}h1{font-size:32px}h2{font-size:21px}header{padding:30px 20px}}@media print{header{background:white;color:black;padding:0;border-bottom:2px solid #555}header p{color:#444}.shell{padding:12px 0}.toc,.copy,.button,.toast{display:none!important}.layout,.top-grid{display:block}.article,.card{border:0;padding:0;background:white}.article h2{break-after:avoid;font-size:16pt}.article h3{break-after:avoid}body{background:white;font-size:10pt;line-height:1.5}.table-wrap{overflow:visible}table{font-size:8pt}tr{break-inside:avoid}td,th{min-width:0;padding:6px}details{display:none}.notice{background:#eee}}
'''
js=r'''
let timeout;
function notify(t){const n=document.getElementById('toast');n.textContent=t;n.classList.add('show');clearTimeout(timeout);timeout=setTimeout(()=>n.classList.remove('show'),2200);}
async function copy(t){try{await navigator.clipboard.writeText(t);notify('Скопировано');}catch(e){const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();let ok=false;try{ok=document.execCommand('copy');}catch(e){}a.remove();if(ok)notify('Скопировано');else{const m=document.getElementById('manual-copy');m.hidden=false;m.value=t;m.focus();m.select();notify('Текст выделен — Ctrl+C / Cmd+C');}}}
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>copy(document.getElementById(b.dataset.copy).textContent)));
'''
header='''<header><div class="eyebrow">ДОПОЛНЕНИЕ 07 / GEMINI × SUNO × СВОЙ ГОЛОС</div><h1>Свой тембр.<br>Без лишних подписок.</h1><p>Разовое обучение модели, новые конверсии, работа с артефактами и честная экономика одной песни в месяц. Под твой сценарий: Windows, NVIDIA и минимум дополнительных расходов.</p><div class="badges"><span>Проверено · 12.09.2026</span><span>Kits / Applio / доработка</span><span>Стихи — позже</span><span>Библиотека 70 IDs не меняется</span></div></header>'''
top='''<div class="top-grid"><section class="card"><div class="label">Основной кандидат без оплаты сервису</div><div class="big">Applio локально</div><p>Один раз подготовить свои реальные записи и обучить модель. Затем использовать её для новых разрешённых вокальных источников. Нужны подходящее железо и разовая настройка.</p><p class="muted">Точная NVIDIA/VRAM пока неизвестны. Это не обещание работы любой конфигурации и не готовый клон твоего голоса.</p></section><section class="card"><div class="label">Почему Kits не «оплатить один раз»</div><div class="big">Модель замораживается</div><p>После окончания подписки сохранённый clone становится недоступен. Накопленные download minutes сгорают. Free не даёт скачивать готовые результаты.</p><p class="muted">В карточке Starter и FAQ есть расхождение по Professional Cloning — в базе оно отмечено, а не замаскировано.</p></section></div>'''
steps='''<section class="card"><h2>Обновить существующий Gem — без пересборки</h2><a class="button" href="VOICE_ADDON_2026-09-12.zip" download>Скачать дополнение ZIP</a><ol><li>Распакуй архив.</li><li>Открой свой Gem → Edit → Knowledge.</li><li>Добавь <code>07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt</code>. Предыдущие шесть файлов оставь — теперь источников семь.</li><li>Добавь короткий блок ниже в конец Instructions. Если свои инструкции не меняла, в архиве есть и полная версия V2 для замены.</li><li>Save/Update. Для чистой проверки отправь <code>CHECK_ADDON.txt</code>; для продолжения песни используй её паспорт.</li></ol><button class="copy" data-copy="patch">Копировать дополнение к Instructions</button><details><summary>Показать короткое дополнение</summary><pre id="patch">'''+escape(patch)+'''</pre></details><details><summary>Полная версия Instructions V2 — только если не нужно сохранять собственные правки</summary><button class="copy" data-copy="full">Копировать полную версию</button><pre id="full">'''+escape(full)+'''</pre></details><p class="muted">Пакет звуков/70IDs повторно загружать не нужно. Программы, installers, .pth/.index и голосовые записи в этом архиве отсутствуют. Здесь — подготовленная база и инструкции.</p></section>'''
practical='''<section class="card"><h2>Что будем делать на практике</h2><div class="flow"><b>Свои записи</b><i>→</i><b>Training → своя модель</b><i>→</i><b>Разрешённая партия</b><i>→</i><b>Conversion</b><i>→</i><b>Audio в Studio</b></div><p>Конвертация прежде всего меняет тембр. Она не обязана исправлять неверные слова и ноты исходника. Поэтому сначала сохраняем хорошую мелодию/подачу, затем тестируем собственный тембр на коротком фрагменте.</p><div class="notice"><b>Важное условие:</b> разрешение скачать Suno WAV не является автоматическим подтверждением права использовать его в стороннем AI-конвертере. В Terms есть широкий пункт10; в архиве подготовлен точный вопрос Suno. Для обучения локальной модели — только твои реальные записи. Технический маршрут ниже условен до проверки прав на конкретный source.</div><button class="copy" data-copy="first">Копировать первый запрос Gem</button><details><summary>Первое сообщение для голосового workflow</summary><pre id="first">'''+escape(first)+'''</pre></details><p class="muted">Для точного локального setup понадобятся модель NVIDIA, VRAM и сведения о подготовленных реальных записях. Подписку сейчас покупать не предлагаю.</p></section>'''
html='<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Свой тембр — Kits, Applio и дополнение Gemini</title><style>'+css+'</style></head><body>'+header+'<main class="shell">'+top+steps+practical+'<div class="layout"><nav class="toc" aria-label="Содержание"><strong>Полная база дополнения</strong>'+''.join(nav)+'</nav><article class="article">'+str(soup)+'</article></div><textarea id="manual-copy" hidden style="width:100%;height:150px" aria-label="Текст для ручного копирования"></textarea><div class="foot">Документальный ресерч и проверка конкретных параметров кода, не слуховой benchmark. В твоём аккаунте/на компьютере ничего не устанавливалось, не обучалось и не конвертировалось. Инструменты подбираются по задаче; платные опции не навязываются.</div></main><div id="toast" class="toast" role="status"></div><script>'+js+'</script></body></html>'
out=Path('/home/user/VOICE_WORKFLOW_GUIDE_2026-09-12.html');out.write_text(html)
# A portable copy inside the package points to the already extracted readme, not a missing sibling ZIP.
portable=html.replace('<a class="button" href="VOICE_ADDON_2026-09-12.zip" download>Скачать дополнение ZIP</a>','<p class="muted">Архив уже распакован. Добавь TXT №07 в Knowledge существующего Gem.</p>')
(P/'READ_ME.html').write_text(portable)
# Validate before final packaging.
for f in [out,P/'READ_ME.html']:
 h=BeautifulSoup(f.read_text(),'html.parser');ids=[x['id'] for x in h.find_all(id=True)]
 assert len(ids)==len(set(ids))
 assert all(a['href'][1:] in ids for a in h.select('a[href^="#"]'))
 assert not [x for x in h.find_all(['script','link','img']) if x.get('src') or x.get('href')]
 for b in h.select('[data-copy]'):assert b['data-copy'] in ids
 j='\n'.join(x.string or '' for x in h.find_all('script'))
 jp=Path('/home/user/_work/voice_addon_sources/reader.js');jp.write_text(j)
 subprocess.run(['node','--check',str(jp)],check=True,capture_output=True,text=True)
assert len(full)<8000
assert len(re.findall(r'^## 7\.',kb,re.M))==18
audit=json.loads(Path('/home/user/_work/voice_addon_sources/applio_3_6_4_ui_audit.json').read_text())
values={r['names'][0]:r for r in audit}
assert values['protect']['maximum']==0.5 and values['protect']['value']==0.5
assert values['pitch']['value']==0 and values['index_rate']['value']==0.75
assert values['rms_mix_rate']['value']==1 and values['f0_method']['value']=='rmvpe'
with (P/'TEMPLATES'/'VOICE_AB_TEST_PLAN.csv').open(encoding='utf-8-sig') as f:
 rows=list(csv.reader(f));assert all(len(r)==len(rows[0]) for r in rows)
 assert all(r[1]=='PLANNED' for r in rows[1:])
assert not list(P.rglob('*.pth')) and not list(P.rglob('*.exe')) and not list(P.rglob('*.bat'))
report={'verified_date':'2026-09-12','knowledge_files_to_add':1,'total_existing_gem_knowledge_after_update':7,'kb_sections':18,'full_instructions_chars':len(full),'code_reference':'Applio 3.6.4','audit':'Static inspection of UI definitions and protective-blend pipeline; no conversion executed','no_voice_model_or_installer_included':True,'previous_music_library_changed':False,'user_account_install_training_conversion_tested':False}
(P/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
lines=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name!='CHECKSUMS.sha256':lines.append(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.relative_to(P).as_posix())
(P/'CHECKSUMS.sha256').write_text('\n'.join(lines)+'\n')
zp=Path('/home/user/VOICE_ADDON_2026-09-12.zip')
with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file():z.write(f,P.name+'/'+f.relative_to(P).as_posix())
with zipfile.ZipFile(zp) as z:assert z.testzip() is None
print('PASS',report)
print('ZIP:',zp.stat().st_size,'bytes;', 'HTML:',out.stat().st_size,'bytes')
