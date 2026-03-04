from tkinter import *
from tkinter import messagebox


# ------------------ ПЕРВОЕ ОКНО ------------------

window = Tk()
window.geometry("600x400")
window.title("Library")


def Create_Account():
    login = enter_login.get()
    password = enter_password.get()

    if login == "" or password == "":
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return

    window.destroy()  # закрываем первое окно
    open_library(login)


# ------------------ ВТОРОЕ ОКНО ------------------

def open_library(username):
    new_window = Tk()
    new_window.geometry("600x500")
    new_window.title("Главное меню библиотеки")

    Label(new_window,
          text=f"Добро пожаловать, {username}!",
          font=("Arial", 16, "bold")).pack(pady=20)

    # ----- Функции -----

    def add_book():
        book_name = book_entry.get()

        if book_name == "":
            messagebox.showerror("Ошибка", "Введите название книги!")
        else:
            book_list.insert(END, book_name)
            book_entry.delete(0, END)

    def delete_book():
        selected = book_list.curselection()

        if not selected:
            messagebox.showerror("Ошибка", "Выберите книгу для удаления!")
        else:
            book_list.delete(selected)

    # ----- Интерфейс -----

    Label(new_window,
          text="Введите название книги:",
          font=("Arial", 12)).pack(pady=5)

    book_entry = Entry(new_window, width=30)
    book_entry.pack(pady=5)

    Button(new_window,
           text="Добавить книгу",
           bg="blue",
           fg="white",
           width=20,
           command=add_book).pack(pady=5)

    Button(new_window,
           text="Удалить выбранную книгу",
           bg="red",
           fg="white",
           width=20,
           command=delete_book).pack(pady=5)

    book_list = Listbox(new_window, width=50, height=15, font=("Arial", 12))
    book_list.pack(pady=20)

    new_window.mainloop()


# ------------------ ИНТЕРФЕЙС ПЕРВОГО ОКНА ------------------

Label(window,
      text="Создайте учетную запись",
      font=("Arial", 14, "bold")).pack(pady=20)

Label(window,
      text="Введите логин",
      font=("Arial", 12)).pack()

enter_login = Entry(window, width=25)
enter_login.pack(pady=5)

Label(window,
      text="Введите пароль",
      font=("Arial", 12)).pack()

enter_password = Entry(window, width=25, show="*")
enter_password.pack(pady=5)

Button(window,
       text="Создать",
       bg="green",
       fg="white",
       width=15,
       command=Create_Account).pack(pady=20)


window.mainloop()