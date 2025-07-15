from PySide6.QtWidgets import QWidget, QProgressDialog
from PySide6.QtCore import QThread, Signal
import os


class BootloaderUpdateThread(QThread):
    done = Signal(int)

    def __init__(self):
        super(BootloaderUpdateThread, self).__init__()

    def run(self):
        result = os.system('pkexec grub-mkconfig -o /boot/grub/grub.cfg')
        self.done.emit(result)