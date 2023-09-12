def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    d=len(s)
    while d>a:
        a+=s[0]
    return a
print(main(int(input())))