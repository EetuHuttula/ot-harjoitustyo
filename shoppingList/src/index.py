"""Main entry point for the shopping list application."""

from tkinter import Tk
from ui.ui import UI


def main():
    """Initialize and start the shopping list application."""
    window = Tk()
    window.title("ShoppingListApp")
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
