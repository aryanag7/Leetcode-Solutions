class Solution:
    def interpret(self, command: str) -> str:
        # x = command.replace("()", "o").replace("(al)","al")
        # return x
      
        string=""
        for i in range(len(command)):
            if command[i]=="G":
                string=string+command[i]
            elif command[i]=="(":
                if command[i+1]=="a":
                    string=string+"al"    
                else:
                    string=string+"o"
        return string  
