import pandas as pd
import numpy as np

chat_id = 1134491798

def solution(x: np.array) -> float:
    df = pd.DataFrame({'chat_id': chat_id, 'x': x})
    group_means = df.groupby('chat_id')['x'].mean()
    return group_means[chat_id]
