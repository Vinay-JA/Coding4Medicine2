def readfasta(file_path):
    dna = {}
    currentheader=None
    currentsequence=""
    with open(file_path, 'r') as fastafile:
        for line in fastafile:
            line = line.strip()
            if line.startswith(">"):
                if currentheader is not None:
                    dna[currentheader] = currentsequence
                currentheader=line[1:].split()[0]
                currentsequence = ""
            else:
                curerentsequence+=line
    if currentheader is not None:
        dna[currentheader]=currentsequence

    return dna
fastafilepath = "/Users/vinayjagtiani/Code/Coding4Medicine/Project 2/fasta.txt"
dna = readfasta(fastafilepath)
print (dna)

