def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        while digits and digits[-1] == 9:
            digits.pop()
            res.append(0)
        if not digits:   #[9]
            return [1] + res
        else:
            digits[-1] += 1
            return digits + res