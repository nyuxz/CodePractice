# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordsList = str.split(' ')
        if len(wordsList) != len(pattern):
            return False

        # pattern is string, using pattern.find function
        # wordslist is list, using wordslist.index function
        # map(pattern.find, pattern) will return a map-object, convert it to list to see results
        print(list(map(pattern.find, pattern)))
        print(list(map(wordsList.index, wordsList)))

        # in python2.x we can compare two map-object, however python3.x cannot
        return list(map(pattern.find, pattern))== list(map(wordsList.index, wordsList))



class Solution_2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(words) != len(pattern):
            return False

        print(list(set(pattern)))
        print(list(set(words)))
        print(list(set(zip(pattern, words))))

        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))


class Solution_3(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordsList = str.split(' ')
        if len(wordsList) != len(pattern):
            return False
        
        hashmap = {}
        
        for i in range(len(wordsList)):
            if pattern[i] not in hashmap:
                if wordsList[i] not in list(hashmap.values()):
                    hashmap[pattern[i]] = wordsList[i]
                else:
                    return False     
            elif hashmap[pattern[i]] != wordsList[i]:
                return False
        
        return True


if __name__ == '__main__':
	print (Solution().wordPattern("abba","dog cat cat dog"))
	print (Solution_2().wordPattern("abba","dog cat cat dog"))






