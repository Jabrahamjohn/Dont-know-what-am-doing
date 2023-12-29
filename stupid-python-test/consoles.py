import cmd

class HelloWorld(cmd.Cmd):
    
    def do_greetings(self,line):
        print ("Hi AJ here.how are you ?")

    def do_EOF(self, line):
        return True
    
if __name__ == '__main__':
    HelloWorld().cmdloop()