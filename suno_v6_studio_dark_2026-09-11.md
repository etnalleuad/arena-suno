# Suno v6 + Studio 2.0 — рабочая база под твой звук

**Обновлено: 11 сентября 2026.** v6 выпущена **9 сентября**. Это новая версия исследования, заменяющая прогнозы о v6 из базы от 6 сентября. Старый документ сохранён как исторический срез. [5](https://suno.com/release-notes/introducing-v6)

**Твои условия:** Premier; русский вокал; все три сценария Studio — доработка песни, работа со своим аудио/MIDI и сборка с нуля. Направления: **deconstructed dark art-pop / darkwave; поэтичный альтернативный indie / post-punk; индустриальная органика и trip-hop с электрическим нервом, 89–105 BPM**. Никаких шаблонов фонка, рэпа и коммерческого dance-pop.

**Главный вывод:** не существует подтверждённого «заклинания», которое превращает любое поле Suno в гарантированный генератор изолированного инструмента. Управляемость получается из **правильной операции, выбранного объекта, чистого источника, короткого диапазона и подходящего инструмента**. Для точных нот и намеренной диссонантности MIDI/Wavetable часто рациональнее очередного аудиопромпта.

**Уровни доказательности:** **ОФ** — официальная функция/инструкция; **НАБЛ** — наблюдение конкретного автора с указанной датой; **ПРАКТ** — предложенный мной рабочий приём, не подтверждённый моими генерациями в Suno. Объявленная возможность не означает стопроцентную точность каждого результата.

**Что проверено:** свежие Help и Release Notes, полные транскрипты двух официальных v6-видео от 9–10 сентября, документация/демонстрация Studio 2.0, независимый hands-on The Verge, ранние пользовательские и авторские отчёты. Закрытые Discord-каналы не прочитаны; полноценный корпус свежих Reddit/TikTok-тестов v6 получить не удалось. Старые Studio-наблюдения ниже помечены датами. Доступа к твоему аккаунту нет: промпты — подготовленные к тестированию рецепты, не обещание измеренной надёжности.

---

## БЛОК 1. LYRICS ENGINEERING v6 — РУССКИЙ ВОКАЛ И ТОЧЕЧНЫЕ ПРАВКИ

### 1.1. Что действительно изменилось для текстов

**ОФ:** v6 позволяет просить об изменении конкретной строки/слова в существующей песне естественным языком. В официальном walkthrough это показано в **Simple Mode с существующей песней как входом**. Advanced Mode с собственными Lyrics и структурной разметкой остаётся. Старый Replace Section не исчез — появился более прямой способ сформулировать задачу. [3](https://help.suno.com/en/articles/13924481) [1](https://www.youtube.com/watch?v=_lHvWn2SNC4)

| Что требуется | Куда идти | Чего не делать |
|---|---|---|
| Написать новую песню на свой русский текст | Create → Advanced → Lyrics + Styles | Не помещать весь текст в список Style-тегов |
| Заменить слово в готовой песне | Simple: прикрепить песню и точно назвать изменение; либо Replace в редакторе | Не запускать полный Create без исходника и ждать той же песни |
| Исправить исполнение одной вокальной фразы | Выбрать вокальный клип/диапазон в Studio, затем локальная замена | Не выделять весь stereo mix, если менять сопровождение не требуется |
| Исправить только текст в карточке | Редактирование отображаемых Lyrics | Не ожидать изменения аудио |
| Получить определённое произношение любой ценой | Реальный вокальный дубль / монтаж | Не считать CAPS гарантией фонетического контроля |

**ПРАКТ — точный запрос для готового аудио:** сначала прикрепи нужную песню. Здесь слова в кавычках — пример; замени их на реально существующие.

```text
In the attached song, replace only the first occurrence of the Russian word "голос" with "холод" in the first verse. Keep all other lyrics unchanged. Preserve the existing vocal melody, phrasing, arrangement and duration as closely as possible.
```

Почему **first occurrence**: без него можно случайно попросить заменить слово во всех повторениях. Если мест несколько, добавь секцию и примерный таймкод, а затем проверь результат на слух.

**Не обещание побитовой неизменности:** новая функция заявлена как локальная правка, но для важного мастера сравнивай также соседние фразы, бэки, переходы и длительность. «Остальное сохранено» в ответе Chat — ещё не акустическая проверка.

### 1.2. Вокальный бриф под твою эстетику

Для твоих направлений важны не абстрактные `beautiful vocals`, а **дистанция, степень распева, артикуляция и динамический контраст**. Ниже — авторские варианты. Выбор женского/мужского характера здесь художественный пример, не предположение о твоём голосе.

**Близкий тёмный женский голос — ПРАКТ:**

```text
Russian-language solo female alto, close-miked and intimate, dark breath-led tone, clear consonants, speech-inflected singing that remains pitched, restrained vibrato, selective falsetto at phrase endings, emotional tension without arena-style belting
```

**Сдержанный мужской indie-вокал — ПРАКТ:**

```text
Russian-language solo low tenor, conversational melodic phrasing, slightly frayed tone, clear diction, restrained dynamics, short melodic phrases with room to breathe, intimate rather than theatrical
```

- `speech-inflected singing` — разговорная интонация внутри пения, а не просьба о рэпе.
- `breath-led` / `breathy` — тембровое намерение, не точное расписание вдохов.
- `dry` — пространственная обработка, не отсутствие эмоций.
- Если нужны надлом и интимность, не добавляй автоматически `powerful`, `anthemic`, `soaring chorus`: они могут вести к другой драматургии.

**Разметка собственного текста — ПРАКТ:**

```text
[Verse - intimate, low register, sparse phrasing]
Под кожей тянется провод.
В ладонях темнеет вода.

[Refrain - fragile, close-miked]
Не трогай тишину руками —
Она ещё полна меня.

[Bridge - whispered, exposed]
Я слышу, как дышит стена.

[Final Refrain - restrained intensity]
Не трогай тишину руками —
Она ещё полна меня.
```

Это направляющая разметка, а не опубликованный язык команд v6. В раннем тесте HookGenius автор увидел отражение локальных указаний в результате и его описании, но это один неслепой тест и не измерение точности русского вокала. [2](https://hookgenius.app/learn/suno-v6-guide/)

### 1.3. Ударения и артикуляция: что сохраняем, что перепроверяем

**Нет подтверждённой новой универсальной фонетической разметки v6 для русского языка.** Не следует продавать CAPS, дефисы или combining accents как появившийся «официальный словарь произношения».

**ПРАКТ — порядок ремонта:**

1. Нормальная кириллица, правильная `ё`, понятный контекст.
2. Уменьшить слоговую перегрузку и сложные стыки согласных.
3. Локально попробовать `замОк` / `зАмок`, а не капитализировать весь текст.
4. Отдельным тестом — `замо́к` / `за́мок`: кириллическая буква + U+0301, не латинские `ó` / `á`.
5. Если нужно — исполнительское написание вроде `ничевО`; литературный текст сохранить отдельно.
6. Перейти к новой словесной правке v6 или Replace выделенной фразы.
7. Если точность критична — записать слово/фразу и смонтировать.

**Запрос для выделенного вокального участка:**

```text
In the selected vocal phrase, pronounce the Russian word "замок" as a door lock, with stress on the second syllable: "замОк". Preserve the existing singer, melody and rhythmic placement as closely as possible. Change no other words.
```

**Важно:** если ошибка вызвана тем, что на две доли поставлено слишком много слогов, простая замена регистра буквы может ничего не изменить. Сначала решай ритмическую задачу.

| Средство | Что оно может подсказать | Чего оно не фиксирует |
|---|---|---|
| Запятая, точка, `...` | Членение, завершение мысли, недоговорённость | Паузу в миллисекундах |
| `—` / `-` | Разрыв фразы, дробление или повтор слогов | Отдельную нотную длительность |
| Пустая строка | Разделение строф/фраз | Один гарантированный такт тишины |
| `(ещё)` | Произносимый ответ/эдлиб/повтор | Отдельную изолированную вокальную дорожку |
| `[Whispered Vocals]` | Манеру исполнения | Сохранение личности певца |
| CAPS / `!` | Акцент и экспрессию | Точное ударение или уровень фейдера |

**Для точной паузы — timeline. Для точных высот — MIDI/вокальный редактор. Для определённого человеческого произношения — запись.**

### 1.4. Vocal Gender, Voice и Persona — разные уровни

| Контроль | Для чего | Не заменяет |
|---|---|---|
| **Vocal Gender** в реальном интерфейсе | Направить общий тип вокала | Закрепление одного конкретного певца |
| Вокальный текст в Styles | Регистр, тембр, манеру, дистанцию | Реальный переключатель или Voice-профиль |
| **Verified Voice** | Использовать собственный проверенный голос | Нетронутую запись живого исполнения |
| **Style Persona** | Повторять характер удачной песни | Точный identity-lock в любом новом жанре |
| **Max Mode** | По Suno, уменьшать уход от Voice/референса на длинных генерациях | Исправление каждой фонемы и гарантию идеального сходства |

Наличие Vocal Gender в Advanced-интерфейсе описано в свежих обзорах. Текущий официальный переходный tutorial подтверждает сохранение Voices, Covers и персонализации в v6. [1](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) [1](https://www.youtube.com/watch?v=tkKGNBzkHwE)

**Поправка к старой базе:** отдельная Voices FAQ всё ещё содержит требование выбрать v5.5. Оно устарело после retirement старых моделей; ориентир для текущей доступности — свежая v6 FAQ и видео от 10 сентября, а не эта оставшаяся строка. [3](https://help.suno.com/en/articles/13924481)

Для работы своим Voice используй собственную запись и штатную проверку. Артистические референсы из твоего списка ниже переводятся в музыкальные признаки — они не являются инструкцией клонировать их голоса.

### 1.5. Бэки для art-pop: лучше короткие функции, чем «хор вообще»

**ПРАКТ:** раздели ведущий голос, ответы, шёпот и атмосферные вокальные слои. Одна просьба `add rich backing vocals` легко даёт слишком много партий или другую интонацию.

| Роль | Формулировка | Где оставлять пространство |
|---|---|---|
| Короткий ответ | `a quiet response after the lead phrase` | После окончания главной строки |
| Шёпотный дубль | `a sparse whispered double on selected phrase endings` | Только в отдельных точках |
| Длинная вокальная подложка | `a restrained sustained vowel layer beneath the refrain` | Не под каждой согласной |
| Контрмелодия | `a simple high-register countermelody in the gaps` | Между ведущими фразами |

В спонсированном Studio 2.0-тесте Moe Lueker добавленная гармония разошлась по времени с ведущим вокалом; автор отказался от неё. Это **августовское наблюдение до v6**, но хороший повод проверять бэки по времени, а не верить слову `harmonizes`. [3](https://moelueker.com/blog/suno-studio-2-tutorial-full-song-walkthrough)

---

## БЛОК 2. STYLE & SOUND DESIGN v6 — НОВЫЕ КОНТРОЛЫ И ТВОИ ЖАНРЫ

### 2.1. Что вышло, что изменилось, а что уже было

| Возможность | Статус на 11 сентября | Практический смысл |
|---|---|---|
| **v6** | Новый флагман, Pro/Premier | Отправная точка для определённого брифа |
| **v6-wild** | Новая экспериментальная ветка, Pro/Premier | Искать неожиданные фактуры, ритмы, интонации |
| **v6-mini** | Новая быстрая ветка, все планы | Быстрая разведка; не списывать удачный дубль из-за названия модели |
| **Variety** | Новый контроль расширения Style | Разделять буквальное следование брифу и стилистические развилки |
| **Max Mode** | Подтверждённый реальный переключатель в текущем v6 workflow | Больше вычислений; дороже; ориентирован на устойчивость сложной/длинной генерации |
| Сложные задания в **Simple Mode** | Расширенный способ работы | Модель выбирает процесс по описанию результата, а не только сочиняет песню |
| Несколько источников за один запрос | Подтверждено | Раздать референсам разные роли: ритм, вокальная энергия, атмосфера |
| Текст + аудио + изображения + видео | Подтверждено | Использовать мультимодальные входы вместе |
| Выделить фрагмент, изолировать, построить на его основе | Подтверждён составной сценарий | Не обязательно делать каждое действие отдельным ручным этапом |
| Локальная правка секции/слова естественным языком | Подтверждено | Уточнять готовую песню без нового общего брифа |
| **Custom Models** | Были до v6; существующие автоматически переводятся на v6 | Не нужно заново загружать каталог только ради смены движка; результат всё равно перепроверить |
| **Sounds** | Был до v6; актуальная справка обновлена | Отдельный путь для One Shot / Loop; не новая гарантия чистых стемов |
| MIDI, Wavetable, plugins, automation, Take Lanes | Функции Studio 2.0, выпущенной в августе | Не приписывать их появление релизу v6 |
| Умение Chat учитывать BPM, копирование FX, правки Wavetable/экспорта | Studio-патч от 2 сентября | Остаётся актуальным, но это не новое обновление от 9 сентября |
| Старые модели | Свежая FAQ говорит: retired | Старые песни не удаляются; новые итерации — на семействе v6 |

Официальные источники: релиз, v6 FAQ, текущие модели и release log. [5](https://suno.com/release-notes/introducing-v6) [3](https://help.suno.com/en/articles/13924481) [1](https://help.suno.com/en/articles/13924801) [2](https://suno.com/release-notes)

**«v6 Pro» в разговорах — обычно v6 с отметкой платного доступа Pro, а не четвёртая модель.** Официальное семейство состоит из v6, v6-wild и v6-mini; обе старшие доступны и твоему Premier. [2](https://suno.com/pricing) [10](https://www.aimusicpreneur.com/ai-tools-news/suno-v6-v6-wild-v6-mini-launch/)

Все три варианта поддерживают **до 8 минут за генерацию**. Это верхний предел, не обещание длины каждого трека и не способность безошибочно держать вокал восемь минут. [1](https://help.suno.com/en/articles/13924801)

**Пока не считать выпущенным:** обещанные будущие opt-in продукты вокруг конкретных артистов и их вознаграждения. Само партнёрство с индустрией не превращает голоса и каталоги всех названных тобой артистов в свободные пресеты. [1](https://suno.com/blog/introducing-v6)

### 2.2. Max Mode, Variety, Weirdness и остальные регуляторы

| Контроль | Что известно | Как применить к твоей задаче | Типичная ошибка |
|---|---|---|---|
| **Variety** | Расширяет/обновляет входной Style; `0` сохраняет ручной контроль над тегами | Для проверки конкретной формулировки — 0; для разведки — вернуть Normal/повысить | Считать его тем же самым, что Weirdness |
| **Weirdness** | Степень перехода от Safe к Chaos; исторический нормальный ориентир — 50 | Менять отдельно, после проверки базового поведения | Ожидать, что 0 автоматически уберёт лишние инструменты |
| **Style Influence** | Сила следования стилевому входу | Поднять в отдельном тесте, если точный бриф не удерживается | Утверждать, что 50% буквально отбрасывает половину слов |
| **Audio Influence**, где доступен | Влияние аудио/Voice-ориентира | Подбирать под сохранение мелодии/идентичности; не мешать намеренной смене тембра | Ожидать побитового сохранения исходника при 100 |
| **Max Mode** | По Suno, больше вычислений перед созданием; помогает уменьшить drift | Пробовать для >2 минут, Covers/Voices и сложной преемственности | Включать на каждом коротком percussion-тесте как «улучшайзер мастера» |
| **Vocal Gender** | Реальный контроль типа вокала | Согласовать со Style и выбранным Voice | Ожидать постоянную личность певца |
| **Duration: Auto / Custom** | Отдельный контроль длины | Для короткой идеи — ограничить объём; в Studio прежде всего выделять диапазон | Предполагать, что короткая генерация обязательно дешевле |
| **Personalize / My Taste** | Персонализация; официальный v6 tutorial связывает её и с направлениями Variety | На диагностике отключить или зафиксировать; для личной разведки — использовать осознанно | Забыть, что генерации могли получать разные стилевые направления |

Variety и Max подтверждены актуальной FAQ и двумя официальными walkthrough; интерфейс остальных параметров описан в свежих UI-обзорах. [3](https://help.suno.com/en/articles/13924481) [1](https://www.youtube.com/watch?v=_lHvWn2SNC4) [1](https://www.youtube.com/watch?v=tkKGNBzkHwE) [1](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode)

**Критически важное разделение интерфейсов:** эти опции документированы прежде всего в **Create → Advanced → More Options**. Не установлено, что каждый параметр одинаково показывается в каждом действии Studio. Если в генерации конкретной дорожки нет Variety или Max, запись `Variety: 0` / `Max Mode: On` в тексте **не считается активацией отсутствующего переключателя**. Проверяй видимые настройки и фактическую операцию.

#### Max Mode: что стоит денег

**ОФ:** стандартная генерация песни — **10 credits за две версии**. Max стоит больше; большое количество изображений/видео также может повышать цену. Точную универсальную надбавку Max в просмотренной текущей справке найти не удалось. **Не подставляю выдуманное «всегда 20/30/40» — смотри цену перед Create.** [3](https://help.suno.com/en/articles/13924481)

**Не путать с мифом:** старые `[Is_MAX_MODE: MAX](MAX)` и похожие псевдокоды не являются новым переключателем. Декабрьские/январские дискуссии о «скрытом MAX» — другая история, не инструкция к платной функции v6. [4](https://www.reddit.com/r/SunoAI/comments/1pyly41/in_regards_of_max_mode/)

**Custom Models:** актуальная Help подтверждает от шести собственных треков, до трёх приватных моделей и создание через model picker. Это не новая сентябрьская функция, но теперь её движок — v6. В двух launch-time обзорах у Create Custom Model замечена цена **100 credits**; сама свежая Help цену не фиксирует, поэтому это интерфейсное наблюдение, а не обещание неизменного тарифа. Уже существующую модель не нужно пересоздавать только ради перехода: официально объявлено автоматическое обновление. [1](https://help.suno.com/en/articles/11362497) [1](https://weraveyou.com/2026/09/suno-v6-models-features-editing-sampling-advanced-mode) [2](https://hookgenius.app/learn/suno-v6-guide/) [3](https://help.suno.com/en/articles/13924481)

### 2.3. v6 или v6-wild: рабочее разделение

**ОФ:** Suno рекомендует v6 для более определённой цели, wild — для вариативного поиска. Официальное видео подчёркивает: различие лучше оценивать по нескольким результатам, а не по одной паре. Можно найти идею в wild и развивать её через v6. [1](https://www.youtube.com/watch?v=_lHvWn2SNC4)

**ПРАКТ — под твой звук:**

| Стадия | С чего начать | Почему |
|---|---|---|
| Найти странный электрический жест, необычную вокальную фразу | v6-wild | Разнообразие здесь полезно |
| Сгенерировать понятную новую партию под существующие аккорды | v6, если выбор доступен в операции | Ошибочный инструмент здесь не «счастливая случайность» |
| Сохранить свой Voice через длинный трек | v6 + отдельный тест Max | Проверяем преемственность, а не только первые 20 секунд |
| Вернуть намеренную шероховатость | Сначала описание конкретной шероховатости; затем wild/FX/MIDI | Слово `raw` не говорит, где именно должна быть неровность |
| Точные паузы, ноты и диссонансы | MIDI / timeline, а не другой генератор | Это структурно более контролируемый путь |

**Не нужно автоматически «улучшать» каждый удачный wild-take через v6.** Повторная генерация может убрать именно ту хрупкость, ради которой ты его сохранил. Иногда лучший следующий шаг — crop, comping, FX и автоматизация без нового синтеза.

**Официальный совет:** сначала послушать модели на defaults. **Моя дополнительная диагностическая настройка:** для проверки буквального Style отключить Variety и Personalize, остальные значения сначала оставить штатными. После этого менять по одному параметру. Это способ поставить опыт, не универсальный «лучший preset v6».

`Variety = 0` **не делает генерацию детерминированной**: две версии всё равно могут различаться. Оно убирает один источник изменения стилевого задания, а не всю случайность.

### 2.4. Архитектура промпта: три разных языка задачи

| Поверхность | Что писать | Пример начала |
|---|---|---|
| **Advanced → Styles** | Звуковую картину всей композиции | `Deconstructed dark art-pop, sparse broken drums...` |
| **Simple с прикреплёнными входами** | Что сделать с конкретными источниками | `Use the rhythm from the first reference...` |
| **Studio Chat** | Операцию над выбранным объектом | `Generate an isolated electric-piano part in the selected region...` |

**Ошибка:** скопировать общий Style песни со списком drums, bass, guitar, vocals в запрос на одну дорожку Keys. Ты сам снова перечисляешь полный ансамбль.

**ПРАКТ — общий Style:**

```text
Microgenre + rhythmic identity + dominant timbres + vocal delivery + arrangement contrast + production priorities
```

**ПРАКТ — Studio-задача:**

```text
Operation + destination + selected range + one musical role + source relationship + output boundaries
```

Это схемы составления текста, не зарезервированные ключи Suno. YAML/JSON и CAPS не превращают их в API.

**Про лимиты:** HookGenius сообщает, что на live v6-интерфейсе счётчики показывали 1 000 символов Styles и 5 000 Lyrics. Это наблюдение интерфейса, а не объявленный лимит сообщений Studio Chat. Все полные Style-примеры ниже подготовлены короче 1 000 символов. [2](https://hookgenius.app/learn/suno-v6-guide/)

### 2.5. Три готовых полных Style-промпта — только твои направления

**ПРАКТ.** Это брифы для **всей песни в Advanced**, не промпты на отдельный stem. Artist names намеренно не вставлены. Вокальный тип в примерах можно заменить на нужный, одновременно согласовав Vocal Gender/Voice.

#### A. Deconstructed Dark Art-Pop / Darkwave

**Styles:**

```text
Deconstructed dark art-pop with coldwave atmosphere, 94 BPM, 4/4, D minor. Fractured drum patterns with deliberate gaps, a pressure-heavy mono sub, brittle glassy synth chords and sparse metallic gestures. Intimate Russian-language female alto, clear consonants, breath-led phrasing and brief fragile falsetto at phrase endings. Restrained verses open into an unsettling refrain rather than a triumphant chorus. Tension comes from silence, register shifts and displaced accents. Keep the lead close and intelligible while distorted textures occupy the background and phrase gaps.
```

**Exclude Styles:**

```text
radio dance-pop, festival EDM, rap, trap, phonk, arena belting, cheerful acoustic strumming
```

**Что сохраняет направление:** паузы, отдельные звуковые жесты, давление саба, хрупкая подача. **Что не нужно:** превращать `dark` в бесконечную кинематографическую подложку.

#### B. Поэтичный альтернативный Indie / Post-Punk

**Styles:**

```text
Poetic Russian-language alternative indie rock with coldwave post-punk tension, 102 BPM, 4/4, E minor. A melodic picked bass, lean dry drums, a wiry single-note electric-guitar counterline and occasional muted electric-piano chords. Intimate low-tenor singing with clear diction, conversational melodic phrasing and a slightly frayed tone. The refrain grows through a moving bassline and sharper guitar accents, not stadium volume. Leave gaps around the words. Narrow, tactile verses contrast with a modestly wider refrain; restrained saturation and a close, exposed lead vocal.
```

**Exclude Styles:**

```text
rap, trap, phonk, commercial dance-pop, stadium rock, blues guitar solos, operatic vocals
```

**Важно:** этот пример допускает гитару **на гитарной дорожке**. Если отдельно генерируешь Keys, общий список ансамбля сюда не переносится.

#### C. Индустриальная органика / Trip-Hop с электрическим нервом

**Styles:**

```text
Industrial organic trip-hop with an electric nervous edge, 96 BPM, 4/4, D minor. Heavy sparse kick and snare, uneven mechanical percussion, short electrical cracks, a dense sine-based sub and low dusty electric-piano voicings. Intimate Russian-language singing with restrained dynamics and precise consonants. Contrast the human voice with machine-like accents; let the groove breathe between impacts. Build tension through texture and rhythmic omissions, then strip back before the final refrain. Keep the sub centered and stable, the lead dry and close, and the distortion confined to percussion and background layers.
```

**Exclude Styles:**

```text
rap, trap hi-hat rolls, phonk, radio pop, festival EDM drops, glossy choir stacks, blues shuffle
```

**Не путать плотность с многослойностью:** плотный sub и три точных удара могут звучать тяжелее, чем двадцать одновременно играющих слоёв.

### 2.6. Перевод твоих референсов в рабочие признаки

**ПРАКТ:** это декомпозиция направления, не обещание воспроизвести конкретного артиста.

| Ты описываешь | Полезные английские слова | Что указать дополнительно |
|---|---|---|
| Деконструкция | `fractured rhythm, negative space, displaced accents, abrupt dropouts` | Где пропускать атаки; точные пропуски потом сделать на timeline |
| Телесность / близость | `close-miked vocal, tactile percussion, breath-led phrasing` | Какой источник должен быть близким |
| Хлёсткий ток | `short electrical crack, hard transient, brief noisy tail` | Это FX/перкуссия, не электрогитара |
| Механический стрекот | `relay chatter, metallic ticks, irregular ratchet-like percussion` | Изолированный ритмический слой, без мелодии |
| Плотный саб | `sine-based mono sub, sustained weight, restrained harmonics` | Регистр и место относительно kick |
| Нервные клавиши | `tine electric piano, short hammered attacks, uneven sparse chord stabs` | Источник — клавишный, не щипковая гитара |
| Стеклянная хрупкость | `glassy high-register synth chords, thin attack, exposed decay` | Синтезатор или пианино: выбрать одно |
| Мрачная органика | `dry hand percussion, wood knocks, bowed metal texture` | Не обязательно добавлять acoustic guitar |
| Поэтичность | `conversational melodic phrasing, clear diction, room between lines` | Реальный текст важнее слова `poetic` |
| Контролируемая грязь | `localized saturation, band-limited distortion, clean low end` | На каких дорожках грязь допустима |

**Если нужен действительно кривой звук:** не проси просто «играй неправильно». The Verge в тестах v6 не добилась желаемых out-of-tune/dissonant результатов. Практически надёжнее задать интервалы в MIDI, detune на синтезаторе, микросдвиги и обрывы в монтаже. Это не утверждение, что v6 вообще неспособна на диссонанс; это выбор более управляемого метода. [1](https://www.theverge.com/ai-artificial-intelligence/991977/suno-releases-its-first-ai-music-model-made-with-record-industry-help)

### 2.7. Новые многоисточниковые промпты v6

**ОФ:** в Simple можно объединять несколько входов и объяснять роль каждого. Это реальное отличие v6 workflow. **ПРАКТ:** назначай референсам роли, а не просто прикрепляй пять песен со словами `make it like these`. Загружай только материал, который вправе использовать. [3](https://help.suno.com/en/articles/13924481)

**Ритм из первого, атмосфера из второго — Simple:**

```text
Use only the broken drum feel from the first attached reference and the sparse electrical atmosphere from the second. Write an original industrial-organic art-pop arrangement at 96 BPM. Keep the harmonic material original. Use the supplied Russian lyrics, with an intimate solo vocal and clear diction. The refrain should intensify through texture and silence, not a festival-style drop.
```

**Своя напевка — Simple:**

```text
Build a restrained dark art-pop arrangement around the melody and phrasing of my attached voice memo. Keep the supplied Russian lyrics. Use sparse broken drums, a centered sub and electric-piano chords, leaving the vocal exposed. Preserve the melodic contour as closely as possible; do not turn the delivery into rap.
```

**Образ как палитра, не как повод переписать музыку — Simple:**

```text
Use the attached image only to guide the texture and atmosphere. Keep the attached audio as the reference for tempo, melodic contour and section lengths. Aim for cold metallic detail, intimate space and restrained tension. Keep the supplied Russian lyrics unchanged.
```

Это всё ещё генеративные просьбы. Если напевку нужно сохранить **в исходном аудио**, оставь её отдельной неизменяемой дорожкой Studio и строй сопровождение вокруг неё; не прогоняй сам дубль через полную генерацию.

Для точного создания Keys/Drums картинки и видео обычно лишние: усложняют условия и могут увеличивать стоимость. Их рациональнее использовать на стадии поиска общей атмосферы.

### 2.8. Exclude: точечно, а не «запретить всё»

- В **Advanced Styles** отдельные нежелательные категории лучше держать в Exclude.
- В **Studio Chat** предложение `Do not include drums in the output` — нормальная инструкция операции. Это не то же самое, что набить негативными названиями поле Style.
- Не исключай `pop` целиком, если нужен **art-pop**; исключай `radio dance-pop`, `commercial pop polish` и конкретные нежелательные манеры.
- Не исключай `distortion` целиком, если индустриальная окраска нужна; ограничивай её ролями.
- `Instrumental` означает отсутствие вокала, **не** «только один инструмент».
- Exclude не является hard mute уже существующей дорожки и не исправляет автоматически сгенерированный WAV.

**НАБЛ:** HookGenius увидел, что Exclude отображается в результирующем Style как добавленные `-term`. Не путай такое отображение с доказательством, что модель самовольно переписала исходный бриф. Но и не превращай ручной `-guitar` в выдуманный универсальный командный синтаксис. [2](https://hookgenius.app/learn/suno-v6-guide/)

---

## БЛОК 3. STUDIO 2.0 / PREMIER — ПОКАНАЛЬНАЯ РАБОТА, MIDI И РЕМОНТ

### 3.1. Четыре операции, которые нельзя смешивать

| Операция | Что выбрать | Что просить | Наиболее частая ошибка |
|---|---|---|---|
| **Добавить новую партию** | Пустую Audio-дорожку и нужный диапазон | `Generate an isolated ... part` | Копировать на неё старый клип и незаметно превратить задачу в Cover |
| **Переосмыслить существующее исполнение** | Конкретный исходный Audio/MIDI-клип | `Transform the selected source...` | Просить transform на пустом участке без источника |
| **Обработать звук** | Существующий трек/плагин | `Use effects only; do not generate new audio` | Получить новый дубль вместо EQ/сатурации |
| **Изменить ноты / тембр инструмента** | MIDI-клип и его Wavetable | `Edit the MIDI notes` / `Change the synth preset` | Ожидать, что текстовый аудиогенератор даст такую же точность |

**ОФ:** Studio Chat видит selection, треки, клипы и темп, умеет редактировать проект, создавать MIDI/аудио и эффекты. Но текстовая команда не становится жёсткой границей DSP только потому, что написана капсом. [1](https://help.suno.com/en/articles/13670721)

**Drums, Bass, Keys, Vocals, FX — музыкальные роли и удобные имена.** Основные типы дорожек Studio — **Audio и MIDI**. Переименование Audio-трека в `KEYS_ONLY` не создаёт аппаратный фильтр, физически запрещающий генератору гитару. Если конкретный диалог дополнительно предлагает тип инструмента, выбери его, но всё равно проверь звук.

### 3.2. Подготовка сессии: до первого промпта

**ПРАКТ — рабочий каркас:**

```text
REF_FULL
DRUMS_MAIN
PERC_MACHINE
BASS_SUB
BASS_EDGE
KEYS_TINES
PAD_AIR
GTR_COUNTER
VOX_LEAD
VOX_RESPONSES
FX_ELECTRIC
```

Это названия, не обязательный список и не команда создать одиннадцать партий. Для первого эскиза хватит Drums, Bass, Keys и Lead. GTR нужен только в гитарном направлении.

1. **Сохрани оригинал** отдельной версией/файлом. `REF_FULL` используй для сравнения.
2. Проверь BPM, первую долю, размер и тональный центр. У загруженного аудио цифра project BPM не исправляет автоматически tempo drift.
3. Не проигрывай одновременно исходный full mix и полный комплект его стемов — это удвоение.
4. На новый инструмент создай **действительно пустую Audio-дорожку**.
5. Начни с **4–8 тактов**, а не со всей песни. Это продюсерский ориентир, не объявленный оптимальный лимит v6.
6. Выдели именно эту дорожку и этот диапазон, затем открой Chat.
7. Сначала проверь, **что именно сделано**: создан Audio-take, MIDI-клип или FX-цепь.
8. Прослушай обе take lanes в solo, затем в миксе; commit только подходящую.

**ОФ:** новые варианты живут в Take Lanes; первый может автоматически прослушиваться, но это ещё не то же самое, что окончательно поставить его на основную дорожку. [1](https://help.suno.com/en/articles/13670913)

### 3.3. Контекст: что должно направлять дорожку, но не попадать в её выход

| Генерируем | Полезный музыкальный ориентир | Что не должно случайно стать частью нового stem |
|---|---|---|
| Drums | Пульс, расположение секций, акценты ведущей фразы | Вокал, бас, аккорды |
| Bass | Kick и гармонический каркас | Старый бас-дубль, полноценная клавишная партия |
| Keys | Гармония и паузы вокала | Гитара из исходного референса, drums, lead vocal |
| Vocals | Аккомпанемент, текст, при необходимости референс исполнения | Новая копия всего инструментала, случайный хор |
| FX | Позиция перехода и пульс | Полная новая музыкальная композиция |

**ПРАКТ:** формулировка `Use the other tracks only as timing and harmonic context; do not reproduce them in the output` объясняет задачу, но не гарантирует идеального разделения.

**Что важно не выдумывать:** в рассмотренной официальной справке нет полного протокола, какие muted/solo-треки участвуют в AI-контексте каждого типа операции. Поэтому не утверждаю «Mute всегда исключает из генерации». Если интерфейс позволяет явно выбирать источники — выбирай их. Если контекст неясен, используй отдельную облегчённую копию сессии только с нужными guide-клипами.

**Просьба к Chat перед сложной операцией:**

```text
Before making changes, identify the selected track and time range, and explain whether you will create a new audio part, transform a source clip, edit MIDI or apply effects. Do not generate anything yet.
```

Ответ полезен для обнаружения неверной задачи, но не заменяет проверку реально выбранного объекта. История Chat хранится в проекте: старые просьбы тоже могут запутывать текущую работу.

### 3.4. Формула поканального промпта

**ПРАКТ — шесть обязательных смысловых частей:**

1. **Operation:** новая партия, преобразование, MIDI или FX.
2. **Destination:** выбранная пустая дорожка либо выбранный исходный клип.
3. **Range:** выделенный участок; при необходимости его длина в тактах.
4. **One role:** конкретный инструмент и функция.
5. **Context relationship:** следовать гармонии/груву, заполнять паузы, не дублировать lead.
6. **Boundaries:** только этот элемент в выходе, остальные клипы не менять.

**Слабый запрос:**

```text
Dark organic keys with electric energy, deep bass and an emotional voice.
```

Ты перечислил полный ансамбль и не определил, что должно появиться на выбранной дорожке.

**Более управляемый запрос:**

```text
Generate an isolated tine electric-piano accompaniment in the selected eight-bar region on the empty audio track. Use sparse mid-register chord stabs with a hammered attack and a soft decay. Follow the existing harmony and leave gaps for the lead vocal. Return electric piano only, without guitar, bass, drums or voices. Leave all existing clips unchanged.
```

**Это повышение определённости задания, не обещание 100% успеха.** Если даже правильный краткий запрос дважды возвращает гитару, меняй маршрут, а не добавляй сорок синонимов слова `only`.

### 3.5. Банк поканальных промптов: Drums, Bass, Keys, Vocals, FX

**Все примеры — ПРАКТ, для Studio Chat.** Перед запуском выбери указанный тип объекта. `one isolated part` означает одну музыкальную роль, а не просьбу отменить стандартную выдачу двух вариантов.

**Общий учебный стенд:** 96 BPM, 4/4, D minor, 8 тактов = 20 секунд. Если работаешь с готовой песней, **не навязывай ей эти цифры** — используй её реальные параметры. При доступных настройках для диагностики: v6, Variety 0, Personalize Off, Max Off; Weirdness/Style Influence сначала штатные. Не все эти переключатели обязаны быть доступны в каждой Studio-операции.

#### DRUMS_MAIN — тяжёлая разреженная ритм-секция

**Выделение:** 8 тактов на пустой Audio-дорожке.

```text
Generate one isolated drum-kit part in the selected eight-bar region on the empty audio track. Follow the session tempo. Use a heavy short kick, a dry snare, restrained closed hats and deliberate gaps, with a broken industrial trip-hop feel. Keep the pattern stable enough to support Russian vocal phrasing, with a small variation near the end. Return drums only, without bass, chords, guitars, synth melodies or voices. Do not modify the existing tracks.
```

**Проверка:** нет ли гармонического подслоя; совпадает ли первая атака с нужной долей; не заполнил ли генератор все паузы.

**Если слишком обычный beat:** сначала удали отдельные удары монтажом или попроси один конкретный пропуск; не меняй сразу модель, жанр и все регуляторы.

#### PERC_MACHINE — механический стрекот отдельно от основных drums

**Выделение:** пустая Audio-дорожка, тот же диапазон.

```text
Generate an isolated mechanical-percussion layer for the selected region. Use dry relay clicks, thin metallic ticks and brief irregular rattles between the main drum hits. Follow the existing pulse but keep the density low. This is an unpitched accent layer, not a drum kit or melodic instrument. Do not include kick, snare, bass, chords or voices. Leave the existing arrangement unchanged.
```

**Если получается целая песня:** переходи к One Shot в Sounds и собирай рисунок из отдельных звуков вручную (§3.10).

#### BASS_SUB — плотный, но устойчивый низ

**Предпочтительный точный путь:** MIDI → Wavetable (§3.7–3.8). Ниже — аудиовариант.

```text
Generate one isolated monophonic synth-bass part in the selected region on the empty audio track. Follow the existing chord roots and leave space around the kick attacks. Use a dense sine-based low register, restrained saturation and simple note movement. Avoid chordal playing and high-register runs. Return bass only, without drums, keys, guitar or vocals. Keep the surrounding tracks unchanged.
```

**Проверка:** нет ли двух нот одновременно, струнной атаки вместо synth bass, неправильных корней, сильного ритмического расхождения с kick.

#### BASS_EDGE — электрическая фактура над сабом

**Выделение:** отдельная пустая Audio-дорожка. Не заменяет BASS_SUB.

```text
Generate an isolated mid-bass texture that answers the existing sub-bass rhythm in the selected region. Use short, gritty synthesized pulses with a narrow noisy edge and a restrained low-frequency body. Keep it sparse and monophonic. This layer should add electrical tension, not a second full bassline. Do not include drums, guitar, chords or vocals. Do not change the existing sub track.
```

**Инженерный смысл:** основной sub остаётся стабильным; агрессию регулируешь отдельным фейдером. Точную частотную границу задавай EQ после генерации, не надейся на текстовое «срезать ровно 120 Hz».

#### KEYS_TINES — электрическое пианино, не гитара

**Выделение:** пустая Audio-дорожка. Не клади на неё гитарный stem перед этим действием.

```text
Generate an isolated tine electric-piano accompaniment in the selected eight-bar region on the empty audio track. Use sparse mid-register chord stabs, hammer-struck attacks and soft decays. Follow the existing harmony and place the chords in the gaps between lead-vocal phrases. Keep the tone intimate and slightly worn. Return electric piano only: no plucked strings, guitar, bass, drums or voices. Leave every existing clip unchanged.
```

**Проверка:** действительно ли источник слышится как клавишный, а не только называется Keys в подписи; нет ли гитарных slides/strums и повторённого аккомпанемента.

#### PAD_AIR — синтетическая подложка вместо неопределённых «атмосферных keys»

**Выделение:** пустая Audio-дорожка либо MIDI-дорожка с подходящим Wavetable-патчем.

```text
Generate one isolated synthesizer-pad part in the selected region. Follow the existing chords with slowly changing sustained voicings in the upper midrange. Use a glassy, thin texture with a soft attack, leaving the lead vocal exposed. Keep the low register empty. Return synth pad only, without piano attacks, guitar, percussion, bass or voices. Preserve all existing clips.
```

**Если важны ноты и точные вступления:** MIDI-патч даст больше контроля; длинный release может звучать за границей MIDI-ноты — учитывай это при построении пауз.

#### VOX_LEAD — новая ведущая партия

**Выделение:** пустая Audio-дорожка; нужный текст должен быть передан в доступное Lyrics-поле или явно включён в запрос. Для изменения существующего исполнения используй §3.9, а не этот сценарий.

```text
Generate an isolated Russian lead-vocal part for the selected region using the supplied lyrics. Follow the existing accompaniment and section length. Use intimate, close-miked melodic singing, clear consonants, restrained vibrato and space between phrases. Keep the voice exposed and avoid rap delivery or theatrical belting. Return a solo lead vocal only, with no instruments, choir or backing vocals. Leave the accompaniment unchanged.
```

**Голос:** если действие реально предлагает выбор Voice/Vocal Gender, задай его там. Если не предлагает, не считай имя персонажа в тексте жёстким выбором профиля.

**Если в выходе есть сопровождение:** сравни второй take; затем вокальная изоляция или короткая перегенерация. Даже официальная демонстрация Studio 2.0 показывает сценарий, где после vocal cover пришлось извлекать lead через Advanced Split. [1](https://www.youtube.com/watch?v=GZHp3WFc9Ps)

#### VOX_RESPONSES — тихие ответы, а не полный хор

**Выделение:** небольшой диапазон после конкретной фразы ведущего голоса.

```text
Generate a single quiet backing-vocal response in the selected gap after the lead phrase. Sing only "не трогай" in Russian, softly and close to the microphone. Keep the response shorter than the lead phrase and let it end before the next lead entry. No choir, added lyrics, lead-vocal doubling across the whole section or instrumental accompaniment. Leave the existing lead unchanged.
```

**Проверка:** конец ответа не перекрывает следующую согласную. При необходимости подвинь клип вручную. Одно и то же удачное короткое «эхо» можно повторить монтажом — не надо генерировать его заново десять раз.

#### FX_ELECTRIC — отдельный электрический удар

**Предпочтение:** Sounds → One Shot для самого звука, затем placement в Studio. Если генерируешь прямо на timeline — выбери пустой Audio-участок.

```text
Create one isolated short electrical crack: a hard dry transient followed by a brief sputtering noisy tail. Intimate and metallic, not cinematic. No beat, melody, bassline, voices or background ambience.
```

**Проверка:** нужная атака, длина хвоста, отсутствие музыки. Обрезка и fade — вручную. Текст `short` не фиксирует миллисекунды.

#### FX_TEXTURE — редкая электрическая среда

**Выделение:** отдельная Audio-дорожка, не VOX_LEAD и не весь stereo mix.

```text
Generate a sparse isolated background texture for the selected region: dry relay chatter, distant wire-like resonance and occasional electrical ticks. Leave substantial silence between events. Keep the texture unpitched and unobtrusive so the Russian lead remains clear. No drum groove, harmonic pad, bassline, guitar or voices. Do not alter any existing track.
```

**Если постоянно получается ambience-музыка:** создай 2–3 One Shot и расставь их. Для твоей эстетики пустота — полноценная часть аранжировки.

#### GTR_COUNTER — дополнительная дорожка для indie/post-punk

```text
Generate one isolated electric-guitar counterline in the selected region on the empty audio track. Use wiry single notes, restrained tremolo picking and occasional short muted attacks. Follow the existing harmony and answer the lead vocal in its gaps. Keep the part lean rather than strummed or soloistic. Return guitar only, without bass, drums, keyboards or voices. Preserve the other tracks.
```

Это отдельная роль. Не пытайся одновременно получить из одного generated stem `tine piano`, `bowed guitar`, `synth pad` и «строго один инструмент».

### 3.6. Почему вместо клавиш получается гитара — дерево диагностики

| Возможная причина | Как проверить | Что делать |
|---|---|---|
| На самом деле выбран гитарный клип / его transform | Посмотреть selection и source, а не имя дорожки | Для новой партии выбрать пустой Audio-участок; для смены тембра — MIDI |
| На «новую» дорожку уже скопирован исходный stem | Видна waveform до генерации | Не путать пустой destination и reference source |
| Слишком неопределённые слова | В промпте только `organic`, `electric`, `nervous`, `keys` | Назвать `tine electric piano`, `hammer-struck attacks`, роль и регистр |
| Источник содержит гитару и bleed | Прослушать исходный stem в solo | Более чистый source, Remove FX/разделение по необходимости, MIDI-транскрипция |
| Style/персонализация уводят задание | Сравнить исходный и итоговый Style; проверить доступные Variety/My Taste | Отключить расширение для диагностического теста |
| Сгенерирован полный ансамбль | Прослушать новый take в solo | Новая короткая part-add попытка; затем разделение или MIDI |
| Играет старый full mix | Mute/solo именно новых и старых слоёв | Устранить двойное воспроизведение |
| Подпись Chat неверна | Сравнить заявленную операцию и фактический звук | Не принимать текстовый отчёт за доказательство исполнения |

**ПРАКТ — тест в три шага:**

1. **A:** пустая Audio-дорожка, 4–8 тактов, короткий точный piano-only запрос, одна пара.
2. **B:** тот же диапазон и запрос, но облегчённый/чистый референс; ещё одна пара.
3. Если инструмент всё ещё неверный — **C: MIDI → явно выбранный клавишный тембр**, либо запись/внешний инструмент.

**Не надо:** по двадцать раз повторять `ONLY KEYS`, одновременно обнуляя Style Influence. Нулевой Style Influence не является обещанием точнее следовать твоему piano-описанию.

Исторически такие ошибки подтверждаются не только твоим описанием: в r/SunoAI от 1 мая запросы `Only Synth` / `Only Bass` возвращали drums и смешанные тембры. Это **не тест v6**, а полезное описание проблемы, которую нельзя считать устранённой одним новым номером модели. [1](https://www.reddit.com/r/SunoAI/comments/1t0xdgl/suno_studio_cover_not_isolating_instruments/)

### 3.7. MIDI вместо угадывания: три маршрута

#### A. Нарисовать точную партию

**ОФ:** + Track → MIDI; Wavetable загружается автоматически. Выдели пустой диапазон → + Add Midi Clip; двойной клик открывает piano roll. Ноты можно рисовать, двигать, менять длительности и velocity, quantize. [1](https://help.suno.com/en/articles/13670593)

**ПРАКТ:**

1. Сначала сделай 4–8 тактов keys.
2. Выбери разреженные voicings и оставь паузы под слова.
3. На отдельном MIDI-треке создай монофонический bass из гармонических опор.
4. Выбери инструменты/патчи явно.
5. Исправляй ноты руками, а не через просьбу «сделай гармоничнее».

**Запрос Chat именно на ноты:**

```text
Create an eight-bar MIDI clip on the selected MIDI track. Write a sparse monophonic bass part in D minor at the project tempo, using long root notes with occasional short pickups. Keep all notes between MIDI note numbers 31 and 45. Do not generate audio and do not add other tracks. I will choose the synth sound myself.
```

Chat может ошибиться и здесь — но ошибку в MIDI видно и можно исправить непосредственно. Числа MIDI не зависят от того, называет ли конкретная DAW middle C как C3 или C4.

#### B. Извлечь ноты из удачного аудио

**ОФ:** Studio поддерживает audio → MIDI; Help описывает перенос аудиоклипа на MIDI-дорожку для транскрипции. В доступном контекстном меню также может использоваться Get MIDI. [5](https://help.suno.com/en/articles/13670529)

**ПРАКТ:**

1. Начни с самого чистого одиночного инструмента, а не полного stereo mix.
2. Получи MIDI.
3. Удали ghost notes, лишние октавы и неверные длительности.
4. Проверь регистр, одновременные ноты и фактическую тональность.
5. Сыграй файл нужным синтезатором/клавишным инструментом.

Это особенно полезно, если гитарная **мелодия** нравится, но нужна клавишная **окраска**. Движение нот сохраняешь редактируемым, звук выбираешь отдельно.

**Транскрипция не безошибочна.** Scale assist подсвечивает ноты тональности, а не автоматически исправляет музыкальные ошибки.

#### C. MIDI как референс генеративного аудио

**ОФ:** MIDI → generated audio / audio cover показан в официальном Studio 2.0 walkthrough. Это не слух о будущей функции. [1](https://www.youtube.com/watch?v=GZHp3WFc9Ps)

```text
Use the selected MIDI clip as the performance reference. Generate an isolated electric-piano rendition that follows its pitches, note onsets and note lengths as closely as possible. Keep the sparse chord voicings. Do not add guitar, drums, bass or voices, and do not rewrite the phrase structure.
```

**Различие:** MIDI → Wavetable даёт непосредственное управление нотами; MIDI → генератор снова допускает переинтерпретацию. Если важны абсолютно конкретные ноты и паузы, оставляй MIDI-инструмент или исходное записанное аудио.

Если Chat утверждает, что такого пути нет, сначала проверь выбор клипа и текущий интерфейс. Старые ответы Chat из Reddit не опровергают официальную демонстрацию; но они показывают, почему полезен запасной маршрут MIDI → аудиорендер → audio reference.

#### Два приложенных MIDI-старта

В комплекте `suno_v6_midi_starters_96bpm.zip`:

- `KEYS_Dm_96bpm_8bars.mid` — редкие клавишные аккорды;
- `BASS_Dm_96bpm_8bars.mid` — монофонические басовые опоры;
- `README.txt` — параметры и порядок импорта.

**Это написанные мной учебные MIDI-файлы, не генерации Suno и не музыкальные тесты v6.** Проверяется стандартная структура MIDI. Они не содержат готового звука, Wavetable-пресетов или записи вокала. В Suno из твоего аккаунта они здесь не запускались.

Общий стенд: **96 BPM, 4/4, 8 тактов, ровно 20 секунд**, гармония `Dm(add9) → Bbmaj7 → Gm(add9) → Asus4 → A`. В финальном A есть C-sharp — осознанная доминанта к D minor, а не ошибка, которую нужно автоматически заменить.

### 3.8. Wavetable: точный sub, синтетические keys, контролируемая нервозность

**ОФ:** Wavetable имеет два основных осциллятора и sub, warp/unison, фильтр, envelopes, LFO, modulation matrix, mono/poly и glide. Можно сохранять патчи, загружать собственные wavetables и захватывать материал с timeline. [1](https://help.suno.com/en/articles/13670657)

**Важная граница:** Wavetable — синтезатор, **не библиотека сэмплированного акустического рояля**. Он подходит для synthetic keys, стеклянных аккордов и саба. Для точно заданного реалистичного рояля используй записанный инструмент или MIDI в DAW с подходящим piano-инструментом. Само слово `piano` не добавляет сэмплер.

Все запросы ниже — **ПРАКТ**, запускать на выбранной MIDI-дорожке/Wavetable, не в поле Styles песни.

**Патч 1 — устойчивый sub:**

```text
Change only the Wavetable preset on this MIDI track. Make a monophonic sine-based sub bass with a fast but click-free attack, a short release and restrained harmonic saturation. Disable wide unison and keep the low end centered. Preserve every MIDI note and do not generate new audio or tracks.
```

**Патч 2 — хрупкие synthetic keys:**

```text
Change only this Wavetable preset into a soft synthetic electric-keyboard sound: short bright attack, warm filtered body, moderate decay and little sustain. Keep polyphony for the written chords, with no glide and no wide unison. Preserve the MIDI notes exactly. Do not create an audio cover.
```

**Патч 3 — нервный стеклянный слой:**

```text
Design a thin glassy Wavetable pad with a slow attack and subtle wavetable movement. Keep the low register restrained. Add gentle, slow pitch instability only to the upper texture, not to the bass foundation. Preserve the existing MIDI clip and do not generate another musical part.
```

**ПРАКТ — ручные стартовые ориентиры, не «заводские настройки v6»:**

| Звук | Что держать стабильным | Где добавить характер |
|---|---|---|
| Sub | Mono, небольшая ширина, спокойный pitch, короткий release | Умеренные гармоники, отдельный mid-bass слой |
| Keys | Чёткие note on/off, читаемый attack | Velocity, filter envelope, лёгкая детюнировка |
| Pad | Ноты гармонии и место относительно вокала | LFO на cutoff/wavetable, automation громкости |
| Электрическая фактура | Уровень и отсутствие лишнего sub | Noise-rich wavetable, фильтр, ритмическая модуляция |

**Для намеренной диссонантности:** впиши малую секунду или тритон в конкретный MIDI-аккорд. **Для неровного исполнения:** двигай отдельные атаки/velocity осмысленно, не добавляй случайность ко всему сразу. **Для обрыва:** укорачивай клип и управляй хвостом эффекта. Так «деконструкция» становится аранжировкой, а не надеждой на слово `experimental`.

### 3.9. Inpainting / Replace в Studio: точечный, но не слепой ремонт

| Дефект | Первый выбор |
|---|---|
| Слово или ударение | Новый словесный edit v6 либо короткая замена вокальной фразы |
| Плохая нота в MIDI | Ручная правка в piano roll |
| Хорошая нота, плохой тембр MIDI-инструмента | Поменять патч |
| Плохой тембр аудиофразы, нужно новое исполнение | Transform/Cover выделенного источника |
| Громкость/реверб/сатурация | FX/automation без генерации |
| Один удачный take и одна плохая фраза | Comping нескольких вариантов |
| Плохой финал целиком | Extend/новая финальная секция |

**ПРАКТ — алгоритм замены:**

1. Сохранить оригинал и отметить проблемную точку.
2. Выбрать нужный **stem**, не всю песню по привычке.
3. Выделить естественную фразу с атакой и окончанием. Использовать короткий диапазон, который допускает UI; не обещается любой минимальный размер.
4. Назвать только одно требуемое изменение.
5. Сохранить узнаваемые признаки: source, текст, пульс, гармонический контекст.
6. Прослушать обе версии **до и после** шва.
7. Проверить отсутствие лишних слогов, другого певца, аккомпанемента и timing drift.
8. Commit лучший вариант; при необходимости монтажный fade/crossfade.

**Пример: обработать существующую вокальную фразу, не сочинять новую:**

```text
Replace only the selected lead-vocal phrase. Keep the same Russian words, melodic contour, rhythm and vocal character as closely as possible, but make the consonants clearer and reduce the excessive breathiness. Return lead vocal only. Leave the accompaniment and the material outside this selection unchanged.
```

**Пример: менее плотные drums только в bridge:**

```text
Replace the selected drum passage with a sparser version at the same tempo. Remove most of the hi-hat activity, keep the important kick and snare accents, and leave a clear gap before the next refrain. Return drums only. Do not alter bass, keys or vocals.
```

**Не отдавай хороший трек на полный reroll ради клика или 1 dB баланса.** И не делай 12 последовательных Recreate через каждый предыдущий результат, если цель — сохранить характер исходника: держи исходный approved take точкой сравнения.

### 3.10. Sounds и FX: электрический нерв без случайного ансамбля

**ОФ, актуальная справка:** Create → Sounds → **One Shot** или **Loop**, BPM и Key для музыкального материала; на запрос выдаются два сэмпла. И там же прямо написано, что **Loops may include full musical arrangements**. Значит, Sounds полезен, но не является доказанным способом всегда обойти проблему полного микса. [1](https://help.suno.com/en/articles/10625537)

**ПРАКТ — лучше три точных One Shot, чем один расплывчатый «industrial loop»:**

```text
A single dry metal relay click with a sharp attack and a tiny rattling tail. Close-up mechanical sound. No rhythm, music or voices.
```

```text
A short isolated electrical sputter, thin and abrasive, with a fast decay. No cinematic impact, sustained bass, melody or ambience.
```

```text
One muted wooden knock with a small metallic resonance. Intimate and tactile. No beat, instruments playing a tune or voices.
```

Дальше — монтаж в Studio: расставь разные удары, оставь пропуски, чуть меняй уровни и отдельные позиции. Не регенерируй весь рисунок ради перестановки одного щелчка.

**При 96 BPM:** четверть = 625 мс, восьмая = 312,5 мс, шестнадцатая = 156,25 мс. Это реальные временные ориентиры для сетки/Delay, а не текстовые теги генератора.

#### Генерировать эффект, а не новую музыкальную дорожку

**ОФ:** в Studio есть Compressor, EQ, Reverb, Convolution, Delay, Distortion, Gate, а также создаваемые Chat плагины и automation. VST/AU не загружаются. [1](https://help.suno.com/en/articles/13670785)

**ПРАКТ — обычная обработка:**

```text
Process the selected percussion track using effects only. Add restrained distortion and a short delay, then reduce the output level to avoid a loudness jump. Do not generate, replace or rearrange any audio clips.
```

**ПРАКТ — идея своего плагина:**

```text
Build an audio effect for the selected texture track: a band-limited rhythmic tremolo with tempo-synced eighth-note and sixteenth-note rates. Include Depth, Rate, Tone, Mix and Output controls. It must process the input audio, not generate a new song or instrument part.
```

Созданный плагин — не автоматически проверенный профессиональный DSP-продукт. Проверь bypass на сопоставимой громкости, крайние положения ручек, экспорт и устойчивость. Если Chat предлагает Build It! / Adjust Something First, уточни параметры до построения.

**Стоимость:** бесплатность создания новых плагинов объявлялась **на старте Studio 2.0**; сама справка допускает будущую тарификацию. Не обещаю бессрочный нулевой расход. [1](https://help.suno.com/en/articles/13670785)

### 3.11. Сведение: грязь локально, русский вокал читаемо

**ПРАКТ — архитектура вместо универсального preset:**

| Дорожка | Основная задача | Чего избегать |
|---|---|---|
| Drums | Читаемая атака и управляемые хвосты | Длинный общий reverb, размывающий пропуски |
| Perc/FX | Нерв и детали в паузах | Слишком высокая плотность под согласными |
| Sub | Устойчивый фундамент | Широкий низ и излишняя pitch-модуляция |
| Bass Edge | Агрессия в середине | Дублирование всей энергии sub |
| Keys | Гармония и тактильность | Низкие плотные аккорды одновременно с басом |
| Lead | Ясные слова, близость | Сатурация/эхо на каждой согласной |
| Responses/Pad | Глубина и контраст | Полноценный второй lead на всём протяжении |

**Практические решения:**

- Если kick маскирует bass, сначала измени note placement/длины, затем подбирай sidechain.
- Если компрессор слушает весь DRUMS_MAIN, ducking могут вызывать не только kick, но и snare/hat. Для kick-only реакции нужен подходящий отдельный сигнал/трек.
- Эхо на конце строки делай Delay/automation, а не дополнительными скобками в исходных Lyrics, когда требуется точный timing.
- Сложную окраску клади на отдельный texture-слой, а не обязательно на весь master.
- Gain staging и сравнение при близкой громкости нужны даже для «грязного» арт-звука.
- Если вокал уже имеет длинные встроенные эффекты, Remove FX может помочь, но это AI-обработка, способная изменить характер. Сравнивай с оригиналом.

### 3.12. Если новый stem содержит лишнее: спасение и экспорт

**ОФ:** Take Lanes предлагают feedback `Multiple stems`, после которого доступен Stem Separator. Это прямой признак того, что интерфейс предусматривает случаи многослойного выхода. [1](https://help.suno.com/en/articles/13670913)

| Режим | Для чего | Ограничение |
|---|---|---|
| **Auto Split** | Быстро получить до 12 общих категорий | Не максимальная точность каждого инструмента |
| **Split from Mix** | Один целевой инструмент + остальной микс | Проверять и target, и complement |
| **Advanced Split** | Избирательные инструменты из списка почти 100, Premier | Новый чистый результат не обязательно идентичен оригинальному исполнению |

**Не переписываем июньскую механику без доказательства:** Suno объяснила новый Advanced-подход как пересоздание части по исходнику. Не найдено подтверждения, что v6 внезапно превратила все такие результаты в исходные скрытые дорожки, точно суммирующиеся обратно в stereo mix. [1](https://suno.com/blog/stem-separation-updates)

**ПРАКТ — когда разделять не стоит:** если мелодия/роль полностью неудачная, сначала выбери другой take или способ создания. Извлечение чистого инструмента из плохой музыкальной идеи не улучшит композицию.

**Опубликованные ориентиры credits:** Auto Split — 50. Для Split from Mix и Advanced Help пишет 10 за результат/extraction и уточняет 20 за два создаваемых результата; для Advanced — на выбранный stem. Итоговую цену операции проверять в UI. Нельзя считать «10 за stem» и «10 за весь комплект» одним и тем же. [1](https://help.suno.com/en/articles/12702337)

**Экспорт в FL Studio / Ableton / Logic:**

1. Сохранить исходный master-reference.
2. Экспортировать approved multitrack с общей стартовой позицией и хвостами.
3. Использовать WAV; Studio документирует 32-bit WAV/MP3, Full Song / Selected Range / Multitrack и отдельные stem WAV. [5](https://help.suno.com/en/articles/13670529)
4. MIDI сохранить отдельно: WAV не сохраняет редактируемые ноты.
5. Не auto-warp каждый stem независимо без проверки.
6. Проверить начало, середину и конец: time-aligned старт не устраняет локальный drift.
7. Учесть, какие FX/automation уже напечатаны в экспорт.
8. Не проигрывать одновременно original full mix и все его компоненты.

Studio официально предупреждает о возможном раннем/позднем попадании новых генераций относительно долей. Для проверки — метроном и solo, не только визуальное совпадение начала клипов. [5](https://help.suno.com/en/articles/13670529)

### 3.13. Три полных рабочих маршрута

#### Сценарий A. Есть готовая песня Suno

**ПРАКТ:**

1. Сохрани оригинал; выпиши, что уже удачно: текст, мелодия, голос, грув.
2. Реши, **добавляешь** новый инструмент или **заменяешь** существующий.
3. Для добавления попробуй пустую Audio-дорожку и короткий диапазон.
4. Для замены получи нужные stems/complement и исключи старую партию из итогового воспроизведения.
5. Не оставляй старую гитару внутри full mix и не жди, что mute отдельного guitar stem уберёт её из stereo mix.
6. Новые Keys проверь по §3.6. Если нужны те же ноты, используй MIDI.
7. Ошибку русского слова чини локально; хороший голос не отправляй на новый полный Create.
8. Перенеси удачную партию в аналогичные секции копированием, затем сделай нужные вариации монтажом/automation.
9. Проверяй новые стыки и сохрани новую версию.

#### Сценарий B. Есть своё аудио или MIDI

1. Импортируй оригинал и сохрани нетронутую копию.
2. Если это запись — выставь правильную стартовую позицию/темп; для новой записи используй latency calibration и count-in.
3. Если это MIDI — исправь ноты до звукового поиска.
4. Начни с двух опор: harmonic guide + rhythm, затем bass.
5. Добавляй новые части на отдельные дорожки, не преобразовывая ценный оригинал по привычке.
6. Собственный вокал, который должен остаться настоящей записью, держи вне выбранного generation target.
7. Если нужен новый AI-дубль — делай его как отдельную версию, не подменяй архив.
8. Собери аранжировку и эффекты; только потом оцени, какой фрагмент действительно требует нового синтеза.

#### Сценарий C. С нуля по дорожкам

1. Поставь учебный стенд **96 BPM, 4/4, D minor** или свои параметры.
2. Импортируй приложенные KEYS/BASS MIDI либо напиши свои 8 тактов.
3. Выбери Wavetable-патчи: сначала гармония и bass звучат предсказуемо.
4. Создай DRUMS_MAIN одной короткой генерацией; утверди грув.
5. Добавь PERC_MACHINE или собери его из One Shot.
6. Создай/запиши VOX_LEAD, оставляя тексту место.
7. Добавь только действительно нужные Responses/FX.
8. Разверни approved материал в форму; делай контрасты мьютами, новыми нотами и automation.
9. Генерируй отдельно только переходы и фразы, которым реально нужна новая музыкальная идея.
10. Сведи и экспортируй. Если точный пианистический тембр или сложный вокальный редактор нужен вне Studio — передай MIDI/WAV в DAW, не пытайся загрузить VST в Suno.

**Важная оговорка:** независимо сгенерированные части могут не составить удачную полифонию сами собой. Общая гармония, короткий диапазон и явные роли уменьшают проблему; человеческое решение, что убрать, остаётся необходимым.

### 3.14. Пример формы: 2:40 без стандартного «поп-дропа»

**ПРАКТ — план для собственного проекта, не команда генератора.** При 96 BPM, 4/4 и первой доле в 00:00 такт длится 2,5 секунды.

| Раздел | Такты | Таймкод | Что происходит по дорожкам |
|---|---|---|---|
| Intro | 1–4 | 00:00–00:10 | Один FX-жест, редкие keys, без полного drum kit |
| Verse 1 | 5–16 | 00:10–00:40 | Lead впереди; sub и короткие drums; FX в паузах |
| Tension | 17–20 | 00:40–00:50 | Убрать часть ударов, изменить voicing, повысить напряжение |
| Refrain | 21–28 | 00:50–01:10 | Больше mid-bass/контрлинии, но не обязательный вокальный крик |
| Interlude | 29–32 | 01:10–01:20 | Механический слой и один инструмент |
| Verse 2 | 33–40 | 01:20–01:40 | Возврат к более пустой фактуре |
| Bridge | 41–48 | 01:40–02:00 | Снять drums, оставить exposed voice/keys; конкретный MIDI-диссонанс |
| Final Refrain | 49–60 | 02:00–02:30 | Вернуть вес; менять распределение слоёв, а не просто громкость |
| Outro | 61–64 | 02:30–02:40 | Разбирать аранжировку, оставить один смысловой жест |

Если у реального трека свободное вступление, другой BPM или дрейф, эта арифметика не определяет его границы автоматически.

**Extend для плохого финала:** если неудача начинается в 02:30, а последняя правильная граница — 02:20, выбирай продолжение от **02:20**, сохраняя нужное начало, а не автоматически после конца файла.

```text
Continue from the selected splice point at the established tempo. Strip the arrangement back to the existing vocal character, sparse electric-piano chords and a few mechanical accents. Resolve the phrase without introducing a new hook, a new singer or a large cinematic ending.
```

Это просьба к новому продолжению. Выбор точки — на waveform; `[02:20]` в Lyrics не создаёт реальный splice.

### 3.15. Что говорят люди: полезные наблюдения и их границы

| Источник и дата | Что сообщает | Как использовать без преувеличения |
|---|---|---|
| **Официальный v6 walkthrough, 9 сентября** | Wild показывает более широкий набор направлений; Variety расширяет Style; Max предназначен для преемственности | Это объяснение продукта, не независимый benchmark. [1](https://www.youtube.com/watch?v=_lHvWn2SNC4) |
| **The Verge, 9 сентября, hands-on** | В примерах лучше узнал жанры; были проигнорированы отдельные указания, не получилась требуемая расстроенность, отмечены вокальные артефакты; разница Wild не всегда очевидна | Для art-pop намеренную неровность стоит задавать и средствами MIDI/FX; не объявлять одну модель универсально лучше. [1](https://www.theverge.com/ai-artificial-intelligence/991977/suno-releases-its-first-ai-music-model-made-with-record-industry-help) |
| **HookGenius, 9 сентября** | В одном тесте разброс между двумя takes мешал оценить изменение промпта; описаны поля/Variety/Exclude | Слушать обе версии, повторять условия. Нельзя принимать фразу автора о «потере половины authority при 50%» за техническую спецификацию. [2](https://hookgenius.app/learn/suno-v6-guide/) |
| **Jack Righteous, обновлено 10 сентября** | Тестирование продолжается; mini иногда дал автору предпочтительный take; сообщества дают смешанные отзывы | Сравнивать по задаче, не по престижу имени модели. Это авторские/агрегированные наблюдения, не универсальный рейтинг. [10](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-next-music-industry-model-confirmed-so-far) |
| **Комментарий @ezappa72 к запуску, 10 сентября** | Заявляет о примерно 60 генерациях; не нравится «пластиковый» результат v6, предпочитает wild | Один пользовательский отчёт без опубликованного контролируемого корпуса. Не консенсус. [1](https://x.com/suno/status/2097846245540888664) |
| **Moe Lueker, 21 августа, Studio 2.0 — до v6** | Добавил piano через новую дорожку/выделение; потом вручную поправил уровень/fade; повторил удачную партию копированием; часть бэков не подошла по timing | Полезный реальный процесс. Видео спонсировалось Suno; художественный жанр ролика не переносится в твои шаблоны. [3](https://moelueker.com/blog/suno-studio-2-tutorial-full-song-walkthrough) |
| **r/SunoAI, Studio 2.0, 13 августа — до v6** | Пользователи показывают противоречивые ответы Chat, лишние слои и проблемы с генерируемыми партиями | Проверять фактическое действие и аудио, а не уверенное сообщение ассистента. [1](https://www.reddit.com/r/SunoAI/comments/1vnesak/introducing_studio_20/) |
| **r/SunoAI, 1 мая — до v6** | `Only Synth` и `Only Bass` могли вернуть сопровождение или другой инструмент | Это прежний failure mode, не проверенная характеристика v6. [1](https://www.reddit.com/r/SunoAI/comments/1t0xdgl/suno_studio_cover_not_isolating_instruments/) |

**Чего пока нет в этой выборке:** достаточной серии независимых тестов именно русского dark art-pop/industrial trip-hop на v6, публикуемых success rates для «только Keys», достоверного общего тарифа Max, доказательства безошибочного одиночного инструмента во всех Studio-операциях.

**Discord/TikTok:** не выдаю недоступные каналы и непроверенные ролики за изученный инсайд. Поиск свежих материалов проведён, но пригодный для доказательных выводов post-release-корпус не получен. Прежние «MAX-коды» и дорелизные впечатления не засчитываются как новая практика v6.

**Официальные видео — точные главы:**

- `Suno v6 Is Here` — **11:14** Advanced/Variety, **12:05** wild, **15:14** Max; **9:41** редактирование песни, **10:27** отдельные слова. [1](https://www.youtube.com/watch?v=_lHvWn2SNC4)
- `How to Transition Your Workflow` — **2:20** defaults, **2:37** Variety, **3:09** My Taste, **3:26** Max, **3:59** Custom Models. [1](https://www.youtube.com/watch?v=tkKGNBzkHwE)
- `Introducing Studio 2.0` — **2:55** MIDI, **6:29** запись/latency, **8:07** cover записи, **9:54** stems, **11:03** Remove FX, **11:46** эффекты, **16:08** плагины. [1](https://www.youtube.com/watch?v=GZHp3WFc9Ps)

### 3.16. Экономия credits и протокол проверки

**ОФ:** у Premier 10 000 credits в месяц и 60 обычных song downloads. Экспорт через Studio освобождён от стандартной download-квоты; generation credits при этом не становятся бесконечными. Повторные форматы/stems одной песни не считаются отдельными новыми песнями для квоты. [2](https://suno.com/pricing) [1](https://help.suno.com/en/articles/13614785)

**ПРАКТ — деньги тратить на музыку, не на монтаж:**

1. Сначала уточнить роль и scope; потом нажимать Generate.
2. Слушать обе версии; не отбрасывать вторую автоматически.
3. Не извлекать все stems каждого черновика.
4. Не включать Max на каждом коротком тесте, если нет задачи на преемственность.
5. Не регенерировать одинаковый approved фрагмент ради его появления во втором припеве.
6. Не исправлять фейдер, EQ, паузу или ноту MIDI полной генерацией.
7. После двух неудачных пар на изоляцию менять путь: другой источник, MIDI, One Shot, split — не только формулировку.
8. Не считать Undo возвратом credits.

**Тест A — Variety, только там, где контроль реально доступен:**

- A: один и тот же Style/Lyrics/Voice, Variety 0, два запуска.
- B: всё то же, Variety Normal, два запуска.
- По две версии с запуска → восемь результатов.
- При стандартном full-song тарифе это **40 credits**; не переносить эту арифметику автоматически на другие Studio-действия.
- Сравнить фактические Styles, жанровый разброс и точность роли, а не только «какой трек приятнее».

**Тест B — v6 против wild:** один бриф и референс, фиксированные доступные настройки, несколько takes каждой модели. Сначала оценивать соблюдение роли и текста, затем интересность фактуры. Удачный wild-take не обязан проходить через повторную генерацию v6.

**Тест C — Max:** тот же длинный проект/Voice/Cover, один режим без Max, другой с Max. Сравнить начало, середину, последние 30 секунд, голос и мелодию. Записать фактическую цену Max как `M`; не считать «дороже» эквивалентом «лучше».

| Run | Операция / модель | Источник | Диапазон | Настройки | Цена UI | Результат |
|---|---|---|---|---|---:|---|
| A1 | New audio part / выбранная модель | Guide clips | 8 тактов | Зафиксированы | По UI | Только нужный инструмент? |
| A2 | Та же | Те же | Тот же | Без изменений | По UI | Случайный разброс? |
| B1 | Та же | Один осознанно изменённый source | Тот же | Те же | По UI | Стало ли меньше лишних слоёв? |
| C | MIDI + Wavetable | Исправленные ноты | Тот же | Патч | По действию | Точность notes/timing |

**Пропускать take дальше по цепочке только после пяти проверок:**

- [ ] Верный инструмент и одна нужная музыкальная роль.
- [ ] Нет ненужного сопровождения/второго голоса в solo.
- [ ] Правильные harmony, register и timing.
- [ ] Русский текст понятен; ударения и стыки проверены.
- [ ] Фрагмент улучшает песню в контексте, а не только впечатляет отдельно.

### 3.17. Короткая памятка для следующей сессии

**Если нужна только одна дорожка:**

```text
Choose the operation.
Select the actual destination and range.
Name one instrument and its musical role.
Explain how it follows the source.
Keep the output limited to that part.
Audition both takes in solo and in context.
Use MIDI or editing when exact control matters.
```

**Минимальный порядок под твой industrial art-pop:**

1. **96 BPM / D minor / 8 тактов** для учебного стенда.
2. KEYS MIDI → synthetic-keyboard patch.
3. BASS MIDI → mono sub patch.
4. DRUMS_MAIN → одна короткая пара.
5. VOX_LEAD → свой русский текст / собственный дубль.
6. PERC_MACHINE и FX → One Shot или редкие отдельные слои.
7. Развернуть форму через отбор, копирование, паузы и automation.
8. Только затем решать, нужен ли wild для новой идеи или Max для длинной преемственности.

**Что не делать:** общий Style всей песни на дорожке Keys; Cover случайного исходника вместо нового инструмента; скрытые MAX-теги; смешение Variety с Weirdness; вера в название трека или отчёт Chat вместо прослушивания.

**Итог:** v6 расширяет язык творческого задания, но настоящий контроль в Studio появляется тогда, когда ты отделяешь **нотное содержание, тембр, контекст, аудиогенерацию и обработку**. Для твоей эстетики особенно важно сохранять удачные странности, а точные ноты, паузы и соотношение слоёв доводить руками.
