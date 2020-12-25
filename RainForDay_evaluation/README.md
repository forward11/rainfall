# 六盘山全连接模型预测日雨量
1. 使用隆德、泾源的数据作为features的一部分，进行预测在月雨量上取得了不错的效果
2. 回过头来，之前没加入两个参考站的日雨量效果较差，再加入后看看日雨量的效果
3. 困难在于三个站的数据之间的merge

## 实验结果
Average daily rainfall in 2019 - real :  2.814647887323944
Average daily rainfall in 2019 - pred:  2.85994
real is bigger than pred by:  -0.015836753178213987 

Average daily rainfall in 201907-09 - real : 2.354716981132076
Average daily rainfall in 201907-09 - pred : 2.2898154
real is bigger than pred by : 0.028343574999952128 

Average daily rainfall in 201908-12 - real : 3.4965034965034976
Average daily rainfall in 201908-12 - pred : 3.7051587
real is bigger than pred by : -0.05631478440750046 

R-square is  0.9073249074687747
## 结果分析
可以看到，模型全年的误差在1.5%左右，上半年预测低了2.8%，下半年预测高了5.6%，可以分析图像找到原因：在下半年会有暴雨天气，增幅非常大，模型预测不会达到峰值高度，导致预测值偏小，不过这个误差不是很大，而且这对实验来说是有利好的。模型预测值偏大，在进行2020预测时，就会更加突出人工降雨的效果，因为真实值比偏大的预测值还大就可以说明效果。
