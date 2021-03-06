from AppInterfaceClasses.ModeWindows.TraininngModeWindow import TrainingModeWindow
from AppLogicClasses.SubsidiaryFiles.MNISTDataReader import MnistDigitInfo


class TrainingModeWindowResponder:
    MIN_VALUE = 0
    MAX_VALUE = 100
    INIT_VALUE = 50

    def __init__(self, window: TrainingModeWindow):
        self.window = window

    def end_set_up(self):
        self.window.slider.setMaximum(TrainingModeWindowResponder.MAX_VALUE)
        self.window.slider.setMinimum(TrainingModeWindowResponder.MIN_VALUE)
        self.window.slider.setValue(TrainingModeWindowResponder.INIT_VALUE)

    def get_switch_speed_coefficient(self):
        return (self.window.slider.value() / (
                    TrainingModeWindowResponder.MAX_VALUE - TrainingModeWindowResponder.MIN_VALUE)) ** 0.5

    def set_up_new_info(self, info: MnistDigitInfo):
        self.window.matrix_widget.set_matrix(info.matrix)
