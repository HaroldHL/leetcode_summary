def groupAnagrams(strs):
        hashMap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [word]
            else:
                hashMap[sortedWord].append(word)
        res = []
        for value in hashMap.values():
            res.append(value)
        return res

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))