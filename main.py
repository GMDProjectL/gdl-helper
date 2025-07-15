#!/usr/bin/env python3
import os
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from window.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()