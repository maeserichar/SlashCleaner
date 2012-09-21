import sys
import os

def SlashCleaner(fileName):
    
    dirtyFile = open(fileName, 'r')
    cleanFile = open(fileName+'clean', 'w')
    
    insideTag = False
    
    for line in dirtyFile.readlines():
        lastCharacter = '/0'
        cleanLine = ""
        for character in line:
            if (character == '<'):
                insideTag = True
            elif (lastCharacter == '>'):
                insideTag = False
                if (character == ' '):
                    continue
            if (insideTag):
                cleanLine += character
            else:
                if (character == '/'):
                    if (lastCharacter != ' '):
                        cleanLine += ' '
                        
                if (lastCharacter == '/'):
                    if (character != ' '):
                        cleanLine += ' '
                        
                cleanLine += character    
            lastCharacter = character
        cleanFile.write(cleanLine)
    
    dirtyFile.close()
    cleanFile.close()
    
if (__name__ == '__main__'):
    fileName = sys.argv[1]
    rootDir = os.getcwd()
    print 'Looking for files called ' + fileName + ' in folder ' + rootDir
    for root, subFolders, files in os.walk(rootDir):
        for aFile in files:
            if (aFile == fileName):
                fullFileName = os.path.join(root, aFile)
                print 'Processing file ' + fullFileName
                SlashCleaner(fullFileName)
