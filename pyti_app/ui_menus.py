"""Build application-wide menus for the main window."""

from PySide6.QtWidgets import QMenuBar

from .example_dialog import zeige_beispiele


def baue_menues(window, basis_pfad):
    menu_bar = QMenuBar(window)
    tools = menu_bar.addMenu("Werkzeuge")
    examples = tools.addAction("Beispiele")
    examples.setToolTip("Öffnet das allgemeine Pyti-Cookbook")
    examples.triggered.connect(lambda: zeige_beispiele(window, basis_pfad))
    admin = tools.addAction("Administration")
    admin.setToolTip("Systemstatus, Einstellungen und Level verwalten")
    creator = tools.addAction("Eigenes Level erstellen")
    creator.setToolTip("Level entwerfen und als Python-Datei exportieren")
    help_menu = menu_bar.addMenu("Hilfe")
    about = help_menu.addAction("Über Pyti")
    about.setToolTip("Projektinformationen, Mitwirkende und Sicherheitshinweise")
    return menu_bar, (tools, help_menu), (examples, admin, creator, about)
