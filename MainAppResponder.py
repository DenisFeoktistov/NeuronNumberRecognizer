from PyQt5.QtCore import QTimer


from TrainModeResponder import TrainModeResponder


class MainAppResponder:
    def __init__(self, app):
        self.app = app

        self.train_mode_responder = TrainModeResponder(self)

    def start(self):
        self.train_mode_responder.start()
