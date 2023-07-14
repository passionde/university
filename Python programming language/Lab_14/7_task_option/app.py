import crud

# Добавление преподавателей
# crud.add_teacher("Иванов Иван Иванович")
# crud.add_teacher("Гончаров Дмитрий Алексеевич")
# crud.add_teacher("Покачеев Сергей Михайлович")
# crud.add_teacher("Михайлова Нина Петровна")

# Добавление вида контроля
# crud.add_kind_control("Зачет")
# crud.add_kind_control("Зачет с оценкой")
# crud.add_kind_control("Экзамен")

# Добавление дисциплин
# crud.add_discipline(1, "Математика", 5, 2, 1)
# crud.add_discipline(2, "Русский язык", 10, 5, 0)
# crud.add_discipline(3, "Информатика", 2, 1, 1)
# crud.add_discipline(1, "История", 3, 0, 8)

# Назначение преподавателей на дисциплины
# crud.append_teachers_to_disciplines(1, [3, 4])
# crud.append_teachers_to_disciplines(2, [1])
# crud.append_teachers_to_disciplines(3, [2])
# crud.append_teachers_to_disciplines(4, [1, 2, 3, 4])

# Вывод информации
crud.all_disciplines()
crud.all_teachers()