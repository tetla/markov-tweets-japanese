from tqdm import tqdm
import time

# 1秒ごとの進捗を10回表示
def main():
    for i in tqdm(range(10)):
        time.sleep(1)