from aqt.browser import Browser
from aqt.qt import QAction, QDialog, QVBoxLayout, QTextEdit, QPushButton
from .extract import get_uworld_ids_from_cards


# Add action to Browser context menu
def on_browser_will_show(browser: Browser) -> None:
    action: QAction = QAction("Get UWorld IDs from Cards", browser)
    action.triggered.connect(lambda: get_uworld_ids_from_cards(browser))
    browser.form.menuEdit.addAction(action)
