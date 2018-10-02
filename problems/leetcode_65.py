from pdb import set_trace


class Solution(object):
    def isNumber(self, s):
        """
        Determine if a string is a valid number

        Parameters
        ----------
        s: str
            A string
        
        Returns
        -------
        bool:
            True if a valid string
        
        Notes
        -----
        A: Start
        B: plus/minus
        D: Dot
        E: exp
        F: Final
        S: space
        X: Invalid
        """

        def what_is(char):
            """
            Return a state corresponding to the type of character
            
            Parameters
            ----------
            char : str
                A Charecter
            
            Returns
            -------
            str:
                Type label
            """
            if char.isdigit():
                return 'num'
            if char == 'e':
                return 'exp'
            if char in ['+', '-']:
                return 'sym'
            if char == ' ':
                return 'space'
            if char == '.':
                return 'dot'
            else:
                return 'alpha'

        det_finite_automata = {
            'A': {
                'num': 'F',
                'sym': 'B',
                'dot': 'D',
                'exp': 'X',
                'space': 'A',
                'alpha': 'X'
            },
            'B': {
                'num': 'F',
                'sym': 'X',
                'exp': 'X',
                'dot': 'X',
                'space': 'B',
                'alpha': 'X'
            },
            'D': {
                'num': 'F',
                'sym': 'X',
                'dot': 'X',
                'exp': 'X',
                'space': 'X',
                'alpha': 'X'
            },
            'E': {
                'num': 'F',
                'sym': 'B',
                'dot': 'X',
                'exp': 'X',
                'space': 'S',
                'alpha': 'X'
            },
            'F': {
                'num': 'F',
                'sym': 'B',
                'dot': 'D',
                'exp': 'E',
                'space': 'F',
                'alpha': 'X'
            },
            'S': {
                'num': 'F',
                'sym': 'B',
                'dot': 'D',
                'exp': 'E',
                'space': 'S',
                'alpha': 'X'
            },
            'X': {
                'num': 'X',
                'sym': 'X',
                'dot': 'X',
                'exp': 'X',
                'space': 'X',
                'alpha': 'X'
            },
        }

        next_ = 'A'
        is_dot = None
        for c in s:
            key = what_is(c)
            next_ = det_finite_automata[next_][key]
            if is_dot:
                det_finite_automata['D'] = det_finite_automata['X']
            is_dot = next_ if next_ == 'D' else None            

        return next_ == 'F'

if __name__ == "__main__":
    s = '  5.5.5'
    sol = Solution()
    print(sol.isNumber(s))


