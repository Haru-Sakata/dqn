REPLAY_BUFFER_SIZE = 10 ** 5
BATCH_SIZE = 32
LEARNING_START_STEP = 500
FINAL_STEP = 10 ** 5
GAMMA = 0.9
UPDATE_INTERVAL = 1
TARGET_UPDATE_INTERVAL = 100
STATE_WINDOW = 1
EXPLORATION_TYPE = 'constant'
EXPLORATION_EPSILON = 0.1
EXPLORATION_DURATION = 10 ** 4
CONVS = []
FCS = [50, 50]

LR = 1e-2
OPTIMIZER = 'adam'
MOMENTUM = 0.95
EPSILON = 1e-2
GRAD_CLIPPING = 10.0

DEVICE = '/gpu:0'
MODEL_SAVE_INTERVAL = 10 ** 4
