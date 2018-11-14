import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd#数据挖掘
"""
pandas三大数据结构：series(一维数据),DataFrame（二维数据）,Panel（三维结构数据/面板数据）
"""
# 标准正态分布
stock_day_rise = np.random.normal(0,1,[500,504])
# print(stock_day_rise.shape)
"""
DataFrame---
index：行索引，axis=0
columns：列索引，axis=1
"""
# 数据变成DataFrame结构
stock_df =pd.DataFrame(stock_day_rise)
# print(type(stock_df))
# 获取某某股票
# print(stock_day_rise.shape[0])
# 获取某某交易日
# print(stock_day_rise.shape[1])
# 添加行索引，构造索引值列表
stock_code = ['股票'+str(i) for i in range(stock_day_rise.shape[0])]
# print(stock_code)

# print(stock_day_rise)
"""
# 使用pd.date_range():生成一组连续的时间序列
start:开始时间
end:结束时间
periods:时间天数
freq:递进单位，默认1天，‘B’是略过周末
"""


d =pd.date_range('2017-01-01',periods=stock_day_rise.shape[1],freq='B')
# print(d)
# index:代表索引；columns:代表列索引
stock_day_rise=pd.DataFrame(stock_day_rise,index=stock_code,columns=d)
# print(stock_day_rise)
"""
DataFrame的属性

"""
# 行索引index
de = stock_day_rise.index
# 列索引columns
co = stock_day_rise.columns
# 通过values直接获取array的值，不包含索引,返回一个二维数组
v = stock_day_rise.values
# 通过T进行转置
t =stock_day_rise.T
# print(t)
arr = np.array([[1,2,3],[4,5,6]])
# print(arr.T)
# print(arr.shape,arr.T.shape)
# 通过整体查询参数，简单查看数据的结构，默认是前5行
# print(stock_day_rise.head(10))
# 通过整体查询参数，简单查看数据的结构，默认是后5行
# print(stock_day_rise.tail(1))
"""
修改索引值
"""
# 修改行索引值(必须整体修改，不能单独修改某一个)
# stock_day_rise=stock_day_rise.index[3]
# print(stock_day_rise)
s = ["股票_"+str(i) for i in range(stock_day_rise.shape[0]) ]#重构行索引
stock_day_rise.index=s
# print(stock_day_rise)
# 重设索引，将原来的索引删除，drop丢弃原来的索引或者变成一列值
# 添加新的按照下表数字的索引
stock_day_rise=stock_day_rise.reset_index(drop=True)
# print(stock_day_rise)
# 以某列值设置为新的索引
df =pd.DataFrame({'month':[1,4,7,10],'year':[1,1,2,2],'sale':[55,40,84,31]})
# 可以设置索引，具有索引的结构
df = df.set_index(['month'])
# print(df)
# 可以设置多重索引，具有多重索引的结构，相当于三维数组结构

df =pd.DataFrame({'month':[1,4,7,3],'year':[1,1,1,1],'sale':[45,45,5,45]})
df =df.set_index(['year','month'])
# print(df)
# 通常会使用MultiIndex这种结构解决三维数据表示问题df.index
"""
series
"""
stock_day_rise=stock_day_rise.T
# print(stock_day_rise)
stock_day_rise =stock_day_rise.head()
# print(stock_day_rise[0]['2017-01-02'])
# 使用某个股票每天的数据
data =pd.read_csv('D:/data/stock_day/stock_day.csv')
# print(data.head())
# 直接使用行列索引（先列后行）
print(data[['open','high','close']])
print(data['open']['2018-02-27'])
# 结合loc或者iloc使用索引,可以先行后列
print(data.loc['2018-02-27':'2018-02-23','open'])
# iloc通过索引下标
print(data.iloc[0:3,0])
# 使用ix组合索引获取数据
print(data.ix[0:4,['open','close','high','low']])
# 对内容修改
data['open']=1
print(data['open'])
# 排序
# 对索引进行排序
print(data.sort_index())
# 对内容进行排序;by:对。。进行排序；ascending:指定排序的顺序，从小到大
print(data.sort_values(by='high',ascending=False).head())
