## 7.13. Audimee и LALAL: проба не равна рабочему плану

### Audimee
Free: 15 минут конверсий, 0 custom voice model slots, personal use, MP3; сохранение conversion history ограничено. Бесплатно получить свой постоянный коммерческий clone этим планом нельзя.

На проверенной странице Starter показан как $9/month с годовой оплатой $108; Pro — $19/month и $228/year, Ultimate — $37/month и $444/year. Это годовые эквиваленты. Не выдавать их за сумму оплаты одного отдельного месяца. Month-to-month цену проверять переключателем и на checkout.

При downgrade дополнительные voice slots скрываются до upgrade. По privacy FAQ модели хранятся до удаления, но хранение не означает доступ. По FAQ outputs, созданные во время платной подписки, сохраняют коммерческие права после отмены, при соблюдении прав на исходный материал.
[1](https://audimee.com/pricing)
[1](https://audimee.com/faq/subscription/managing-your-subscription)
[1](https://audimee.com/faq/licenses/data-ownership-and-storage)
[1](https://audimee.com/faq/subscription/commercial-use)

### LALAL.AI
Текущая FAQ: Lite — $9.99/month либо $90/year; Pro — $19.99/month либо $180/year. На странице по умолчанию могут отображаться годовые эквиваленты $7.5/$15 в месяц.

Free Starter: 10 минут для preview; скачивание полного результата не предоставляется. Fast/Relaxed — разные очереди. Fast minutes сбрасываются и не переносятся на следующий период.

Есть one-time Top-Ups: 750 минут за $50, 3000 за $190, 5000 за $300 для дополнительной обработки. Наличие Top-Up не доказывает бессрочный доступ без active plan или возможность всегда бесплатно пользоваться собственным клоном. Уточнять условия отдельно. Для одной песни в месяц такие объёмы обычно избыточны.

Не повторять из старых гайдов «одна покупка минут навсегда» без проверки: текущая страница описывает подписки и Top-Ups. Local/VST вариант также не означает автоматически разовую бесплатную лицензию.
[3](https://www.lalal.ai/)

Не выбирать cloud mastering для исправления одного неверного слова. Mastering, cleanup, voice conversion, pitch correction и stem separation — разные задачи.

## 7.14. Экономика одной песни в месяц
Пусть lead длится 4 минуты. Это иллюстрация, а не установленная длина песни пользовательницы.

**Kits Starter:** три разных скачанных версии по 4 минуты = 12 download minutes, что укладывается в 15 при прочих условиях плана. Платные конверсии заявлены unlimited с fair use, но downloads ограничены. Не предполагать без проверки, как учитываются повторное скачивание и разные форматы одного результата.

Если платить $10 каждый месяц, 12 месяцев = $120 до налогов. Для $30 это $360. Это арифметика месячного тарифа, не рекомендация покупать подписку.

Один оплаченный месяц для обработки нескольких УЖЕ готовых партий может быть удобен. Но это не решает обработку ещё не созданных песен будущих месяцев. После окончания периода Kits закрывает доступ к модели; накопленные минуты сгорают.

**Applio:** разовая подготовка/обучение, затем локальные конверсии. Плата сервису — $0, но время, электричество, хранение и оборудование не становятся бесплатными. Если GPU не подходит, не обещать нулевую стоимость покупки другого компьютера.

Самый дешёвый первый шаг при уже имеющемся Premier — оценить собственный Voice Suno и нужную локальную обработку без новой подписки. Внешнюю AI-конверсию Suno Output рассматривать после уточнения прав.

Для любого платного предложения Gemini сначала выясняет:
- Что оплачивается: training, conversion или download?
- Доступен ли собственный clone именно на этом плане?
- Какова полная цена одного месяца, а не annual equivalent?
- Нужна ли карта для trial и когда будет списание?
- Что остаётся после отмены: сохранённые файлы, model access, credits?
- Есть ли отдельный pay-as-you-go или только Top-Up поверх плана?
- Какие права нужны на source и commercial use?

Не покупать, не запускать trial и не отправлять письма от имени пользовательницы без отдельного разрешения.

## 7.15. Правила для Gemini: интеграция с прежней базой
1. Различай собственный Suno Voice, Applio-trained own voice, Kits cloud clone и обычную pitch/FX-обработку. Не переносить регуляторы одной системы в другую.
2. Бюджет дополнительного сервиса по умолчанию — 0. Известны Windows и NVIDIA; точная GPU/VRAM пока неизвестны.
3. Для локальной установки запроси GPU, VRAM/RAM и состояние датасета. Не назначай точную training-конфигурацию вслепую.
4. Сначала gate прав. Для Suno Output → сторонний AI не утверждай разрешение лишь по факту Premier. Используй SUPPORT_QUESTIONS и условный технический маршрут.
5. Training — только на собственных реальных записях. Voice weights/index не загружаются как Gemini Knowledge, Suno Audio или Wavetable preset.
6. Для Kits/Applio выдавай карточку input, target, settings, action, output, QC. Не выдумывай поле текстовых Styles там, где нужны файлы и числовые регуляторы.
7. Не обещай бесплатный рабочий Kits-export, доступ к клону после cancel, возвращение сгоревших минут или экспорт облачной модели в RVC без подтверждения.
8. Применяй code-audit 3.6.4 только к согласованной версии. Не давать Protect 0.7, не путать знак Pitch и не заявлять, что максимум Protect включает максимум дополнительного смешивания исходных features в этой реализации.
9. Не советуй глобально отключать антивирус/файрвол, скачивать случайные .exe/.pth или включать public sharing личного голоса.
10. Не считать голос успешно клонированным по названию профиля. Заявлять о действиях, прослушиваниях и измерениях только при фактическом доступе.
11. Музыкальный PART_2 с 70 IDs остаётся без изменений. В нём нет модели её голоса. Для персонального голосового процесса вести отдельный VOICE_STATE.
12. Темы и тренды стихов пока отложены. Применять существующую практику Lyrics из KB02/04 можно, но новый ресерч не выдумывать.

Формат короткого ответа:
Задача → разрешённый source/статус прав → лучший бесплатный маршрут → что установлено и чего ещё нет → input/target → настройки одной пробы → критерии сравнения → fallback → VOICE_STATE_DELTA.

## 7.16. VOICE_STATE — расширение паспорта песни
- song_id
- requested_route: Suno-native / Applio-local / Kits / Audimee / traditional-DSP
- source_origin: real-own-recording / Suno-output / third-party / unknown
- source_rights_for_external_AI: confirmed / clarification-needed / not-permitted / unknown
- source_filename / vocal-only / wetness / timing_origin
- target_voice_owner: myself
- own_dataset_status / clean_audio_minutes / training_data_rights
- gpu_model / vram / ram / driver / app_version
- model_file / matching_index / model_sample_rate / embedder / vocoder
- selected_checkpoint / why_selected
- inference_parameters / test_excerpt
- output_filename / actual_duration / alignment_checked
- likeness / diction / pitch / artifacts / dynamics / mix_result
- cloud_plan / monthly_or_annual / download_minutes / expiration_if_known
- current_extra_budget
- approved_variant / next_one_action

Шаблон не создаёт реальные файлы модели. Unknown — допустимое значение. Вне доступного чата не обещать надёжную память: выдавать актуальный паспорт для сохранения.

## 7.17. Следующий конкретный шаг
Существующий Gem и новую песню можно продолжать использовать. Для точного локального voice-setup нужны:
1. Название NVIDIA и объём VRAM.
2. Есть ли 10–30 минут собственных сухих реальных записей или пока только короткий референс?
3. Какой source планируется конвертировать и установлено ли разрешение на внешнее AI-использование?

После этого — одна короткая проба, а не покупка трёх подписок.

## 7.18. Доказательность и источники
Официальные страницы проверены 12.09.2026. Некоторые Help-статьи имеют даты 2024/2025 и сопоставлены с текущим pricing. Расхождения вынесены явно. Обучение, конверсия и слепое слуховое сравнение на записях пользовательницы не проводились. Проверка Python AST и pipeline подтверждает определения полей и условия кода, а не качество будущего аудио.

Основные прямые источники:
https://www.kits.ai/pricing
https://help.kits.ai/hc/en-us/articles/45057016270611-Voice-Changer-Kits-Studio
https://help.kits.ai/hc/en-us/articles/40742972060435-How-is-Instant-Voice-Cloning-different-from-Professional-Voice-Cloning
https://help.kits.ai/hc/en-us/articles/25367001343635-What-is-Professional-Voice-Cloning
https://help.kits.ai/hc/en-us/articles/25498080455187-What-happens-to-my-custom-trained-AI-voice-models-if-I-cancel-my-subscription
https://help.kits.ai/hc/en-us/articles/28297197996051-What-happens-to-my-download-minutes-after-I-cancel-my-subscription
https://docs.applio.org/getting-started/installation/
https://docs.applio.org/getting-started/training/
https://docs.applio.org/getting-started/inference/
https://docs.applio.org/guides/how-create-datasets/
https://github.com/IAHispano/Applio/releases/tag/3.6.4
https://github.com/IAHispano/Applio/blob/3.6.4/tabs/inference/inference.py
https://github.com/IAHispano/Applio/blob/3.6.4/rvc/infer/pipeline.py
https://ultimatevocalremover.com/
https://www.audacityteam.org/features/noise-reduction/
https://techivation.com/t-de-esser/
https://bertomaudio.com/denoiser-classic.html
https://www.auburnsounds.com/products/Graillon.html
https://www.reaper.fm/purchase.php
https://audimee.com/pricing
https://audimee.com/faq/subscription/managing-your-subscription
https://audimee.com/faq/licenses/data-ownership-and-storage
https://audimee.com/faq/subscription/commercial-use
https://www.lalal.ai/
https://suno.com/terms
https://splice.com/terms
