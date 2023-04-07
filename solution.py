
import pandas as pd
import numpy as np


chat_id = 1134491798

def solution(x: np.array) -> float:
    y = x / 10  
    b = np.sum(y) / np.sum(10 - np.mean(x))  
    return b + 19 
