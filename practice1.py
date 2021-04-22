from math import*
import pandas as pd


if __name__ == '__main__':

    r = float(input('请输入半径'))
    if(r > 0):
        print(f'周长为{2*pi}')
    else:
        print('周长为0')

    num_1, num_2 = float(input('请输入数字1')), float(input('请输入数字2'))
    print(f'两数之积为{num_1*num_2}')

    output_sting = input('请输入字符串')
    line_num = int(input('请输入行数'))
    for i in range(line_num):
        print(output_sting)

    num_list = pd.read_csv('perl_practice/test1_file/number_practice')
    result = []
    num_list.columns = ['value']
    for i in num_list['value']:
        if(i%3 == 0):
            result.append(i)
    pd.DataFrame(result).to_csv('perl_practice/test1_file/number_result.txt', index=0)

    path = input('请输入路径')
    with open(path) as f1:
        gene = f1.read()
    gene = list(gene.replace('>NT_086364.3 Homo sapiens chromosome 16 sequence, ENCODE region ENm008', ''))
    print(f'碱基A的数目为{gene.count("A")}')
    print(f'碱基C的数目为{gene.count("A")}')
    print(f'碱基T的数目为{gene.count("A")}')
    print(f'碱基G的数目为{gene.count("A")}')
    print(f'该基因长度为{len(gene)}')
    print(f'该基因8-11位碱基为{gene[8:12]}')
    gene[8:12] = ['T', 'A', 'C', 'G']

    with open('perl_practice/test1_file/sort_join_split') as f2:
        string1 = f2.readline()
        string2 = f2.readline()
    string1 = list(string1.replace('"', '').replace(';\n', '').split('-'))
    string2 = list(string2.replace('"', '').replace(';\n', '').split(','))
    string2 = [int(x) for x in string2]
    string1.sort()
    string2.sort(reverse=1)
    string1 = str(string1)
    string2 = str(string2).replace(',', ':')
    print(string1)
    print(string2)




