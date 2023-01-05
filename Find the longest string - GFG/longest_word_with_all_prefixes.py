
class TrieNode:

    def __init__(self) -> None:
        self.children = [None]*26
        self.end = False
        self.cntPfx = 0
        self.endWord = 0

class Trie:
    def __init__(self) -> None:
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def convertCharToIdx(self,char):
        return ord(char)-ord('a')

    def insert(self,word):
        ptr = self.root
        wordLen = len(word)
        prevPfx = 0
        for w in range(wordLen):
            idx = self.convertCharToIdx(word[w])
            if not ptr.children[idx]:
                ptr.children[idx]=self.getNode()
            ptr = ptr.children[idx]
            ptr.cntPfx+=1

        ptr.end=True
        ptr.endWord+=1

    def longestWordPrefix(self,vocab):
        maxLen=0
        longestWord = None
        prevMaxWord = None
        for word in vocab:
            ptr = self.root
            wordLen = len(word)
            for w in range(wordLen):
                idx = self.convertCharToIdx(word[w])
                ptr = ptr.children[idx]
                if not ptr.end:
                    break
            print(f"prev max word {prevMaxWord} longest word {longestWord} curr word {word} is end {ptr.end}")
            if ptr.end and wordLen>maxLen:
                maxLen=wordLen
                prevMaxWord = word
                longestWord = word
            if ptr.end and wordLen==maxLen and prevMaxWord and word<prevMaxWord:
                longestWord=word
                prevMaxWord=word


        return longestWord if longestWord else ""
                

# words = ['n','ni','ninja','nin','ninj','ning','ninga']
words = "mioeqmcf nripfgldvfszdveewbtl kaptdyslzecggjqxcebovnopc elebvxlfnlbbletznxmlgkinm xgtpqrimtxdajkdnqkyrasazdea pxqomkbbzrjp twdatxyjkxsklbjgxuoj mccafq iegfassr sovrcfniabmwqekxhtqwtznxyp vqnbbuzofzsqnieamwqwqpurmqe szmxiuxnjffxwyswkupedo mswxhm fxampvpvkbwokbmbalascm eujxerpqdvxafppzdexxxn jmuk ujzyavcewzigiblkgrrel cgmurreogkypbtt tlhphqvdbabvtqkfwmh evhd og krthlu bcxdjaprqavwvjlurftmcwddczb wthtwfwqmbrmaopacdpztbajdlh gkdhdoviy bmuixitidsl bnzzxevfnsrkjb rfqnmzptdexhykmaze lfoytkxbebxaavv trwzaxyaysxfeaoxqsnzsgli kusypstkdz vdmecbtbuc vokpyma wumjxhcuirtgasgaotezqjlfbquezp kzryozvjsdabgggzx zvdioezdhyolthvltdoacpbwab hforuospfhgxverrysve xmmoisefz jbhkohikhtxqarklkpyaeoxvkk hsnfxupg tnhfqffd gpttvzvuxqcfjeqjlhulls evntrdrkkjlulhsdegqufeytebg mvqhxeosgsfaxsdvxuoowbnhzi zf ylzavlhyvedknglfacqmexwlxeuq ruypjndvms ipxonmyapeba hspoqzpb jyoqvhecuyuykxopr ugmmnjbkthhuoffvqomxpks hbheyjoafuusebn hdamvawzqrbnvgxwevtbw pkauphtpwzlvsavbcwdrnyrzopfzp zlbourajiczvcwqyoyuinri uvsepqexedpksmwzzmiyejmh gnbfjpoqkqdw bpsvveqykfpnwpydfjnsabjrx czcjrmcycgwcajmmmodneluhg agojaxiixcad ejxulnmhdsku zghsgzgonpfhvfvxvwxbju lfqta wy dojemhzgrvnplcaxvwqr rkfwliqscaayznmpubnodzo zuzybsrdfgfrepsutnyrinrqij wqsjiypylibdi iq qbuvufmmnhxapkgolcmpaqcbegnmev llctgicaekbtfwlsajigdmhdxhmz sovkokjxnyrytebuswaevvg iwwfsxbinoqlxdynclwc htgozgomrhnvqg nzybfvodmcyvsbmoe wvfzkqjsazmrngib bdrpslafasfgzdflxquawfuckyw huuxuflqwjiqhzurscdvr mxvvazqjljmbdrmgvxsgwakbybhbcf pysweywtvbmtdtcvtxsmn auipcyhkcudsbvempfevbvhetf zshzbvu npxzpfqcgdwcicogi dntjisyqiyc exunkglagyedlpgxhzqybqtfald nrqiootjtwchrlwc nufjqbeaeezobohsyk liubh oplaviqkeiofdrxrklobzypmzifq pynoxyergnwgrbqgnhrcwexby ajvjbhmmnpcukpeeyacqppolei ieilcdbvhcjudgcrvnuuo zccydttddxstoixixczxbxd zrnehmnjkegtqqwoan gaodapdlmwyykvthrmxd fpnhhgmlndkmethnekgowgicdsz eaqpbxfmannfbkhbhmbw ktrkcwnbufwe pttkrzaxfhuhzbgwwpkhbvejhm zuwvvdvkzucy"
words = words.split(" ")
# Trie object
t = Trie()

# Construct trie
for key in words:
    t.insert(key)


print(t.longestWordPrefix(words))
