from sys import argv
chars = ('A','C','G','T')
def makehist(s,chars):
    '''takes a DNA string and returns a dictionary with the nucleotide frequencies'''
    hist = dict((c,0) for c in chars)
    for char in s:
        try: hist[char]+=1
        except KeyError: pass
    return hist

if __name__ == "__main__":
    #fname = 'rosalind_dna.txt'
    fname = argv[1]
    with open(fname) as f:
        s = f.read()
    hist = makehist(s,chars)
    msg = ' '.join([str(hist[c]) for c in chars])
    print(msg)