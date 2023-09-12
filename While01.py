def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=len(s)
    ans=0
    while i<n:
        if s[i] in '1234567890':
            ans+=1
        i+=1
    return ans
