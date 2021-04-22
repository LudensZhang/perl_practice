#!/usr/bin/perl;
#################################################################
#author: Ya-ru Miao                                             #
#contact: miaoyr@hust.edu.cn                                    #
#perl base_func.pl 3.fasta_seq.title 3.fasta_seq.txt save_file  #
#To find the reverse complementary sequence of genes in the list#
#################################################################
$gene_ls=$ARGV[0];
$RNA_seq=$ARGV[1];
$save_file=$ARGV[2];

if(length($RNA_seq) == 0){
	die("ERROR: must specify a sequence file");
}
if(length($gene_ls) == 0){
	die("ERROR: must specify a gene list file");
}
if(length($save_file) == 0){
	die("ERROR: must specify a name of the file to save the result");
}
#array;sort;join;split;pop;push;shift;unshift
@gene_ls;
sub gene_array{
	open(GENES,$gene_ls);
	@gene_ls=<GENES>;
	chomp(@gene_ls);
	print "split and join function\n";
	$gene = $gene_ls[0];
    my @words=split / /,$gene;
	print "The raw value is:\n";
	print "$gene\n";
    print "After split by blank, the first value is:\n";
	print "$words[0]\n";
	my $new=join(";", @words);
	print "After join by ';', the first value is:\n";
	print "$new\n";
	printf("%s%s","*"x100,"\n");
	printf("%s%s"," "x100,"\n");
	printf("%s%s","*"x100,"\n");
    #caculate the length of array by scalar function
	my $length=scalar(@gene_ls);
	print "There are $length genes in total\n";
	my @sorted_ls=sort(@gene_ls);
	print "the sorted gene list are:\n";
	foreach $var (@sorted_ls){
	    print "$var\n";
	}
	my @tmp_ls=@gene_ls;
	my $first = shift(@tmp_ls); 
	print "The fist gene is $first\n";
	my $a = pop(@tmp_ls);
	print "The last gene is $a\n";
	my @tmp_ls=@gene_ls;
	splice(@tmp_ls,-1,0,"my_tag");
	my $tmp_len=scalar(@tmp_ls);
	my $insert=$tmp_ls[$tmp_len-2];
	print "my insert value is '$insert'\n";
	splice(@tmp_ls,1,1,"P53");
	print "The substitute value is $tmp_ls[1]\n";
	print "the left gene list are:\n";
	foreach $var (@tmp_ls){
	    print "$var\n";
	}
}
#hash reverse
%seq_hash;
%seq_length_hash;
sub seq_reverse{
	my ($seq,$id)=@_;
	$seq=uc($seq);
	my $r_seq=reverse $seq;
    	$r_seq=~ tr/ACGT/TGCA/;
    	$seq_hash{$id}=$r_seq;
	my $seq_length=length($r_seq);
	$seq_length_hash{$id}=$seq_length;
}

#hash functions;
sub seq_to_hash{
	open(RNASEQ, $RNA_seq);
	my $id;
	my $seq;
	my @lines=<RNASEQ>;
	chomp(@lines);
	my $count=0;
	foreach $rna (@lines){
		if ($rna =~ /^>/){
			my $r_seq;
			if (length($seq)>0){
			    seq_reverse($seq,$id);
			}
			$id=$rna;
			$seq="";
		}else{
			$seq.=$rna;
		}
	}
    #reverse the last sequence
    seq_reverse($seq,$id);
	my @keys = keys%seq_hash;
	my @values = values%seq_hash;
	print "the first key is $keys[0]\n";
	my $var=substr($values[0],0,10);
    print "the first value is $var......\n";
	delete $seq_hash{$keys[0]};
	@keys = keys%seq_hash;
	print "the first key is $keys[0]\n";
    printf("%s %s %s %s","*"x100,"\n"x3,"*"x100,"\n");
	
print "sort by key:\n";
foreach $key (sort keys %seq_length_hash)
{
    my $var = $seq_length_hash{$key};
    print "$key:$var\n";
}

print "sort by value:\n";
foreach $key ( sort { $seq_length_hash{$a} <=> $seq_length_hash{$b} } keys %seq_length_hash)
{
	my $var = $seq_length_hash{$key};
	print "$key:$var\n";
}
}
#extract seq of genes
sub ID_to_seq{
    for $var (@gene_ls){
	    if (grep ($var, %seq_hash)){
		    print SAVE "$var\t$seq_length_hash{$var}\n$seq_hash{$var}\n";
		}
	}
}
open SAVE,">$save_file";
gene_array();
printf("%s %s %s %s","*"x100,"\n"x3,"*"x100,"\n");
seq_to_hash();
ID_to_seq();
close GENES;
close RNASEQ;
close SAVE;
print "Done!\n";
