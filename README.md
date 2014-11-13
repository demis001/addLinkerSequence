addLinkerSequence
=================

Add linker sequence to the contig in a fasta file

Install
=======

```
git clone https://github.com/demis001/addLinkerSequence.git
cd addLinkerSequence
```

Add the `add_linker_to_contigs.py` to your PATH in _.bashrc_

```
PATH=$PATH:[full path to]/addLinkerSequence
```

USAGE
=======
To get help:

```
add_linker_to_contigs.py -h
```

To add the linker to the contigs in a fasta file:

```
add_linker_to_contigs.py test.fasta NNN > out.fa
``` 

To add the linker and join all contigs into a single sequence

```
add_linker_to_contigs.py test.fasta NNN --singleseq > out.fa
```
Generate concatinated pseudo Genome
```
grep -v ">"  out.fa  |  tr -d "\t\n\r" > temp.fa
cat  temp.fa   | awk '{print ">out_pseudoGenome\n"$0}' > out_pseudoGenome_linker.fa && rm temp.fa
```
