from pathlib import Path
import json,csv,hashlib,re
ROOT=Path('/home/user/suno_gemini_kit'); P2=ROOT/'PART_2_STUDIO_ASSETS'; WORK=Path('/home/user/_work/dark_kit')
a=json.loads((WORK/'assets_media.json').read_text())
recipes=[
('R01','Wavetable_Clean_Sub','Bass',['M02','M04','M11','L03'],'''КУДА: Studio → выбранная MIDI-дорожка → Wavetable. Не импортировать этот TXT как preset.
ЗАЧЕМ: устойчивый моно-саб; не менять уже написанные ноты.
ШАГИ: сначала импорт MIDI; выбрать дорожку; открыть Wavetable/Chat; применить описание; проверить register и mono. Если нужен более слышимый бас на маленьких динамиках — немного гармоник, а не обязательно больше громкости.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only the Wavetable preset on the selected MIDI track. Use a monophonic sine-based sub with a click-free fast attack, restrained harmonics and a short release. Keep the low end centered and disable wide unison. Preserve every MIDI note and do not generate audio or additional tracks.
ПРОВЕРИТЬ: правильные корни; нет лишних октав; bass не перекрывает kick; длины release не съедают паузы.
'''),
('R02','Wavetable_Bass_Edge','Bass',['M02','N01'],'''КУДА: дубликат MIDI-баса, отдельная дорожка BASS_EDGE, НЕ основной BASS_SUB.
ЗАЧЕМ: электрическая агрессия в середине при устойчивом чистом сабе.
ШАГИ: продублировать MIDI; на копии выбрать более богатый спектром патч; добавить Distortion и EQ; срезать конкурирующий низ по слуху; подмешать тихо. Это не обязательная цепь на весь mix.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only the sound on this duplicate MIDI track into a restrained gritty mid-bass layer. Preserve the note pattern. Use moderate distortion and reduce its lowest frequencies with EQ so the original sub remains the foundation. Do not alter the original bass track or generate a new musical part.
ПРОВЕРИТЬ: solo и сумма; mono; при bypass громкость сравнима; нет дополнительной мелодии.
'''),
('R03','Wavetable_Synthetic_Keys','Keys',['M01','M03','M08','L04','L09'],'''КУДА: MIDI-дорожка с Wavetable. Это рецепт, не .vst/.fxp/Suno preset.
ЗАЧЕМ: синтетические electric keys вместо случайной гитары в аудиогенерации.
ШАГИ: импортировать M01/M03; выбрать полифонический клавишный patch; короткий ясный attack; decaying body; без glide; оставить места под свой Voice.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only this Wavetable preset into a soft synthetic electric-keyboard sound with a short hammered attack, warm filtered body and moderate decay. Keep polyphony for the written chords, no glide and restrained width. Preserve all MIDI notes. Do not create an audio cover or a guitar part.
ВАЖНО: Wavetable не библиотека сэмплированного рояля. Для реалистичного acoustic piano — подходящий инструмент в DAW или собственная запись.
'''),
('R04','Wavetable_Glass_Pad','Pad',['M05','M06','M12','L05','L11'],'''КУДА: выбранная MIDI-дорожка Wavetable, затем automation.
ЗАЧЕМ: хрупкая верхняя фактура, не мешающая сабу и русским согласным.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Design a thin glassy Wavetable pad on the selected MIDI track. Use a slow attack, restrained low frequencies and gentle wavetable movement. Keep the written pitches and rhythm. Do not generate new audio, melodies, bass or voices.
РУЧНОЙ КОНТРОЛЬ: если нужно напряжение, вписать нужный интервал в MIDI; немного detune только на texture-слое; автоматизировать volume/cutoff. Не вводить число процентов как мета-тег Lyrics.
ПРОВЕРИТЬ: согласные lead слышны; tails не заполняют задуманные остановки; в mono слой не исчезает.
'''),
('R05','Studio_Electric_Perc_FX','FX',['L02','L06','F02','F03'],'''КУДА: Audio-дорожка PERC_MACHINE или FX_ELECTRIC → штатные эффекты.
ЗАЧЕМ: усилить электрическую фактуру без новой музыкальной генерации.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Process the selected percussion track using effects only. Add restrained distortion, shape the tone with EQ and use a short delay that follows the project tempo. Match the output level to the bypassed signal. Do not generate, replace or rearrange audio clips.
ПРОВЕРИТЬ: не превратить каждую паузу в непрерывный шум; не усиливать верх до болезненной резкости; сравнить громкость с bypass.
'''),
('R06','Own_Voice_Studio_Clarity','Vocals',[],'''КУДА: выбранная Audio-дорожка с собственным approved Voice, на копии проекта/дорожки.
ЗАЧЕМ: сведение, а не подмена личности певца.
ПОРЯДОК: сначала уровень фраз/automation; затем умеренный EQ и Compressor; потом очень дозированное пространство. Неправильное слово не исправится эквалайзером — нужен локальный edit/Replace или настоящий дубль.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Process the selected lead-vocal track using effects and level automation only. Preserve the existing singer, words and performance. Keep the voice close and intelligible, reduce obvious tonal harshness gently and control uneven phrase levels. Do not regenerate the vocal, add harmonies or change other tracks.
ОГРАНИЧЕНИЯ: не заявлять встроенный de-esser или Melodyne-подобный редактор как доказанную штатную функцию Studio. Если точечного ремонта не хватает — R07.
'''),
('R07','Own_Voice_REAPER_Cleanup','Vocals',[],'''КУДА: дополнительная локальная DAW REAPER, только если пользовательница согласна. Не Suno plugin slot.
REAPER: полноценная 60-дневная оценочная версия; далее требуется подходящая лицензия, это не обещание вечной бесплатности. https://www.reaper.fm/download.php
ПОРЯДОК: импорт общего stereo reference и stems с одинакового старта; отключить ненужный auto tempo-match; сохранить исходник; править на копии.
1. Item gain/volume automation для скачков фраз.
2. ReaEQ — убрать ненужный гул/тональный перекос, не вырезать жизнь из всего верха.
3. ReaComp — мягкий контроль динамики, сравнение при одинаковой громкости.
4. Свистящие: локальное уменьшение gain, либо настроенный de-essing/multiband инструмент (например ReaXcomp) по реальной записи.
5. ReaTune/похожий редактор — только для реально неверных нот, осторожно с переходами и узнаваемостью.
6. ReaFIR Subtract — только при стационарном шуме и подходящем noise-only участке. Не обучать noise profile на всей вокальной фразе и не объявлять это универсальным удалением AI shimmer.
7. Финальные fades, проверка стыков, небольшие Delay/Reverb по необходимости.
Если фонемы разрушены, фаза плавает или вокал стал другим человеком — лучше заменить проблемную фразу/записать её, чем усиливать denoise.
Это текстовый маршрут, а не готовый импортируемый FX-chain. Чужие sample-ограничения по AI сохраняются: локальная традиционная DSP-обработка не равна загрузке в генеративный сервис.
'''),
('R08','Own_Voice_Delay_Throws','Vocals',[],'''КУДА: selected lead-vocal Audio track или отдельный effect/response layer; Delay/automation.
ЗАЧЕМ: редкое эхо на окончании строки, а не мутный vocal на всём треке.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Use the existing vocal audio and effects only. Add a restrained delay throw on the selected phrase ending, following the project tempo. Keep the next lead phrase clear. Do not generate extra words, new singers or instrumental parts.
ОРИЕНТИРЫ: при 96 BPM четверть625ms, восьмая312.5ms, шестнадцатая156.25ms. Для другого BPM пересчитать: 60000/BPM. Проверить реальные контролы; текстовый Style не устанавливает delay time.
'''),
('R09','Aligned_Export_And_Check','Export',['S01','S02','S03'],'''КУДА: Studio Export / внешняя DAW. Этот TXT не импортировать как инструмент.
1. Отобрать и commit нужные takes.
2. Не проигрывать full mix вместе со всеми его стемами.
3. Выбрать общую стартовую/конечную точку, сохранить начальную тишину и tails.
4. Экспортировать Multitrack WAV и reference; MIDI отдельно.
5. Зафиксировать BPM, key и origin первой доли. Одинаковый старт не гарантирует отсутствие local drift.
6. Проверить начало, середину, конец, mono, peak/true peak и loudness при наличии измерителя.
7. Не задавать формат/битность/LUFS словами в Style. Не нормализовать каждый stem независимо ради громкости.
8. S01–S03 — инструментальные эскизы, не masters и не наборы отдельных extracted stems.
'''),
('R10','GM_Drum_MIDI_Mapping','Drums',['M09','M10','L01','L02','D01','D02','D04','F01','D10','D09'],'''КУДА: внешняя DAW с drum sampler / пользовательским сопоставлением one-shots. В обычном Wavetable эти ноты не становятся автоматически барабанами.
M09, MIDI channel10: note36→D01, note38→D02, note42→D04.
M10, MIDI channel10: note75→F01, note37→D10, note76→D09. Это пользовательская карта звуков; GM-kit может иметь другие тембры.
В REAPER можно сопоставить one-shots через ReaSamplOmatic5000 или другой имеющийся sampler; для каждого звука настроить note range/trigger. Не обещать мгновенный native drum-rack Suno.
Если остаёшься в Suno Studio: импортируй готовые Audio-лупы L01/L02 либо расставь D/F one-shots на Audio-дорожках. Для них НЕ требуется импорт M09/M10.
''')]
for aid,slug,role,related,body in recipes:
 p=P2/'RECIPES'/f'{aid}_{slug}.txt';p.parent.mkdir(exist_ok=True)
 p.write_text(f'{aid} — {slug}\nВерсия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.\nСвязанные материалы: {", ".join(related) or "свой вокал/свой проект"}\n\n'+body)
 a.append({'id':aid,'file':p.name,'path':p.relative_to(P2).as_posix(),'kind':'recipe','role':role,'description_ru':body.split('\n')[1] if len(body.split('\n'))>1 else slug,'destination':'Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.','not_destination':'Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.','related':related,'source':'authored_workflow_recipe','third_party_audio':False,'contains_human_voice':False,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
a=sorted(a,key=lambda z:z['id'])
assert len(a)==70 and len({x['id'] for x in a})==70
known={x['id'] for x in a}
for r in a:
 assert (P2/r['path']).is_file(),r
 assert all(x in known for x in r.get('related',[])),r
(P2/'ASSET_INDEX.json').write_text(json.dumps({'library_id':'DARK_PRODUCTION_KIT_V1','version':'2026-09-11','media_count':60,'recipe_count':10,'assets':a},ensure_ascii=False,indent=2))
cols=['id','file','path','kind','role','description_ru','bpm','key','bars','root_note','duration_s','sample_rate','bit_depth','channels','destination','not_destination','related','peak_dbfs','true_peak_dbfs_4x','source','sha256']
with (P2/'ASSET_INDEX.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader()
 for r in a:
  q=r.copy();q['related']=' | '.join(r.get('related',[]));w.writerow(q)

intro='''# 05 — Реальный каталог файлов и рецептов
LIBRARY_ID: DARK_PRODUCTION_KIT_V1
VERSION: 2026-09-11

Это индекс реально созданного PART_2_STUDIO_ASSETS: 48 WAV, 12 MIDI, 10 текстовых рецептов.
Сам индекс НЕ содержит исходное аудио и НЕ означает, что Gemini прослушал файлы, имеет доступ к папке на компьютере или что файлы уже импортированы в Suno.
Все музыкальные исходники здесь оригинально синтезированы/сочинены для этого комплекта; аудио третьих лиц и голоса отсутствуют. Это заготовки, не готовые финальные песни, не записи живых инструментов и не личный Voice-профиль.

ПРИОРИТЕТ ВЫБОРА
- Точные ноты keys: M01 (Dm96) или M03 (Em102), MIDI track → Wavetable, рецепт R03.
- Быстро готовый keys-sound: L04 (Dm96) или L09 (Em102), AUDIO track. Не Wavetable preset.
- Sub: M02→R01 (редактируемые ноты) или L03 (готовый Audio loop).
- Барабаны внутри Suno: L01 Audio либо D01/D02/D04 one-shots. M09/M10 не играют автоматически как kit в обычном Wavetable.
- Машинный слой: L02 Audio либо F01/D10/D09.
- Электрический акцент: F02 на отдельный Audio FX track.
- Свой Voice: R06/R08; для дополнительного локального ремонта R07. В библиотеке НЕТ чужого голоса для клонирования.
- Целый инструментальный reference: S01/S02/S03. Это MIX, не отдельный stem. Не класть S01 на Keys как piano-only.

КЛАССЫ
D — drums/percussion one-shots; F — electrical FX; N — pitched one-shots; L — loops; S — multi-part instrumental sketches; M — MIDI; R — recipes.
Все WAV: 48 kHz, PCM 24-bit, технически проверены на finite samples/длину/цифровой clipping. Mono/stereo указаны по файлу. Нет обещания, что любой звук подходит любой песне.
Данные peak/true-peak — технические измерения файлов, не прослушивание музыкального качества.
Предпрослушивание в BROWSE_LIBRARY.html — сокращённая mono PCM16-копия 22.05 kHz. Для работы брать исходный WAV, а не preview.

ФОРМАТ РЕКОМЕНДАЦИИ GEMINI
ASSET_ID → точный путь → тип дорожки/слота → действие → что не делать → проверка.
Не придумывать IDs/имена. Если нужного нет — сказать «в каталоге нет» и дать поисковый запрос/способ создания. Не подразумевать, что вся библиотека уже находится в текущем проекте. Если исходник не загружен в чат, оценка звука идёт по описанию каталога, не от лица слушателя.

РАБОТА С ТЕМПОМ/ТОНАЛЬНОСТЬЮ
96 BPM/4-4/8 bars = 20s; 4 bars = 10s. 90/100/102 — другие длительности. Материал Em102 не подставлять в Dm96 без решения о транспонировании и tempo-match.
У root_note — высота одиночного тона, а не готовая тональность всей песни. У drums/noise key=None. Не назначать noise-file тональность по имени или догадке.
В Dm-палитре последний A может содержать C-sharp; в Em — B с D-sharp; в F#m — C# с E-sharp. Это осознанные доминанты, не обязательные ошибки.

'''
blocks=[intro]
for r in a:
 line=f"## {r['id']} | {r['file']}\nPATH: PART_2_STUDIO_ASSETS/{r['path']}\nTYPE: {r['kind']} | ROLE: {r['role']}\n"
 if r['kind']!='recipe':
  line+=f"BPM: {r.get('bpm') if r.get('bpm') is not None else 'not specified'} | KEY: {r.get('key') or 'not assigned'} | ROOT: {r.get('root_note') or 'n/a'} | BARS: {r.get('bars') or 'n/a'} | DURATION_S: {r.get('duration_s')}\n"
  if 'channels' in r:line+=f"WAV: 48000 Hz / PCM24 / {r['channels']} channel(s) | PEAK_DBFS: {r['peak_dbfs']} | TRUE_PEAK_4X_DBFS: {r['true_peak_dbfs_4x']}\n"
  if 'note_count' in r:line+=f"MIDI: {r['note_count']} notes | note numbers {r['pitch_min']}..{r['pitch_max']} | channel {r['midi_channel_1based']}\n"
 line+=f"ЗАЧЕМ: {r['description_ru']}\nКУДА: {r['destination']}\nНЕ ДЕЛАТЬ: {r['not_destination']}\nСВЯЗИ: {', '.join(r.get('related',[])) or 'none'}\n"
 if r.get('usage_ru'):line+=f"ИСПОЛЬЗОВАНИЕ: {r['usage_ru']}\n"
 if r['kind']=='recipe':line+='\n'+(P2/r['path']).read_text()
 blocks.append(line+'\n')
cat='\n'.join(blocks)
(P2/'ASSET_CATALOG_RU.md').write_text(cat)
(WORK/'knowledge_catalog.txt').write_text(cat)
(WORK/'assets_all.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
print('Catalog ready:',len(a),'items;',len(cat),'characters')
