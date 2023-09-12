def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=len(s)
    ans=0
    while i<n:
        if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
            ans+=1
        i+=1
    return ans

