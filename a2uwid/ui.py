from aqt.browser import Browser
from aqt.qt import QAction, QDialog, QVBoxLayout, QTextEdit, QPushButton
from .extract import get_uworld_ids_from_cards
from .settings_dialog import SettingsDialog


# Add action to Browser context menu
def on_browser_will_show(browser: Browser) -> None:
    action: QAction = QAction("A2UWID: Get IDs", browser)
    action.triggered.connect(lambda: get_uworld_ids_from_cards(browser))
    browser.form.menuEdit.addAction(action)

    settings_action: QAction = QAction("A2UWID: settings", browser)
    settings_action.triggered.connect(lambda: SettingsDialog(browser).exec())
    browser.form.menuEdit.addAction(settings_action)
