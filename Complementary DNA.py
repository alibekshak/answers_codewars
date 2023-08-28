def DNA_strand(dna):
    complementary = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }
    
    return "".join(complementary[i] for i in dna)