from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import json,hashlib,shutil,zipfile,re,csv
ROOT=Path('/home/user');P=ROOT/'CHAT_RESTORE_2026-09-12';P.mkdir(exist_ok=True)
K1=ROOT/'suno_gemini_kit/PART_1_GEMINI';K2=ROOT/'suno_gemini_kit/PART_2_STUDIO_ASSETS';VA=ROOT/'VOICE_ADDON_2026-09-12'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,rel):
 dst=P/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst);return dst

h=P/'PROJECT_HANDOFF.md';s=h.read_text()
start=s.index('## 8.');end=s.index('## 9.')
s=s[:start]+Path('/home/user/_work/handoff_key_facts.md').read_text()+'\n'+s[end:]
s=s.replace('Для удобства они сохранены вJPEG без переноса вложенных метаданных; исходныеPNG остались в предыдущем чате.', 'Исходные PNG сохранены в архиве; дополнительно сделан JPEG-контактный лист для быстрого обзора.')
s=s.replace('Снимки включены в папку PHOTOS в переносимом архиве; это пользовательские фотографии, не AI-иллюстрации.', 'Четыре снимка включены в папку PHOTOS; это пользовательские фотографии, не AI-иллюстрации.')
s=s.replace('Новые факты', 'Новые факты')
# Light typography without altering identifiers or URLs.
lines=[]
for line in s.splitlines():
 if 'http' not in line and not line.startswith('`'):
  line=re.sub(r'(?<=[А-Яа-яЁё])(?=[A-Za-z])|(?<=[A-Za-z])(?=[А-Яа-яЁё])',' ',line)
  line=re.sub(r'(?<=\d)(?=[А-Яа-яЁё])|(?<=[А-Яа-яЁё])(?=\d)',' ',line)
  line=line.replace('RTX3050','RTX 3050').replace('8GBVRAM','8 GB VRAM')
 lines.append(line)
s='\n'.join(lines)+'\n'
s=s.replace('**Этот тестовый файл ещё НЕ получен.**', '**Этот тестовый файл ещё НЕ получен. Новые сообщения пользовательницы обновляют этот статус.**')
h.write_text(s)

# Seven active knowledge modules, preserving the technical snapshots.
A=P/'ACTIVE_KNOWLEDGE';A.mkdir(exist_ok=True)
for src in sorted((K1/'KNOWLEDGE').glob('*.txt')):copy(src,'ACTIVE_KNOWLEDGE/'+src.name)
kb7=(VA/'07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt').read_text()
kb7=kb7.replace('Компьютер Windows с NVIDIA; точная GPU, VRAM, RAM и драйвер пока НЕ известны.', 'Обновление пользовательницы: Windows x64, RTX 3050 Laptop GPU с 4 GB VRAM, RAM 32 GB, i5-12500H. Драйвер неизвестен; датасет нужно записать с нуля. Состояние микрофона и следующий тест см. в CURRENT_STATE паспорта.')
kb7=kb7.replace('точная GPU/VRAM пока неизвестны', 'GPU и VRAM уже известны из актуального паспорта; драйвер пока неизвестен')
kb7=kb7.replace('Точная GPU, VRAM, RAM и драйвер пока НЕ известны.', 'GPU/RAM известны из текущего паспорта; драйвер неизвестен.')
kb7=kb7.replace('Для точного локального voice-setup нужны:\n1. Название NVIDIA и объём VRAM.\n2. Есть ли 10–30 минут собственных сухих реальных записей или пока только короткий референс?\n3. Какой source планируется конвертировать и установлено ли разрешение на внешнее AI-использование?', 'Обновлённый этап: GPU — RTX 3050 Laptop 4 GB, RAM 32 GB; готовых записей для датасета пока нет. Сейчас нужна короткая raw-запись имеющимся микрофоном. После её проверки — подготовка датасета, свободного места и локальной установки. Не повторять уже отвеченные вопросы о GPU и наличии датасета.')
kb7='CURRENT UPDATE — 12.09.2026: профиль железа и состояние микрофона берутся из PROJECT_HANDOFF / CURRENT_STATE. Этот модуль дополнен пользовательскими фактами; технический code-audit по-прежнему относится к Applio 3.6.4.\n\n'+kb7
(A/'07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt').write_text(kb7)
assert len(list(A.glob('*.txt')))==7

