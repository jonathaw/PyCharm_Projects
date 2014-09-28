import os
import timeit
import math
import __main__
__main__.pymol_argv = ['pymol', '-qc']  # Pymol: quiet and no GUI '-qc'
import pymol
from pymol import cmd
pymol.finish_launching()

start = timeit.default_timer()
crys_name = 'X1OHZ_AB_aln.pdb'
PDBS_PATH = '/Users/jonathan/Desktop/pdbsfortest'
PDBS_PATH = '/Users/jonathan/eden/DoCoh_test/jobs/'
CSV_PATH = '/Users/jonathan/Desktop/rmsd_model.csv'
main_dict = {}


def read_aln(docoh, query):
    seq = []
    if docoh == 'coh':
        msa = open('/Users/jonathan/PycharmProjects/pymol_stuff/crys_cohs_12_21.9.8.fasta_aln', 'r')
    else:
        msa = open('/Users/jonathan/PycharmProjects/pymol_stuff/crys_docs_12_21.9.8.fasta_aln', 'r')
    for line in msa:
        if line[0] == '>' and query in line:
            for line_in in msa:
                if line_in[0] == '>':
                    break
                seq += line_in.strip()
    msa.close()
    return seq


def fasta_length(seq):
    return len(''.join(seq).translate(None, '-'))


def msa_segment(docoh, query, template):
    q_seq = read_aln(docoh, query)
    t_seq = read_aln(docoh, template)
    aln_thr_gaps = 0
    crys_gaps = 0
    aln_thr_seg_in = []
    crys_seg_in = []
    for pos in range(0, len(q_seq)):
        if q_seq[pos] == '-' and t_seq[pos] == '-':
            crys_gaps += 1
            aln_thr_gaps += 1
            #print 'both gaps'
        elif q_seq[pos] == '-' and t_seq[pos] != '-':
            crys_gaps += 1
            #print 'crys gap'
        elif q_seq[pos] != '-' and t_seq[pos] == '-':
            aln_thr_gaps += 1
            #print 'aln_thr gap'
        elif q_seq[pos] != '-' and t_seq[pos] != '-':
            aln_thr_seg_in.append(pos - aln_thr_gaps + 1)
            crys_seg_in.append(pos - crys_gaps + 1)
            #print "aln_thr ", pos - aln_thr_gaps + 1, "crys: ", pos - crys_gaps + 1
    return aln_thr_seg_in, crys_seg_in


for pdb in os.listdir(PDBS_PATH):
    if pdb.endswith(".pdb"):
        cmd.reinitialize()
        names_split = pdb.split('_')
        q_name_coh = names_split[0]
        q_name_doc = names_split[1]
        t_name_coh = names_split[3]
        t_name_doc = names_split[4]
        out_num = names_split[5].split('.')[0]

        aln_thr_seg_coh, crys_seg_coh = msa_segment('coh', q_name_coh, t_name_coh)
        aln_thr_seg_doc, crys_seg_doc = msa_segment('doc', q_name_doc, t_name_doc)
        aln_coh_length = fasta_length(read_aln('coh', q_name_coh))
        crys_coh_length = fasta_length(read_aln('coh', t_name_coh))

        aln_thr_seg_doc_added = [i+aln_coh_length for i in aln_thr_seg_doc]
        crys_seg_doc_added = [i+crys_coh_length for i in crys_seg_doc]
        aln_thr_seg_tot = aln_thr_seg_coh + aln_thr_seg_doc_added
        crys_seg_tot = crys_seg_coh + crys_seg_doc_added
        aln_thr_seg_str = '+'.join(map(str, aln_thr_seg_tot))
        crys_seg_str = '+'.join(map(str, crys_seg_tot))

        cmd.load(PDBS_PATH + pdb, object='query')
        cmd.load('~/Desktop/' + crys_name, object='crys')
        cmd.select('query_sele', 'query and resi '+aln_thr_seg_str)
        cmd.select('crys_sele', 'crys and resi '+crys_seg_str)
        rmsd = cmd.align('crys_sele', 'query_sele', object='alignment')[0]
        main_dict[pdb] = rmsd
        print "finished processing ", pdb
        #cmd.save('/Users/jonathan/Desktop/on_'+t_name_coh+"_"+t_name_doc+".pdb", 'alignment')


print main_dict
stop = timeit.default_timer()

with open(CSV_PATH, 'w') as OUT:
    [OUT.write('{0},{1}\n'.format(key, value)) for key, value in main_dict.items()]
print math.floor((stop - start) / 60), " minutes and ", math.floor((stop - start) % 60), "seconds"
print "wrote results to ", CSV_PATH