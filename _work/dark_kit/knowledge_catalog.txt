# 05 — Реальный каталог файлов и рецептов
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


## D01 | D01_DeepShortKick.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D01_DeepShortKick.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.65
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Короткий плотный синтетический kick; не длинный басовый дроп.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D02 | D02_DryBodySnare.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D02_DryBodySnare.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.45
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.27
ЗАЧЕМ: Сухой snare с телом и коротким шумовым хвостом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D03 | D03_SkinRim.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D03_SkinRim.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.22
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Узкий rim-акцент; заполнять редкие паузы, не весь ритм.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D04 | D04_ClosedSteelHat.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D04_ClosedSteelHat.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.13
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -5.11
ЗАЧЕМ: Короткий закрытый hat.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D05 | D05_OpenDustHat.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D05_OpenDustHat.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.48
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.32
ЗАЧЕМ: Умеренно длинный пыльный hat.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D06 | D06_SoftShake.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D06_SoftShake.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.22
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.56
ЗАЧЕМ: Лёгкий шумовой shaker-акцент.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D07 | D07_BrokenClap.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D07_BrokenClap.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.38
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Небольшой расслаивающийся clap; не стадионный хлопок.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D08 | D08_LowOrganicTom.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D08_LowOrganicTom.wav
TYPE: one_shot | ROLE: Drums
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.6
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Низкий синтетический tom с короткой мягкой атакой.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D09 | D09_ThinWoodKnock.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D09_ThinWoodKnock.wav
TYPE: one_shot | ROLE: Percussion
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.22
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Синтезированный wood-like knock. Это не живая field recording.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D10 | D10_MetalRimTick.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D10_MetalRimTick.wav
TYPE: one_shot | ROLE: Percussion
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.25
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.92
ЗАЧЕМ: Тонкий металлический tick для междолевых акцентов.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D11 | D11_BrushScrape.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D11_BrushScrape.wav
TYPE: one_shot | ROLE: Percussion
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.7
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Синтетический короткий шорох; располагать в паузах вокала.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## D12 | D12_MutedThud.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/01_Drums/D12_MutedThud.wav
TYPE: one_shot | ROLE: Percussion
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.45
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Приглушённый тактильный удар без большого сабового хвоста.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F01 | F01_RelayClick.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F01_RelayClick.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.2
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.88
ЗАЧЕМ: Короткий relay click для механического рисунка.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F02 | F02_ElectricalCrack.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F02_ElectricalCrack.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.42
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.4
ЗАЧЕМ: Хлёсткий короткий электрический crack без голоса и ритма.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F03 | F03_RatchetBurst.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F03_RatchetBurst.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.75
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.86
ЗАЧЕМ: Неровная цепочка relay-щелчков; одиночный жест, не музыкальный луп.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F04 | F04_WireScrape.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F04_WireScrape.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 1.3
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Шероховатый wire-like scrape с меняющейся окраской.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F05 | F05_BandlimitedSpark.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F05_BandlimitedSpark.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 0.55
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Искристый ограниченный по полосе шумовой акцент.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F06 | F06_ShortCircuitStutter.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F06_ShortCircuitStutter.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 1.25
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.6
ЗАЧЕМ: Один рваный электрический stutter; не обещает попадание в любую сетку.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F07 | F07_ReverseMetalSwell.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F07_ReverseMetalSwell.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 2.0
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Обратный металлический подвод к событию; окончание совместить со стыком.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F08 | F08_CableResonance.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F08_CableResonance.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 1.6
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Резонансный кабельный жест; материал синтезирован, не записан в поле.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F09 | F09_StaticDropout.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F09_StaticDropout.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 1.4
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.65
ЗАЧЕМ: Шумовая текстура с провалами; содержит намеренные dropout, не дефект файла.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F10 | F10_AirShiver.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F10_AirShiver.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 2.5
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.74
ЗАЧЕМ: Воздушная синтетическая дрожь. Не человеческий вдох и не вокал.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F11 | F11_SubImpact_D1.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F11_SubImpact_D1.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: D1 | BARS: n/a | DURATION_S: 1.2
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Низкий D1 impact; не накладывать без проверки на саб и kick.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## F12 | F12_TapeStopGesture.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/02_Electric_FX/F12_TapeStopGesture.wav
TYPE: one_shot | ROLE: FX
BPM: not specified | KEY: not assigned | ROOT: n/a | BARS: n/a | DURATION_S: 1.1
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Синтетическое замедление высоты для конца фразы; не реальная лента.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: none
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## L01 | L01_Drums_Broken_96_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L01_Drums_Broken_96_4bars.wav
TYPE: loop | ROLE: Drums
BPM: 96 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.96
ЗАЧЕМ: Изолированный broken-drum loop; соответствует M09.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M09, D01, D02, D04
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L02 | L02_Perc_Machine_96_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L02_Perc_Machine_96_4bars.wav
TYPE: loop | ROLE: Percussion
BPM: 96 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Редкий механический слой без гармонии; соответствует M10.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M10, F01, D10, D09
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L03 | L03_Sub_Dm_96_8bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L03_Sub_Dm_96_8bars.wav
TYPE: loop | ROLE: Bass
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 8 | DURATION_S: 20.0
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Восемь тактов bass-only. MIDI M02 сохраняет редактируемые ноты.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M02, R01
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L04 | L04_Tines_Dm_96_8bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L04_Tines_Dm_96_8bars.wav
TYPE: loop | ROLE: Keys
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 8 | DURATION_S: 20.0
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Восемь тактов изолированных synthetic tines. НЕ гитара и не акустический рояль.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M01, R03
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L05 | L05_Pad_Thin_Dm_96_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L05_Pad_Thin_Dm_96_4bars.wav
TYPE: loop | ROLE: Pad
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Тонкая верхняя подложка для пары Dm/Bb.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M06, R04
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L06 | L06_ElectricalBed_96_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L06_ElectricalBed_96_4bars.wav
TYPE: loop | ROLE: FX
BPM: 96 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.85
ЗАЧЕМ: Редкие электрические события на сетке96; без нотного ансамбля.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: F01, F02, F04, F10
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L07 | L07_Drums_Organic_90_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L07_Drums_Organic_90_4bars.wav
TYPE: loop | ROLE: Drums
BPM: 90 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.666667
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Более лёгкий organic-пульс90, без trap rolls.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: D12, D03, D06
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L08 | L08_Sub_Em_102_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L08_Sub_Em_102_4bars.wav
TYPE: loop | ROLE: Bass
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.411771
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Четырёхтактовый bass-only Em/C/D/B.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M04, R01
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L09 | L09_Keys_Em_102_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L09_Keys_Em_102_4bars.wav
TYPE: loop | ROLE: Keys
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.411771
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Synthetic electric keys для альтернативного indie; пара к M03.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M03, R03
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L10 | L10_SyntheticString_Em_102_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L10_SyntheticString_Em_102_4bars.wav
TYPE: loop | ROLE: Synth string
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.411771
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Синтетическая щипковая контрлиния, не живая гитарная запись.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M07, N09
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L11 | L11_Glass_Fsm_100_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L11_Glass_Fsm_100_4bars.wav
TYPE: loop | ROLE: Keys
BPM: 100 | KEY: F-sharp minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.6
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Хрупкая glass-палитра F#m/D/E/C#.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: M05, M11, R04
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## L12 | L12_Perc_Omissions_100_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/04_Loops/L12_Perc_Omissions_100_4bars.wav
TYPE: loop | ROLE: Percussion
BPM: 100 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 9.6
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Сетка100 с намеренными пропусками; не готовая полная drum-section.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: D08, D09, D10
ИСПОЛЬЗОВАНИЕ: Ритмический или музыкальный луп. Audio-дорожка; сверить BPM/key, затем при необходимости растянуть с сохранением высоты.