# Current reusable Gem instructions, separate from immutable original packages.
ins=(VA/'GEM_INSTRUCTIONS_FULL_V2.txt').read_text()
ins=ins.replace('Windows с NVIDIA, точная GPU/VRAM пока неизвестны.', 'Windows: RTX 3050 Laptop 4 GB, RAM 32 GB. Датасет ещё не записан.')
ins+='\n\nТЕКУЩИЙ ЭТАП: raw-тест имеющегося микрофона через USB-карту, не обучение. GPU/микрофон уже описаны в актуальном паспорте: не задавай эти вопросы заново. Новые сведения пользовательницы обновляют паспорт.\n'
G=P/'GEM_SETUP';G.mkdir(exist_ok=True)
(G/'GEM_INSTRUCTIONS_CURRENT.txt').write_text(ins)
for src,rel in [
 (K1/'00_READ_ME_FIRST.md','GEM_SETUP/INSTALL_ORIGINAL_SIX_FILES.md'),
 (K1/'CHECK_GEM_SETUP.txt','GEM_SETUP/CHECK_CORE.txt'),
 (K1/'START_NEW_SONG.txt','GEM_SETUP/START_NEW_SONG.txt'),
 (VA/'00_HOW_TO_ADD.md','GEM_SETUP/INSTALL_VOICE_ADDON.md'),
 (VA/'CHECK_ADDON.txt','GEM_SETUP/CHECK_VOICE_ADDON.txt'),
 (VA/'FIRST_VOICE_MESSAGE.txt','GEM_SETUP/FIRST_VOICE_MESSAGE_ORIGINAL.txt'),
 (VA/'SUPPORT_QUESTIONS.txt','GEM_SETUP/SUPPORT_QUESTIONS_UNSENT.txt'),
 (VA/'TOOLS_AND_COSTS.csv','GEM_SETUP/TOOLS_AND_COSTS_2026-09-12.csv')]:copy(src,rel)
for src in (K1/'TEMPLATES').iterdir():
 if src.is_file():copy(src,'TEMPLATES/SONGS/'+src.name)
for src in (VA/'TEMPLATES').iterdir():
 if src.is_file():copy(src,'TEMPLATES/VOICE/'+src.name)
if (ROOT/'MY_VOICE_SETUP_RTX3050.txt').exists():copy(ROOT/'MY_VOICE_SETUP_RTX3050.txt','CURRENT_PROFILE/MY_VOICE_SETUP_RTX3050.txt')

# User-visible reference documents retained. The 6 September guide is not the active version.
for name in ['suno_v6_studio_dark_2026-09-11.md','suno_v6_studio_dark_2026-09-11.html','VOICE_WORKFLOW_GUIDE_2026-09-12.html','START_HERE_GEMINI_STUDIO.html']:
 if (ROOT/name).exists():copy(ROOT/name,'REFERENCE_GUIDES/'+name)
for name in ['suno_knowledge_base_ru_2026-09-06.md','suno_knowledge_base_ru_2026-09-06.html']:
 if (ROOT/name).exists():copy(ROOT/name,'ARCHIVE_NOT_CURRENT/'+name)
(P/'ARCHIVE_NOT_CURRENT'/'READ_THIS_FIRST.txt').write_text('Исторический срез6сентября: v6 тогда ещё не была подтверждённым общим релизом в исследовании, а жанровые предпочтения позднее уточнились. Не использовать эти файлы как текущий модельный/жанровый профиль. Активные данные — PROJECT_HANDOFF, ACTIVE_KNOWLEDGE и полный ALL_CONTEXT.\n')
for name in ['PART_1_GEMINI.zip','VOICE_ADDON_2026-09-12.zip','suno_v6_midi_starters_96bpm.zip']:
 if (ROOT/name).exists():copy(ROOT/name,'ORIGINAL_DOWNLOADS/'+name)
for name in ['ASSET_INDEX.json','ASSET_INDEX.csv','ASSET_CATALOG_RU.md','LICENSE_AND_ORIGIN.txt','SOUND_DESIGN_NOTES.md','VALIDATION_REPORT.json']:
 if (K2/name).exists():copy(K2/name,'MEDIA_CATALOG_ONLY/'+name)

# Source scripts for recovery, not for automatic execution.
B=P/'BUILD_SCRIPTS';B.mkdir(exist_ok=True)
script_names=['build_dark_assets.py','build_dark_catalog.py','build_gem_knowledge.py','make_v6_midi.py','render_knowledge_base.py','render_v6_dark.py','render_kit_guides.py','write_kit_readmes.py','validate_and_package_kit.py','build_voice_addon_files.py','render_voice_addon.py']
for name in script_names:
 if (ROOT/'_work'/name).exists():copy(ROOT/'_work'/name,'BUILD_SCRIPTS/'+name)
