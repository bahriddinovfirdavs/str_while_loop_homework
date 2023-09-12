def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    n=len(s)
    ans=0
    while i<n:
        if s[i] in 'qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM':
            ans+=1
        i+=1
    return ans
