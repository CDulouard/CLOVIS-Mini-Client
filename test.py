from DataLogger import *
import time
import pandas as pd

test = DataLogger(stack_size=15, columns=["A", "B", "C"], file_size=5, delay_save=60)
test.add(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
test.add(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
test.add(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
test.add(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
test.add(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))

time.sleep(10)
test.stop()
time.sleep(1)
print("fin")