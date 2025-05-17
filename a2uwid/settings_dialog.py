from aqt.qt import (
    QDialog,
    QButtonGroup,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QDialogButtonBox,
    QLabel,
)
from aqt import mw
from typing import Dict, Optional, cast


class SettingsDialog(QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("UWorld ID Extractor Settings")
        self.setMinimumWidth(300)

        layout: QVBoxLayout = QVBoxLayout(self)

        # Step group
        self.step_group = QButtonGroup(self)
        step_box = QGroupBox("Select Step")
        step_layout = QVBoxLayout()
        self.step1_radio = QRadioButton("Step1")
        self.step2_radio = QRadioButton("Step2")
        self.step_none_radio = QRadioButton("None")
        self.step_group.addButton(self.step1_radio)
        self.step_group.addButton(self.step2_radio)
        self.step_group.addButton(self.step_none_radio)
        step_layout.addWidget(self.step1_radio)
        step_layout.addWidget(self.step2_radio)
        step_layout.addWidget(self.step_none_radio)
        step_box.setLayout(step_layout)
        layout.addWidget(step_box)

        # Exam type group
        self.exam_group = QButtonGroup(self)
        exam_box = QGroupBox("Select Exam Type")
        exam_layout = QVBoxLayout()
        self.usmle_radio = QRadioButton("USMLE")
        self.comlex_radio = QRadioButton("COMLEX")
        self.exam_none_radio = QRadioButton("None")
        self.exam_group.addButton(self.usmle_radio)
        self.exam_group.addButton(self.comlex_radio)
        self.exam_group.addButton(self.exam_none_radio)
        exam_layout.addWidget(self.usmle_radio)
        exam_layout.addWidget(self.comlex_radio)
        exam_layout.addWidget(self.exam_none_radio)
        exam_box.setLayout(exam_layout)
        layout.addWidget(exam_box)

        # Load saved settings
        self._load_settings()

        # Buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.save_settings)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def _load_settings(self):
        step = self.config.get("step_filter", "None")
        exam = self.config.get("exam_filter", "None")
        if step == "Step1":
            self.step1_radio.setChecked(True)
        elif step == "Step2":
            self.step2_radio.setChecked(True)
        else:
            self.step_none_radio.setChecked(True)

        if exam == "USMLE":
            self.usmle_radio.setChecked(True)
        elif exam == "COMLEX":
            self.comlex_radio.setChecked(True)
        else:
            self.exam_none_radio.setChecked(True)

    @property
    def config(self) -> Dict:
        default: Dict = {"step_filter": None, "exam_filter": None}
        config: Optional[Dict] = mw.addonManager.getConfig(__name__)
        if config is None:
            mw.addonManager.writeConfig(__name__, default)
            return default
        else:
            return config

    @config.setter
    def config(self, val: Dict) -> None:
        mw.addonManager.writeConfig(__name__, val)

    def save_settings(self) -> None:
        config: Dict = self.config
        if self.step1_radio.isChecked():
            config["step_filter"] = "Step1"
        elif self.step2_radio.isChecked():
            config["step_filter"] = "Step2"
        else:
            config["step_filter"] = None

        if self.usmle_radio.isChecked():
            config["exam_filter"] = "Step"
        elif self.comlex_radio.isChecked():
            config["exam_filter"] = "COMLEX"
        else:
            config["exam_filter"] = None

        self.config = config
        self.accept()
