from src.table import table

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids.
    Nucleotides are translated in triplets using the table dictionary;
    each amino acid is encoded with a string of length 1."""
    protein = ''

    seq = seq.replace(" ", "")  # Remove any spaces

    # Optionally, pad the sequence with 'N' (a placeholder for any nucleotide) if it's not a multiple of 3
    while len(seq) % 3 != 0:
        seq += 'N'

    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon in table:
            protein += table[codon]
        else:
            protein += '?'

    return protein
