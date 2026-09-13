# CONSOLIDATED_INDEX — что где лежит 13.09.2026

Быстрая карта чтобы не грузить всё подряд в Gemini и не дублировать.

## Актуальный хэнд-офф (читать первым)
* `PROJECT_HANDOFF_2026-09-13.md` — **главный файл** (скрины Suno, новая цель «качественный референс для Suno», час видео доступен, следующий шаг). Заменяет старый `PROJECT_HANDOFF.md` (12.09).
* `CAPABILITIES_AND_PIPELINE_2026-09-13.md` — что я могу сделать с твоими загрузками прямо здесь (ffmpeg, анализ, отделение вокала, подготовка датасета).
* `RESEARCH_TODO_2026-09-13.md` — что исследовать дальше (P0/P1/P2/P3).

## Аудио и измерения (локально, не в git)
* `mic_test_raw.wav` (8.4MB) — `проверка.wav` 49.4с
* `voice_recordings/kukla_na_polke_raw.wav` (12MB) 70.3с
* `voice_recordings/metelitsa_raw.wav` (21MB) 122.8с
* `voice_recordings/TECHNICAL_ANALYSIS.json` — цифры по трём файлам
* `voice_recordings/SOURCE_FILES.json` — откуда скачано + sha256
* `voice_recordings/A_level_only_mono.wav` / `B_hpf80_same_level.wav` — A/B 17с
* `voice_recordings/levels_overview.png` / `mic_test_spectrum.png` — графики
* Эти файлы **не коммитим** в git чтобы не превысить 128MB лимит — хранятся локально и в CHAT_RESTORE как отдельные оригиналы при необходимости.

## Архив переноса (не трогать, чек-суммы валидны)
* `CHAT_RESTORE_2026-09-12/` — полный перенос: `ACTIVE_KNOWLEDGE/` 7 txt, `GEM_SETUP/` инструкции + проверки + вопросы поддержке, `PHOTOS/` 4 png + контактный лист, `MEDIA_CATALOG_ONLY/` индекс 70 ID, `ORIGINAL_DOWNLOADS/` 3 zip, `REFERENCE_GUIDES/` html, `BUILD_SCRIPTS/`.
* `ALL_CONTEXT_FOR_NEW_CHAT_2026-09-12.txt` — один файл со всеми 7 модулями для загрузки в Gemini (дублируется в корне и в CHAT_RESTORE — оставляем оба пути для совместимости).
* `PART_2_STUDIO_ASSETS.zip` (37MB, sha256 `c7b919dce14...`) — **внешний медиа-архив** 48 WAV +12 MIDI+10 рецептов. Внутрь CHAT_RESTORE не включён специально — скачивать отдельно. Каталог есть в `MEDIA_CATALOG_ONLY/`.

## Дубликаты — что можно игнорировать
* `suno_knowledge_base_ru_2026-09-06.*` и `suno_v6_studio_dark_...` в корне = дубли `CHAT_RESTORE/ARCHIVE_NOT_CURRENT/` + `REFERENCE_GUIDES/` — старые гайды, не актуальные после 12.09.
* `VOICE_ADDON_2026-09-12/` в корне = дублирует `CHAT_RESTORE/ORIGINAL_DOWNLOADS/VOICE_ADDON...zip` + `ACTIVE_KNOWLEDGE/07...`
* `MY_VOICE_SETUP_RTX3050.txt` в корне = копия `CHAT_RESTORE/CURRENT_PROFILE/`
* `VOICE_WORKFLOW_GUIDE_...html` / `START_HERE_GEMINI_STUDIO.html` — рендеры из `CHAT_RESTORE/REFERENCE_GUIDES/` — можно не грузить повторно.

## Что грузить в новый чат Gemini (минимальный набор)
1. `PROJECT_HANDOFF_2026-09-13.md` (или `ALL_CONTEXT...` если нужен полный контекст)
2. `CAPABILITIES_AND_PIPELINE_2026-09-13.md` (если будешь грузить видео)
3. При необходимости: `voice_recordings/TECHNICAL_ANALYSIS.json` + один скрин Suno
4. Не грузить: весь `CHAT_RESTORE.zip` целиком, `PART_2...zip` если говорим только про голос, все 4 фото микрофона повторно.

## Что есть в `_work/`
* Скрипты сборки (`build_*.py`, `render_*.py`), `dark_kit/` с собранными ассетами, `transfiles_...` логи скачивания, `v6_research_notes_...` — служебные, не нужны для Gemini.

---
*Карта создана 13.09.2026, ветка arena/01a09ad4-arena-suno. Следующий перенос — достаточно одного `PROJECT_HANDOFF_2026-09-13.md` + `ALL_CONTEXT...txt` если нужен полный Gem.*
