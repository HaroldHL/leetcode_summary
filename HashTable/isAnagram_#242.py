def isAnagram(s,t):
        # 暴力法 sorted_str 是否相等 o(NlogN)
        # return True if sorted(s) == sorted(t) else False
        # hashmap count
        if len(s) != len(t):
            return False
        hashMap = {}
        
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
                
        for i in t:
            s
            hashMap[i] -= 1
        
        for i in hashMap:
            if hashMap[i] != 0:
                return False
        return True