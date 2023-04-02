
def check(s, wordDict, i, n,q ,t,m ):
    if(q == s) :
        return True
    for j in range(i, n):
        t += s[j]
        if t in wordDict:
            q += t
            sz = len(t)
            i += sz
            m = t
            t = ""
            if(check(s,wordDict,i, n,q, t,m)): 
                return True
            i -= sz
            q = q[:-sz]
            t = m
    return False

def wordBreak(s, dictionary):
    wordDict = list(dictionary)
    n = len(s)
    sz = len(wordDict)
    q,t,m = "","",""
    cnt = 0
    return check(s,wordDict,0, n,q, t,m)
    