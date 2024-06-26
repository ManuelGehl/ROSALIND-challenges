from motif_enumeration import MotifEnumeration
import pytest

# Define inputs according to numbering of rosalind
k_1, distance_1, sequences_1 = 3, 1, ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
k_4, distance_4, sequences_4 = 3, 3, ["AAAAA", "AAAAA", "AAAAA"]
k_7, distance_7, sequences_7 = 5, 2, ["TCTGAGCTTGCGTTATTTTTAGACC", "GTTTGACGGGAACCCGACGCCTATA",
                                      "TTTTAGATTTCCTCAGTCCACTATA", "CTTACAATTTCGTTATTTATCTAAT",
                                      "CAGTAGGAATAGCCACTTTGTTGTA", "AAATCCATTAAGGAAAGACGACCGT"]

# Define outputs according to numbering of rosalind
output_1 = ["ATA", "ATT", "GTT", "TTT"]
output_4  =["AAA", "AAC", "AAG", "AAT", "ACA", "ACC", "ACG", "ACT", "AGA", "AGC", 
            "AGG", "AGT", "ATA", "ATC", "ATG", "ATT", "CAA", "CAC", "CAG", "CAT",
            "CCA", "CCC", "CCG", "CCT", "CGA", "CGC", "CGG", "CGT", "CTA", "CTC",
            "CTG", "CTT", "GAA", "GAC", "GAG", "GAT", "GCA", "GCC", "GCG", "GCT", 
            "GGA", "GGC", "GGG", "GGT", "GTA", "GTC", "GTG", "GTT", "TAA", "TAC",
            "TAG", "TAT", "TCA", "TCC", "TCG", "TCT", "TGA", "TGC", "TGG", "TGT",
            "TTA", "TTC", "TTG", "TTT"]
