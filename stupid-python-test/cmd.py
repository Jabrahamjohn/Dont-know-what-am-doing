import cmd, sys

class person(cmd.Cmd):
    intro = 'what do you say we give it a go'
    prompt = 'aj'
    file = None

    def greetings(self,line):
        print ("Hi AJ here.how are you ?")

    def EOF(self, line):
        return True
if __name__ == '__main__':
    person().cmdloop