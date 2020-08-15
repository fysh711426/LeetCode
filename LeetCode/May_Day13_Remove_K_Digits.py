class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 確保數字小的項目排在前面
        stack = []
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # 刪除剩餘的項目
        if k > 0:
            stack = stack[:-k]
        
        # 合併字串並刪除前導零
        return "".join(stack).lstrip("0") or "0"