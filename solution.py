import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 1134491798

def solution(x: np.array) -> float:
  
    n = len(x)
    mu = x.mean()
    se = np.sqrt(1/n)
    t = norm.ppf(0.975)  
    return t * se / mu
