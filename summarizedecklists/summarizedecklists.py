#!/usr/bin/python3

class decklistsummarizer(object):
    """docstring for decklistsummarizer."""

    def __init__(self):
        super(decklistsummarizer, self).__init__()
        self.usageincards = {}
        self.usageindecks = {}
        self.totalcards = 0
        self.totaldecks = 0

    def addDecklist(self,deckstr):
        decklines = deckstr.splitlines()
        for line in decklines:
            splitline = line.split(' ')
            amount = int(splitline[0])
            name = " ".join(splitline[1:-1])
            number = splitline[-1]
            if number not in self.usageincards:
                self.usageincards[number] = (name, amount)
            else:
                self.usageincards[number] = (name, self.usageincards[number][1] + amount)
            if number not in self.usageindecks:
                self.usageindecks[number] = (name, 1)
            else:
                self.usageindecks[number] = (name, self.usageindecks[number][1] + 1)
            self.totalcards += amount
        self.totaldecks += 1

    def addDump(self,filename):
        with open(filename) as f:
            dump = f.readlines()
        indeck = 0
        deckstr = ""
        for line in dump:
            if len(line) < 5:
                continue
            indeck += int(line[0])
            deckstr += line
            if indeck >= 50:
                indeck = 0
                self.addDecklist(deckstr)
                deckstr = ""

    def main(self):
        filename = "everydecklistformsasteelrequiem2royalbattle.txt"
        self.addDump(filename)
        with open("summary.csv", 'w') as o:
            o.write("Number,Name,Usage Of Total Cards,Usage Of Total Cards as %,Number of Decklists That Include It,% of Decklists that include it,\n")
            o.write(",," + str(self.totalcards) + ",100%," + str(self.totaldecks) + ",100%,\n")
            sortedusageincards = sorted(self.usageincards.keys())
            for card in sortedusageincards:
                outputstring = card + "," + str(self.usageincards[card][0]) + "," + str(self.usageincards[card][1]) + "," + str(self.usageincards[card][1]*100/self.totalcards) + "," + str(self.usageindecks[card][1]) + "," + str(self.usageindecks[card][1]*100/self.totaldecks) + ","
                o.write(outputstring+"\n")

if __name__ == '__main__':
    d = decklistsummarizer()
    d.main()
