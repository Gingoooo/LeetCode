class Solution:
    def dayOfYear(self, date: str) -> int:
        """
        1. 查詢閏年定義
        公元年分非4的倍數，為平年。
        公元年分為4的倍數但非100的倍數，為閏年。
        公元年分為100的倍數但非400的倍數，為平年。
        公元年分為400的倍數為閏年。
        """
        list_month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = [int(n) for n in date.split('-')]
        # 判斷是否 2 月
        if m <= 2:
            return sum(list_month_days[:m])+d
        # 判斷是否
        else:
            if ((y % 400) == 0) | ((y % 4 == 0) & (y % 100 != 0)):
                return (sum(list_month_days[:m])+d)+1
            else:
                return sum(list_month_days[:m])+d