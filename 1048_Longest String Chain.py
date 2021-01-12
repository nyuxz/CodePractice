class Solution:
    def longestStrChain(self, words):
        """
        典型的动态规划的场景。设dp[i]为word[i]的单词链最长距离，
        如果word[i]是word[j]的predecessor，那么有dp[i] = max(dp[i], dp[j] + 1)。
        至于如何判断word[i]是否是word[j]的predecessor？对两个单词进行逐位比较，只允许有某一个的字符不一样。"""
        words = sorted(words, key=lambda word:len(word))
        word_dict = {}

        for word in words:
            word_dict[word] = 1

        longest = 1
        for word in words:
            for i in range(len(word)):
                if word[:i] + word[i + 1:] in word_dict:
                    word_dict[word] = word_dict[word[:i] + word[i + 1:]] + 1
                    longest = max(longest, word_dict[word])
                    
        return longest