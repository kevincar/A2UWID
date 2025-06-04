import re
from re import Match, Pattern
from anki.notes import Note
from anki.cards import CardId
from aqt import QClipboard, mw
from aqt.utils import showWarning
from aqt.browser import Browser
from typing import Dict, List, Optional, Sequence, Set, cast


def get_uworld_ids_from_cards(browser: Browser):

    # Get selected card IDs
    selected_card_ids: Sequence[CardId] = browser.selectedCards()

    if not selected_card_ids:
        return

    # Map card IDs to note IDs
    note_ids: Set = {mw.col.get_card(c).nid for c in selected_card_ids}

    # Load config
    config: Dict = cast(Dict, mw.addonManager.getConfig(__name__))
    step_filter: str = config.get("step_filter", "Step2")
    exam_filter: str = config.get("exam_filter", "Step")
    if exam_filter is None or step_filter is None:
        showWarning(
            "WARNING!\n\nNo Step or exam type selected.\n"
            + "Set preferences in Settings for proper tag filtering.\n\n"
            + "IDs for multiple exams copied"
        )
        exam_filter = ""
        step_filter = ""

    pattern: Pattern = re.compile(
        r".*" + step_filter + r".*UWorld.*" + exam_filter + r"[^0-9]+(\d+)$"
    )
    uworld_ids: Set = set()

    for nid in note_ids:
        note: Note = mw.col.get_note(nid)
        for tag in note.tags:
            match: Optional[Match] = pattern.fullmatch(tag)
            if match:
                uworld_ids.add(match.group(1))

    if not uworld_ids:
        return

    # Create comma-separated list
    id_list: str = ", ".join(sorted(uworld_ids, key=int))
    clipboard: Optional[QClipboard] = mw.app.clipboard()
    if clipboard:
        clipboard.setText(id_list)
