import argparse
parser = argparse.ArgumentParser(prog='gtf2bed12.py', description='''
    This script takes a GTF format file and outputs its corresponding
    BED12 format file.
    WARNING: the name should end with gtf.gz
''')
parser.add_argument('GTF')
args = parser.parse_args()

import os
import re

name = re.sub('.gtf.gz', '', args.GTF)

cmd = 'gtfToGenePred {name}.gtf.gz {name}.genePred'.format(name = name)
os.system(cmd)

cmd = 'genePredToBed {name}.genePred {name}.bed12'.format(name = name)
os.system(cmd)

cmd = 'sort -k1,1 -k2,2n {name}.bed12 | gzip > {name}.sorted.bed12.gz'.format(name = name)
os.system(cmd)

cmd = 'rm {name}.genePred {name}.bed12'.format(name = name)
os.system(cmd)
