from MNISTDataReader import read_info


if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(read_info(n, mode="training"))
