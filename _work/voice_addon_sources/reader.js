
let timeout;
function notify(t){const n=document.getElementById('toast');n.textContent=t;n.classList.add('show');clearTimeout(timeout);timeout=setTimeout(()=>n.classList.remove('show'),2200);}
async function copy(t){try{await navigator.clipboard.writeText(t);notify('Скопировано');}catch(e){const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();let ok=false;try{ok=document.execCommand('copy');}catch(e){}a.remove();if(ok)notify('Скопировано');else{const m=document.getElementById('manual-copy');m.hidden=false;m.value=t;m.focus();m.select();notify('Текст выделен — Ctrl+C / Cmd+C');}}}
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>copy(document.getElementById(b.dataset.copy).textContent)));