(B/'README.txt').write_text('''Не запускать автоматически.
Это исходники созданных в прежнем чате документов и процедурной музыкальной библиотеки, а не установщики Suno/Applio и не модели голоса.
Внутри могут быть абсолютные пути /home/user и ссылки на вспомогательные файлы прежней сборки. Для восстановления нужно адаптировать пути и зависимости; это работа для помощника, если она действительно потребуется.
Обычное продолжение разговора не требует запуска ни одного скрипта. Готовые WAV/MIDI надёжнее сохранить отдельным PART_2_STUDIO_ASSETS.zip.
Основные зависимости использованной сборки: Python3, numpy, scipy, soundfile, markdown-it-py, beautifulsoup4, Pillow; для проверки JS использовался Node.js. Установленные пакеты в новый чат не переносятся автоматически.
Процедурный rebuild может зависеть от версий библиотек; не обещается побитово одинаковый результат во всяком окружении. Original media archive и hashes — источник истины.
''')
for name in ['v6_midi_validation.json']:
 if (ROOT/'_work'/name).exists():copy(ROOT/'_work'/name,'TECHNICAL_AUDITS/'+name)
for name in ['applio_3_6_4_ui_audit.json']:
 if (ROOT/'_work/voice_addon_sources'/name).exists():copy(ROOT/'_work/voice_addon_sources'/name,'TECHNICAL_AUDITS/'+name)
(P/'TECHNICAL_AUDITS'/'README.txt').write_text('Аудит статических значений/условий кода и структуры MIDI, не испытание голоса. JSON Applio — запись исследования, не импортируемый preset. Tooltip в коде может противоречить runtime; правильные оговорки даны в KB07.\n')

# Preserve the four current microphone photographs byte-for-byte; create an additional overview.
PH=P/'PHOTOS';PH.mkdir(exist_ok=True)
photos=[]
labels=['Microphone with foam','Microphone without foam','Another microphone view','USB audio adapter']
for i in range(1,5):
 src=ROOT/'uploads'/f'image-{i}.png'
 if src.exists():
  dst=copy(src,f'PHOTOS/MIC_0{i}.png');photos.append((dst,labels[i-1]))
