from main_script import *
import numpy as np

test = getHistory()
profit = test['profit_loss_pct']
profit_day = test['profit_loss_pct'][-1]
profit_day = np.round(profit_day, 2)
print(profit_day)