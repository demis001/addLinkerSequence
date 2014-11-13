addLinkerSequence
=================

Add linker sequence to the contig in a fasta file

Install
=======
git clone https://github.com/demis001/addLinkerSequence.git
cd addLinkerSequence

Add the `add_linker_to_contigs.py` to your PATH in .bashrc
`PATH=$PATH:[full path to]/addLinkerSequence`

USAGE
=======
`add_linker_to_contigs.py -h` to get help
`add_linker_to_contigs.py  contig98_R.rasembonsis_final_sorted_size_replicate_copyNum.fa  NNNNNCACACACTTAATTAATTAAGTGTGTGNNNNN > out.fa` to add the linker to the contigs in a fasta file

1. Generate pseudo genome in one go
`./add_linker_to_contigs.py  contig98_R.rasembonsis_final_sorted_size_replicate_copyNum.fa  NNNNNCACACACTTAATTAATTAAGTGTGTGNNNNN | grep -v ">" | tr -d "\t\n\r" > contig98_R.rasembonsis_final_pseudoGenome_linker.fa`

2. Add header to the pseudo genome
`cat  contig98_R.rasembonsis_final_pseudoGenome_linker.fa   | awk '{print ">R.rasembonsis_pseudoGenome\n"$0}' > R.rasembonsis_pseudoGenome_linker.fa`

Future update:

Add the above two step process to a single script.
