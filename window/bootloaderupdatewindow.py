from PySide6.QtWidgets import QProgressDialog
from locales import i18n_get


class BootloaderUpdateWindow(QProgressDialog):
    def __init__(self, parent=None):
        super(BootloaderUpdateWindow, self).__init__(parent)
        self.setWindowTitle(i18n_get("bootloader_settings_button"))
        self.setLabelText(i18n_get("bootloader_settings_box_progress"))
        self.setCancelButton(None)
        self.setMinimumDuration(0)
        self.setRange(0, 0)