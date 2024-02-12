class Read:

    def __init__(self, name : str, sequence : str) -> None:
        
        self.name = name
        self.sequence = sequence



class FastaToRead:

    def __init__(self, pathToFastaFile : str) -> None:
        
        self.filePath = pathToFastaFile


    
    def convertToReadObjects(self) -> list[Read]:

        reads : list[Read] = []



        # Get file contents

        with open(self.filePath, 'r') as file:



            line1 = file.readline()
        

            while line1:

                line2 = file.readline()
                
            
                if not line2:
                    break 
                

                line1 = line1.strip()
                name = line1[1:]
                sequence =  line2.strip()
                
                # Create Read Object

                readObject : Read = Read(name = name, sequence = sequence)
                
                reads.append(readObject)

                line1 = file.readline()



        return reads
    




if __name__ == '__main__':

    fastaToRead = FastaToRead("reads.fa")

    readObjects = fastaToRead.convertToReadObjects()

    print()

