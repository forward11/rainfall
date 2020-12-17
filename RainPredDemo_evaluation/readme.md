# 六盘山神经网络模型评估
1. 该程序是对RainPredDemo的模型评估，用来验证降雨量的增加中，模型的误差有多少
2. train:2008-2016  val:2017-2018  test:2019
 
## 实验结果
1. * real is bigger than pred by:  0.3659110819331484
* 201901-07 real rainfall:  2.354716981132076
* 201901-07 pred rainfall:  1.8125645
* real is bigger than pred by : 0.29910797173386094 

* 201908-11 real rainfall:  3.4965034965034976
* 201908-11 pred rainfall:  2.428411
* real is bigger than pred by : 0.43983184334491837
    该对比实验说明，模型对大雨量的预测能力比较差

2. 加上r_square之后，发现r_square的值非常低，仅为0.21，说明pred_y和test_y相关值很小，而理论上，两者应该越相近越好。。。