## M01 | M01_Keys_Dm_96_8bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M01_Keys_Dm_96_8bars.mid
TYPE: midi | ROLE: Keys
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 8 | DURATION_S: 20.0
MIDI: 48 notes | note numbers 53..69 | channel 1
ЗАЧЕМ: Редкие Dm(add9)/Bbmaj7/Gm(add9)/Asus4/A voicings; пара к L04. C-sharp в финальном A намеренный.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L04, R03
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M02 | M02_Bass_Dm_96_8bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M02_Bass_Dm_96_8bars.mid
TYPE: midi | ROLE: Bass
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 8 | DURATION_S: 20.0
MIDI: 17 notes | note numbers 31..45 | channel 1
ЗАЧЕМ: Монофонический бас к M01; пара к L03.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L03, R01
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M03 | M03_Keys_Em_102_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M03_Keys_Em_102_4bars.mid
TYPE: midi | ROLE: Keys
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.41176
MIDI: 16 notes | note numbers 54..66 | channel 1
ЗАЧЕМ: Разреженные клавишные Em/Cmaj7/D/B для альтернативного indie.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L09, R03
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M04 | M04_Bass_Em_102_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M04_Bass_Em_102_4bars.mid
TYPE: midi | ROLE: Bass
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.41176
MIDI: 8 notes | note numbers 35..47 | channel 1
ЗАЧЕМ: Опорный бас Em-палитры; B как доминанта содержит D-sharp в keys.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L08, R01
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M05 | M05_GlassChords_Fsm_100_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M05_GlassChords_Fsm_100_4bars.mid
TYPE: midi | ROLE: Keys
BPM: 100 | KEY: F-sharp minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.6
MIDI: 16 notes | note numbers 56..68 | channel 1
ЗАЧЕМ: Стеклянная F-sharp minor-палитра: F#m/D/E/C#.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L11, R04
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M06 | M06_Pad_Dm_96_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M06_Pad_Dm_96_4bars.mid
TYPE: midi | ROLE: Pad
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
MIDI: 16 notes | note numbers 57..69 | channel 1
ЗАЧЕМ: Верхняя подложка Dm/Bb, без басового регистра.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L05, R04
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M07 | M07_StringCounter_Em_102_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M07_StringCounter_Em_102_4bars.mid
TYPE: midi | ROLE: Synth string
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.41176
MIDI: 12 notes | note numbers 52..63 | channel 1
ЗАЧЕМ: Контрлиния для синтетического щипкового тембра; это не запись гитариста.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: L10, N09
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M08 | M08_SparseMotif_Dm_96_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M08_SparseMotif_Dm_96_4bars.mid
TYPE: midi | ROLE: Lead
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
MIDI: 12 notes | note numbers 62..69 | channel 1
ЗАЧЕМ: Небольшой высокий мотив в паузах; не конкурировать с голосом.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: N06, R03
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M09 | M09_Drums_GM_96_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M09_Drums_GM_96_4bars.mid
TYPE: gm_drum_midi | ROLE: Drums
BPM: 96 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
MIDI: 34 notes | note numbers 36..42 | channel 10
ЗАЧЕМ: GM channel 10. Kick36/snare38/hat42. Не проигрывать обычным Wavetable как готовый kit.
КУДА: External DAW + mapped drum sampler only
НЕ ДЕЛАТЬ: Default Wavetable is NOT a GM drum kit; use paired WAV loop in Suno.
СВЯЗИ: L01, D01, D02, D04, R10
ИСПОЛЬЗОВАНИЕ: Только DAW с drum-map или сопоставлением своих one-shot. В Suno удобнее связанный WAV-луп.


