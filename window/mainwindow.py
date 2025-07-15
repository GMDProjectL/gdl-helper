import os
from PySide6.QtWidgets import QWidget, QMessageBox
from ui_generated.ui_mainwindow import Ui_MainWindow
from locales import i18n_get
from window.bootloaderupdatewindow import BootloaderUpdateWindow
from bootloader_update_thread import BootloaderUpdateThread


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit_button.clicked.connect(self.close)
        self.ui.remove_lockfile_button.clicked.connect(self.remove_lockfile_pressed)
        self.ui.envvars_button.clicked.connect(self.envvars_pressed)
        self.ui.bootloader_settings_button.clicked.connect(self.bootloader_settings_pressed)
        self.translate_ui()
    
    def translate_ui(self):
        self.ui.remove_lockfile_button.setText(i18n_get("remove_lockfile_button"))
        self.ui.envvars_button.setText(i18n_get("envvars_button"))
        self.ui.bootloader_settings_button.setText(i18n_get("bootloader_settings_button"))
        self.ui.quit_button.setText(i18n_get("quit_button"))
    
    def remove_lockfile_pressed(self):
        reply = QMessageBox.question(self, 
                                     i18n_get("remove_lockfile_button"),
                                     i18n_get("remove_lockfile_box_text"),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            result = os.system('pkexec rm -f /var/lib/pacman/db.lck')
            if result != 0:
                QMessageBox.critical(self, 
                                     i18n_get("remove_lockfile_button"), 
                                     i18n_get("remove_lockfile_box_error"))
                return
            
            QMessageBox.information(self, 
                                    i18n_get("remove_lockfile_button"), 
                                    i18n_get("remove_lockfile_box_success"))
    
    def envvars_pressed(self):
        os.system('kwrite /etc/environment')
    
    def bootloader_settings_pressed(self):
        old_content = ''
        if os.path.exists('/etc/default/grub'):
            with open('/etc/default/grub', 'r') as f:
                old_content = f.read()
        
        os.system('kwrite /etc/default/grub')

        new_content = ''
        if os.path.exists('/etc/default/grub'):
            with open('/etc/default/grub', 'r') as f:
                new_content = f.read()
        
        if old_content == new_content:
            return
        
        question = QMessageBox.question(self, 
                                        i18n_get("bootloader_settings_button"), 
                                        i18n_get("bootloader_settings_box_text"),
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if question == QMessageBox.No:
            return
        
        self.bootloader_update_window = BootloaderUpdateWindow(self)

        self.working_thread = BootloaderUpdateThread()
        self.working_thread.done.connect(self.bootloader_update_finished)

        self.working_thread.start()
        self.bootloader_update_window.show()
    
    def bootloader_update_finished(self, result):
        self.bootloader_update_window.close()

        if result == 0:
            QMessageBox.information(self, 
                                    i18n_get("bootloader_settings_button"), 
                                    i18n_get("bootloader_settings_box_success"))
        else:
            QMessageBox.critical(self, 
                                 i18n_get("bootloader_settings_button"), 
                                 i18n_get("bootloader_settings_box_error"))