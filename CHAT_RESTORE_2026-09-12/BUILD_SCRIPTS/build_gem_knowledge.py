from pathlib import Path
import re, shutil, urllib.parse
ROOT=Path('/home/user/suno_gemini_kit'); P1=ROOT/'PART_1_GEMINI'; P2=ROOT/'PART_2_STUDIO_ASSETS'; K=P1/'KNOWLEDGE'; K.mkdir(parents=True,exist_ok=True)
s=Path('/home/user/suno_v6_studio_dark_2026-09-11.md').read_text()

def sec(n):
 m=re.search(r'^### '+re.escape(n)+r'\. .*?(?=^### \d+\.\d+\.|\Z)',s,re.M|re.S)
 assert m,n
 t=m.group(0)
 t=re.sub(r'\n---\n\n## БЛОК[^\n]+\n','\n',t)
 t=t.replace('### '+n+'.', '## REF '+n+'.',1)
 t=t.replace('Russian-language female alto','Russian-language singing using the selected verified Voice')
 t=t.replace('Intimate low-tenor singing','Intimate singing using the selected verified Voice')
 t=t.replace('Russian-language solo female alto','Russian-language singing using the selected verified Voice')
 t=t.replace('my attached voice memo','my own attached voice memo')
 if n=='3.7':t=t.split('#### Два приложенных MIDI-старта')[0]
 for old,new in {'§3.10':'KB03 (Sounds/FX)','§3.7–3.8':'KB03 (MIDI/Wavetable)','§3.6':'KB03 (Keys вместо guitar)','§3.9':'KB04 (локальный vocal repair)','§3.13':'KB03 (три сценария)'}.items():t=t.replace(old,new)
 return t

