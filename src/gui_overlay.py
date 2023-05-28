import tkinter as tk


class Overlay:
    """
    A class that creates an overlay window.

    Args:
        txt: The text to display in the overlay window.
        font: The font to use for the text in the overlay window.
    """

    def __init__(self, txt: str = "Listening...", font=("Helvetica", 16)) -> None:
        """
        Initialize the overlay window.
        """
        # Create the root window.
        self.root = tk.Tk()

        # Set the window properties.
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg='white')

        # Calculate the window size.
        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # Set the window geometry.
        self.root.geometry("+{}+{}".format(width - 150, height - 90))

        # Create the label.
        self.label = tk.Label(self.root, text=txt, font=font, bg='white')

        # Pack the label.
        self.label.pack(padx=10, pady=5)

    def __enter__(self) -> "Overlay":
        # Update the window.
        self.root.update()

        # Deiconify the window.
        self.root.deiconify()

        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        # Destroy the window.
        self.root.destroy()
