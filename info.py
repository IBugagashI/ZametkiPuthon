import Note

def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\n1 - вывод всех заметок из файла\n2 - добавить заметку\n3 - удалить заметку\n4 - редактировать заметку\n5 - выбрать заметку по дате\n6 - показать заметку по id\n7 - выход\n\nВведите число: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Работа завершена")