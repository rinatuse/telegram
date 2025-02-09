DEMO_DATA = {
    "courses": [
        {
            "title": "Общая фармакология",
            "lessons": [
                {
                    "title": "Введение в фармакологию",
                    "content": """
Фармакология - это наука о лекарственных веществах и их действии на организм.

Основные разделы фармакологии:
1. Общая фармакология - изучает общие закономерности действия лекарств
2. Частная фармакология - изучает отдельные группы лекарственных средств
3. Клиническая фармакология - изучает применение лекарств в клинической практике

Ключевые понятия:
- Фармакокинетика - что происходит с лекарством в организме
- Фармакодинамика - как лекарство действует на организм
- Дозировка - количество лекарства, необходимое для достижения лечебного эффекта
""",
                    "access_code": "farm101",
                    "questions": [
                        {
                            "text": "Что изучает фармакология?",
                            "options": [
                                {
                                    "text": "Лекарственные вещества и их действие на организм",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Только способы приготовления лекарств",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Только народную медицину",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Только химический состав лекарств",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Какой раздел НЕ относится к фармакологии?",
                            "options": [
                                {"text": "Общая фармакология", "is_correct": False},
                                {"text": "Частная фармакология", "is_correct": False},
                                {
                                    "text": "Клиническая фармакология",
                                    "is_correct": False,
                                },
                                {"text": "Социальная фармакология", "is_correct": True},
                            ],
                        },
                        {
                            "text": "Что такое фармакодинамика?",
                            "options": [
                                {
                                    "text": "Как лекарство действует на организм",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Как организм действует на лекарство",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Способ приема лекарства",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Скорость выведения лекарства",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Что называется дозировкой лекарственного средства?",
                            "options": [
                                {
                                    "text": "Количество лекарства для достижения лечебного эффекта",
                                    "is_correct": True,
                                },
                                {"text": "Время приема лекарства", "is_correct": False},
                                {
                                    "text": "Способ производства лекарства",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Форма выпуска препарата",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Что изучает общая фармакология?",
                            "options": [
                                {
                                    "text": "Общие закономерности действия лекарств",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Только побочные эффекты",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Только способы применения",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Только взаимодействие лекарств",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Что такое фармакокинетика?",
                            "options": [
                                {
                                    "text": "Что происходит с лекарством в организме",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Скорость растворения таблетки",
                                    "is_correct": False,
                                },
                                {"text": "Производство лекарств", "is_correct": False},
                                {"text": "Хранение лекарств", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Какая наука изучает применение лекарств в клинической практике?",
                            "options": [
                                {
                                    "text": "Клиническая фармакология",
                                    "is_correct": True,
                                },
                                {"text": "Фармацевтика", "is_correct": False},
                                {"text": "Фармакогнозия", "is_correct": False},
                                {"text": "Токсикология", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое биодоступность?",
                            "options": [
                                {
                                    "text": "Доля лекарства, достигающая системного кровотока",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Скорость действия лекарства",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Время выведения лекарства",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Концентрация лекарства в таблетке",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Что изучает частная фармакология?",
                            "options": [
                                {
                                    "text": "Отдельные группы лекарственных средств",
                                    "is_correct": True,
                                },
                                {"text": "Общие закономерности", "is_correct": False},
                                {
                                    "text": "Только редкие препараты",
                                    "is_correct": False,
                                },
                                {"text": "Только рецептуру", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое период полувыведения?",
                            "options": [
                                {
                                    "text": "Время уменьшения концентрации препарата в крови вдвое",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Период хранения лекарства",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Время действия препарата",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Срок годности лекарства",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Какой путь введения лекарства считается энтеральным?",
                            "options": [
                                {
                                    "text": "Через желудочно-кишечный тракт",
                                    "is_correct": True,
                                },
                                {"text": "Внутривенно", "is_correct": False},
                                {"text": "Через кожу", "is_correct": False},
                                {"text": "Внутримышечно", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое толерантность к лекарственному препарату?",
                            "options": [
                                {
                                    "text": "Снижение эффективности при повторном применении",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Полное отсутствие эффекта",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Усиление действия препарата",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Индивидуальная непереносимость",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Как называется способность лекарства накапливаться в организме?",
                            "options": [
                                {"text": "Кумуляция", "is_correct": True},
                                {"text": "Адаптация", "is_correct": False},
                                {"text": "Абсорбция", "is_correct": False},
                                {"text": "Элиминация", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое идиосинкразия?",
                            "options": [
                                {
                                    "text": "Необычная реакция на обычные дозы лекарства",
                                    "is_correct": True,
                                },
                                {"text": "Привыкание к препарату", "is_correct": False},
                                {"text": "Правильная дозировка", "is_correct": False},
                                {
                                    "text": "Способ применения лекарства",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Какой путь введения обеспечивает самое быстрое действие препарата?",
                            "options": [
                                {"text": "Внутривенный", "is_correct": True},
                                {"text": "Пероральный", "is_correct": False},
                                {"text": "Подкожный", "is_correct": False},
                                {"text": "Ректальный", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое тахифилаксия?",
                            "options": [
                                {
                                    "text": "Быстрое снижение эффекта при повторном применении",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Усиление действия препарата",
                                    "is_correct": False,
                                },
                                {"text": "Медленное всасывание", "is_correct": False},
                                {"text": "Побочный эффект", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Как называется превращение лекарства в организме?",
                            "options": [
                                {"text": "Метаболизм", "is_correct": True},
                                {"text": "Абсорбция", "is_correct": False},
                                {"text": "Экскреция", "is_correct": False},
                                {"text": "Распределение", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое терапевтический индекс?",
                            "options": [
                                {
                                    "text": "Отношение токсической дозы к терапевтической",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Скорость выведения препарата",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Время действия лекарства",
                                    "is_correct": False,
                                },
                                {"text": "Концентрация в крови", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Какой орган является основным в метаболизме лекарств?",
                            "options": [
                                {"text": "Печень", "is_correct": True},
                                {"text": "Почки", "is_correct": False},
                                {"text": "Легкие", "is_correct": False},
                                {"text": "Сердце", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое плацебо?",
                            "options": [
                                {
                                    "text": "Лекарственная форма без действующего вещества",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Сильнодействующий препарат",
                                    "is_correct": False,
                                },
                                {"text": "Природное лекарство", "is_correct": False},
                                {"text": "Витаминный комплекс", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Как называется первое прохождение лекарства через печень?",
                            "options": [
                                {
                                    "text": "Эффект первого прохождения",
                                    "is_correct": True,
                                },
                                {"text": "Первичная абсорбция", "is_correct": False},
                                {"text": "Начальный метаболизм", "is_correct": False},
                                {"text": "Печеночный барьер", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое синергизм лекарственных веществ?",
                            "options": [
                                {
                                    "text": "Усиление действия при совместном применении",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Ослабление действия препаратов",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Отсутствие взаимодействия",
                                    "is_correct": False,
                                },
                                {"text": "Побочный эффект", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Какой путь выведения лекарств является основным?",
                            "options": [
                                {"text": "Почечный", "is_correct": True},
                                {"text": "Через кожу", "is_correct": False},
                                {"text": "Через легкие", "is_correct": False},
                                {"text": "Через кишечник", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Что такое антагонизм лекарственных веществ?",
                            "options": [
                                {
                                    "text": "Ослабление действия при совместном применении",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Усиление действия препаратов",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Отсутствие взаимодействия",
                                    "is_correct": False,
                                },
                                {"text": "Накопление в организме", "is_correct": False},
                            ],
                        },
                        {
                            "text": "Как называется наименьшая действующая доза лекарства?",
                            "options": [
                                {
                                    "text": "Минимальная терапевтическая доза",
                                    "is_correct": True,
                                },
                                {"text": "Токсическая доза", "is_correct": False},
                                {"text": "Летальная доза", "is_correct": False},
                                {"text": "Поддерживающая доза", "is_correct": False},
                            ],
                        },
                    ],
                },
                {
                    "title": "Лекарственные формы и пути введения",
                    "content": """
Лекарственные формы:
1. Твердые: таблетки, капсулы, порошки, гранулы
2. Жидкие: растворы, суспензии, эмульсии
3. Мягкие: мази, кремы, гели, суппозитории
4. Газообразные: аэрозоли, спреи

Пути введения лекарств:
1. Энтеральные:
   - Пероральный (через рот)
   - Сублингвальный (под язык)
   - Ректальный

2. Парентеральные:
   - Внутривенный
   - Внутримышечный
   - Подкожный
   - Внутрикожный

3. Ингаляционный

4. Местное применение:
   - Накожное
   - Глазные капли
   - Назальные спреи
""",
                    "access_code": "farm102",
                    "questions": [
                        {
                            "text": "Какая лекарственная форма относится к твердым?",
                            "options": [
                                {"text": "Таблетки", "is_correct": True},
                                {"text": "Сиропы", "is_correct": False},
                                {"text": "Мази", "is_correct": False},
                                {"text": "Аэрозоли", "is_correct": False},
                            ],
                        },
                    ],
                },
                {
                    "title": "История фармакологии",
                    "content": """
Основные этапы развития фармакологии:

Древний мир:
- Египетские папирусы с рецептами (XVI век до н.э.)
- Труды Гиппократа (V-IV век до н.э.)
- Работы Галена (II век н.э.)

Средние века:
- Развитие алхимии
- Труды Авиценны
- Появление первых аптек

Новое время:
- Парацельс и развитие ятрохимии
- Выделение морфина (1806)
- Синтез ацетилсалициловой кислоты (1897)

XX век:
- Открытие пенициллина (1928)
- Развитие химиотерапии
- Создание синтетических лекарств
""",
                    "access_code": "farm103",
                    "questions": [
                        {
                            "text": "Кто написал 'Канон врачебной науки'?",
                            "options": [
                                {"text": "Авиценна", "is_correct": True},
                                {"text": "Гиппократ", "is_correct": False},
                                {"text": "Гален", "is_correct": False},
                                {"text": "Парацельс", "is_correct": False},
                            ],
                        },
                    ],
                },
                {
                    "title": "Разработка и исследование лекарств",
                    "content": """
Этапы разработки лекарственных средств:

1. Поиск и создание новых соединений:
   - Химический синтез
   - Выделение из природных источников
   - Биотехнологические методы

2. Доклинические исследования:
   - Исследования in vitro
   - Опыты на животных
   - Изучение токсичности

3. Клинические исследования:
   - Фаза I: безопасность
   - Фаза II: эффективность
   - Фаза III: масштабные испытания
   - Фаза IV: пострегистрационные исследования

4. Регистрация и внедрение
""",
                    "access_code": "farm104",
                    "questions": [
                        {
                            "text": "Какая фаза клинических исследований оценивает безопасность препарата?",
                            "options": [
                                {"text": "Фаза I", "is_correct": True},
                                {"text": "Фаза II", "is_correct": False},
                                {"text": "Фаза III", "is_correct": False},
                                {"text": "Фаза IV", "is_correct": False},
                            ],
                        },
                    ],
                },
                {
                    "title": "Нормативное регулирование в фармакологии",
                    "content": """
Основные аспекты регулирования:

1. Законодательная база:
   - Федеральные законы
   - Постановления правительства
   - Приказы Минздрава

2. Контроль качества:
   - Государственная фармакопея
   - Стандарты GMP
   - Сертификация

3. Правила оборота:
   - Рецептурный отпуск
   - Безрецептурный отпуск
   - Списки контролируемых веществ

4. Фармаконадзор:
   - Мониторинг безопасности
   - Регистрация побочных эффектов
   - Пострегистрационное наблюдение
""",
                    "access_code": "farm105",
                    "questions": [
                        {
                            "text": "Что такое GMP?",
                            "options": [
                                {
                                    "text": "Надлежащая производственная практика",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Система контроля продаж",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Правила транспортировки",
                                    "is_correct": False,
                                },
                                {"text": "Стандарт хранения", "is_correct": False},
                            ],
                        },
                    ],
                },
            ],
        },
        {
            "title": "Антибиотики",
            "lessons": [
                {
                    "title": "Основы антибиотикотерапии",
                    "content": """
Антибиотики - это вещества природного или полусинтетического происхождения, подавляющие рост микроорганизмов или вызывающие их гибель.

Основные принципы антибиотикотерапии:
1. Выбор препарата с учетом чувствительности микроорганизма
2. Правильная дозировка и длительность курса
3. Учет противопоказаний и побочных эффектов
4. Мониторинг эффективности лечения

Механизмы действия антибиотиков:
- Нарушение синтеза клеточной стенки
- Нарушение синтеза белка
- Нарушение синтеза нуклеиновых кислот
- Нарушение функции клеточной мембраны

Понятие антибиотикорезистентности:
- Природная устойчивость
- Приобретенная устойчивость
- Механизмы развития резистентности
""",
                    "access_code": "anti101",
                    "questions": [
                        {
                            "text": "Что такое антибиотики?",
                            "options": [
                                {
                                    "text": "Вещества, подавляющие рост микроорганизмов или вызывающие их гибель",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Вещества, укрепляющие иммунитет",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Противовирусные препараты",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Противоаллергические средства",
                                    "is_correct": False,
                                },
                            ],
                        },
                        {
                            "text": "Что такое антибиотикорезистентность?",
                            "options": [
                                {
                                    "text": "Устойчивость микроорганизмов к действию антибиотиков",
                                    "is_correct": True,
                                },
                                {
                                    "text": "Аллергия на антибиотики",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Побочный эффект антибиотиков",
                                    "is_correct": False,
                                },
                                {
                                    "text": "Способ применения антибиотиков",
                                    "is_correct": False,
                                },
                            ],
                        },
                    ],
                },
                {
                    "title": "Пенициллины и цефалоспорины",
                    "content": """
Бета-лактамные антибиотики:

Пенициллины:
1. Природные (бензилпенициллин)
2. Полусинтетические:
   - Оксациллин
   - Ампициллин
   - Амоксициллин

Цефалоспорины:
1. I поколение (цефазолин)
2. II поколение (цефуроксим)
3. III поколение (цефтриаксон)
4. IV поколение (цефепим)
5. V поколение (цефтаролин)

Механизм действия:
- Нарушение синтеза пептидогликана
- Бактерицидный эффект
""",
                    "access_code": "anti102",
                    "questions": [
                        {
                            "text": "К какому поколению относится цефтриаксон?",
                            "options": [
                                {"text": "III поколение", "is_correct": True},
                                {"text": "II поколение", "is_correct": False},
                                {"text": "IV поколение", "is_correct": False},
                                {"text": "I поколение", "is_correct": False},
                            ],
                        }
                    ],
                },
                {
                    "title": "Макролиды и аминогликозиды",
                    "content": """
Макролиды:
- Эритромицин
- Азитромицин
- Кларитромицин
- Джозамицин

Особенности макролидов:
1. Механизм действия
2. Спектр активности
3. Показания к применению
4. Побочные эффекты

Аминогликозиды:
- Стрептомицин
- Гентамицин
- Амикацин
- Тобрамицин

Характеристики аминогликозидов:
1. Бактерицидное действие
2. Постантибиотический эффект
3. Ототоксичность
4. Нефротоксичность
""",
                    "access_code": "anti103",
                    "questions": [
                        {
                            "text": "Какой препарат относится к макролидам?",
                            "options": [
                                {"text": "Азитромицин", "is_correct": True},
                                {"text": "Амикацин", "is_correct": False},
                                {"text": "Ампициллин", "is_correct": False},
                                {"text": "Цефазолин", "is_correct": False},
                            ],
                        }
                    ],
                },
                {
                    "title": "Тетрациклины и фторхинолоны",
                    "content": """
Тетрациклины:
- Тетрациклин
- Доксициклин
- Миноциклин
- Тигециклин

Характеристики тетрациклинов:
1. Широкий спектр действия
2. Бактериостатический эффект
3. Особенности применения
4. Противопоказания

Фторхинолоны:
1. Поколения:
   - I (налидиксовая кислота)
   - II (ципрофлоксацин)
   - III (левофлоксацин)
   - IV (моксифлоксацин)

2. Особенности:
   - Бактерицидное действие
   - Биодоступность
   - Показания
   - Побочные эффекты
""",
                    "access_code": "anti104",
                    "questions": [
                        {
                            "text": "Какой тип действия характерен для тетрациклинов?",
                            "options": [
                                {"text": "Бактериостатический", "is_correct": True},
                                {"text": "Бактерицидный", "is_correct": False},
                                {"text": "Фунгицидный", "is_correct": False},
                                {"text": "Противовирусный", "is_correct": False},
                            ],
                        }
                    ],
                },
                {
                    "title": "Комбинированная антибиотикотерапия",
                    "content": """
Принципы комбинированной терапии:
1. Показания:
   - Тяжелые инфекции
   - Полимикробные инфекции
   - Профилактика резистентности

2. Виды комбинаций:
   - Синергидные
   - Аддитивные
   - Антагонистические

3. Правила комбинирования:
   - Совместимость препаратов
   - Учет механизмов действия
   - Мониторинг побочных эффектов

4. Примеры комбинаций:
   - Амоксициллин + клавулановая кислота
   - Триметоприм + сульфаметоксазол
   - Ампициллин + гентамицин
""",
                    "access_code": "anti105",
                    "questions": [
                        {
                            "text": "Какой тип взаимодействия антибиотиков наиболее желателен при комбинированной терапии?",
                            "options": [
                                {"text": "Синергидный", "is_correct": True},
                                {"text": "Антагонистический", "is_correct": False},
                                {"text": "Нейтральный", "is_correct": False},
                                {"text": "Индифферентный", "is_correct": False},
                            ],
                        }
                    ],
                },
            ],
        },
        {
            "title": "Сердечно-сосудистые препараты",
            "lessons": [
                {
                    "title": "Антигипертензивные средства",
                    "content": """
Препараты для лечения артериальной гипертензии:

1. Ингибиторы АПФ:
   - Эналаприл
   - Лизиноприл
   - Рамиприл
   - Периндоприл

2. Блокаторы кальциевых каналов:
   - Амлодипин
   - Нифедипин
   - Верапамил

3. Бета-адреноблокаторы:
   - Бисопролол
   - Метопролол
   - Атенолол

4. Диуретики:
   - Гидрохлортиазид
   - Индапамид
   - Фуросемид

Принципы лечения гипертонии:
- Индивидуальный подбор терапии
- Регулярный контроль АД
- Длительное применение
- Комбинированная терапия при необходимости
""",
                    "access_code": "card101",
                    "questions": [
                        {
                            "text": "К какой группе относится эналаприл?",
                            "options": [
                                {"text": "Ингибиторы АПФ", "is_correct": True},
                                {"text": "Бета-блокаторы", "is_correct": False},
                                {
                                    "text": "Блокаторы кальциевых каналов",
                                    "is_correct": False,
                                },
                                {"text": "Диуретики", "is_correct": False},
                            ],
                        }
                    ],
                },
                {
                    "title": "Антиангинальные средства",
                    "content": """
Препараты для лечения ишемической болезни сердца:

1. Нитраты:
   - Нитроглицерин
   - Изосорбида динитрат
   - Изосорбида мононитрат

2. Бета-адреноблокаторы в кардиологии:
   - Механизм антиангинального действия
   - Показания к применению
   - Противопоказания

3. Антиагреганты:
   - Ацетилсалициловая кислота
   - Клопидогрел
   - Тикагрелор

4. Статины:
   - Аторвастатин
   - Розувастатин
   - Симвастатин
""",
                    "access_code": "card102",
                },
                {
                    "title": "Антиаритмические препараты",
                    "content": """
Классификация антиаритмических препаратов:

Класс I (блокаторы натриевых каналов):
- IA (хинидин, прокаинамид)
- IB (лидокаин, мексилетин)
- IC (пропафенон, флекаинид)

Класс II (бета-адреноблокаторы):
- Пропранолол
- Метопролол
- Бисопролол

Класс III (блокаторы калиевых каналов):
- Амиодарон
- Соталол
- Дронедарон

Класс IV (блокаторы кальциевых каналов):
- Верапамил
- Дилтиазем
""",
                    "access_code": "card103",
                },
                {
                    "title": "Сердечные гликозиды",
                    "content": """
Сердечные гликозиды и их применение:

1. Препараты:
   - Дигоксин
   - Строфантин
   - Коргликон

2. Механизм действия:
   - Влияние на Na+/K+-АТФазу
   - Инотропный эффект
   - Влияние на проводимость

3. Показания:
   - Сердечная недостаточность
   - Мерцательная аритмия
   - Трепетание предсердий

4. Побочные эффекты и токсичность:
   - Аритмии
   - Тошнота, рвота
   - Нарушения зрения
""",
                    "access_code": "card104",
                },
                {
                    "title": "Гиполипидемические средства",
                    "content": """
Препараты для коррекции липидного обмена:

1. Статины:
   - Механизм действия
   - Основные представители
   - Показания к применению
   - Побочные эффекты

2. Фибраты:
   - Механизм действия
   - Представители группы
   - Особенности применения

3. Секвестранты желчных кислот:
   - Принцип действия
   - Показания
   - Противопоказания

4. Ингибиторы PCSK9:
   - Новый класс препаратов
   - Механизм действия
   - Клиническое применение
""",
                    "access_code": "card105",
                },
            ],
        },
    ]
}
