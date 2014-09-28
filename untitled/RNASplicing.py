def tranlate( dna ):
    gencode = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
                'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
                'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
                'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
                'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
                'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
                'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
                'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
                'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'\_', 'TAG':'\_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', }
    i = 0
    pep = ''
    while i+3 <= len( dna ):
        pep += gencode[dna[i:i+3]]
        i += 3
    return pep

IN = open("/Users/jonathan/Desktop/temp.txt", "r")

dict = {}

for line in IN:
    if line[0] == '>':
        name = line.strip()
        dict[name] = ''
    else:
        dict[name] += line.strip()

gene = max(dict.values(), key=len)

introns = {}

for seq in dict:
    if dict[seq] == gene:
        continue
    introns[gene.find(dict[seq])] = dict[seq]

gene_spliced = gene
for intron in introns:
    gene_spliced = gene_spliced.replace(introns[intron], '')
print gene_spliced
print tranlate( gene_spliced )