def max_overlap_string(leftString, rightString):

    max_overlap_length = min(len(leftString), len(rightString))
    
    for i in range(max_overlap_length, 0, -1):

        if leftString[-i:] == rightString[:i]:
            return leftString[-i:] 
    
    return ""  

# Example usage:
# Example usage:
leftString = "GCCTGTAGCTTAATCAACTGGACGCTGTTCGTGAAGCACCTCTCACATGATGGTTCTGCATGAAGGCTTCGCCTGCAACGAGGTGCTGCAGAAATCAGGA"
rightString = "ATCAACTGGACGCTGTTCGTGAAGCACCTCTCACATGATGGTTCTGCATGAAGGCTTCGCCTGCAACGAGGTGCTGCAGAAATCAGGAAATCGAAGGCGA"
print(max_overlap_string(leftString, rightString))




print(len(max_overlap_string(leftString, rightString)))




t = "ATCAACTGGACGCTGTTCGTGAAGCACCTCTCACATGATGGTTCTGCATGAAGGCTTCGCCTGCAACGAGGTGCTGCAGAAATCAGGA"

print(t[-40:])
