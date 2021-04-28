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
    for num in form_test.index:
        form_test.loc[num, 'col1'] = round(form_test.loc[num, 'col1'], 2)
        form_test.loc[num, 'col2'] = eval(str(form_test.loc[num, 'col2'])[0:11])
        form_test.loc[num, 'col3'] = format(form_test.loc[num, 'col3'], 'e')
        form_test.loc[num, 'col4'] = hex(form_test.loc[num, 'col4'])
    print('格式化输出为')
    print(form_test)
    form_test.to_csv('perl_practice/test3_file/form_print.txt', sep='\t', header=None)
