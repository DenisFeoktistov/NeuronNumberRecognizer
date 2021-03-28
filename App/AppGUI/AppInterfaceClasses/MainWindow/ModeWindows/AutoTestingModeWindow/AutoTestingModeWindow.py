from __future__ import annotations


import App.AppGUI.AppInterfaceClasses.MainWindow.MainWindow as MainWindow
import App.AppGUI.AppInterfaceClasses.MainWindow.ModeWindows.AutoTestingModeWindow.AutoTestingModeWindowResponder as \
    AutoTestingModeWindowResponder
import App.AppGUI.AppInterfaceClasses.MainWindow.ModeWindows.SubsidiaryFiles.AutoModeTemplateWindow as \
    AutoModeTemplateWindow


class AutoTestingModeWindow(AutoModeTemplateWindow.AutoModeTemplateWindow):
    def __init__(self, main_window: MainWindow.MainWindow) -> None:
        super().__init__(main_window)

        self.responder = AutoTestingModeWindowResponder.AutoTestingModeWindowResponder(self)

    def set_up(self) -> None:
        self.responder.set_up()

    def show(self) -> None:
        super().show()

        self.main_window.outlines_for_modes_buttons["Automatic testing"].setVisible(True)

    def close(self) -> None:
        super().close()

        self.main_window.outlines_for_modes_buttons["Automatic testing"].setVisible(False)
