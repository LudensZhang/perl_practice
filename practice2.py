import pandas as pd
import numpy as np
import re

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


if __name__ == '__main__':

    predicted_target = pd.read_csv('perl_practice/test2_file/2.1Predicted_Targets_Info.txt', sep='\t')
    with open('perl_practice/test2_file/2.1name.txt') as f1:
        gene_name = list(f1.read().split('\n'))
        for id in gene_name:
            print(f'result has been saved as perl_practice/test2_file/{id}_result.csv')
            predicted_target.loc[predicted_target['Target'] == id].to_csv(f'perl_practice/test2_file/{id}_result.csv', index=0)

    gene_info = pd.read_csv('perl_practice/test2_file/2.2gene_info.txt', sep='\t')
    gene_id = pd.read_csv('perl_practice/test2_file/2.2gene_id')
    gene_info.columns = ['log2TPM']
    expression = []
    for i in gene_id['gene_ID']:
        expression.append(gene_info.loc[i, 'log2TPM'].sum())
    gene_id.insert(1, 'log2TPM', expression)
    print(gene_id)
    print('above result has been saved as perl_practice/test2_file/gene_expression_result.csv')
    gene_id.to_csv('perl_practice/test2_file/gene_expression_result.csv', index=0)

    fred = pd.read_csv('perl_practice/test2_file/fred.txt', header=None) #将数据读入，且第一行不为行号
    fred.columns = ['words']
    print('包含“fred”的行号为')
    for i in fred.index:
        if('fred' in fred.loc[i, 'words']):
            print(i)
    print('仅有"fred"的行号为')
    for i in fred.index:
        if(re.search('^fred$', fred.loc[i, 'words'])):
            print(i)

    with open('perl_practice/test2_file/2.4CALR.txt') as f2:
        f2.readline()
        calr_gene = f2.read()
        calr_gene = calr_gene.replace('\n', '')
        calr_cds = np.array(list(calr_gene[53:1307]))
        print(calr_cds)
        np.save('perl_practice/test2_file/CALR_cds', calr_cds)
