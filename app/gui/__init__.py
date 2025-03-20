import tkinter as tk

# Configuration globale pour les fenêtres
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

def set_window_size(window):
    """
    Configure la taille d'une fenêtre Tkinter.
    :param window: La fenêtre à configurer (Tk ou Toplevel).
    """
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

# Exporter les classes et la fonction
from .login import LoginWindow
from .main_window import MainApplication
from .registration import RegistrationWindow

__all__ = ["LoginWindow", "MainApplication", "RegistrationWindow", "set_window_size"]