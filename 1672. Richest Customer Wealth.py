class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for account in accounts:
            if sum(account) > output:
                output = sum(account)
        return output