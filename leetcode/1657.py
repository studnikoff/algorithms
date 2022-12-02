class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        letters_ht1 = self.make_hashtable(word1)
        letters_ht2 = self.make_hashtable(word2)

        if set(letters_ht1.keys()) != set(letters_ht2.keys()):
            return False
        
        if sorted(letters_ht1.values()) != sorted(letters_ht2.values()):
            return False
        else:
            return True


    def make_hashtable(self, word):
        hashtable = dict()
        for i in word:
            if i in hashtable.keys():
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        return hashtable