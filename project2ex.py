def read_fasta_file(file_path):
    dna = {}
    current_header = None #key
    current_sequence = "" #value

    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()#remove emptyy space begening or at the end line
            if line.startswith('>'):
                # New header line
                if current_header is not None:
                    # Save the previous sequence
                    dna[current_header] = current_sequence
                    # Extract the first word as the key
                current_header = line[1:].split()[0]
                current_sequence = ""
            else:
                # Sequence line
                current_sequence +=line

    # Add the last sequence
    if current_header is not None:
        dna[current_header] = current_sequence

    return dna

# Example usage:
fasta_file_path =  "/Users/vinayjagtiani/Code/Coding4Medicine/Project 2/fasta.txt"
dna = read_fasta_file(fasta_file_path)
print(dna)