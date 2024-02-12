from Read import Read, FastaToRead




# Input: list of reads
# Output: dictionary where key = name , value = Read object with self.BBR_Name and self.BBR_Length



# This function takes in 2 strings and outputs whether or not sequenceToTheRight is a BBR of mainSequence
# If yes, then it returns True, theCommonSequence, length
# If no, then it returns False, None, -1

def isBBR(mainSequence : str, rightSequence : str, mainSequenceMaxBBRLength : int):

    
    lastPartOfMain : str = mainSequence[-mainSequenceMaxBBRLength:]
    firstPartOfRight : str = rightSequence[:mainSequenceMaxBBRLength]

    if (lastPartOfMain != firstPartOfRight):
        return False, None, -1
    

    mainSequenceTracker = len(mainSequence) - mainSequenceMaxBBRLength
    rightSequenceTracker = mainSequenceMaxBBRLength




    # if we get to this point, that means there is a larger BBR for main
    # while we still have characters to read

    length = mainSequenceMaxBBRLength
    commonSequence = lastPartOfMain
    
    while mainSequenceTracker >= 0 and rightSequenceTracker < len(rightSequence):

        # Compare corresponding characters

        if(mainSequence[mainSequenceTracker] == rightSequence[rightSequenceTracker]):

            commonCharacter = mainSequence[mainSequenceTracker]
            commonSequence += commonCharacter

            length += 1

            mainSequenceTracker -= 1
            rightSequenceTracker += 1

            


        else:
            break


    return True, commonSequence, length



def getBestBuddyToTheRightForEachRead(reads : list[Read]) -> dict:

    numReads : int = len(reads)


    for i in range(numReads):

        for j in range(i+1,numReads):

            read1 : Read = reads[i]
            read2 : Read = reads[j]

            sequence1 = read1.sequence
            sequence2 = read2.sequence


            seq2IsBBR , commonSeqeuence , lengthOfCommonSequence = isBBR(sequence1,sequence2, read1.MaxBBR_Length)

            if(not seq2IsBBR):

                continue

            read1.BBR_Name = read2.name
            read1.BBR_Sequence = commonSeqeuence
            read1.MaxBBR_Length = lengthOfCommonSequence









if __name__ == "__main__":

    fastaToRead = FastaToRead("reads.fa")

    readObjects : list[Read] = fastaToRead.convertToReadObjects()

    dictionary = getBestBuddyToTheRightForEachRead(reads= readObjects)
