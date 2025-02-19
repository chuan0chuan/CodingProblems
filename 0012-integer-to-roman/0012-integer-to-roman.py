class Solution:
    def intToRoman(self, num: int) -> str:
        nums = str(num)  # 把数字转换为字符串，方便遍历
        result = []  # 存放转换后的罗马数字

        # 定义一个映射表，分别对应个位、十位、百位、千位
        roman_map = [
            ("I", "V", "X"),  # 个位（1, 5, 10）
            ("X", "L", "C"),  # 十位（10, 50, 100）
            ("C", "D", "M"),  # 百位（100, 500, 1000）
            ("M", "", "")      # 千位（1000, 没有5000, 没有10000）
        ]

        # 逆序遍历数字（从个位到千位）
        for i in range(len(nums) - 1, -1, -1):
            digit = int(nums[i])  # 当前位的数字
            roman_unit = roman_map[len(nums) - 1 - i]  # 获取该位数的映射表
            one, five, ten = roman_unit  # 分别是 1, 5, 10 对应的罗马字符

            if digit == 0:
                continue  # 如果是0，直接跳过
            elif digit <= 3:
                char = one * digit  # 1, 2, 3 直接重复 I, X, C, M
            elif digit == 4:
                char = one + five  # 4 变成 IV, XL, CD
            elif digit == 5:
                char = five  # 5 变成 V, L, D
            elif digit <= 8:
                char = five + one * (digit - 5)  # 6, 7, 8 变成 VI, VII, VIII
            else:  # digit == 9
                char = one + ten  # 9 变成 IX, XC, CM

            result.append(char)  # 把当前位的罗马数字加入结果

        return "".join(result[::-1])  # 逆序拼接，保证罗马数字从高位到低位