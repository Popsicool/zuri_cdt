'''
Task title:
    Implementing a Cascading Palindrome

Style:
    pycodestyle validation was used

Time Complexity:

    Converting the input parameter to a string:
        O(1).

    Splitting the parameter using split():
        O(n), where n is the length of the parameter.

    Iterating through the split components:
        This step iterates through each component once,
        which takes O(m) time, where m is the number of
        components obtained after splitting.

    _check_pal method:
        Checking if a string is a palindrome takes O(k) time,
        where k is the length of the string being checked.
        Since this method is called for each component,
        the time complexity of the palindrome check step is O(m * k),
        where m is the number of components and k is
        the average length of a component.

    Overall time complexity is O(n + m * k).

Space Complexity:

    The space complexity is dominated by the storage of the input components
    and the potential palindromic segments,
    leading to an overall space complexity of O(n).

'''


class Palindrome:
    '''
    palindrom class
    '''
    def __init__(self, param=None) -> None:
        '''
        Initialize the class with a paramater
        '''
        self.param = param

    def _check_pal(self, word) -> bool:
        '''
        Private method to check if a string is a palindrom
        '''
        if word[0] != word[-1]:
            '''
            check if first letter is not equals to last letter.
            Since indexing a list has a constant time complexity, 0(1),
            this operation doesn't prolong the run
            time but instead prevent future time
            usage and operation if it can be deduced that
            word is not a palindrom using first and last character
            '''
            return False
        return word == word[::-1]

    def find_palindrom(self) -> str:
        '''
        it find all the palindrom in the parameter passed
        and return them all as a string joined with a space
        '''
        if not self.param:
            '''
            If no param was passed, return empty string
            '''
            return ""
        if not isinstance(self.param, str) and not isinstance(self.param, int):
            '''
            check if proper input type is provided
            integer is allowed alongside string because
            the input will be converted to str with str() operation
            which has a constant time complexity
            '''
            return "Invalid input: Parameter must be a string or integer"
        '''
        split parameter into a list with the built in split function
        which has a time and space complexity of 0(n)
        '''
        texts = str(self.param).split()
        '''
        using list comprehension, first convert the text to lower,
        check if its a palindrom, if yes, add to list
        conversion to lower takes a time complexity of O(n), needed to ensure
        case differences doesn't affect.
        Eg Hannah with uppercase H and lowercase h
        '''
        all_palid = [text for text in texts if self._check_pal(text.lower())]
        return ' '.join(all_palid)


if __name__ == "__main__":
    '''
    Only run when not imported
    '''
    # example 1, check with a palindrom integer,
    example1 = Palindrome(12321)
    print(f'12321 as number Returns: {example1.find_palindrom()}')
    # example 2, check palindrum number passed as a string
    example2 = Palindrome("12321")
    print(f'12321 as a string Returns: {example2.find_palindrom()}')
    # example 3, check non palindrum integer
    example3 = Palindrome(123215)
    print(f'123215 as number Returns: {example3.find_palindrom()}')
    # example 4, test non palindrum number passed as a string
    example4 = Palindrome("123215")
    print(f'123215 as a string Returns: {example4.find_palindrom()}')
    # example 5, test with no input
    example5 = Palindrome()
    print(f'No input Returns: {example5.find_palindrom()}')
    # example 6, test with a list
    example6 = Palindrome([1, 1])
    print(f'test with List Returns: {example6.find_palindrom()}')
    # example 7, test with a dict
    example7 = Palindrome({"A": "a"})
    print(f'test with Dict Returns: {example7.find_palindrom()}')
    # example 8, test with 1230321 09234 0124210 provided on zuriboard
    example8 = Palindrome('1230321 09234 0124210')
    print(f'1230321 09234 0124210 Returns: {example8.find_palindrom()}')
    # example 9, test abcd5dcba 1230321 09234 0124210 provided on zuriboard
    example9 = Palindrome('abcd5dcba 1230321 09234 0124210')
    print(f'1230321 09234 0124210 Returns: {example9.find_palindrom()}')
    # example 10, test with a string containing both palindrom and no palindrom
    example10 = Palindrome(
        "Hannah Montana is an American teen sitcom created by \
        Michael Poryes Rich Correll and Barry O'Brien that aired on \
        Disney Channel for four seasons")
    print(f'Example10 Returns: {example10.find_palindrom()}')
    # example 11, test with a string containing both palindrom and no palindrom
    example11 = Palindrome(
        "Aibohphobia Lemel Tenet areall palindrom including 1234554321"
        )
    print(f'Example11 Returns: {example11.find_palindrom()}')
