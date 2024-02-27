def check_duplicates_in_first_column(file_path):

    first_words = set()
    duplicate_found = False
    

    with open(file_path, 'r') as file:
        for line in file:

            words = line.strip().split(' ')
        
            if words[0] in first_words:
                print(f"Duplicate word found in first column: {words[0]}")
                duplicate_found = True
            else:
                first_words.add(words[0])
    
    if not duplicate_found:
        print("No duplicates found in the first column.")

# Example usage
file_path = 'BBR_Lines.txt'
check_duplicates_in_first_column(file_path)



