# Last updated: 7/30/2025, 9:41:25 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                first_pop_val = stack.pop()
                second_pop_val = stack.pop()
                if token == "+":
                    val = second_pop_val + first_pop_val
                    stack.append(val)
                elif token == "-":
                    val = second_pop_val - first_pop_val
                    stack.append(val)
                elif token == "*":
                    val = second_pop_val * first_pop_val
                    stack.append(val)
                elif token == "/":
                    val = int(second_pop_val / first_pop_val)
                    stack.append(val)
        return stack.pop()