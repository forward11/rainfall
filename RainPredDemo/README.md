# 六盘山神经网路评估
1. 全连接神经网络
2. train:2008-2017  val:2018-2019  test:2020
3. 使用六盘山气象站的数据进行预测，历史回归模型
4. 对风速风向进行了修正，结果仍然不明显
5. 

## 实验结果
201901-07 real rainfall:  452.8 
201901-07 pred rainfall:  482.03033 
real is bigger than pred by : -0.060640031098114146  

201908-11 real rainfall:  491.1 
201908-11 pred rainfall:  364.05542 
real is bigger than pred by : 0.3489704400098983 

对后半段雨水量大的预测不出来，导致pred偏小
