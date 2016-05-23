class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        characters = {}
        for i in s:
            if i in characters:
                characters[i] += 1
            else:
                characters[i] = 1
        minstring = []
        stringpoint = 0
        for i in s:
            if i in minstring:
                characters[i] -= 1
                continue
            while (len(minstring) > 0) and ((minstring[-1] > i) and (characters[minstring[-1]] > 0)):
                # print minstring[-1], i, chara
                del minstring[-1]
            minstring.append(i)
            characters[i] -= 1
                # if (len(minstring) > 0) and ((minstring[-1] > i) and (characters[i] > 0)):
                #     minstring[-1] = i
                #     characters[i] -= 1
                #     break
                # else:
                #     minstring.append(i)
                #     characters[i] -= 1

        return "".join(minstring)



so = Solution()
print so.removeDuplicateLetters("bcabc")