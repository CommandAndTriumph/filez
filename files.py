
import sys, argparse, statistics

class DoTheThing:


    def __init__(self, args):
        self.thefile = args.thefile



    def count_lines(self):
        '''return the number of lines in the file'''
        fileobject = open(self.thefile, 'r')
        linecount = 0
        for i in fileobject:
            linecount += 1
        fileobject.close()
        return linecount



    def count_word(self, theword):
        ''' return the number of times 'theword' appears in the file'''
        story = open(self.thefile, 'r')
        wordcount = 0
        for i in story:
            splitstory = i.split(" ")
            for j in range(len(splitstory)):
                if str.lower(splitstory[j]).strip('\n.,"?<>!@#$%^&*()|[]{}') == theword:
                    wordcount += 1
        return wordcount


    def most_common_word(self):
        fileobject = open(self.thefile, 'r')
        wordlist = []
        for i in fileobject:
            wordsplit = i.split(" ")
            for j in range(len(wordsplit)):
                wordstrip = str.lower(wordsplit[j]).strip('\n.,"?<>!@#$%^&*()|[]{}')
                wordlist.append(wordstrip)
        wordlist = [x for x in wordlist if x != '']
        return statistics.mode(wordlist)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read a file and do things")
    parser.add_argument("thefile", help="the file to pass in")

    thing = DoTheThing(parser.parse_args())

    # uncomment lines here on what thing you want to test

    # print(thing.count_lines())
    # print(thing.count_word('tapping'))
    print(thing.most_common_word())