from sys import argv
dna = ('A','C','G','T')

if __name__ == "__main__":
    #fname = 'rosalind_dna.txt'
    fname = argv[1]
    with open(fname) as f:
        s = f.read()
    rna = s.replace('T','U')
    print(rna)