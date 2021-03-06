from AppLogicClasses.ModeResponders.TrainingModeResponder import TrainModeResponder


class MainAppResponder:
    def __init__(self, app):
        self.app = app

        self.training_mode_responder = TrainModeResponder(self)

    def start(self):
        self.training_mode_responder.start()
