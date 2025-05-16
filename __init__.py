from aqt.gui_hooks import browser_will_show

from .extract import *
from .ui import on_browser_will_show

# Register hook
browser_will_show.append(on_browser_will_show)