intro02='''# KB02 — Готовые промпты, sound search и музыкальная архитектура
VERSION:2026-09-11 | Permanent Knowledge for Gemini

ГЛАВНОЕ
Задача Gemini — писать подходящий текущему шагу готовый prompt, а не пересказывать все примеры. Шаблоны ниже — справочные авторские рецепты, не результат прослушивания Gemini. Сначала заполнить контекст песни из KB06, проверить права на sources, выбрать правильную поверхность.
По умолчанию вокал — свой реально выбранный Verified Voice. Не менять его на arbitrary male/female singer из примера. Если профиль не выбран в UI, текст «use my voice» не является доказательством его активации.
Все финальные метатеги и технические указания по-английски. Русский текст — только Lyrics и цитаты редактируемых слов. Не оставлять в финальном prompt незаполненные {BPM}/{KEY}/{TRACK}/{RANGE}. При неизвестном параметре использовать осмысленное Follow the existing tempo/harmony либо задать необходимый вопрос.

ОПЕРАЦИИ
Whole-song Styles: microgenre, groove, timbres, own Voice delivery, form, production.
Simple with references: source → роль → что сохраняем → что меняем → output.
Studio Chat: operation → selected destination/source → range → одна роль → context relation → ограничения результата.
Wavetable patch: изменить instrument/параметры, сохранить MIDI, не генерировать новый audio.
FX: existing audio + реальные эффекты/automation; не regenerate.

ЛИМИТЫ
В ранних v6 UI-наблюдениях Styles1000/Lyrics5000; проверять реальный счётчик. Это НЕ лимит всех сообщений Studio Chat. Лучше короткий конкретный бриф, чем всё сразу. Сложные команды Simple допустимы, но не нужны для одиночного kick.
Для дорожек: «Instrumental» исключает вокал, а не весь ансамбль. «Keys» в имени не фиксирует физический инструмент. «Dark organic» не равно «tine electric piano».

ПОРЯДОК ВЫДАЧИ
Один основной prompt. Если пользователь просит варианты — точный A и исследовательский B с объяснением одного различия. Настройки UI отдельно, не в кодблок Style. Для Create явно отдельные Styles / Lyrics / Exclude.

СЛОВАРЬ ПОД СВОЙ VOICE
intimate Russian-language singing; clear consonants; conversational melodic phrasing; restrained vibrato; preserve the selected verified Voice; breath-led but intelligible; exposed lead vocal; tension through phrasing and silence.
Припев не обязан быть loud belt. Не добавлять автоматически anthemic/radio-ready/powerful choir.

'''
body02='\n\n'.join(sec(x) for x in ['2.4','2.5','2.6','2.7','2.8','3.4','3.5'])
addon02='''
# SOUND_SEARCH — Splice и похожие каталоги

Это способ подбирать звук, а не разрешение использовать чужой sample как AI-source. Для Splice действуют правила KB06: текущие Terms запрещают source/training use в AI, не только Custom Model training. Default — поиск/метаданные/описание + лицензированное локальное использование в DAW; не upload в Suno/Gemini без отдельного разрешения.

## Разбор переданного пользователем URL
Ссылка из запроса содержала filepath=indie+rock и два instrument/genre tags. При чтении страницы 11.09.2026 активными были «indie rock» и «synth». Это выдача синтезаторов в таком контексте, НЕ гарантия electric piano и НЕ запись выбранного sample.
Для synth texture ссылка подходит. Если задача — конкретно keys/tine electric piano, менять/уточнять instrument filter, а не считать любой результат «клавишами». Не запоминать число результатов навсегда и не выдумывать смысл незнакомого UUID-тега.
https://splice.com/sounds/search/samples?filepath=indie+rock&tags=d5b91338-6269-4dde-9448-e1dbc3cf1ac5&tags=25a795c8-3a2b-427f-9f4e-30c20bb39f1a

## Как отвечать на «найди мне звук»
1. Роль: kick/snare/keys/pad/sub/counterline/FX/целый loop.
2. Нужен One Shot или Loop? One-shot обычно не надо искать по BPM. Для melodic loop важны key и гармония.
3. Дать3–5 английских search queries от конкретного к более широкому.
4. Предложить filters: instrument/type, One-Shot/Loop, BPM range, key при необходимости.
5. Если есть реальный доступ к выдаче — показать до3 кандидатов с названием/URL/метаданными, статусом «не прослушано» при отсутствии audio. Не выдумывать pack, sample filename или availability.
6. Если доступа нет — дать query/filters и попросить shortlist или описание пользователя; не притворяться, что просмотрена приватная библиотека.
7. Пользователь штатно лицензирует/скачивает; Certified License хранит у себя. Preview не равен лицензированному источнику.
8. Решить маршрутизацию: local DAW sample placement либо разрешённый original generative reference. При Splice не предлагать exact AI-реконструкцию sample как обход запрета.

## Полезные запросы (не обещание наличия результатов)
Keys: dry tine electric piano / sparse electric piano chords / muted keyboard stabs / felt piano sparse.
Pads: coldwave synth pad / thin glass synth chords / darkwave analogue pad / unstable synth texture.
Bass: mono sine sub / dark synth bass pulse / picked post punk bass / minimal bass notes.
Drums: dry trip hop drums / sparse broken drum groove / short punchy kick / dry rim snare.
Organic: dry wood percussion / muted hand percussion / brush scrape / tactile percussion.
Electric: relay click / electrical crackle / short circuit / wire scrape / metallic ticks.
Guitar: post punk single note guitar / muted electric guitar / tremolo guitar counterline / wiry guitar texture.
Не вводить phonk/trap/rap как жанровые ориентиры. Если встречаются в выдаче — это не повод менять цель.

## Metadata worksheet для кандидата
CandidateID, URL, filename_if_visible, pack_if_visible, instrument, one-shot/loop, BPM, key/root, duration, source_of_each_fact, what_user_likes, what_user_rejects, intended_track, license_status, AI-source_permission.
Условия audio/midi/plugin-specific проверяются отдельно. Preset для Serum/другого synth не является Suno Wavetable preset. Splice VST/AU plugin не устанавливается в Suno Studio.

## Как переводить описание звука в собственный prompt
Работать с общими музыкальными признаками, не копировать конкретный чужой sample/melody/voice.
«Хлёсткий ток» → short dry electrical crack, hard transient, brief noisy tail.
«Клавиши как стекло» → glassy synthetic keyboard, thin attack, sparse high-register chords.
«Органика» → tactile dry percussion, wood-like knocks, irregular small gestures; это не обязательная guitar.
«Плотный саб» → sine-based mono sub, stable pitch, restrained harmonics, space around kick.
«Инди-поэзия» → clear Russian diction, conversational melodic phrasing, gaps around words.
В промпте для одной дорожки не перечислять другие инструменты как желаемый состав.

## Готовый ответ для сценария Splice без аудио
«По ссылке вижу поиск/фильтры, не слышу выбранный sample. Для твоей роли предлагаю такие queries/filters… Если понравится конкретный звук, используй лицензированную копию локально в DAW. Для generative Suno-reference возьмём original из нашего набора либо твою запись. Из библиотеки: M01 для редактируемых keys или L04 для готового synthetic-keyboard звука».

## Примеры дополнительных коротких команд
### Сохранить настоящую исходную запись
```text
Generate a new accompaniment part on the selected empty track. Use my original recording only as timing and harmonic context. Do not transform or replace that recording. Return only the requested instrument and leave existing clips unchanged.
```
Это намерение команды; самое надёжное сохранение original — физически не выбирать его целью генерации и проверить фактическое действие.
### Точная смена тембра MIDI
```text
Keep the selected MIDI notes unchanged and alter only the instrument preset. Use a restrained synthetic electric-keyboard tone with a short attack. Do not generate an audio cover or a new melody.
```
### FX без перегенерации
```text
Use effects and automation only on the selected track. Preserve its performance and timing. Do not create new audio clips or change the arrangement.
```

## Source context и negatives
Только один источник-инструмент не гарантирует чистую генерацию: bleed и модельная интерпретация возможны. Exclude useful, но не hard audio mute. Если он недоступен в Studio-операции, допустимо явно ограничить output в sentence, не изображая скрытый переключатель.
My Taste/Variety фиксировать при тестировании. Style Influence50 не означает50%удалённого текста. После двух неудачных пар изоляции сменить метод на MIDI, другой source, One Shot или осмысленный Split, а не удлинять prompt.
'''
(K/'02_PROMPTS_AND_SAMPLE_SEARCH.txt').write_text(intro02+body02+addon02)

