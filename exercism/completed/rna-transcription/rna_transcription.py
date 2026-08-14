def to_rna(dna_strand):
    # result = ""
    # if not dna_strand:
    #     return ""
    # for char in dna_strand:
    #     if char == "G":
    #         result += "C"
    #     if char == "C":
    #         result += "G"
    #     if char == "T":
    #         result += "A"
    #     if char == "A":
    #         result += "U"
    # return result

    # rule = str.maketrans('GCTA','1234')
    # result = dna_strand.translate(rule)
    # return result

    # dict_code = {'G':'C','C':'G','T':'A','A':'U'}
    # result = ''
    # for char in dna_strand:
    #     result += dict_code[char]
    # return result

    dict_code = {'G':'C','C':'G','T':'A','A':'U'}
    return ''.join(dict_code[char] for char in dna_strand)
 