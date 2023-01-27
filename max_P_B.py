import numpy as np

# 模拟3000个客户端的信噪比
snr = np.random.rand(3000)
# 模拟3000个客户端的带宽
bandwidth = np.random.rand(3000)
# 模拟3000个客户端的发射功率
power = np.random.rand(3000)
# 模拟3000个客户端的ID
client_id = np.array(range(3000))

# 初始化结果列表
result = []

# 总带宽限制
B = 1000
# 总发射功率限制
P = 100

# 迭代10次
for i in range(10):
    # 找到当前信噪比最大的用户
    max_snr_index = np.argmax(snr)
    #如果当前用户的带宽加上总带宽小于等于限制带宽,并且当前用户的发射功率加上总发射功率小于等于限制发射功率
    if (np.sum(bandwidth[result])+bandwidth[max_snr_index]<=B) and (np.sum(power[result])+power[max_snr_index]<=P):
        # 将当前用户的id加入结果列表
        result.append(client_id[max_snr_index])
        # 将选中的用户的信噪比设置为最小值
        snr[max_snr_index] = -np.inf
    else:
        #如果当前用户带宽加上总带宽大于限制带宽,或者当前用户发射功率加上总发射功率大于限制发射功率,就跳过这个用户
        snr[max_snr_index] = -np.inf

print(result)
