import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


if __name__ == '__main__':

    def total(t):
        sum = 0
        for i in t:
            sum += i
        return sum

    def above_average(t):
        above_avg = []
        for i in t:
            if(i >= np.mean(t)):
                    above_avg.append(i)
        return above_avg


    test = np.arange(1, 1001,1)
    print(above_average(test))

    form_test = pd.read_csv('perl_practice/test3_file/form_test', sep=' ', header=None)
    form_test.columns = ['col1', 'col2', 'col3', 'col4']
    form_test['col1'] = round(form_test['col1'], 2)

    col2 = []
    for num in form_test['col2']:
        col2.append(format(num, '10f'))
    form_test['col2'] = col2

    col3 = []
    for num in form_test['col3']:
        col3.append(format(num, 'e'))
    form_test['col3'] = col3

    col4 = []
    for num in form_test['col4']:
        col4.append(hex(num))
    form_test['col4'] = col4

    form_test.to_csv('perl_practice/test3_file/form_print.txt', sep='\t', header=None)
