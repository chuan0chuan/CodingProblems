class Solution:
    def __init__(self):
        self.letterMap =[
            "",     #0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.answer = ""
    
    def trackBack(self, digits, index):
        if index == len(digits):
            self.result.append(self.answer)
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for i in range(len(letters)):
            self.answer += letters[i] #a
            self.trackBack(digits, index + 1) #ad 
            self.answer=self.answer[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.trackBack(digits, 0)
        return self.result