from tkinter import Tk, ttk
from ui.ui import UI

def main():

    window = Tk()
    window.title("ShoppingListApp")
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()