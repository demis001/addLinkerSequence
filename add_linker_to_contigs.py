#!/usr/bin/env python
# encoding: utf-8
"""
add_linker_to_contigs.py

Created by Dereje Jima on Nov 13, 2014
"""
from __future__ import with_statement
import sys
import argparse
__author__    = "Dereje Jima"
__copyright__ = "Copyright 2014 Dereje Jima"
__license__   = "Apache v2.0"
__purpose__  = "Add a linker sequence to a contig  in a fasta file to reconstract pseudo genome"

from itertools import groupby
def fasta_parse(fasta_name):
    """
    Given a fasta file. yield tuples of header, sequence lines
    """
    try:
        fh = open(fasta_name)
    except IOError:
        print "The file, %s, does not exist" % (fasta_name)
        return
    # ditch the boolean (x[0]) and just keep the header or sequence since we know they alternate.
    iter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in iter:
        # drop the ">"
        header = header.next()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in iter.next())
        yield header, seq


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a linker sequence at  end of contigs in a fasta file for pseudo genome concatination.')
    parser.add_argument('infile', default='s',help='Parse FASTA files (.fa) to add a linker sequence at the end of each sequence contig')
    parser.add_argument('linker', default ='s', help='Linker sequence you want to add at the end of the a contig sequence, eg "NNNNNCACACACTTAATTAATTAAGTGTGTGNNNNN"')
    parser.add_argument('--singleseq', action='store_true', default=False, help='Concatenate all sequences into a single fasta sequence')
    args = parser.parse_args()
    infile = args.infile
    linkerseq = args.linker
    gen = fasta_parse(infile)
    for i, headseq in enumerate(gen):
        header, seq = headseq
        if not args.singleseq:
            if i > 0:
                sys.stdout.write("\n")
            sys.stdout.write(">" + header + "\n")
        else:
            if i == 0 and args.singleseq:
                sys.stdout.write(">" + header + "\n")
        sys.stdout.write(seq + linkerseq)
    sys.stdout.write("\n")
