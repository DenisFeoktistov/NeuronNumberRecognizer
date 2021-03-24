# Real constants
MATRIX_WIDTH = MATRIX_HEIGHT = 28
INPUTS = MATRIX_WIDTH * MATRIX_HEIGHT
OUTPUTS = 10

NETWORKS_DIRECTORY_PATH = "./data/networks/"

# Constants, but you can experiment with them between launches
# ----------------------------------------------------------------------------------------------
ITERATIONS_FOR_MINI_BATCH = 10
# ----------------------------------------------------------------------------------------------
NETWORK_TEMPLATES = [[INPUTS, 30, 30, OUTPUTS], [INPUTS, 16, 16, OUTPUTS], [INPUTS, 30, OUTPUTS]]

NETWORK_MAIN_TEMPLATE_INDEX = 2
NETWORK_MAIN_TEMPLATE = NETWORK_TEMPLATES[NETWORK_MAIN_TEMPLATE_INDEX]
# ----------------------------------------------------------------------------------------------
SPEED_TEMPLATES = [0.03, 0.05, 0.1, 0.3, 0.5, 0.9, 1.0]

MAIN_LEARNING_SPEED_INDEX = 0
MAIN_LEARNING_SPEED = SPEED_TEMPLATES[MAIN_LEARNING_SPEED_INDEX]