output_7 = ['AAACT', 'AAATC', 'AACAC', 'AACAT', 'AACCT', 'AACTA', 'AACTC', 'AACTG', 
            'AACTT', 'AAGAA', 'AAGCT', 'AAGGT', 'AAGTC', 'AATAC', 'AATAT', 'AATCC', 
            'AATCT', 'AATGC', 'AATTC', 'AATTG', 'ACAAC', 'ACACA', 'ACACC', 'ACACG', 
            'ACACT', 'ACAGA', 'ACAGC', 'ACATC', 'ACATG', 'ACCAT', 'ACCCT', 'ACCGT', 
            'ACCTA', 'ACCTC', 'ACCTG', 'ACCTT', 'ACGAC', 'ACGAG', 'ACGAT', 'ACGCT', 
            'ACGGT', 'ACGTC', 'ACGTT', 'ACTAA', 'ACTAG', 'ACTAT', 'ACTCA', 'ACTCC', 
            'ACTCG', 'ACTCT', 'ACTGA', 'ACTGC', 'ACTGT', 'ACTTA', 'ACTTC', 'ACTTT', 
            'AGAAA', 'AGAAC', 'AGAAG', 'AGAAT', 'AGACA', 'AGACT', 'AGATA', 'AGATC', 
            'AGCAT', 'AGCCA', 'AGCGT', 'AGCTA', 'AGCTC', 'AGCTG', 'AGCTT', 'AGGAT', 
            'AGGTA', 'AGGTC', 'AGTAA', 'AGTAC', 'AGTAT', 'AGTCC', 'AGTCG', 'AGTCT', 
            'AGTGA', 'AGTTG', 'ATAAA', 'ATAAC', 'ATACA', 'ATACC', 'ATAGA', 'ATATA', 
            'ATATC', 'ATATG', 'ATATT', 'ATCAG', 'ATCCC', 'ATCCG', 'ATCCT', 'ATCGA', 
            'ATCGC', 'ATCTA', 'ATCTC', 'ATCTG', 'ATGAC', 'ATGAT', 'ATGCA', 'ATGCC', 
            'ATGGA', 'ATGGC', 'ATGTA', 'ATGTC', 'ATTAA', 'ATTAC', 'ATTAG', 'ATTAT', 
            'ATTCA', 'ATTCC', 'ATTCG', 'ATTGA', 'ATTGC', 'ATTGG', 'ATTGT', 'ATTTA', 
            'ATTTC', 'ATTTG', 'ATTTT', 'CAAAG', 'CAACC', 'CAACT', 'CAAGA', 'CAAGC', 
            'CAATA', 'CAATT', 'CACAC', 'CACAG', 'CACCT', 'CACGT', 'CACTA', 'CACTT', 
            'CAGAA', 'CAGAC', 'CAGAT', 'CAGGT', 'CAGTA', 'CAGTC', 'CATAA', 'CATAC', 
            'CATAG', 'CATAT', 'CATCC', 'CATCT', 'CATGA', 'CATGT', 'CATTA', 'CATTG', 
            'CATTT', 'CCAAG', 'CCATA', 'CCATG', 'CCATT', 'CCCGT', 'CCCTA', 'CCCTT', 
            'CCGAA', 'CCGAC', 'CCGAT', 'CCGCT', 'CCGGT', 'CCGTA', 'CCGTC', 'CCGTG', 
            'CCGTT', 'CCTAC', 'CCTAT', 'CCTCA', 'CCTCC', 'CCTTA', 'CCTTC', 'CCTTG', 
            'CCTTT', 'CGAAA', 'CGAAG', 'CGACA', 'CGACT', 'CGAGT', 'CGATA', 'CGATG', 
            'CGATT', 'CGCAA', 'CGCAT', 'CGCCA', 'CGCGA', 'CGCTA', 'CGCTC', 'CGCTT', 
            'CGGAC', 'CGGAT', 'CGGCA', 'CGGTA', 'CGGTC', 'CGGTT', 'CGTAA', 'CGTAC', 
            'CGTCA', 'CGTCG', 'CGTCT', 'CGTTA', 'CGTTT', 'CTAAC', 'CTAAG', 'CTAAT', 
            'CTACA', 'CTACC', 'CTACG', 'CTACT', 'CTAGA', 'CTAGC', 'CTAGG', 'CTAGT', 
            'CTATA', 'CTATC', 'CTATG', 'CTATT', 'CTCAT', 'CTCCG', 'CTCGT', 'CTCTA', 
            'CTCTT', 'CTGAA', 'CTGAG', 'CTGCA', 'CTGCC', 'CTGTA', 'CTGTT', 'CTTAA', 
            'CTTAC', 'CTTAG', 'CTTAT', 'CTTCA', 'CTTGA', 'CTTTA', 'CTTTC', 'CTTTG', 
            'CTTTT', 'GAAAT', 'GAACA', 'GAACT', 'GAAGT', 'GAATG', 'GAATT', 'GACAC', 
            'GACAT', 'GACCA', 'GACCT', 'GACGT', 'GACTT', 'GAGAA', 'GAGAT', 'GAGCT', 
            'GATAA', 'GATAC', 'GATAG', 'GATAT', 'GATCA', 'GATCC', 'GATCG', 'GATCT', 
            'GATGT', 'GATTA', 'GATTC', 'GATTG', 'GATTT', 'GCAAT', 'GCACT', 'GCATC', 
            'GCATT', 'GCCAT', 'GCCGT', 'GCCTA', 'GCCTT', 'GCGAT', 'GCGGT', 'GCGTC', 
            'GCGTT', 'GCTAA', 'GCTAC', 'GCTAG', 'GCTAT', 'GCTGA', 'GCTGT', 'GCTTA', 
            'GCTTT', 'GGAAT', 'GGACA', 'GGATA', 'GGATC', 'GGATT', 'GGCTA', 'GGGAT', 
            'GGTAC', 'GGTAG', 'GGTAT', 'GGTCA', 'GGTCG', 'GGTTA', 'GTAAA', 'GTAAG', 
            'GTACA', 'GTACC', 'GTACG', 'GTAGA', 'GTATA', 'GTATC', 'GTATG', 'GTATT', 
            'GTCAA', 'GTCAG', 'GTCCG', 'GTCCT', 'GTCGA', 'GTCGC', 'GTCGT', 'GTCTA', 
            'GTCTG', 'GTGAA', 'GTGAG', 'GTGCA', 'GTGCG', 'GTTAA', 'GTTAC', 'GTTAG', 
            'GTTAT', 'GTTCA', 'GTTCC', 'GTTCG', 'GTTGA', 'GTTTA', 'TAAAC', 'TAAAG', 
            'TAACA', 'TAACC', 'TAACT', 'TAAGA', 'TAAGC', 'TAATA', 'TAATC', 'TACAC', 
            'TACAG', 'TACCC', 'TACCG', 'TACCT', 'TACGA', 'TACGC', 'TACGT', 'TACTA', 
            'TACTC', 'TACTG', 'TAGAA', 'TAGAC', 'TAGAG', 'TAGAT', 'TAGCC', 'TAGCG', 
            'TAGGA', 'TAGTC', 'TATAA', 'TATAC', 'TATAT', 'TATCA', 'TATCC', 'TATCG', 
            'TATGA', 'TATGC', 'TATGG', 'TATGT', 'TATTA', 'TATTG', 'TCAAC', 'TCAAT', 
            'TCACC', 'TCACG', 'TCACT', 'TCAGA', 'TCATA', 'TCATG', 'TCCAA', 'TCCAC', 
            'TCCAG', 'TCCAT', 'TCCCA', 'TCCCT', 'TCCGA', 'TCCGC', 'TCCGT', 'TCCTA', 
            'TCCTG', 'TCCTT', 'TCGAA', 'TCGAC', 'TCGAT', 'TCGCC', 'TCGCT', 'TCGGA', 
            'TCGGC', 'TCGGG', 'TCGGT', 'TCGTC', 'TCTAC', 'TCTAG', 'TCTAT', 'TCTCC', 
            'TCTCT', 'TCTGG', 'TCTGT', 'TCTTA', 'TCTTT', 'TGAAA', 'TGAAC', 'TGAAT', 
            'TGACA', 'TGACC', 'TGACT', 'TGAGA', 'TGAGC', 'TGAGT', 'TGATA', 'TGATC', 
            'TGATG', 'TGATT', 'TGCAA', 'TGCAC', 'TGCAG', 'TGCAT', 'TGCCA', 'TGCCG', 
            'TGCCT', 'TGCGA', 'TGCGT', 'TGCTT', 'TGGAA', 'TGGAT', 'TGGTA', 'TGTAA', 
            'TGTAG', 'TGTAT', 'TGTCC', 'TGTCG', 'TGTGG', 'TGTTA', 'TTAAA', 'TTAAC', 
            'TTAAG', 'TTAAT', 'TTACA', 'TTACC', 'TTACG', 'TTACT', 'TTAGA', 'TTAGC', 
            'TTAGG', 'TTAGT', 'TTATA', 'TTATC', 'TTATG', 'TTATT', 'TTCAA', 'TTCAC', 
            'TTCAT', 'TTCCA', 'TTCCC', 'TTCCT', 'TTCGA', 'TTCGG', 'TTCGT', 'TTCTA', 
            'TTCTG', 'TTGAA', 'TTGAC', 'TTGAG', 'TTGAT', 'TTGCA', 'TTGCG', 'TTGGA', 
            'TTGGG', 'TTGTG', 'TTTAA', 'TTTAC', 'TTTAG', 'TTTAT', 'TTTCA', 'TTTCC', 
            'TTTCG', 'TTTGA', 'TTTGG', 'TTTTA', 'TTTTG']

def test_1():
    motif_enumeration = MotifEnumeration()
    motif_enumeration.k_size = k_1
    motif_enumeration.distance = distance_1
    motif_enumeration.sequences = sequences_1
    motif_enumeration.create_k_mers()
    motif_enumeration.create_neighbours()
    motif_enumeration.find_motif()
    assert motif_enumeration.motifs == sorted(output_1)

def test_4():
    motif_enumeration = MotifEnumeration()
    motif_enumeration.k_size = k_4
    motif_enumeration.distance = distance_4
    motif_enumeration.sequences = sequences_4
    motif_enumeration.create_k_mers()
    motif_enumeration.create_neighbours()
    motif_enumeration.find_motif()
    assert motif_enumeration.motifs == sorted(output_4)

def test_7():
    motif_enumeration = MotifEnumeration()
    motif_enumeration.k_size = k_7
    motif_enumeration.distance = distance_7
    motif_enumeration.sequences = sequences_7
    motif_enumeration.create_k_mers()
    motif_enumeration.create_neighbours()
    motif_enumeration.find_motif()
    assert motif_enumeration.motifs == sorted(output_7)