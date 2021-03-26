from SubsidiaryFiles.Classes.Network.Network import Network
from SubsidiaryFiles.Modules.NetworkFilesAndNames import *
from SubsidiaryFiles.Modules.MNISTDataReader import get_random_info


class TextApp:
    MODE = "training"
    ERROR_MESSAGE = "Wrong input! Please, try again"

    def __init__(self):
        self.network = Network()

    def start(self):
        select_network_flag = True
        while True:
            if select_network_flag:
                self.select_network()
            self.start_network_cycle()
            select_network_flag = self.select_other()

    def select_other(self):
        print("Want to select other network or continue?")
        input_text = "Select other(0) / continue(1): "
        answer = input(input_text)
        while answer not in ["0", "1"]:
            self.show_error()
            answer = input(input_text)
        return answer == "0"

    def select_network(self):
        name = self.get_name()
        self.network.set_network(name)

    def start_network_cycle(self):
        branch_number = self.get_int_info("Select number of iterations for branches: ")
        info_number = self.get_int_info("Print info every ... iterations: ")
        save_number = self.get_int_info("Save changes every ... iterations: ")
        for iteration in range(1, branch_number + 1):
            for _ in range(self.network.batch_size):
                info = get_random_info(TextApp.MODE)
                self.network.process_matrix(matrix=info.matrix, correct_answer=info.value,
                                            propagation=True)

            if iteration % info_number == 0:
                print(f"{iteration} branches were processed...")
            if iteration % save_number == 0:
                self.network.save_changes()
        self.network.save_changes()
        print(f"{branch_number} branches were processed...")
        print("Success!")

    def get_int_info(self, input_text: str):
        number = input(input_text)
        while not number.isdigit():
            self.show_error()
            number = input(input_text)
        return int(number)

    def show_error(self):
        print(TextApp.ERROR_MESSAGE)

    def get_name(self):
        input_text = "Enter network name: "
        print("Networks: ")
        for info in get_all_primary_info():
            print("\t----------------")
            print(f"\tNetwork name: {info['name']}")
            print(f"\tBatches: {info['batches']}")
        print("\t----------------")
        print("Select network")
        return input(input_text)
