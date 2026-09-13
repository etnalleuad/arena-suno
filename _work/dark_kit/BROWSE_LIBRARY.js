
const audioData=JSON.parse(document.getElementById('audio-data').textContent||'{}');
const metaData=JSON.parse(document.getElementById('meta-data').textContent||'{}');
const player=document.getElementById('audio-player'),plabel=document.getElementById('play-label');
let noticeTimer;
function notify(s){const n=document.getElementById('toast');n.textContent=s;n.classList.add('show');clearTimeout(noticeTimer);noticeTimer=setTimeout(()=>n.classList.remove('show'),2200);}
async function copyText(text){try{await navigator.clipboard.writeText(text);notify('Скопировано');}catch(e){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();let ok=false;try{ok=document.execCommand('copy');}catch(e){}t.remove();if(ok)notify('Скопировано');else{const box=document.getElementById('manual-copy');box.hidden=false;box.value=text;box.focus();box.select();notify('Текст выделен — нажми Ctrl+C / Cmd+C');}}}
document.querySelectorAll('[data-copy-target]').forEach(b=>b.addEventListener('click',()=>copyText(document.getElementById(b.dataset.copyTarget).textContent)));
document.querySelectorAll('[data-asset]').forEach(b=>b.addEventListener('click',()=>{const a=metaData[b.dataset.asset];copyText('Для текущей песни рассмотрим '+a.id+'.\nФайл: PART_2_STUDIO_ASSETS/'+a.path+'\nТип: '+a.kind+'; роль: '+a.role+'\nЭто файл в моей локальной библиотеке, не обязательно прикреплённое здесь аудио. Объясни куда его импортировать или как применить, согласуй BPM/key с песней, дай следующий шаг. Не делай вид, что уже прослушал или загрузил его в мой проект.');}));
document.querySelectorAll('[data-play]').forEach(b=>b.addEventListener('click',()=>{const id=b.dataset.play;if(!audioData[id])return;player.src='data:audio/wav;base64,'+audioData[id];plabel.textContent=(b.dataset.label||id);player.play().catch(()=>notify('Нажми Play в плеере'));}));
const search=document.getElementById('search'),filter=document.getElementById('filter');
function applyFilter(){if(!search||!filter)return;const q=search.value.trim().toLowerCase(),k=filter.value;let n=0;document.querySelectorAll('.asset').forEach(c=>{const show=(!q||c.dataset.search.includes(q))&&(!k||c.dataset.group===k);c.hidden=!show;if(show)n++;});document.getElementById('result-count').textContent=n+' / '+document.querySelectorAll('.asset').length;}
if(search)search.addEventListener('input',applyFilter);if(filter)filter.addEventListener('change',applyFilter);applyFilter();