## M10 | M10_Percussion_Map_96_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M10_Percussion_Map_96_4bars.mid
TYPE: gm_drum_midi | ROLE: Percussion
BPM: 96 | KEY: not assigned | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
MIDI: 15 notes | note numbers 37..76 | channel 10
ЗАЧЕМ: Channel10: 75→F01,37→D10,76→D09. Пользовательское сопоставление в DAW обязательно.
КУДА: External DAW + mapped drum sampler only
НЕ ДЕЛАТЬ: Default Wavetable is NOT a GM drum kit; use paired WAV loop in Suno.
СВЯЗИ: L02, R10
ИСПОЛЬЗОВАНИЕ: Только DAW с drum-map или сопоставлением своих one-shot. В Suno удобнее связанный WAV-луп.


## M11 | M11_Sub_Fsm_100_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M11_Sub_Fsm_100_4bars.mid
TYPE: midi | ROLE: Bass
BPM: 100 | KEY: F-sharp minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.6
MIDI: 8 notes | note numbers 30..47 | channel 1
ЗАЧЕМ: Низкая опора для F-sharp minor; для тихих динамиков добавить умеренные гармоники.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: N03, L11, R01
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## M12 | M12_GlassArp_Dm_96_4bars.mid
PATH: PART_2_STUDIO_ASSETS/MIDI/M12_GlassArp_Dm_96_4bars.mid
TYPE: midi | ROLE: Keys
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
MIDI: 16 notes | note numbers 58..76 | channel 1
ЗАЧЕМ: Разреженный glass-arp; точный рисунок можно менять в piano roll.
КУДА: Studio MIDI track + Wavetable / external DAW MIDI instrument
НЕ ДЕЛАТЬ: Not an Audio WAV clip or FX preset. MIDI has no stored sound.
СВЯЗИ: N06, R04
ИСПОЛЬЗОВАНИЕ: Импорт на отдельную MIDI-дорожку; выбрать патч, сверить BPM и редактировать ноты.


