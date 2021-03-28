from __future__ import annotations


import App.AppGUI.AppInterfaceClasses.MainWindow.MainWindow as MainWindow
import App.AppGUI.AppInterfaceClasses.MainWindow.ModeWindows.ManualTestingModeWindow.ManualTestingModeWindowResponder as \
    ManualTestingModeWindowResponder


class ManualTestingModeWindow:
    def __init__(self, main_window: MainWindow.MainWindow) -> None:
        self.main_window = main_window
        self.responder = ManualTestingModeWindowResponder.ManualTestingModeWindowResponder(self)

    def set_up(self) -> None:
        self.responder.set_up()

    def show(self) -> None:
        self.main_window.clear_button.setVisible(True)
        self.main_window.clear_button.setEnabled(True)

        self.main_window.line_width_slider.setVisible(True)
        self.main_window.line_width_slider.setEnabled(True)

        self.main_window.line_width_label.setVisible(True)

        self.main_window.outlines_for_modes_buttons["Manual testing"].setVisible(True)

        self.responder.show()

    def close(self) -> None:
        self.main_window.clear_button.setVisible(False)
        self.main_window.clear_button.setEnabled(False)

        self.main_window.line_width_slider.setVisible(False)
        self.main_window.line_width_slider.setEnabled(False)

        self.main_window.line_width_label.setVisible(False)

        self.main_window.outlines_for_modes_buttons["Manual testing"].setVisible(False)

        self.responder.close()
