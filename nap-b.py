import itertools
import numpy as np
import time

n = 20 # 荷物の個数
baggage_index = np.arange(n) # 荷物iのindex
A = [3, 6, 5, 4, 8, 5, 3, 4, 3, 5, 6, 4, 8, 7, 11, 8, 14, 6, 12, 4]
C = [7, 12, 9, 7, 13, 8, 4, 5, 3, 10, 7, 5, 6, 14, 5, 9, 6, 12, 5, 9]
W = 55
maxi_c = 0

# 実行前の時間を記録
start_time = time.time()
for i_1 in baggage_index:
    # 取り出す個数を指定した組み合わせを取得
    pair_set = itertools.combinations(baggage_index, i_1+1)
    for pair in pair_set: 
        sum_a = 0
        sum_c = 0
        for i_2 in list(pair):
            sum_a += A[i_2]
            sum_c += C[i_2]
        if sum_a <= W and maxi_c < sum_c:
            # 最適値更新
            maxi_c = sum_c
            value_a = sum_a
            pair_num = (np.array(pair)+1)
            
# 実行後の時間を記録
end_time = time.time()
# 実行時間を計算
execution_time = end_time - start_time

print("総重量: {0}\n総価格: {1}\ni = {2}\n実行時間: {3}".format(value_a, maxi_c, list(pair_num), execution_time))


            