## N01 | N01_Sub_D2.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N01_Sub_D2.wav
TYPE: one_shot | ROLE: Bass
BPM: not specified | KEY: not assigned | ROOT: D2 | BARS: n/a | DURATION_S: 1.01
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота D2; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R01
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N02 | N02_Sub_E2.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N02_Sub_E2.wav
TYPE: one_shot | ROLE: Bass
BPM: not specified | KEY: not assigned | ROOT: E2 | BARS: n/a | DURATION_S: 1.01
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота E2; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R01
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N03 | N03_Sub_Fsharp1.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N03_Sub_Fsharp1.wav
TYPE: one_shot | ROLE: Bass
BPM: not specified | KEY: not assigned | ROOT: Fsharp1 | BARS: n/a | DURATION_S: 1.21
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота Fsharp1; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R01
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N04 | N04_Sub_A1.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N04_Sub_A1.wav
TYPE: one_shot | ROLE: Bass
BPM: not specified | KEY: not assigned | ROOT: A1 | BARS: n/a | DURATION_S: 1.01
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота A1; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R01
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N05 | N05_Tine_D4.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N05_Tine_D4.wav
TYPE: one_shot | ROLE: Keys
BPM: not specified | KEY: not assigned | ROOT: D4 | BARS: n/a | DURATION_S: 2.08
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота D4; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R03
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N06 | N06_Glass_A4.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N06_Glass_A4.wav
TYPE: one_shot | ROLE: Keys
BPM: not specified | KEY: not assigned | ROOT: A4 | BARS: n/a | DURATION_S: 2.8
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.98
ЗАЧЕМ: Одиночная синтезированная нота A4; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R03
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N07 | N07_MutedKey_E4.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N07_MutedKey_E4.wav
TYPE: one_shot | ROLE: Keys
BPM: not specified | KEY: not assigned | ROOT: E4 | BARS: n/a | DURATION_S: 1.63
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.98
ЗАЧЕМ: Одиночная синтезированная нота E4; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R03
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N08 | N08_MetalTone_D3.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N08_MetalTone_D3.wav
TYPE: one_shot | ROLE: Keys
BPM: not specified | KEY: not assigned | ROOT: D3 | BARS: n/a | DURATION_S: 2.05
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота D3; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R03
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## N09 | N09_SyntheticString_E3.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/03_Pitched_OneShots/N09_SyntheticString_E3.wav
TYPE: one_shot | ROLE: Synth string
BPM: not specified | KEY: not assigned | ROOT: E3 | BARS: n/a | DURATION_S: 1.5
WAV: 48000 Hz / PCM24 / 1 channel(s) | PEAK_DBFS: -7.0 | TRUE_PEAK_4X_DBFS: -6.99
ЗАЧЕМ: Одиночная синтезированная нота E3; менять высоту осмысленно, не путать с аккордовым лупом.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: R03
ИСПОЛЬЗОВАНИЕ: Одиночный звук. Перетащить на Audio-дорожку и поставить в нужную точку; не превращать автоматически в длинную песню.


## R01 | R01_Wavetable_Clean_Sub.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R01_Wavetable_Clean_Sub.txt
TYPE: recipe | ROLE: Bass
ЗАЧЕМ: ЗАЧЕМ: устойчивый моно-саб; не менять уже написанные ноты.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: M02, M04, M11, L03

R01 — Wavetable_Clean_Sub
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: M02, M04, M11, L03

КУДА: Studio → выбранная MIDI-дорожка → Wavetable. Не импортировать этот TXT как preset.
ЗАЧЕМ: устойчивый моно-саб; не менять уже написанные ноты.
ШАГИ: сначала импорт MIDI; выбрать дорожку; открыть Wavetable/Chat; применить описание; проверить register и mono. Если нужен более слышимый бас на маленьких динамиках — немного гармоник, а не обязательно больше громкости.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only the Wavetable preset on the selected MIDI track. Use a monophonic sine-based sub with a click-free fast attack, restrained harmonics and a short release. Keep the low end centered and disable wide unison. Preserve every MIDI note and do not generate audio or additional tracks.
ПРОВЕРИТЬ: правильные корни; нет лишних октав; bass не перекрывает kick; длины release не съедают паузы.


