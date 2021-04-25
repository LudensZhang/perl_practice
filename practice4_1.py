import pandas as pd
from Bio import SeqIO
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='perl_practice/test4_file/3.fasta_seq.txt', help='input fasta file, support multiple fasta in one file')
    #默认路径为perl_practice/test4_file/3.fasta_seq.txt
    gene_id = []
    gene_seq = []
    gene_len = []
    args = parser.parse_args()
    for seq_record in SeqIO.parse(args.file, "fasta"):
        gene_id.append(seq_record.id)
        gene_seq.append(seq_record.seq)
        gene_len.append(len(seq_record))

    gene_info = pd.DataFrame(list(zip(gene_id, gene_seq, gene_len)), columns=['id', 'seq', 'len'])

    for i in gene_info.index:
        gene_info.loc[i, 'cg_content'] = (gene_info.loc[i, "seq"].count("C")+
                                          gene_info.loc[i, "seq"].count("G"))/gene_info.loc[i, 'len']

    gene_info = gene_info.drop('seq', axis=1)
    gene_info = gene_info.append({'id':'',
                                  'len':sum(gene_info['len']),
                                  'cg_content':sum(gene_info['cg_content'])},
                                  ignore_index=True)
    print(gene_info)
    print('above result has been saved as perl_practice/test4_file/final_result.txt')
    gene_info.to_csv('perl_practice/test4_file/final_result.txt', sep='\t')
