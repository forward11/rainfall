# 六盘山全连接模型预测日雨量
1. 使用隆德、泾源的数据作为features的一部分，进行2019年日雨量的预测，得到的R-square、平均值表现不错
2. 事实证明，在不论是月雨量还是日雨量，其他站点的雨量都是重要参数，我们就是用日雨量模型对2020年进行预测，看看效果
   
## 实验结果
Average daily rainfall in 2020 - real :  2.817611940298508
Average daily rainfall in 2020 - pred:  2.7112591
real is bigger than pred by:  0.03922635523451054 

Average daily rainfall in 202007-09 - real : 2.1363207547169814
Average daily rainfall in 202007-09 - pred : 2.2529469
real is bigger than pred by : -0.05176602312318417 

Average daily rainfall in 202008-11 - real : 4.009836065573769
Average daily rainfall in 202008-11 - pred : 3.5114276
real is bigger than pred by : 0.14193897059174176 

### 2019作为对比
Average daily rainfall in 2019 - real :  2.814647887323944
Average daily rainfall in 2019 - pred:  2.85994
real is bigger than pred by:  -0.015836753178213987 

Average daily rainfall in 201907-09 - real : 2.354716981132076
Average daily rainfall in 201907-09 - pred : 2.2898154
real is bigger than pred by : 0.028343574999952128 

Average daily rainfall in 201908-12 - real : 3.4965034965034976
Average daily rainfall in 201908-12 - pred : 3.7051587
real is bigger than pred by : -0.05631478440750046 


## 结果分析
1. 可以看到2019年的上半年pred小了2.8%，在2020年pred大了5%；同时2019上半年的real平均值为2.81，2020为2.13。这两项数值表明，2020年上半年的雨量比2019年是有所降低的，(2.13-2.35)/2.35=-9.36%，即大概降低9.36%
2. 如果我们假设下半年没有进行人工降雨，并且假设下半年也会同比减少9.36%左右
3. 实际上下半年的real比pred高了14%，我们注意到2019年的模型中下半年pred大了5.63%，假设模型在2020年下半年也有次误差，则扣除误差，增量大概为14%+5.63%=19.63%
4. 按照实际值来看，下半年的real为4.01，而2019下半年的real为3.50，增加了14.57%，而根据上半年显示2020雨水少，应该下半年也会减少9.36%，实际却增加14.57%，这表示降雨效果达到了9.36%+14.57%=23.93%
5. 两个方面的证据都表示降雨的增加会达到20%

## 残差图
由残差图可以看出，下半年与上半年相比，震荡更加明显，且总体上偏向正值，上半年的残差图比较接近0，说明降雨效果还是比较明显的