## R02 | R02_Wavetable_Bass_Edge.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R02_Wavetable_Bass_Edge.txt
TYPE: recipe | ROLE: Bass
ЗАЧЕМ: ЗАЧЕМ: электрическая агрессия в середине при устойчивом чистом сабе.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: M02, N01

R02 — Wavetable_Bass_Edge
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: M02, N01

КУДА: дубликат MIDI-баса, отдельная дорожка BASS_EDGE, НЕ основной BASS_SUB.
ЗАЧЕМ: электрическая агрессия в середине при устойчивом чистом сабе.
ШАГИ: продублировать MIDI; на копии выбрать более богатый спектром патч; добавить Distortion и EQ; срезать конкурирующий низ по слуху; подмешать тихо. Это не обязательная цепь на весь mix.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only the sound on this duplicate MIDI track into a restrained gritty mid-bass layer. Preserve the note pattern. Use moderate distortion and reduce its lowest frequencies with EQ so the original sub remains the foundation. Do not alter the original bass track or generate a new musical part.
ПРОВЕРИТЬ: solo и сумма; mono; при bypass громкость сравнима; нет дополнительной мелодии.


## R03 | R03_Wavetable_Synthetic_Keys.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R03_Wavetable_Synthetic_Keys.txt
TYPE: recipe | ROLE: Keys
ЗАЧЕМ: ЗАЧЕМ: синтетические electric keys вместо случайной гитары в аудиогенерации.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: M01, M03, M08, L04, L09

R03 — Wavetable_Synthetic_Keys
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: M01, M03, M08, L04, L09

КУДА: MIDI-дорожка с Wavetable. Это рецепт, не .vst/.fxp/Suno preset.
ЗАЧЕМ: синтетические electric keys вместо случайной гитары в аудиогенерации.
ШАГИ: импортировать M01/M03; выбрать полифонический клавишный patch; короткий ясный attack; decaying body; без glide; оставить места под свой Voice.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Change only this Wavetable preset into a soft synthetic electric-keyboard sound with a short hammered attack, warm filtered body and moderate decay. Keep polyphony for the written chords, no glide and restrained width. Preserve all MIDI notes. Do not create an audio cover or a guitar part.
ВАЖНО: Wavetable не библиотека сэмплированного рояля. Для реалистичного acoustic piano — подходящий инструмент в DAW или собственная запись.


## R04 | R04_Wavetable_Glass_Pad.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R04_Wavetable_Glass_Pad.txt
TYPE: recipe | ROLE: Pad
ЗАЧЕМ: ЗАЧЕМ: хрупкая верхняя фактура, не мешающая сабу и русским согласным.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: M05, M06, M12, L05, L11

R04 — Wavetable_Glass_Pad
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: M05, M06, M12, L05, L11

КУДА: выбранная MIDI-дорожка Wavetable, затем automation.
ЗАЧЕМ: хрупкая верхняя фактура, не мешающая сабу и русским согласным.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Design a thin glassy Wavetable pad on the selected MIDI track. Use a slow attack, restrained low frequencies and gentle wavetable movement. Keep the written pitches and rhythm. Do not generate new audio, melodies, bass or voices.
РУЧНОЙ КОНТРОЛЬ: если нужно напряжение, вписать нужный интервал в MIDI; немного detune только на texture-слое; автоматизировать volume/cutoff. Не вводить число процентов как мета-тег Lyrics.
ПРОВЕРИТЬ: согласные lead слышны; tails не заполняют задуманные остановки; в mono слой не исчезает.


## R05 | R05_Studio_Electric_Perc_FX.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R05_Studio_Electric_Perc_FX.txt
TYPE: recipe | ROLE: FX
ЗАЧЕМ: ЗАЧЕМ: усилить электрическую фактуру без новой музыкальной генерации.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: L02, L06, F02, F03

R05 — Studio_Electric_Perc_FX
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: L02, L06, F02, F03

