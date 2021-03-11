from __future__ import annotations


import AppFiles.AppInterfaceClasses.MainWindow.MainWindow as MainWindow
import AppFiles.AppInterfaceClasses.MainWindow.ModeWindows.SubsidiaryFiles.AutoModeTemplateWindowResponder as \
    AutoTemplateWindowResponder


class AutoModeTemplateWindow:
    def __init__(self, main_window: MainWindow.MainWindow) -> None:
        self.main_window = main_window
        self.responder = AutoTemplateWindowResponder.AutoModeTemplateWindowResponder(self)

    def show(self) -> None:
        self.main_window.next_button.setVisible(True)
        self.main_window.next_button.setEnabled(True)

        self.main_window.switch_speed_label.setVisible(True)

        self.main_window.digit_label.setVisible(True)

        self.responder.show()

    def close(self) -> None:
        self.main_window.next_button.setVisible(False)
        self.main_window.next_button.setEnabled(False)

        self.main_window.switch_speed_label.setVisible(False)

        self.main_window.digit_label.setVisible(False)

        self.main_window.outlines_for_modes_buttons["Automatic testing"].setVisible(False)

        self.responder.close()
