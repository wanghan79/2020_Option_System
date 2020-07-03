import os
import string

class PythonCmdPrompt:
    def read_scripts(self, path):
        try:
            with open(path) as f:
                while(True):
                    cmd = f.readline()
                    if cmd == None:
                        break
                    os.system(cmd)
        except FileNotFoundError:
            print("Warnning: the file is not found, please try again")
        except Exception:
            pass
    def type_cmd(self, cmd):
        os.system(cmd)
    def show_in_notepad(self):
        pass
    def help(self):
        print("read commands in txt file cmd: read path+name")
        print("terminate execution cmd: exit")


    def exe(self):
        while(1):
            cmd = input().split()
            if(cmd[0] == 'read'):
                self.read_scripts(cmd[1])
            elif(cmd[0] == 'help'):
                self.help()
            elif(cmd[0] == 'exit'):
                return
            else:
                self.type_cmd(cmd[0])

pcp = PythonCmdPrompt()
pcp.exe()


#input case:
'''
notepad
ipconfig
read cmds.txt  
'''