КУДА: Audio-дорожка PERC_MACHINE или FX_ELECTRIC → штатные эффекты.
ЗАЧЕМ: усилить электрическую фактуру без новой музыкальной генерации.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Process the selected percussion track using effects only. Add restrained distortion, shape the tone with EQ and use a short delay that follows the project tempo. Match the output level to the bypassed signal. Do not generate, replace or rearrange audio clips.
ПРОВЕРИТЬ: не превратить каждую паузу в непрерывный шум; не усиливать верх до болезненной резкости; сравнить громкость с bypass.


## R06 | R06_Own_Voice_Studio_Clarity.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R06_Own_Voice_Studio_Clarity.txt
TYPE: recipe | ROLE: Vocals
ЗАЧЕМ: ЗАЧЕМ: сведение, а не подмена личности певца.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: none

R06 — Own_Voice_Studio_Clarity
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: свой вокал/свой проект

КУДА: выбранная Audio-дорожка с собственным approved Voice, на копии проекта/дорожки.
ЗАЧЕМ: сведение, а не подмена личности певца.
ПОРЯДОК: сначала уровень фраз/automation; затем умеренный EQ и Compressor; потом очень дозированное пространство. Неправильное слово не исправится эквалайзером — нужен локальный edit/Replace или настоящий дубль.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Process the selected lead-vocal track using effects and level automation only. Preserve the existing singer, words and performance. Keep the voice close and intelligible, reduce obvious tonal harshness gently and control uneven phrase levels. Do not regenerate the vocal, add harmonies or change other tracks.
ОГРАНИЧЕНИЯ: не заявлять встроенный de-esser или Melodyne-подобный редактор как доказанную штатную функцию Studio. Если точечного ремонта не хватает — R07.


## R07 | R07_Own_Voice_REAPER_Cleanup.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R07_Own_Voice_REAPER_Cleanup.txt
TYPE: recipe | ROLE: Vocals
ЗАЧЕМ: REAPER: полноценная 60-дневная оценочная версия; далее требуется подходящая лицензия, это не обещание вечной бесплатности. https://www.reaper.fm/download.php
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: none

R07 — Own_Voice_REAPER_Cleanup
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: свой вокал/свой проект

КУДА: дополнительная локальная DAW REAPER, только если пользовательница согласна. Не Suno plugin slot.
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


## R08 | R08_Own_Voice_Delay_Throws.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R08_Own_Voice_Delay_Throws.txt
TYPE: recipe | ROLE: Vocals
ЗАЧЕМ: ЗАЧЕМ: редкое эхо на окончании строки, а не мутный vocal на всём треке.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: none

R08 — Own_Voice_Delay_Throws
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: свой вокал/свой проект

КУДА: selected lead-vocal Audio track или отдельный effect/response layer; Delay/automation.
ЗАЧЕМ: редкое эхо на окончании строки, а не мутный vocal на всём треке.
ПРОМПТ ДЛЯ SUNO STUDIO CHAT:
Use the existing vocal audio and effects only. Add a restrained delay throw on the selected phrase ending, following the project tempo. Keep the next lead phrase clear. Do not generate extra words, new singers or instrumental parts.
ОРИЕНТИРЫ: при 96 BPM четверть625ms, восьмая312.5ms, шестнадцатая156.25ms. Для другого BPM пересчитать: 60000/BPM. Проверить реальные контролы; текстовый Style не устанавливает delay time.


## R09 | R09_Aligned_Export_And_Check.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R09_Aligned_Export_And_Check.txt
TYPE: recipe | ROLE: Export
ЗАЧЕМ: 1. Отобрать и commit нужные takes.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: S01, S02, S03

R09 — Aligned_Export_And_Check
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: S01, S02, S03

КУДА: Studio Export / внешняя DAW. Этот TXT не импортировать как инструмент.
1. Отобрать и commit нужные takes.
2. Не проигрывать full mix вместе со всеми его стемами.
3. Выбрать общую стартовую/конечную точку, сохранить начальную тишину и tails.
4. Экспортировать Multitrack WAV и reference; MIDI отдельно.
5. Зафиксировать BPM, key и origin первой доли. Одинаковый старт не гарантирует отсутствие local drift.
6. Проверить начало, середину, конец, mono, peak/true peak и loudness при наличии измерителя.
7. Не задавать формат/битность/LUFS словами в Style. Не нормализовать каждый stem независимо ради громкости.
8. S01–S03 — инструментальные эскизы, не masters и не наборы отдельных extracted stems.


