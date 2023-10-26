# main.py
from notes_manager import NotesManager

def main():
    db_name = 'notes.db'
    manager = NotesManager(db_name)

    while True:
        print("1. Добавить новую заметку")
        print("2. Просмотреть список всех заметок")
        print("3. Просмотреть заметку")
        print("4. Поиск заметок")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            manager.add_note(title, content)
        elif choice == '2':
            notes = manager.view_all_notes()
            for note in notes:
                print(f"ID: {note[0]}, Заголовок: {note[1]}")
        elif choice == '3':
            note_id = input("Введите ID заметки, которую вы хотите просмотреть: ")
            note = manager.get_note_by_id(note_id)
            if note:
                print(f"Заголовок: {note[1]}\nСодержание: {note[2]}")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == '4':
            keyword = input("Введите ключевое слово для поиска: ")
            results = manager.search_notes(keyword)
            for note in results:
                print(f"ID: {note[0]}, Заголовок: {note[1]}")
        elif choice == '5':
            note_id = input("Введите ID заметки, которую вы хотите удалить: ")
            manager.delete_note(note_id)
        elif choice == '6':
            manager.close()
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