font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=ImageFont.truetype(font_path,24) if Path(font_path).exists() else ImageFont.load_default()
canvas=Image.new('RGB',(1500,2110),'#f5f4ee');draw=ImageDraw.Draw(canvas)
for i,(src,label) in enumerate(photos):
 im=ImageOps.exif_transpose(Image.open(src)).convert('RGB');im.thumbnail((715,965))
 col=i%2;row=i//2;x=25+col*750;y=25+row*1050
 draw.text((x,y),f'{i+1}. {label}',font=font,fill='#253226')
 canvas.paste(im,(x+(715-im.width)//2,y+50))
canvas.save(PH/'MIC_CONTACT_SHEET.jpg',quality=90,optimize=True)
(PH/'PHOTO_INDEX.md').write_text('''# Фотографии микрофона
MIC_01.png — поролоновая ветрозащита, корпус, mount и кабель.
MIC_02.png — микрофон без поролона.
MIC_03.png — другой ракурс.
MIC_04.png — USB-звуковая карта с надписью7.1ChannelSound.
MIC_CONTACT_SHEET.jpg — дополнительный обзор из этих же пользовательских фото, не AI-генерация.

Оригинальные четыреPNG скопированы без изменения. По ним не подтверждены точная модель микрофона, тип капсюля и требования питания. Старый скриншот ноутбука среди текущих uploads отсутствует; его необходимые характеристики сохранены в PROJECT_HANDOFF без device/product IDs.
''')
# External media stays separate to avoid duplicating a large binary archive in every chat transfer.
media=ROOT/'PART_2_STUDIO_ASSETS.zip';assert media.exists()
external={'required_for_full_media_recovery':True,'filename':media.name,'bytes':media.stat().st_size,'sha256':sha(media),'contents':'48 WAV + 12 MIDI + 10 recipe texts, catalogs, previews and validation','contained_in_this_chat_restore_zip':False,'why':'Store/download separately. Text and catalog are included here; the full audio library is not duplicated.'}
(P/'EXTERNAL_MEDIA_BACKUP.json').write_text(json.dumps(external,ensure_ascii=False,indent=2))

readme='''# Перенос в новый чат — без GitHub

## Сначала скачать на свой компьютер
1. **CHAT_RESTORE_2026-09-12.zip** — контекст, вся активная текстовая база, оригинальные документы/шаблоны, фото микрофона и исходные скрипты.
2. **PART_2_STUDIO_ASSETS.zip** — отдельная полная медиабиблиотека, около36МБ. Она НЕ продублирована в CHAT_RESTORE.

Эти два архива вместе сохраняют рабочую базу проекта и созданные музыкальные материалы. Пока файлы не скачаны, не следует считать их независимой резервной копией на своём компьютере. Никакой GitHub-репозиторий не создавался и не обновлялся.

## Самый простой старт нового чата
1. Распакуй CHAT_RESTORE.
2. Прикрепи **ALL_CONTEXT_FOR_NEW_CHAT_2026-09-12.txt** — один файл со всем активным контекстом и семью Knowledge-модулями.
3. Скопируй в сообщение **START_NEW_CHAT.txt**.
4. При необходимости добавь **PHOTOS/MIC_CONTACT_SHEET.jpg** и новый raw-аудиотест. Полную библиотеку звуков загружать для обсуждения микрофона не нужно.

Не загружай весьZIP в Gemini автоматически: в нём много файлов, а возможности/лимиты ZIP зависят от продукта. Надёжнее распаковать и передать нужные TXT/MD/изображения. Файл полного контекста намеренно текстовый, без встроенного аудио.

## Если новому чату тяжело читать всё сразу
Сначала передай PROJECT_HANDOFF.md. Далее добавляй нужные файлы из ACTIVE_KNOWLEDGE, напримерKB04длявокала илиKB07дляконверсии. CURRENT_STATE всегда читать первым. Помощник должен честно сообщить, какие вложения он смог прочитать.

## Для восстановления custom Gem
Используй GEM_SETUP/GEM_INSTRUCTIONS_CURRENT.txt в полеInstructions и семьTXT изACTIVE_KNOWLEDGE вKnowledge. В текущем обновлении учтено известное железо. Не загружай параллельно старые архивные гайды как более актуальную базу. Паспорт песни и новый audio — в отдельный разговор этой песни.

## Где что
- PROJECT_HANDOFF.md — последний статус, решения, оборудование, незавершённые шаги.
- ALL_CONTEXT_FOR_NEW_CHAT…txt — самодостаточная активная текстовая сборка.
- ACTIVE_KNOWLEDGE — семь отдельных модулей.
- GEM_SETUP — инструкции и проверки.
- TEMPLATES — формы песен/голоса/реестров, не заполненные результаты тестов.
- CURRENT_PROFILE — профиль ноутбука и план записи.
- PHOTOS — четыре исходные фотографии микрофона и контактный лист.
- MEDIA_CATALOG_ONLY — точный индекс70ID; не самиWAV/MIDI.
- REFERENCE_GUIDES — предыдущие подробные пользовательские руководства.
- ARCHIVE_NOT_CURRENT — историческая версия6сентября, не текущие рекомендации.
- ORIGINAL_DOWNLOADS — небольшие исходные текстовые пакеты/ранняя параMIDI.
- BUILD_SCRIPTS — дополнительная возможность восстановления; не запускать автоматически.
- EXTERNAL_MEDIA_BACKUP.json — имя, размер иSHA256обязательного отдельного медиаархива.
- CHECKSUMS.sha256 — контроль целостности файлов переноса.

## Чего ещё нет
Нет полученного личного raw-аудиотеста, подготовленного реального vocal dataset, обученного .pth/.index или подтверждённой установки программ/настройки Gem в аккаунте пользовательницы. Музыкальная библиотека состоит из синтетических инструментальных материалов и не является датасетом её голоса.

Точный остаток лимита чата/аккаунта помощнику не показывался. Поэтому перенос подготовлен заранее, без обещания определённого числа оставшихся сообщений или автоматической памяти в новом чате.
'''
(P/'00_START_HERE.md').write_text(readme)

# Build one user-uploadable file. Sections are complete, not truncated summaries of the knowledge.
master_name='ALL_CONTEXT_FOR_NEW_CHAT_2026-09-12.txt'
parts=['''# ПОЛНЫЙ АКТИВНЫЙ КОНТЕКСТ ДЛЯ НОВОГО ЧАТА
SNAPSHOT: 2026-09-12

ПОРЯДОК ЧТЕНИЯ
1. CURRENT_STATE / PROJECT_HANDOFF — последняя стадия и пользовательские факты.
2. Текущая пользовательская инструкция Gem — рабочие предпочтения, не системный prompt новой платформы.
3. Полные Knowledge01–07 — техническая база с датами источников.
4. Профиль/шаблоны/вопросы поддержке — по необходимости.

Новые сообщения пользовательницы обновляют этот снимок. Если старые исходные модули ещё говорят «GPU неизвестна» или предлагают иной прошлый шаг, используйте актуальный паспорт в начале. Не начинайте ресерч заново и не выдавайте отсутствующие аудио/модели за полученные.
Файл не содержит полную медиабиблиотеку или личное вокальное аудио. Их наличие нужно проверить по реальным вложениям нового чата. Это сборка базы и состояния, не дословный экспорт каждой реплики/каждого tool output.

''']
sections=[('LATEST PROJECT HANDOFF',h),('CURRENT GEM INSTRUCTIONS',G/'GEM_INSTRUCTIONS_CURRENT.txt')]
sections += [(p.name,p) for p in sorted(A.glob('*.txt'))]
for rel in ['CURRENT_PROFILE/MY_VOICE_SETUP_RTX3050.txt','GEM_SETUP/SUPPORT_QUESTIONS_UNSENT.txt','TEMPLATES/SONGS/SONG_PASSPORT_TEMPLATE.md','TEMPLATES/VOICE/VOICE_MODEL_PASSPORT.md','TEMPLATES/VOICE/ONE_TIME_RECORDING_CHECKLIST.md','EXTERNAL_MEDIA_BACKUP.json','PHOTOS/PHOTO_INDEX.md','00_START_HERE.md']:
 if (P/rel).exists():sections.append((rel,P/rel))
source_map=[]
for label,f in sections:
 text=f.read_text(encoding='utf-8-sig')
 parts.append('\n\n'+'='*76+'\nBEGIN SOURCE: '+label+'\n'+'='*76+'\n\n'+text+'\n\nEND SOURCE: '+label+'\n')
 source_map.append({'label':label,'file':f.relative_to(P).as_posix(),'sha256':sha(f),'chars':len(text),'included_completely':True})
master=''.join(parts)
(P/master_name).write_text(master)
(ROOT/master_name).write_text(master)
shutil.copyfile(P/'START_NEW_CHAT.txt',ROOT/'START_NEW_CHAT.txt')
shutil.copyfile(h,ROOT/'PROJECT_HANDOFF.md')
# A quick-access contact sheet outside the ZIP, optional upload to a new chat.
shutil.copyfile(PH/'MIC_CONTACT_SHEET.jpg',ROOT/'MIC_CONTACT_SHEET.jpg')
(P/'MASTER_SOURCE_MAP.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2))

files=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name not in ['FILE_INDEX.json','CHECKSUMS.sha256']:
  files.append({'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)})
(P/'FILE_INDEX.json').write_text(json.dumps({'snapshot':'2026-09-12','active_knowledge_files':7,'master_file':master_name,'external_media':external,'files':files},ensure_ascii=False,indent=2))

# Exact-content checks: each complete source occurs in the combined file; nothing claims new processing.
for label,f in sections:
 assert f.read_text(encoding='utf-8-sig') in master,label
assert len(list(A.glob('*.txt')))==7
assert len(photos)==4
assert len(json.loads((K2/'ASSET_INDEX.json').read_text())['assets'])==70
assert not list(P.rglob('*.wav')) and not list(P.rglob('*.pth')) and not list(P.rglob('*.index'))
assert not list(P.rglob('PART_2_STUDIO_ASSETS.zip'))
for src,dst in zip([ROOT/'uploads'/f'image-{i}.png' for i in range(1,5)],[PH/f'MIC_0{i}.png' for i in range(1,5)]):assert sha(src)==sha(dst)
checks=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name!='CHECKSUMS.sha256':checks.append(sha(f)+'  '+f.relative_to(P).as_posix())
(P/'CHECKSUMS.sha256').write_text('\n'.join(checks)+'\n')
zp=ROOT/'CHAT_RESTORE_2026-09-12.zip'
with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file():z.write(f,P.name+'/'+f.relative_to(P).as_posix())
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None
 assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
 print('RESTORE ZIP:',len(z.namelist()),'files;',round(zp.stat().st_size/1024**2,2),'MiB')
print('MASTER:',len(master),'characters;',round((ROOT/master_name).stat().st_size/1024,1),'KiB;',len(source_map),'complete sources')
print('CURRENT INSTRUCTIONS:',len(ins),'characters')
print('MEDIA SEPARATE:',external['bytes'],'bytes;',external['sha256'])
print('PASS: content completeness, four exact original photos, 70-item media index, ZIP integrity.')