## R10 | R10_GM_Drum_MIDI_Mapping.txt
PATH: PART_2_STUDIO_ASSETS/RECIPES/R10_GM_Drum_MIDI_Mapping.txt
TYPE: recipe | ROLE: Drums
ЗАЧЕМ: M09, MIDI channel10: note36→D01, note38→D02, note42→D04.
КУДА: Read recipe; apply in the specified UI. NOT importable as audio/MIDI/plugin preset.
НЕ ДЕЛАТЬ: Never drag this TXT into a WAV/MIDI/Wavetable/VST/Voice slot.
СВЯЗИ: M09, M10, L01, L02, D01, D02, D04, F01, D10, D09

R10 — GM_Drum_MIDI_Mapping
Версия 2026-09-11. Тип: ТЕКСТОВЫЙ РЕЦЕПТ, НЕ файл пресета.
Связанные материалы: M09, M10, L01, L02, D01, D02, D04, F01, D10, D09

КУДА: внешняя DAW с drum sampler / пользовательским сопоставлением one-shots. В обычном Wavetable эти ноты не становятся автоматически барабанами.
M09, MIDI channel10: note36→D01, note38→D02, note42→D04.
M10, MIDI channel10: note75→F01, note37→D10, note76→D09. Это пользовательская карта звуков; GM-kit может иметь другие тембры.
В REAPER можно сопоставить one-shots через ReaSamplOmatic5000 или другой имеющийся sampler; для каждого звука настроить note range/trigger. Не обещать мгновенный native drum-rack Suno.
Если остаёшься в Suno Studio: импортируй готовые Audio-лупы L01/L02 либо расставь D/F one-shots на Audio-дорожках. Для них НЕ требуется импорт M09/M10.


## S01 | S01_ArtPop_Dm_96_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/05_Scene_Sketches/S01_ArtPop_Dm_96_4bars.wav
TYPE: scene | ROLE: Scene
BPM: 96 | KEY: D minor | ROOT: n/a | BARS: 4 | DURATION_S: 10.0
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -9.0 | TRUE_PEAK_4X_DBFS: -8.77
ЗАЧЕМ: Инструментальный синтетический эскиз Dm96; место под собственный вокал. НЕ один stem.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: L01, L02, L03, L04, L06
ИСПОЛЬЗОВАНИЕ: Полный инструментальный эскиз. Audio/reference, НЕ изолированный stem. Не смешивать со всеми его компонентами без намерения.


## S02 | S02_IndiePulse_Em_102_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/05_Scene_Sketches/S02_IndiePulse_Em_102_4bars.wav
TYPE: scene | ROLE: Scene
BPM: 102 | KEY: E minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.411771
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -9.0 | TRUE_PEAK_4X_DBFS: -8.98
ЗАЧЕМ: Синтетическая indie-подложка Em102. Щипковая партия не является живой гитарой.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: L08, L09, L10, M09
ИСПОЛЬЗОВАНИЕ: Полный инструментальный эскиз. Audio/reference, НЕ изолированный stem. Не смешивать со всеми его компонентами без намерения.


## S03 | S03_IndustrialGlass_Fsm_100_4bars.wav
PATH: PART_2_STUDIO_ASSETS/AUDIO/05_Scene_Sketches/S03_IndustrialGlass_Fsm_100_4bars.wav
TYPE: scene | ROLE: Scene
BPM: 100 | KEY: F-sharp minor | ROOT: n/a | BARS: 4 | DURATION_S: 9.6
WAV: 48000 Hz / PCM24 / 2 channel(s) | PEAK_DBFS: -9.0 | TRUE_PEAK_4X_DBFS: -8.99
ЗАЧЕМ: Контрастный industrial/glass-эскиз F#m100, без голоса. НЕ набор извлечённых стемов Suno.
КУДА: Studio Audio track / local DAW Audio track
НЕ ДЕЛАТЬ: Not a Wavetable preset, not a Voice profile. WAV on MIDI can trigger transcription.
СВЯЗИ: L11, L12, M11, F02, F06
ИСПОЛЬЗОВАНИЕ: Полный инструментальный эскиз. Audio/reference, НЕ изолированный stem. Не смешивать со всеми его компонентами без намерения.

