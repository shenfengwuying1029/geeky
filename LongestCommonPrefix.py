def longestCommonPrefix(strs):
    stepp = min([len(i) for i in strs]) if len(strs) != 0 else  0
    for i in range(stepp,0,-1):
        if min([x.find(strs[0][0:i]) for x in strs]) == 0 and max([x.find(strs[0][0:i]) for x in strs]) == 0:
            return strs[0][0:i]
    return ''
