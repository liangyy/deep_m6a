import argparse
parser = argparse.ArgumentParser(prog='gtf2bed12.py', description='''
    This script takes a GTF format file and outputs its corresponding
    BED12 format file.
''')
parser.add_argument('--read_method', default = 'zcat', help = '''
    Specify the method to read input file (default is `zcat`)
''')
parser.add_argument('GTF')
args = parser.parse_args()

import os

cmd = 'gtfToGenePred {gtf} {gtf}.genePred'.format(gtf = args.GTF)
os.system(cmd)

cmd = 'genePredToBed {gtf}.genePred {gtf}.bed12'.format(gtf = args.GTF)
os.system(cmd)

cmd = 'sort -k1,1 -k2,2n {gtf}.bed12 | gzip > {gtf}.sorted.bed12.gz'
os.system(cmd)

cmd = 'rm {gtf}.genePred {gtf}.bed12'
os.system(cmd)
