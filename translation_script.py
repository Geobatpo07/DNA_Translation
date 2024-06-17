#%%
inputfile = "dna.txt"

file = open(inputfile, "r")
lines = file.read()

lines = lines.replace("\n", " ")
lines = lines.replace("\r", " ")
lines

lines[40:50]
#%%
from table import table
def translate(seq):
    """Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids.
    Nucleotides are translated in triplets using the table dictionary;
    each amino acid is encoded with a string of length 1."""
    protein = ''
    seq = seq.replace(" ", "")  # Remove any spaces
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if codon in table:
                protein += table[codon]
            else:
                protein += '?'
    else:
        raise ValueError("The sequence length is not a multiple of 3.")

    return protein

#%%
#translated = translate(lines)
print(len(lines))
translate(lines)
help(translate)

#%%
def read_file(file):
    """Read a file and remove special characters."""
    with open(file, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")\
             .replace("\r", "")\
             .replace("\t", "")\
             .replace(" ", "")  # Optional: remove spaces
    return seq

#%%
# Lire les fichiers
prt = read_file("protein.txt")
dna = read_file("dna.txt")

# Traduire la séquence ADN
try:
    translated = translate(dna[20:935])
    print(translated)
except ValueError as e:
    print(e)

#%%
# Comparer les traductions
result = translate(dna[20:938])[:-1] == translate(dna[20:935])
print(result)
