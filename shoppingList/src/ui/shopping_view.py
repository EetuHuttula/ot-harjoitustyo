"""Shopping view module for showing and editing a user's shopping list."""
 # AI generated styles on this view
 
from tkinter import ttk, StringVar, constants
from services.shopping_list_service import ShoppingListService


class ShoppingView:
    """A view that shows a user's shopping list and allows add/remove."""

    def __init__(self, root, username, logout_handler):
        self._root = root
        self._username = username
        self._logout_handler = logout_handler
        self._frame = None
        self._service = ShoppingListService()
        self._listbox = None
        self._message_var = StringVar()
        self._name_entry = None
        self._amount_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _initialize_title(self, frame):
        """Initialize title label."""
        title = ttk.Label(master=frame, text=f"{self._username}")
        title.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="w")

    def _initialize_add_products_section(self, frame):
        """Initialize add products form section."""
        label = ttk.Label(master=frame, text="Add Products")
        label.grid(row=1, column=0, columnspan=3, pady=(0, 10), sticky="w")
        
        name_label = ttk.Label(master=frame, text="Item Name:")
        name_label.grid(row=2, column=0, padx=(0, 10), pady=3, sticky="w")
        self._name_entry = ttk.Entry(master=frame, width=30)
        self._name_entry.grid(row=2, column=1, pady=3, sticky="ew")

        amount_label = ttk.Label(master=frame, text="Amount:")
        amount_label.grid(row=3, column=0, padx=(0, 10), pady=3, sticky="w")
        self._amount_entry = ttk.Entry(master=frame, width=30)
        self._amount_entry.grid(row=3, column=1, pady=3, sticky="ew")

    def _initialize_buttons(self, frame):
        """Initialize action buttons."""
        add_button = ttk.Button(
            master=frame, 
            text="Add To List", 
            command=self._add_item_handler,
            width=12
        )
        add_button.grid(row=4, column=0, padx=(0, 5), pady=3)

        remove_button = ttk.Button(
            master=frame, 
            text="Remove Item", 
            command=self._remove_item_handler,
            width=12
        )
        remove_button.grid(row=4, column=1, padx=(0, 5), pady=3)

        clear_button = ttk.Button(
            master=frame, 
            text="Clear All", 
            command=self._clear_all_handler,
            width=12
        )
        clear_button.grid(row=4, column=2, padx=(0, 5), pady=3)

    def _initialize_action_buttons(self, frame):
        """Initialize additional action buttons: copy and logout."""
        copy_button = ttk.Button(
            master=frame,
            text="Copy to Clipboard",
            command=self._copy_to_clipboard_handler,
            width=16
        )
        copy_button.grid(row=7, column=0, padx=(0, 5), pady=(10, 3), sticky="w")

        logout_button = ttk.Button(
            master=frame,
            text="Logout",
            command=self._logout_handler,
            width=12
        )
        logout_button.grid(row=7, column=2, padx=(0, 5), pady=(10, 3), sticky="e")

    def _initialize_message_label(self, frame):
        """Initialize message display label."""
        message_label = ttk.Label(
            master=frame, 
            textvariable=self._message_var, 
            foreground="green"
        )
        message_label.grid(row=5, column=0, columnspan=3, pady=(0, 10), sticky="w")

    def _initialize_shopping_list(self, frame):
        """Initialize shopping list display."""
        list_label = ttk.Label(
            master=frame, 
            text="Shopping List", 
            font=("Helvetica", 11, "bold")
        )
        list_label.grid(row=6, column=0, columnspan=3, sticky="w", pady=(0, 5))

        self._listbox = ttk.Treeview(
            master=frame, 
            columns=("item", "amount"), 
            show="headings",
            height=10
        )
        self._listbox.heading("item", text="Item")
        self._listbox.heading("amount", text="Amount")
        self._listbox.column("item", width=200, anchor="w")
        self._listbox.column("amount", width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(
            master=frame, 
            orient="vertical", 
            command=self._listbox.yview
        )
        self._listbox.configure(yscrollcommand=scrollbar.set)
        
        self._listbox.grid(row=6, column=0, columnspan=3, sticky="nsew")
        scrollbar.grid(row=6, column=3, sticky="ns")

    def _initialize(self):
        """Initialize the shopping view UI components."""
        frame = ttk.Frame(master=self._root, padding="10")
        self._frame = frame
        
        self._initialize_title(frame)
        self._initialize_add_products_section(frame)
        self._initialize_buttons(frame)
        self._initialize_message_label(frame)
        self._initialize_shopping_list(frame)
        self._initialize_action_buttons(frame)

        self._refresh_list()

    def _refresh_list(self):
        """Refresh the shopping list display."""
        for row in self._listbox.get_children():
            self._listbox.delete(row)
        items = self._service.get_shopping_list(self._username)
        for item in items:
            self._listbox.insert(
                "", 
                "end", 
                iid=str(item.id), 
                values=(item.name, item.amount)
            )

    def _show_message(self, message, clear_after_ms=2000):
        """Display a message and optionally clear it after a delay.
        
        Args:
            message: Message to display
            clear_after_ms: Milliseconds before clearing message (0 to not clear)
        """
        self._message_var.set(message)
        if clear_after_ms > 0:
            self._root.after(clear_after_ms, lambda: self._message_var.set(""))

    def _add_item_handler(self):
        """Handle adding a new item to the shopping list."""
        name = self._name_entry.get().strip()
        amount = self._amount_entry.get().strip()
        
        if not name:
            self._show_message("⚠️ Item name is required", clear_after_ms=0)
            return
        
        try:
            self._service.add_item(self._username, name, amount)
            self._name_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)
            self._show_message("✓ Item added successfully!")
            self._refresh_list()
        except Exception as e:
            self._show_message(f"⚠️ Error: {str(e)}", clear_after_ms=0)

    def _remove_item_handler(self):
        """Handle removing selected item from the shopping list."""
        selection = self._listbox.selection()
        if not selection:
            self._show_message("⚠️ Please select an item to remove", clear_after_ms=0)
            return
        
        try:
            item_id = selection[0]
            self._service.remove_item(self._username, int(item_id))
            self._show_message("✓ Item removed successfully!")
            self._refresh_list()
        except Exception as e:
            self._show_message(f"⚠️ Error: {str(e)}", clear_after_ms=0)

    def _clear_all_handler(self):
        """Handle clearing all items from the shopping list."""
        try:
            self._service.clear_list(self._username)
            self._show_message("✓ All items cleared!")
            self._refresh_list()
        except Exception as e:
            self._show_message(f"⚠️ Error: {str(e)}", clear_after_ms=0)

    def _copy_to_clipboard_handler(self):
        """Format the shopping list and copy to system clipboard."""
        try:
            items = self._service.get_shopping_list(self._username)
            if not items:
                self._show_message("⚠️ List is empty", clear_after_ms=2000)
                return

            lines = ["Shopping List:"]
            for it in items:
                amt = it.amount
                lines.append(f"- {amt} {it.name}")

            text = "\n".join(lines)
            try:
                self._root.clipboard_clear()
                self._root.clipboard_append(text)
            except Exception:
                self._show_message("⚠️ Could not access clipboard", clear_after_ms=0)
                return

            self._show_message("✓ Copied to clipboard!")
        except Exception as e:
            self._show_message(f"⚠️ Error: {str(e)}", clear_after_ms=0)