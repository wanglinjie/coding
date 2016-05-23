class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_list = list(secret)
        guess_list = list(guess)
        bull = 0
        cow = 0
        del_position = []
        # 顺序扫描对应位置是否有相同数字
        for i in xrange(len(secret_list)):
            if secret_list[i] == guess_list[i]:
                bull += 1
                del_position.insert(0, i)
        # 删除对应位置相同的数字
        for i in del_position:
            del secret_list[i]
            del guess_list[i]
        secret_list = sorted(secret_list)
        guess_list = sorted(guess_list)
        i = j = 0
        # 扫描剩余数字中cow的数量
        while (i < len(secret_list)) and (j < len(guess_list)):
            if secret_list[i] == guess_list[j]:
                cow += 1
                i += 1
                j += 1
            elif secret_list[i] < guess_list[j]:
                i += 1
            else:
                j += 1
        return str(bull) + "A" + str(cow) + "B"

secret = "28011235453453534523543454656456576786867976845634512313458237834758723485723845738475883472834172837426481637467256738537841672342834160782384167234682375612374826538273846278374891237624317888888902346213748190643720813746275283472675308234676325612738412083567231084237726567812347823375108234777777774672350812346712038758267340182347826753823467163481723856273048267348237466735"
guess =  "18102128374062734082917408274378190823461273894720981374867238974862758328394710823578293939393939393939374026734082734678271084826734891237401824637823589089237410827348235682730894712356723078423758907289467812518940362710837426735082173486273582374275620817463725078172346723582746712580174870748127563203187425630182374823568902183748265372089472814681278934781028374820873482037"
so = Solution()
print so.getHint(secret, guess)
