import os

class SubDirectory_Find_Using_Recursion:

    def getDirectory(self,PATH):
        """
        @Func : It can find the all subdirectories AND it's files from specified by the path.
        @Param : The PATH is a whole path specified by the user and it's type is string 
        """
        if os.path.isdir(PATH):
            for directories in os.listdir(PATH):
                if PATH != '/':
                    self.getDirectory(PATH + '/' + directories)
        else:
            print PATH
            
print(os.listdir("./"))
PATH  = raw_input("Enter The Directry Name:")
path_object = SubDirectory_Find_Using_Recursion()
path_object.getDirectory(PATH)