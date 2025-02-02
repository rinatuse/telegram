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
                                {"text": "Лекарственные вещества и их действие на организм", "is_correct": True},
                                {"text": "Только способы приготовления лекарств", "is_correct": False},
                                {"text": "Только народную медицину", "is_correct": False},
                                {"text": "Только химический состав лекарств", "is_correct": False}
                            ]
                        },
                        {
                            "text": "Какой раздел НЕ относится к фармакологии?",
                            "options": [
                                {"text": "Общая фармакология", "is_correct": False},
                                {"text": "Частная фармакология", "is_correct": False},
                                {"text": "Клиническая фармакология", "is_correct": False},
                                {"text": "Социальная фармакология", "is_correct": True}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "title": "Антибиотики",
            "lessons": [
                {
                    "title": "Пенициллины",
                    "content": """
Пенициллины - это группа антибиотиков, имеющих в своей структуре 6-аминопенициллановую кислоту.

История открытия:
- 1928 год - Александр Флеминг открыл пенициллин
- 1940 год - начало промышленного производства

Механизм действия:
Пенициллины нарушают синтез клеточной стенки бактерий, что приводит к их гибели.

Применение:
1. Лечение инфекций дыхательных путей
2. Лечение инфекций мочевыводящих путей
3. Профилактика послеоперационных осложнений

Побочные эффекты:
- Аллергические реакции
- Дисбактериоз
- Тошнота и диарея
""",  
                    "access_code": "farm201",
                    "questions": [
                        {
                            "text": "Что лежит в основе структуры пенициллинов?",
                            "options": [
                                {"text": "6-аминопенициллановая кислота", "is_correct": True},
                                {"text": "7-аминоцефалоспорановая кислота", "is_correct": False},
                                {"text": "Бета-лактамное кольцо", "is_correct": False},
                                {"text": "Тиазолидиновое кольцо", "is_correct": False}
                            ]
                        },
                        {
                            "text": "Какой механизм действия пенициллинов?",
                            "options": [
                                {"text": "Нарушение синтеза клеточной стенки бактерий", "is_correct": True},
                                {"text": "Нарушение синтеза белка", "is_correct": False},
                                {"text": "Нарушение синтеза ДНК", "is_correct": False},
                                {"text": "Нарушение энергетического обмена", "is_correct": False}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}