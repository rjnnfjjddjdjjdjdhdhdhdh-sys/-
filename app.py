"""
======================================================
    модуль вывода информации в консоль
======================================================
"""


from storage import load_collection, save_collection
from view import show_menu, show_collection
from core import delete_tasks, edit_task, add_task
from utilits import check_confirm
"""основной цикл"""

def app():
    name_file = "saves.txt"
    collection = load_collection([], name_file)
    is_running = True

    while is_running:
        print('1 - посмотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактирование'
              '\n4 - снять задачу'
              '\n5 - выход')
        choice_user = input("введите команду: ")

        match str(choice_user):
            case "1":  # просмотр списка
                show_collection(collection)
            case "2":  # добавление в список
                add_task(collection, name_file)
            case "3":  # изменение элемента
                edit_task(collection)
                save_collection(collection, name_file)
            case "4":  # удаление элемента
                show_collection(collection)
                delete_tasks(collection)
                save_collection(collection, name_file)
            case "5":  # завершение цикла
                is_running = check_confirm('отключение...')
            case _:  # неверная команда
                print('неверная команда')
                show_menu()

app()