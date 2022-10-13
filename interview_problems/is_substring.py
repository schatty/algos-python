def isSubsequence(s: str, t: str) -> bool:
    t = s + "#" + t
    len_s = len(s)
    
    pi = [0] * len_s
    pi_prev = 0
    
    for i in range(1, len(t)):
        k = pi_prev
        
        while k > 0 and t[i] != t[k]:
            k = pi[k - 1]
        if t[i] == t[k]:
            k += 1
            
        if i < len_s:
            pi[i] = k
            
        pi_prev = k
        
        if k == len_s:
            return True
        
    return False


print(isSubsequence("axc", "ahbgdc"))
