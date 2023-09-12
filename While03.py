def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=len(s)
    ans=0
    while i<n:
        if s[i] in '`~!@#$%^&*()_-+=|\}]{[":;?/><,.]}':
            ans+=1
        i+=1
    return ans
