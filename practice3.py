import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


if __name__ == '__main__':

    def total(t): #求和
        sum = 0
        for i in t:
            sum += i
        return sum

    def above_average(t): #取大于平均值
        above_avg = []
        for i in t:
            if(i >= np.mean(t)):
                    above_avg.append(i)
        return above_avg


    test = np.arange(1, 1001,1) #构建1-1000的测试数组
    print('1-1000求和', sum(test))

    form_test = pd.read_csv('perl_practice/test3_file/form_test', sep=' ', header=None)
    form_test.columns = ['col1', 'col2', 'col3', 'col4']
    form_test['col1'] = round(form_test['col1'], 2) #将第一列保留两位小数

    col2 = []                                       #将第二列控制为10位
    for num in form_test['col2']:
        col2.append(format(num, '10f'))
    form_test['col2'] = col2

    col3 = []                                       #将第三列替换为科学计数法
    for num in form_test['col3']:
        col3.append(format(num, 'e'))
    form_test['col3'] = col3

    col4 = []                                      #将第四列转换为16进制
    for num in form_test['col4']:
        col4.append(hex(num))
    form_test['col4'] = col4

    print('格式化输出为')
    print(form_test)
    form_test.to_csv('perl_practice/test3_file/form_print.txt', sep='\t', header=None)
