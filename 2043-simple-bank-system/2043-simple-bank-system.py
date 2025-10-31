class Bank:
    def __init__(self, balance: List[int]):
        self.bal = [0] + balance
        self.n = len(balance)
    
    def _valid(self, account: int) -> bool:
        return 1 <= account <= self.n
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid(account1) or not self._valid(account2):
            return False
        if self.bal[account1] < money:
            return False
        
        self.bal[account1] -= money
        self.bal[account2] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.bal[account] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account) or self.bal[account] < money:
            return False
        self.bal[account] -= money
        return True
    



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)