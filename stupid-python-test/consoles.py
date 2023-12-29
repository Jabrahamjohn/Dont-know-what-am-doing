import cmd

class HelloWorld(cmd.Cmd):
    intro = 'Hello welcome to not knowing and knowing, type help or ? to list a greeting\n'
    prompt = 'CONSOLE'
    file = None

    def do_greetings(self,line):
        print ("Hi AJ here.how are you ?")

    def do_EOF(self, line):
        return True
    
if __name__ == '__main__':
    HelloWorld().cmdloop()