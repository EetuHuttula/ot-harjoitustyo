"""Base view class for common UI functionality."""

from tkinter import ttk, StringVar, constants


class BaseView:
    """Base class for all UI views."""

    def __init__(self, root):
        """Initialize base view.
        
        Args:
            root: Parent Tk widget
        """
        self._root = root
        self._frame = None
        self._message_variable = None

    def pack(self):
        """Pack the frame into the parent widget."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy the frame and its contents."""
        if self._frame:
            self._frame.destroy()

    def _error(self, message):
        """Display error message.

        Args:
            message: Error message to display
        """
        self._message_variable.set(message)

    def _create_form_field(self, row, label_text, show_char=None):
        """Create a label and entry field pair.
        
        Args:
            row: Grid row position
            label_text: Text for the label
            show_char: Character to show for password fields (e.g., '*')
            
        Returns:
            The Entry widget
        """
        label = ttk.Label(master=self._frame, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5)
        
        entry = ttk.Entry(master=self._frame)
        if show_char:
            entry.config(show=show_char)
        entry.grid(row=row, column=1, padx=5, pady=5)
        
        return entry
