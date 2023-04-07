import pandas as pd
import numpy as np


chat_id = 1134491798 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
      return x[x == chat_id].shape[0] / x.shape[0]  # Ваш ответ