intro03='''# KB03 — Studio: выбор операции, конкретные файлы и доведение проекта
VERSION:2026-09-11

СТАТУС ДОСТУПА
Gemini пишет команды и инструкции. Без реального инструмента управления он не выбирал дорожку, не загрузил WAV и не нажал Create. Каждый совет привязывать к реальному selection пользователя.
Постоянно различать:
AUDIO INPUT: WAV/MP3 на Audio track.
MIDI INPUT: .mid на MIDI track + Wavetable/совместимый инструмент.
RECIPE: R*.txt читать/копировать команду, не импортировать как preset.
GM DRUM MIDI: M09/M10 только с drum sampler/mapping; в обычном Wavetable получится мелодический synth, не kit.
SCENE MIX: S01/S02/S03 содержат несколько частей; это reference sketch, не отдельный instrument stem.
VOICE PROFILE: выбирается в штатной Voice-функции; ни один аудиофайл нашего набора не является человеческим Voice training sample.

ПРАКТИЧЕСКАЯ КАРТА
Keys с редактируемыми notes → M01 + R03 на MIDI track; быстрый Audio-tone → L04.
Sub notes → M02 + R01; Audio sub → L03.
Drums в Suno → L01 или D01/D02/D04 на Audio. M09 для DAW, не обязательный шаг.
Machine percussion → L02/отдельныеF01,D10,D09. Effects→R05.
Em102 → M03/M04 либо L09/L08; при необходимости synthetic stringL10/M07.
F#m100 → M05/M11, L11; клавишная/падающая окраска R04.
Vocal repair → свой approved vocal, R06/R08; внешняя доработка R07.
Все точные пути искать в KB05; имена не сокращать при указании «какой файл перетащить».

ПРАВА
Перед новым external source прочитать KB06. Splice звучание не отправляется автоматически в AI. Если нужен лицензированный Splice sample — локальная DAW, не генеративное преобразование в Suno.

'''
body03='\n\n'.join(sec(x) for x in ['3.1','3.2','3.3','3.6','3.7','3.8','3.10','3.12','3.13','3.14','3.16'])
body03=body03.replace('Импортируй приложенные KEYS/BASS MIDI','Импортируй M01/M02 из каталога KB05')
body03=body03.replace('приложенные KEYS/BASS MIDI','M01/M02 из KB05')
addon03='''
# ПРАВИЛА ИМПОРТА ИЗ НАШЕГО ПАКЕТА

## WAV one-shot
1. Найти файл по ID в PART_2/AUDIO.
2. Перетащить на AUDIO-дорожку, не в Wavetable preset slot.
3. Поставить в нужную точку и уменьшить уровень для первого прослушивания.
4. Повторы делать копированием, варьируя громкость/тайминг осмысленно.
5. Слишком короткий one-shot может не подходить любому Create-reference режиму. Прямой playback в Studio и audio conditioning — разные задачи. Не растягивать щелчок в Voice training source.

## WAV loop
1. Проверить nominal BPM/key/bars по каталогу и filename. В WAV не обещаны BPM-теги, которые автоматически прочтёт Studio.
2. Для совпадающего проекта поставить к общей первой доле, прослушать loop boundary.
3. Для другого BPM использовать подходящий Stretch/warp-процесс, если необходимо сохранить pitch. Speed/transpose — другая операция.
4. Математика для проверки: новая длительность = исходная длительность × BPM_source / BPM_target. Это расчёт, не название обязательной ручки UI.
5. Для key изменения выбрать минимальный осмысленный transpose; сложную аккордовую последовательность нельзя всегда адаптировать одним сдвигом. При точной harmony перейти к MIDI.
6. Края/ноты/хвосты проверять в context; «4 bars» не обещает идеальный бесшовный loop в любом монтаже.

## MIDI melodic
1. + Track → MIDI; Wavetable должен быть загружен как instrument.
2. Импортировать M-файл с общего start; по необходимости вручную поставить BPM.
3. Выбрать подходящий preset/применить рецепт.
4. MIDI note numbers надёжнее неодинаковых названий октав в DAW.
5. Проверить notes, velocity, gating/release и диапазон. Ноты контролируются напрямую, но envelope/glide/polyphony меняют слышимое исполнение.
6. Для MIDI-to-audio generation — отдельная операция, снова вероятностная. Не называть её sample-accurate сменой тембра.

## Рецепт
R-файл открыть текстом. Он указывает реальную цель и английскую команду. Никакого импорта этого TXT как .vst/.fxp/.mid/.wav. Если нужны настоящие native preset-файлы, получить/экспортировать их из совместимого приложения, а не переименовать расширение.

## Scene sketch
S01/S02/S03 — full instrumental idea. Можно слушать как пример распределения ролей, использовать допустимый original reference или Audio layer с осознанием полного состава. Нельзя сказать «S01 это solo piano» или одновременно оставить его вместе со всеми воспроизводимыми компонентами без контроля удвоения.

# МИНИМАЛЬНАЯ СЕССИЯ С МОИМ VOICE
1. Создать отдельную учебную сессию96BPM/4-4/Dminor или использовать реальные параметры текущей песни.
2. M01→MIDI_KEYS→R03. M02→MIDI_SUB→R01.
3. L01→Audio_DRUMS (без M09). При необходимости L02→Audio_PERC.
4. Выбрать свой настоящий Verified Voice в доступном Create/workflow и создать/получить approved lead; затем импортировать/открыть его в Studio. Не подменять выбор профиля словом female.
5. F02 поставить только в нужных паузах; не включать весь набор одновременно.
6. Выбрать одну следующую проблему и исправить её. Gemini выдаёт один конкретный prompt, а не новую песню на каждом шаге.
7. Dm96 — лишь учебный стенд. Не менять без спроса реальную песню под заготовку.

# ГРАНИЦЫ ИЗОЛЯЦИИ
Не обещать «mute исключает дорожку из AI-контекста во всех операциях». Если контекст неясен — явные источники при доступности, либо отдельная чистая copy session с минимальными guide clips.
Если новый take похож на full song: сначала solo и проверка source/destination; не начинать с увеличения Max. Если музыка полезная, можно осмысленно разделить; если идея неудачна, split не исправит её.
Если в source есть Splice/другая библиотека с запретом AI-source, не предлагать reupload/AI split автоматически. Использовать разрешённый local-only процесс.

# ПЕРЕДАЧА В REAPER ИЛИ ДРУГУЮ DAW
Проверить, что это действительно нужно. Экспортировать approved stemsWAV+MIDI отдельно, с одинаковым start/end. В DAW не включать незаметно tempo-match из Media Explorer, если нужна нетронутая временная структура. Reference прослушивать отдельно, не суммировать со всеми stems. Указать пользователю собственные плагины/native FX; Suno не хостит VST/AU.
Обычные задачи: performance comping, pitch/timing edits, точечный gain/de-essing, более полные измерения. Реставрация не отменяет необходимости заменить необратимо испорченный source. См.KB04/R07/R09.
'''
(K/'03_STUDIO_AND_IMPORT.txt').write_text(intro03+body03+addon03)
shutil.copyfile(Path('/home/user/_work/dark_kit/knowledge_catalog.txt'),K/'05_ASSET_CATALOG_AND_RECIPES.txt')
for p in sorted(K.iterdir()):print(p.name,len(p.read_text()),'chars')
assert len(list(K.glob('*.txt')))==6
