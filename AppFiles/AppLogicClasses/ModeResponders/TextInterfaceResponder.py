from __future__ import annotations
import random

from SubsidiaryFiles.Modules.MNISTDataReader import get_random_info
import AppFiles.AppLogicClasses.MainAppResponder as MainAppResponder


class TextInterfaceResponder:
    MODE = "training"
    ERROR_MESSAGE = "Wrong input! Please, try again"

    def __init__(self, main_app_responder: MainAppResponder.MainAppResponder) -> None:
        self.main_app_responder = main_app_responder

    def start(self) -> None:
        branch_number = self.get_int_info("Select number of iterations for branches: ")
        info_number = self.get_int_info("Print info every ... iterations: ")
        save_number = self.get_int_info("Save changes every ... iterations: ")

        for iteration in range(1, branch_number + 1):
            for _ in range(self.main_app_responder.app.network.batch_size):
                info = get_random_info(TextInterfaceResponder.MODE)
                self.main_app_responder.app.network.process_matrix(matrix=info.matrix, correct_answer=info.value,
                                                                   propagation=True)

            if iteration % info_number == 0:
                print(f"{iteration} branches were processed...")
            if iteration % save_number == 0:
                self.main_app_responder.app.network.save_changes()
        self.main_app_responder.app.network.save_changes()
        print(f"{branch_number} branches were processed...")
        print("Success!")
        self.close()

    def get_int_info(self, input_text: str):
        number = input(input_text)
        while not number.isdigit():
            self.show_error()
            number = input(input_text)
        return int(number)

    def show_error(self):
        print(TextInterfaceResponder.ERROR_MESSAGE)

    def close(self):
        self.main_app_responder.close_text_interface()
