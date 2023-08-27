class Solution:
    def is_palindrome(self, x: int) -> bool:
        x_string = str(x)
        y_string = x_string[::-1]  # Reverse x_string
        return x_string == y_string

    def is_palindrome_integer_version(self, x: int) -> bool:
        quotient, remainder = divmod(x, 10)
        print(f"{quotient=} | {remainder=}")

        # 121
        # quotient=12 | remainder=1
        # 12
        # quotient=1 | remainder=2

        # 101
        # quotient=10 | remainder=1
        # 10
        # quotient=1 | remainder=0

        # 102
        # quotient=10 | remainder=2
        # 10
        # quotient=1 | remainder=0


sol = Solution()
print(sol.is_palindrome(102301))
print(sol.is_palindrome_integer_version(10))
