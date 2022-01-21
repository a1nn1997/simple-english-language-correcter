
def englishgrammercorrecter(text):
    """"LanguageTool offers spell and grammar checking.
       Just paste your text here and your errors will be corrected"""
    from gingerit.gingerit import GingerIt

    parser = GingerIt()
    text = parser.parse(text)
    return str(text["result"])
if __name__ == '__main__':
    text = open("grammerchecker.txt", "r+")
    t = text.read()
    t1 = englishgrammercorrecter(t)
    text.write("\n")
    text.write(t1)
    text.close()


