from src.utils import read_file, write_file
from src.translator import translate

def main():
    dna_sequence = read_file('data/dna.txt')
    translated_sequence = translate(dna_sequence)
    write_file('data/protein_translated.txt', translated_sequence)
    print("Translation complete. Check the output file 'data/protein_translated.txt'.")

if __name__ == "__main__":
    main()
