#!/usr/bin/python3
#################################################################
#author: Jing-min Yang

## Linux 极其常用的命令组合
#常用于查找共同基因
# cat coding*|awk -F"\t" '{print $1}'|sort|uniq -c |grep -w 6
# 循环结构批量提取
# for file in *.xls;do awk -F"\t" '($3>$4){print $0}' $file >./../
# 根据文件一的ID查找文件二中符合这个ID的行，用于两文件比对
# awk -F"\t" 'NR==FNR{a[$1];next} NR>FNR{if($1 in a){print$0}}' file1 file2 >../../

#python3 class.py ressequence1.fasta#
## 1.序列文件读取
with open('ressequence1.fasta') as file:
    for line in file:
        print (line)

## 2.接下来我们把描述字段和序列分别提取并存储在字典中
def get_fasta(fasta_path):
	fasta = {}
	with open(fasta_path) as file:
	    sequence = ""
	    for line in file:
	        if line.startswith(">"):
	            # 去除描述字段行中的\n和>
	            name = line[1:].rstrip()
	            fasta[name] = ''
	            continue
	        # 去除序列字段行中的\n，并将所有字符规范为大写字符
	        fasta[name] += line.rstrip().upper()
	return fasta

## 3.看看它具有的生物学意义(为了以后方便调用，使用函数的形式来实现)
## 3.1  核苷酸计数，碱基偏好性：
# 核苷酸计数
def nt_count(seq):
    ntCounts = []
    for nt in ['A', 'C', 'G', 'T']:
        ntCounts.append(seq.count(nt))
    return ntCounts

## 3.2 GC含量：
def cg_content(seq):
    total = len(seq)
    gcCount = seq.count('G') + seq.count('C')
    gcContent = format(float(gcCount / total * 100), '.6f')
    return gcContent    
## 3.3 DNA 翻译为 RNA：
# DNA 翻译为 RNA
import re
def dna_trans_rna(seq):
    rnaSeq = re.sub('T', 'U', seq)
    # method2: rnaSeq = dnaSeq.replace('T', 'U')
    return rnaSeq

## 3.4 RNA 翻译为 蛋白质：
def rna_trans_protein(rnaSeq):
    codonTable = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'',
        'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W',
    }
    proteinSeq = ""
    for codonStart in range(0, len(rnaSeq), 3):
        codon = rnaSeq[codonStart:codonStart + 3]
        if codon in codonTable:
            proteinSeq += codonTable[codon]
    return proteinSeq

## 3.5 获取反向序列：
# 获取反向序列
def reverse_comple(type, seq):
    seq = seq[::-1]
    dnaTable = {
        "A":"T", "T":"A", "C":"G", "G":"C"
    }
    rnaTable = {
        "A": "T", "U": "A", "C": "G", "G": "C"
    }
    res = ""
    if type == "dna":
        for ele in seq:
            if ele in seq:
                if type == "dna":
                    res += dnaTable[ele]
                else:
                    res += rnaTable[ele]
    return res

## 3.6 最后我们来一个main来把上面的函数统统运行一遍
if __name__ == '__main__':             ##  即文件作为脚本直接执行
    oct4 = get_fasta('ressequence1.fasta')
    for name, sequence in oct4.items():
        print ("name: ", name)
        print ("sequence: ", sequence)
        print ("nt_count: ", nt_count(sequence))
        print ("cg_content: ", cg_content(sequence))
        rna = dna_trans_rna(sequence)
        print ("rna: ", rna)
        protein = rna_trans_protein(rna)
        print ("protein: ", protein)
        print ("reverse_comple: ", reverse_comple("dna", sequence))

