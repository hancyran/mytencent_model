import sys

from src.train.train_LGB import trainLGB
from src.utils.LGB_args import args

# train_type = sys.argv[1]
# n = float(sys.argv[2])

# learning_rate_list = args.learning_rate
# objective_list = args.objective
# n_leaves_list = args.num_leaves
reg_lambda = args.reg_lambda

for i, n in enumerate(reg_lambda):
    # f.write('setsid python train_LGB_bg.py cv %.4f> %s 2>&1 &\n' % (n, getLogPath('cv', i)))
    # f.write('setsid python train_LGB_bg.py val %.4f> %s 2>&1 &\n' % (n, getLogPath('val', i)))
    print('Time %d' %i)
    trainLGB('cv', reg_lambda=n)
    trainLGB('val', reg_lambda=n)

