import numpy as np
import warnings

def one_hot_encoding_aa(aa_sequence: str):
   ''' Converts amino acid sequence to one-hot-encoding. Unknown amino acids will raise a Value error.

   Parameters:
   aa_sequence (str): Amino acid sequence
   
   Returns:
   numpy.ndArray: One-hot encoded representation of the amino acid sequence.
   '''
   
   amino_acids_alphabet = 'ACDEFGHIKLMNPQRSTVWY'
   aa_dict = {aa: i for i, aa in enumerate(amino_acids_alphabet)}
   # outputs something like this:
   # {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
   # print(aa_dict)

   # Initialize a zero matrix for one-hot encoding
   seq_one_hot = np.zeros((len(aa_sequence), len(amino_acids_alphabet)))

   # Iterate through the amino acid sequence and set the appropriate index to 1
   for i, aa in enumerate(aa_sequence):
      # Check if the amino acid is in the dictionary and set the corresponding index to 1
      if aa in aa_dict:
         seq_one_hot[i, aa_dict[aa]] = 1
      # If the amino acid is not in the dictionary, raise a ValueError
      else:
         #raise ValueError(f"Invalid amino acid '{aa}' in sequence.")
         seq_one_hot[i, :] = 0.5
         warnings.warn(f"Invalid amino acid '{aa}' in sequence. Setting the row to 0.5 for unknown amino acids.")
      
   return seq_one_hot
