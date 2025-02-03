from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from database import (
    init_db,
    Course,
    Lesson,
    User,
    UserProgress,
    Question,
    QuestionOption,
)
from datetime import datetime

import os
from dotenv import load_dotenv


class EducationBot:
    def __init__(self, token: str):
        self.token = token
        self.db = init_db()
        self.user_states = {}  # Хранит состояние пользователей
        self._init_demo_data()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Регистрируем пользователя, если он новый
        user = (
            self.db.query(User)
            .filter(User.telegram_id == update.effective_user.id)
            .first()
        )
        if not user:
            user = User(
                telegram_id=update.effective_user.id,
                username=update.effective_user.username,
            )
            self.db.add(user)
            self.db.commit()

        # Получаем все курсы из базы
        courses = self.db.query(Course).all()
        keyboard = []

        course_emojis = {"Общая фармакология": "🔬", "Антибиотики": "💊"}

        for course in courses:
            emoji = course_emojis.get(course.title, "📚")
            keyboard.append(
                [
                    InlineKeyboardButton(
                        f"{emoji} {course.title}", callback_data=f"course_{course.id}"
                    )
                ]
            )

        reply_markup = InlineKeyboardMarkup(keyboard)

        welcome_text = (
            "🎓 *Добро пожаловать в образовательный бот по фармакологии!*\n\n"
            "Здесь вы сможете:\n"
            "• Изучать материалы курсов 📚\n"
            "• Проходить тесты ✍️\n"
            "• Отслеживать свой прогресс 📊\n\n"
            "Выберите интересующий вас курс:"
        )

        await update.message.reply_text(
            welcome_text, reply_markup=reply_markup, parse_mode="Markdown"
        )

    @staticmethod
    def generate_progress_bar(current, total, length=10):
        filled = int(length * (current / total))
        empty = length - filled
        return "█" * filled + "░" * empty

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        def create_back_button(keyboard):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        "🏠 Вернуться в главное меню", callback_data="main_menu"
                    )
                ]
            )

        """Обработчик нажатий на кнопки"""
        query = update.callback_query
        await query.answer()

        if query.data == "main_menu":
            courses = self.db.query(Course).all()
            keyboard = []

            course_emojis = {"Общая фармакология": "🔬", "Антибиотики": "💊"}

            for course in courses:
                emoji = course_emojis.get(course.title, "📚")
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            f"{emoji} {course.title}",
                            callback_data=f"course_{course.id}",
                        )
                    ]
                )
            reply_markup = InlineKeyboardMarkup(keyboard)

            await query.edit_message_text(
                "🎓 *Выберите интересующий вас курс:*",
                reply_markup=reply_markup,
                parse_mode="Markdown",
            )

        elif query.data.startswith("course_"):
            course_id = int(query.data.replace("course_", ""))
            course = self.db.query(Course).filter(Course.id == course_id).first()
            if course:
                keyboard = []
                for lesson in course.lessons:
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                lesson.title,
                                callback_data=f"lesson_{course.id}_{lesson.id}",
                            )
                        ]
                    )

                create_back_button(keyboard)
                reply_markup = InlineKeyboardMarkup(keyboard)
                await query.edit_message_text(
                    f"📚 Курс: {course.title}\n" f"Выберите урок:",
                    reply_markup=reply_markup,
                )

        elif query.data.startswith("lesson_"):
            _, course_id, lesson_id = query.data.split("_")
            user_id = query.from_user.id
            self.user_states[user_id] = {
                "course_id": int(course_id),
                "lesson_id": int(lesson_id),
            }

            await query.edit_message_text("Введите код доступа к уроку:")

        elif query.data.startswith("answer_"):
            await self.handle_test_answer(update, context)

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        if user_id in self.user_states:
            state = self.user_states[user_id]

            # Если пользователь проходит тест
            if "test_mode" in state:
                await update.message.reply_text(
                    "Пожалуйста, используйте кнопки для ответа на вопросы теста"
                )
                return

            lesson = (
                self.db.query(Lesson).filter(Lesson.id == state["lesson_id"]).first()
            )

            if update.message.text == lesson.access_code:
                # Получаем вопросы для урока
                questions = (
                    self.db.query(Question)
                    .filter(Question.lesson_id == lesson.id)
                    .all()
                )

                lesson_text = (
                    f"✅ *Код верный!*\n\n"
                    f"📝 *{lesson.title}*\n"
                    f"───────────────\n\n"
                    f"{lesson.content}\n\n"
                    "───────────────\n"
                    "🚀 Готовы проверить свои знания?\n"
                    "Нажмите /test чтобы начать тестирование"
                )

                if not questions:
                    await update.message.reply_text(
                        f"✅ Код верный!\n\n"
                        f"📝 {lesson.title}\n\n"
                        f"{lesson.content}\n\n"
                        "К сожалению, для этого урока пока нет вопросов для тестирования."
                    )
                    return

                # Показываем содержимое урока
                await update.message.reply_text(lesson_text, parse_mode="Markdown")

                # Преобразуем вопросы в список словарей для удобства
                questions_data = []
                for question in questions:
                    options = (
                        self.db.query(QuestionOption)
                        .filter(QuestionOption.question_id == question.id)
                        .all()
                    )
                    options_data = []
                    for option in options:
                        options_data.append(
                            {"text": option.text, "is_correct": option.is_correct}
                        )
                    questions_data.append(
                        {
                            "id": question.id,
                            "text": question.text,
                            "options": options_data,
                        }
                    )

                # Обновляем состояние пользователя
                self.user_states[user_id].update(
                    {
                        "questions": questions_data,
                        "current_question": 0,
                        "correct_answers": 0,
                    }
                )
            else:
                await update.message.reply_text("❌ Неверный код. Попробуйте еще раз.")
        else:
            await update.message.reply_text(
                "Пожалуйста, выберите урок с помощью команды /start"
            )

    async def start_test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Начало тестирования"""
        user_id = update.message.from_user.id
        if user_id not in self.user_states:
            await update.message.reply_text("Сначала выберите урок с помощью /start")
            return

        state = self.user_states[user_id]
        if "questions" not in state:
            await update.message.reply_text("Сначала получите доступ к уроку")
            return

        if not state["questions"]:
            await update.message.reply_text(
                "К сожалению, для этого урока нет вопросов для тестирования"
            )
            return

        try:
            # Получаем первый вопрос
            question = state["questions"][state["current_question"]]

            # Создаем клавиатуру с вариантами ответов
            keyboard = []
            for i, option in enumerate(question["options"]):
                keyboard.append(
                    [InlineKeyboardButton(option["text"], callback_data=f"answer_{i}")]
                )

            reply_markup = InlineKeyboardMarkup(keyboard)

            await update.message.reply_text(
                f"Вопрос {state['current_question'] + 1} из {len(state['questions'])}:\n\n"
                f"{question['text']}",
                reply_markup=reply_markup,
            )

            # Отмечаем, что пользователь в режиме теста
            state["test_mode"] = True
        except Exception as e:
            await update.message.reply_text(
                f"Произошла ошибка при загрузке вопросов. Пожалуйста, начните урок заново с помощью /start"
            )
            print(f"Error in start_test: {e}")
            if user_id in self.user_states:
                del self.user_states[user_id]

    async def handle_test_answer(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        query = update.callback_query
        user_id = query.from_user.id
        state = self.user_states.get(user_id)

        if not state or "test_mode" not in state:
            await query.edit_message_text(
                "Произошла ошибка. Пожалуйста, начните тест заново с помощью /test"
            )
            return

        if not query.data.startswith("answer_"):
            return

        try:
            # Получаем номер выбранного ответа
            answer_index = int(query.data.split("_")[1])

            # Проверяем валидность индекса
            if answer_index >= len(
                state["questions"][state["current_question"]]["options"]
            ):
                await query.answer("Произошла ошибка с вариантом ответа")
                return

            question = state["questions"][state["current_question"]]

            # Проверяем правильность ответа
            is_correct = question["options"][answer_index]["is_correct"]
            if is_correct:
                state["correct_answers"] += 1
                await query.answer("✅ Правильно!")
            else:
                # Находим правильный ответ для показа
                correct_option = next(
                    opt for opt in question["options"] if opt["is_correct"]
                )
                await query.answer(
                    f"❌ Неправильно! Правильный ответ: {correct_option['text']}"
                )

            # Переходим к следующему вопросу
            state["current_question"] += 1

            # Если вопросы закончились, показываем результат
            if state["current_question"] >= len(state["questions"]):
                score = (state["correct_answers"] / len(state["questions"])) * 100
                progress_bar = self.generate_progress_bar(
                    state["correct_answers"], len(state["questions"])
                )

                result_text = (
                    "🎯 *Тест завершен!*\n\n"
                    f"Прогресс: {progress_bar}\n"
                    f"Правильных ответов: {state['correct_answers']} из {len(state['questions'])}\n"
                    f"Ваш результат: {score:.1f}%\n\n"
                    f"{'🎉 Отличная работа!' if score >= 80 else '💪 Продолжайте практиковаться!'}\n\n"
                    "Используйте /start чтобы выбрать новый урок"
                )

                # Сохраняем прогресс в базе данных
                try:
                    user = (
                        self.db.query(User).filter(User.telegram_id == user_id).first()
                    )
                    progress = UserProgress(
                        user_id=user.id,
                        lesson_id=state["lesson_id"],
                        test_score=int(score),
                    )
                    self.db.add(progress)
                    self.db.commit()
                except Exception as e:
                    print(f"Error saving progress: {e}")

                await query.edit_message_text(result_text, parse_mode="Markdown")
                # Очищаем состояние пользователя
                del self.user_states[user_id]

            else:
                # Показываем следующий вопрос
                next_question = state["questions"][state["current_question"]]
                keyboard = []
                for i, option in enumerate(next_question["options"]):
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                option["text"], callback_data=f"answer_{i}"
                            )
                        ]
                    )

                reply_markup = InlineKeyboardMarkup(keyboard)

                question_text = (
                    f"❓ *Вопрос {state['current_question'] + 1} из {len(state['questions'])}*\n\n"
                    f"{next_question['text']}"
                )

                await query.edit_message_text(
                    question_text, reply_markup=reply_markup, parse_mode="Markdown"
                )

        except Exception as e:
            print(f"Error in handle_test_answer: {e}")
            await query.edit_message_text(
                "Произошла ошибка при обработке ответа. Пожалуйста, начните тест заново с помощью /test"
            )
            if user_id in self.user_states:
                del self.user_states[user_id]

    def _init_demo_data(self):
        """Инициализация данных курса по фармакологии"""
        if not self.db.query(Course).first():
            from demo_data import DEMO_DATA

            for course_data in DEMO_DATA["courses"]:
                course = Course(title=course_data["title"])
                self.db.add(course)
                self.db.commit()

                for lesson_data in course_data["lessons"]:
                    lesson = Lesson(
                        title=lesson_data["title"],
                        content=lesson_data["content"],
                        access_code=lesson_data["access_code"],
                        course_id=course.id,
                    )
                    self.db.add(lesson)
                    self.db.commit()

                    # Добавляем вопросы и варианты ответов
                    for question_data in lesson_data["questions"]:
                        question = Question(
                            lesson_id=lesson.id, text=question_data["text"]
                        )
                        self.db.add(question)
                        self.db.commit()

                        for option_data in question_data["options"]:
                            option = QuestionOption(
                                question_id=question.id,
                                text=option_data["text"],
                                is_correct=option_data["is_correct"],
                            )
                            self.db.add(option)
                        self.db.commit()


def main():
    # Создаём бота и регистрируем обработчики

    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise ValueError("Не найден TELEGRAM_BOT_TOKEN в переменных окружения")

    bot = EducationBot(token)

    application = Application.builder().token(bot.token).build()

    async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        print(f"Exception while handling an update: {context.error}")

    application.add_error_handler(error_handler)

    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("test", bot.start_test))
    application.add_handler(CallbackQueryHandler(bot.button_handler))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_text)
    )

    print("Бот запущен...")
    application.run_polling()


# Этот блок тоже должен быть ВНЕ класса (без отступов)
if __name__ == "__main__":
    main()
