import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

if __name__ == '__main__':

    myrec = []
    for seq_record in SeqIO.parse('perl_practice/test4_file/3.fasta_seq.txt', "fasta"):
        rec = SeqRecord(seq_record.seq.reverse_complement(), id=seq_record.id)
        myrec.append(rec)
    SeqIO.write(myrec, 'perl_practice/test4_file/rev_pair_seq.txt', "fasta")

    donors = pd.read_csv('perl_practice/test4_file/donorseq.txt', header=None)
    donors.columns=['donor']
    A_count = []
    T_count = []
    C_count = []
    G_count = []
    for donor in donors['donor']:
        A_count.append(donor.count('A'))
        T_count.append(donor.count('T'))
        C_count.append(donor.count('C'))
        G_count.append(donor.count('G'))
    base_count = pd.DataFrame(list(zip(A_count,
                                       T_count,
                                       C_count,
                                       G_count)),
                              columns=['A', 'T', 'C', 'G'])
    print(base_count)
