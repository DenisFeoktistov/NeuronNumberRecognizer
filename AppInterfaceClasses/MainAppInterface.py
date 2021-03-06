from AppInterfaceClasses.ModeWindows.TraininngModeWindow.TrainingModeWindow import TrainingModeWindow


class MainAppInterface:
    def __init__(self, app):
        self.app = app
        self.training_mode_window = TrainingModeWindow(self)
