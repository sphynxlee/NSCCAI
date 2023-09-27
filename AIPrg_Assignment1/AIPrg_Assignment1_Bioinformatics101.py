# Question 2: Bioinformatics 101
# Step 1 - Convert DNA Sequence to corresponding Codon Sequence
# for example, the following DNA sequence string: GCTCGTAATGATTGT
# should be converted into the following codon sequence: ["GCT","CGT","AAT","GAT","TGT"]
# Step 2 - Convert your codon sequence into an amino acid sequence

# Abbr.  DNA Codons                        Amino Acid
# Ala    GCT, GCC, GCA, GCG                Alanine
# Arg    CGT, CGC, CGA, CGG, AGA, AGG      Arginine
# Asn    AAT, AAC                          Asparagine
# Asp    GAT, GAC                          Aspartic Acid
# Cys    TGT, TGC                          Cysteine
# Gln    CAA, CAG                          Glutamine
# Glu    GAA, GAG                          Glutamic acid
# Gly    GGT, GGC, GGA, GGG                Glycine
# His    CAT, CAC                          Histidine
# Ile    ATT, ATC, ATA                     Isoleucine
# Leu    CTT, CTC, CTA, CTG, TTA, TTG      Leucine
# Lys    AAA, AAG                          Lysine
# Met    ATG                               Methionine
# Phe    TTT, TTC                          Phenylalanine
# Pro    CCT, CCC, CCA, CCG                Proline
# Pyl    UAG                               Pyrrolysine
# Ser    TCT, TCC, TCA, TCG, AGT, AGC      Serine
# Sec    UGA                               Selenocysteine
# Thr    ACT, ACC, ACA, ACG                Threonine
# Trp    TGG                               Tryptophan
# Tyr    TAT, TAC                          Tyrosine
# Val    GTT, GTC, GTA, GTG                Valine

codonDict = {
    'Alanine(Ala)': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Arginine(Arg)': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Asparagine(Asn)': ['AAT', 'AAC'],
    'Aspartic Acid(Asp)': ['GAT', 'GAC'],
    'Cysteine(Cys)': ['TGT', 'TGC'],
    'Glutamine(Gln)': ['CAA', 'CAG'],
    'Glutamic Acid(Glu)': ['GAA', 'GAG'],
    'Glycine(Gly)': ['GGT', 'GGC', 'GGA', 'GGG'],
    'Histidine(His)': ['CAT', 'CAC'],
    'Isoleucine(Ile)': ['ATT', 'ATC', 'ATA'],
    'Leucine(Leu)': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
    'Lysine(Lys)': ['AAA', 'AAG'],
    'Methionine(Met)': ['ATG'],
    'Phenylalanine(Phe)': ['TTT', 'TTC'],
    'Proline(Pro)': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Pyrrolysine(Pyl)': ['UAG'],
    'Serine(Ser)': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Selenocysteine(Sec)': ['UGA'],
    'Threonine(Thr)': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Tryptophan(Trp)': ['TGG'],
    'Tyrosine(Tyr)': ['TAT', 'TAC'],
    'Valine(Val)': ['GTT', 'GTC', 'GTA', 'GTG']
};

def convertDnaToCodon(dnaSequence):
    codonSequence = [];

    for i in range(0, len(dnaSequence), 3):
        codonSequence.append(dnaSequence[i:i+3]);

    return codonSequence

def convertCodonToAminoAcid(codonSequence):
    aminoAcidSequence = [];

    for codon in codonSequence:
        for aminoAcid in codonDict:
            if codon in codonDict[aminoAcid]:
                aminoAcidSequence.append(aminoAcid);

    return aminoAcidSequence

# codon = convertDnaToCodon('GCTCGTAATGATTGT');

dnaSequence = input("Please enter a DNA sequence, for example, GCTCGTAATGATTGT:");
codon = convertDnaToCodon(dnaSequence);
print("Codon Sequence: ", codon);
aminoAcid = convertCodonToAminoAcid(codon);
print("Amino Acid Sequence: ", aminoAcid);