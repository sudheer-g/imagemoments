__author__ = 'Sudheer'
import tkMessageBox

import sys

from gui.basic_gui_layout import main_window


if __name__ == "__main__":
    try:
        main_window()
    except RuntimeError as e:
        tkMessageBox.showerror("Error", "An Unexpected Error Occurred")
    sys.exit(0)
