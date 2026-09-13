from pathlib import Path
import csv,json,re
P=Path('/home/user/VOICE_ADDON_2026-09-12');P.mkdir(exist_ok=True)
T=P/'TEMPLATES';T.mkdir(exist_ok=True)
p=P/'07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt'
s=p.read_text()
lines=[]
for line in s.splitlines():
 if 'http' not in line:
  line=re.sub(r'(?<=[А-Яа-яЁё])(?=[A-Za-z])|(?<=[A-Za-z])(?=[А-Яа-яЁё])',' ',line)
  for a,b in [('release3.6.4','release 3.6.4'),('20–40sec','20–40 sec'),('15–30min','15–30 min'),('3.6.4только','3.6.4 только'),('200–400epochs','200–400 epochs'),('conversionhistory','conversion history'),('customvoice','custom voice'),('voiceclone','voice clone'),('60min/month','60 min/month'),('fullsound','full sound'),('WindowsVST3','Windows VST3'),('16-bit→24-bit','16-bit → 24-bit')]:line=line.replace(a,b)
 lines.append(line)
p.write_text('\n'.join(lines)+'\n')
patch='''

ДОПОЛНЕНИЕ 12.09.2026 — KB07
Используй 07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt для внешней конвертации голоса и выбора дополнительных инструментов. Мой приоритет: удачная партия → собственный тембр, одна песня в месяц, по возможности без новых платежей; Windows с NVIDIA, точная GPU/VRAM пока неизвестны. Сначала проверяй уже доступный Suno Voice и бесплатный локальный путь; не навязывай подписки. Training делается на моих настоящих записях, inference — отдельно для каждой партии. Для Suno Output → другой AI сначала проверяй договорный статус из KB07; оплата Premier не означает автоматическое разрешение. Локальность не снимает ограничения лицензии. Kits замораживает свои модели после отмены, а минуты сгорают по окончании периода. Не обещай бесплатный доступ к клону навсегда или перенос Kits/Suno модели в Applio. Для Applio сначала выясни GPU/VRAM/dataset и версию; затем используй проверенные в KB07 поля, не выдуманные пресеты. Стихи и тренды пока отложены. Старый каталог музыкальных файлов не меняется.
'''
(P/'GEM_INSTRUCTIONS_APPEND.txt').write_text(patch.strip()+'\n')
base=Path('/home/user/suno_gemini_kit/PART_1_GEMINI/GEM_INSTRUCTIONS.txt').read_text()
full=base.rstrip()+patch
assert len(full)<8000,(len(base),len(full))
(P/'GEM_INSTRUCTIONS_FULL_V2.txt').write_text(full)
(P/'00_HOW_TO_ADD.md').write_text('''# Дополнение: голос и дополнительные инструменты
**Версия: 12 сентября 2026.** Это расширение уже установленной базы, не новая обязательная подписка.

## Добавить в существующий Gem
1. Распакуй VOICE_ADDON_2026-09-12.zip.
2. В Gemini открой свой существующий Gem → Edit.
3. В Knowledge добавь **только 07_VOICE_CONVERSION_AND_EXTRA_TOOLS.txt**. Предыдущие шесть файлов оставь. Теперь источников семь.
4. В поле Instructions:
   - если свои инструкции ты ещё не меняла — можно заменить их содержимым **GEM_INSTRUCTIONS_FULL_V2.txt**;
   - если уже дописывала собственные правила — сохрани их и добавь в конец **GEM_INSTRUCTIONS_APPEND.txt**. Не вставляй одновременно обе версии.
5. Нажми Save/Update.
6. Для чистой проверки начни разговор с обновлённым Gem и отправь CHECK_ADDON.txt. Для своей текущей песни возьми сохранённый паспорт — пересоздавать музыку не нужно.

Это тот же обычный custom Gem. Не создавать Labs mini-app. ZIP с установщиками/весами не загружать; в этом дополнении их вообще нет.
Официальная процедура редактирования/Knowledge: [1](https://support.google.com/gemini/answer/15235603?hl=en).

## Что добавлено
- Kits: Instant/Professional, текущие тарифные оговорки, заморозка моделей и потеря минут после окончания подписки.
- Applio: локальное обучение своего голоса и конвертация, Windows/NVIDIA, разовая подготовка датасета.
- Поля inference проверены по исходному коду Applio3.6.4; спорные подписи Protect разобраны отдельно.
- Дополнительные инструменты по задачам: UVR, Audacity, T-De-Esser2, Bertom Denoiser Classic, Graillon Free, REAPER; облачные Kits/Audimee/LALAL сравниваются по реальному доступу и расходам.
- Gate прав для стороннего AI-use Suno Output, готовые вопросы поддержке.
- Форма железа/датасета, паспорт модели, матрица тестов и разовая запись.

## Что не меняется
Пакет PART_2_STUDIO_ASSETS и все70IDs остаются прежними. Ничего повторно скачивать/загружать в музыкальную библиотеку не нужно. В этом дополнении нет настоящей модели твоего голоса, конвертированного вокала или программы Applio.

## Следующий шаг
Открой FIRST_VOICE_MESSAGE.txt, добавь известные сведения и отправь в чат своей песни. Перед подбором точной конфигурации нужны название NVIDIA и VRAM, а также состояние реальных вокальных записей.

## Обязательная честность
Документальный ресерч и проверка полей кода выполнены; на твоём компьютере ничего не устанавливалось, модель не обучалась, аудио не конвертировалось. Условный технический маршрут Suno→внешнийAI не выдаётся за подтверждённое договорное разрешение. В SUPPORT_QUESTIONS.txt есть точный запрос Suno.

Стихи/актуальные темы пока отложены по твоему выбору. Это дополнение только про голос и доработку.
''')
(P/'FIRST_VOICE_MESSAGE.txt').write_text('''Подключён KB07. Работаем с текущей песней и её паспортом.

Хочу сохранить удачную вокальную мелодию и подачу, но получить мой узнаваемый тембр. Дополнительные подписки по возможности не нужны. У меня Windows и NVIDIA.

Точная GPU и VRAM: пока уточню.
Мои сухие реальные записи для обучения: укажу, сколько есть и какого качества.
Исходник для конверсии: укажу — собственная запись / Suno output / другой материал.
Право использовать этот source во внешнем AI: пока уточняется, если это Suno output.

Сначала установи, что уже есть, и задай максимум три необходимых вопроса. Раздели разовое обучение голоса и обработку новой партии. Не придумывай готовую модель или настройки обучения без данных о железе. Для Kits/Applio выдай карту input/target/параметров/действий, а не prompt для несуществующего поля. Начнём с одной короткой проверочной фразы, когда prerequisites и права будут ясны.
''')
(P/'CHECK_ADDON.txt').write_text('''Проверка обновления Gem. Ответь коротко по KB07:
1. Можно ли бесплатно скачать свой преобразованный вокал из Kits Free?
2. Что происходит с Kits-моделью и накопленными download minutes после окончания подписки?
3. Почему «один раз обучить модель» не равно «один раз обработать все будущие песни»?
4. Что нужно узнать о моей NVIDIA до выбора training batch/settings?
5. На каких моих записях нужно обучать Applio? Подходит ли для этого synthetic Suno Voice output автоматически?
6. Разрешает ли сам факт Premier автоматически использовать Suno lead в стороннем AI-конвертере?
7. Куда относятся .pth и .index? Можно ли импортировать их в Wavetable или Knowledge как голос?
8. Допустим ли Protect0.7 в audited Applio3.6.4? Что особенного в значении0.5 в pipeline?
9. Надо ли автоматически сдвигать Pitch на октаву «по полу»?
10. Менялась ли наша музыкальная библиотека и добавлены ли сейчас стихи/тренды?

Ожидаемые смысловые ответы для самопроверки:
1 Нет полноценного бесплатного download по текущим условиям.
2 Модель не удаляется, но недоступна доrenewal; минуты теряются приexpiry и не восстанавливаются.
3 Новая партия каждый раз требует inference; локально нет платы сервису, но есть compute/time.
4 GPU model,VRAM,RAM,version/driver,dataset; не просто «есть NVIDIA».
5 На реальном собственном допустимом аудио, не автоматически на Suno Output.
6 Нет автоматического подтверждения; учитывать clause10 и уточнять уSuno.
7 Это model/index для Applio; не Audio/MIDI/preset Suno и не профиль Gem.
8 Диапазон0…0.5; при0.5 не выполняется дополнительная protective blend-ветка описанного pipeline. Проверка относится к3.6.4.
9 Нет: baseline0; плюс повышает, минус понижает; учитывать музыкальную задачу.
10 Библиотека70IDs прежняя; поэзия/тренды отложены.

Это acceptance checklist, не утверждение, что твой Gem уже прошёл проверку.
''')
(T/'GPU_AND_DATASET_FORM.md').write_text('''# Перед первым локальным обучением

- Windows version:
- NVIDIA model:
- Dedicated GPU memory / VRAM:
- RAM:
- Free disk space:
- NVIDIA driver (если известно):
- Applio installed? Version:
- Minutes of clean real own singing:
- Source recording format:
- Reverb/background music/other voices/clipping:
- Intended conversion source:
- Rights status of source for external AI:

Как найти GPU: Ctrl+Shift+Esc → Performance → GPU. Достаточно модели и выделенной памяти. Пароли, ключи лицензий, серийные номера и персональные документы не нужны.

NVIDIA сама по себе не доказывает, что любая training-конфигурация совместима. Пока эти поля unknown, помощник не должен обещать время обучения или точный batch.
''')
(T/'ONE_TIME_RECORDING_CHECKLIST.md').write_text('''# Записать собственный голос один раз для модели

Цель: 10–30минут полезного сухого реального аудио, а не обязанность перепевать будущие песни каждый месяц. Ориентир соответствует Applio docs; для Kits Professional также проверять текущие требования.

## До записи
- [ ] Только мой настоящий голос и материал с необходимыми правами.
- [ ] Тихое помещение, минимум room echo/вентилятора/музыки.
- [ ] Одна певческая линия, без гармоний и doubles.
- [ ] Без reverb,chorus,сильного autotune/denoise и clipping.
- [ ] Несколько секунд теста прослушаны до длинной записи.
- [ ] Raw-файлы сохраняются отдельно от processed copies.

## Содержание записи — ориентир
- Удобный средний регистр и обычная певческая манера.
- Русские гласные и согласные, короткие и длинные слова.
- Удержанные гласные, небольшие мелодические переходы.
- Более тихое и более эмоциональное исполнение, если оно реально нужно.
- Верхний/нижний удобный регистр без форсирования. Делать перерывы.

## Небольшие оригинальные фразы для проверки дикции
«В тихой комнате гаснет свет».
«Я слышу шаги за закрытой дверью».
«Шорох ветра касается стекла».
«Не торопись: у нас ещё есть время».
«Это мой голос, мой ритм и мой выбор».

Это короткие учебные фразы для записи, не новый раздел про стихи и не обязательный текст будущей песни. Можно заменить своими словами/мелодиями.

## Подготовка
- Убрать кашель, посторонние шумы, неудачные перегруженные куски и длинную тишину.
- Не обрезать начала согласных и не удалять все естественные дыхания.
- Не сделать голос «водяным» агрессивной очисткой.
- Export lossless WAV/FLAC; сохранять raw originals.
- Частота training/pretrained/vocoder должна совпадать по выбранной конфигурации; не выбирать максимальное число вслепую.

ВАЖНО: эти операции относятся к TRAINING DATA. Вход готовой песни для inference нельзя автоматически Truncate Silence — нужна временная привязка к аранжировке.

Ни одного WAV с твоим настоящим голосом или обученного .pth в этом дополнении нет. Их предстоит подготовить на твоём компьютере.
''')
(T/'VOICE_MODEL_PASSPORT.md').write_text('''# VOICE_STATE / LOCAL_MODEL — личный паспорт

- Song ID:
- Route: Suno-native / Applio-local / Kits / Audimee / traditional-DSP
- Target identity: мой собственный голос
- Real training dataset source and rights:
- Clean duration:
- Raw/prepared folder paths:
- App and version:
- GPU / VRAM / RAM:
- Model sample rate / vocoder / embedder:
- Selected checkpoint and reason:
- Exported inference .pth path: NOT CREATED / указать реальный
- Matching .index path: NOT CREATED / указать реальный
- Model backup path:
- Conversion source filename and origin:
- Source rights for external AI: unknown / clarification-needed / confirmed / not-permitted
- Source timing origin:
- Test excerpt:
- Baseline settings:
- Approved A/B variant:
- Full output filename:
- Alignment, diction and likeness checked:
- Cloud subscription/expiry (если применяется):
- Current extra budget:
- Next one action:

Пути не означают, что файлы прикреплены в Gemini. Не загружать веса модели/личные записи в публичный shared Gem. Модель Suno/Kits не считать автоматически portable .pth.
''')
with (T/'VOICE_AB_TEST_PLAN.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['run','status','relative_to','change','pitch','index_rate','volume_envelope','protect','f0_method','autotune','clean_audio','formant_shifting','post_process','source_excerpt','actual_output','likeness','diction','artifacts','decision'])
 for row in [
  ['A','PLANNED','none','baseline 3.6.4',0,.75,1,.5,'rmvpe','off','off','off','off'],
  ['B','PLANNED','A','protect only',0,.75,1,.33,'rmvpe','off','off','off','off'],
  ['C','PLANNED','A','protect only',0,.75,1,.2,'rmvpe','off','off','off','off'],
  ['D','PLANNED','A','index only',0,.5,1,.5,'rmvpe','off','off','off','off'],
  ['E','PLANNED','A','envelope only',0,.75,.5,.5,'rmvpe','off','off','off','off']]:w.writerow(row+['']*6)
(P/'SUPPORT_QUESTIONS.txt').write_text('''Готовые вопросы. Письма НЕ отправлены. Отправлять вручную, если выбран соответствующий сценарий.

SUNO — отдельная сторонняя AI voice conversion
Адрес поддержки: support@suno.com / официальный Help Center.

I am a Premier subscriber and would like clarification on Conditions of Access and Use, clause 10.
I want to take a permitted WAV download of a lead vocal from my own Suno project and use a third-party voice-conversion tool, such as Kits AI or locally running Applio/RVC, to render that existing vocal performance in my own voice.
The third-party voice model would be trained only on my own real recordings. I would not use Suno Output or a Suno Voice Model as training data.
Does your current agreement allow this inference-only, individual post-production use of my permitted Output? Does your answer differ for a local tool versus a cloud service? May I commercially release the resulting song, subject to the usual rights requirements?
Please distinguish this from training or improving a competing model/service. I would appreciate written confirmation for this specific workflow.

KITS — план, заморозка, переносимость
Форма: https://help.kits.ai/hc/en-us/requests/new

I make about one song per month and want to use a clone of my own singing voice.
Your current Starter card lists Professional Voice Cloning, while the FAQ describes Starter with Instant Cloning and lists Professional Cloning for Producer. Which cloning methods are actually included in the current month-to-month Starter plan for my account, and what is the total monthly charge?
I understand that custom models become unavailable and unused download minutes expire when a subscription ends. Please confirm how this applies to my account.
Do you offer any one-time option that allows continued conversion with my own custom model without an active subscription? Can a model trained inside Kits be exported for local inference, and in what supported format? An option to upload .pth models would not by itself answer the export question.
Please also confirm the licence that applies to the results I download while subscribed and use after cancellation.

AUDIMEE — только если выбираем облачную альтернативу
Использовать официальный contact/FAQ, не оплату по неверно понятой годовой цене.

I need one custom singing-voice model for roughly one song per month. What is the current month-to-month price, without annual billing? What access to my trained voice remains after cancellation or downgrade to Free? Are there any one-time credits or model-export options that work without an active subscription?

Не включать в сообщение пароли, ключи, личные документы или сами закрытые голосовые модели. При необходимости приложить только минимально нужный разрешённый пример по запросу поддержки.
''')
# Human/machine-readable purchasing checklist with no invented monthly Audimee rate.
with (P/'TOOLS_AND_COSTS.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['tool','role','pricing_type','snapshot','important_limit','primary_url','verified_date'])
 rows=[
 ['Suno Voice + Studio','native own voice / editing','already paid','existing Premier','not a promise of exact identity each take','https://help.suno.com/en/articles/13924481'],
 ['Applio','local train + voice conversion','free software','no provider subscription','GPU/setup/data needed; rights still apply','https://applio.org/'],
 ['UVR','local separation','free software','no provider minutes','not voice cloning; ML source rights apply','https://ultimatevocalremover.com/'],
 ['Audacity','record/edit/cleanup','free software','offline basic editor','not universal artifact repair','https://www.audacityteam.org/features/noise-reduction/'],
 ['T-De-Esser 2','sibilance','free plugin','personal/commercial per FAQ','requires compatible host, not Suno VST slot','https://techivation.com/t-de-esser/'],
 ['Bertom Denoiser Classic','noise reduction','PWYW including zero','plugin','requires host; not a clone','https://bertomaudio.com/denoiser-classic.html'],
 ['Graillon Free','pitch correction','free edition','plugin','not identity cloning','https://www.auburnsounds.com/products/Graillon.html'],
 ['REAPER','DAW','trial then licence','$60 eligible discounted / $225 commercial, taxes extra','60-day evaluation, not forever free','https://www.reaper.fm/purchase.php'],
 ['Kits','cloud clone + conversion','subscription','$10 / $30 / $60 month cards','Free0downloads; models frozen and minutes lost after expiry; cloning entitlement conflict','https://www.kits.ai/pricing'],
 ['Audimee','cloud singing conversion','subscription','Starter $9/month equivalent, $108 billed yearly','Free0customslots; monthly-only rate not verified here','https://audimee.com/pricing'],
 ['LALAL.AI','cloud stems and tools','subscription + top-ups','$9.99 / $19.99 monthly FAQ','Free preview only; top-up not proven permanent standalone access','https://www.lalal.ai/']]
 for row in rows:w.writerow(row+['2026-09-12'])
print('Created addon files. Full instructions:',len(full),'characters; KB07:',len(p.read_text()),'characters')
