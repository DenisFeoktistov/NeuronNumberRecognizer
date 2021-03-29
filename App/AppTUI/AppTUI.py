from console_progressbar import ProgressBar

from SubsidiaryFiles.Network.Network import Network
from SubsidiaryFiles.Network.SubsidiaryFiles.NetworkFilesAndNames import *
from SubsidiaryFiles.Modules.MNISTDataReader import get_random_info
from SubsidiaryFiles.Modules.FunctionsTUI import enumerate_choice, make_indent, get_int_info


class AppTUI:
    MODE = "training"
    ERROR_MESSAGE = "Incorrect input! Please, try again"
    ACCURACY_TEST_NUMBER = 300
    ACCURACY_TEST_SAMPLE_NUMBER = 3

    ADD_NEW = "Add new network"
    TEACH_NETWORK = "Teach actual network"
    GET_NETWORK_INFO = "Get network info"
    SELECT_OTHER_NETWORK = "Select other network"
    TEST_ACCURACY = "Test network accuracy"
    BREAK = "Stop program"
    JOBS = [TEACH_NETWORK, GET_NETWORK_INFO, TEST_ACCURACY, SELECT_OTHER_NETWORK, ADD_NEW, BREAK]

    def __init__(self) -> None:
        self.network = Network()

    def start(self) -> None:
        self.main_cycle()

    def main_cycle(self) -> None:
        self.select_network()
        make_indent()
        while True:
            job = enumerate_choice(AppTUI.JOBS, "", "Select next action: ")
            make_indent()
            if job == AppTUI.TEACH_NETWORK:
                self.network_cycle()
                make_indent()
            elif job == AppTUI.SELECT_OTHER_NETWORK:
                self.select_network()
                make_indent()
            elif job == AppTUI.ADD_NEW:
                self.add_new_network()
            elif job == AppTUI.GET_NETWORK_INFO:
                self.print_network_info()
            elif job == AppTUI.TEST_ACCURACY:
                self.test_accuracy()
            elif job == AppTUI.BREAK:
                break
            else:
                raise Exception("Something went wrong while selecting action...")

    def test_accuracy(self) -> None:
        correct = 0
        for _ in range(AppTUI.ACCURACY_TEST_SAMPLE_NUMBER):
            correct += self.network.test_accuracy(AppTUI.ACCURACY_TEST_NUMBER)[0]

        correct //= self.ACCURACY_TEST_SAMPLE_NUMBER
        print(f"Average accuracy of {AppTUI.ACCURACY_TEST_SAMPLE_NUMBER} tests ({AppTUI.ACCURACY_TEST_NUMBER} "
              f"iterations each): {correct * 100 // AppTUI.ACCURACY_TEST_NUMBER}%")

    def add_new_network(self) -> None:
        input_text = "Enter new network name: "
        name = input(input_text)
        while not check_name(name):
            print("Incorrect name! Try again.")
            name = input(input_text)

        add_new_network(name)

        make_indent()
        self.select_network()

    def print_network_info(self) -> None:
        info = self.network.get_info()
        pairs = list(zip(info.keys(), info.values()))
        print(f"Actual network info:")
        for pair in pairs:
            print(f"\t{pair[0]}: {pair[1]}")

    def select_network(self) -> None:
        name = self.get_name()
        if name != AppTUI.ADD_NEW:
            self.network.set_network(name)
        else:
            self.add_new_network()

    def network_cycle(self) -> None:
        branch_number = get_int_info("Select number of iterations for branches: ", AppTUI.ERROR_MESSAGE)

        pb = ProgressBar(total=branch_number, prefix=f'Processing: ', suffix='', decimals=1,
                         length=30, fill='█', zfill=' ')
        for iteration in range(1, branch_number + 1):
            for _ in range(self.network.batch_size):
                info = get_random_info(AppTUI.MODE)
                self.network.process_matrix(matrix=info.matrix, correct_answer=info.value,
                                            propagation=True)
            pb.print_progress_bar(iteration)

        self.network.save_changes()
        print("Success!")

    @staticmethod
    def get_name() -> str:
        info = enumerate_choice([AppTUI.ADD_NEW, *get_all_primary_info()], "", "Select network: ")
        return info["name"] if info != AppTUI.ADD_NEW else AppTUI.ADD_NEW
