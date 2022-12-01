class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """

        vowl_list = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        a_cnt, b_cnt = 0, 0
        for i in range(len(s)/2):
            if s[i] in vowl_list:
                a_cnt += 1
            if s[-i-1] in vowl_list:
                b_cnt += 1

        if a_cnt == b_cnt:
            return True
        else:
            return False