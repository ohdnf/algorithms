class Linter:
    def __init__(self):
        self.stack = list()
        self.error = ''

    def lint(self, text):
        for idx, char in enumerate(text):
            if self.is_opening_brace(char):
                self.stack.append(char)
            elif self.is_closing_brace(char):
                if self.match_recent_opening_brace(char):
                    pass
                else:
                    # raise SyntaxError
                    self.error = f'Incorrect closing brace: {char} at index {idx}'
            
        if self.stack:
            # raise SyntaxError
            self.error = f'{self.stack[-1]} does not have a closing brace'
    
    def is_opening_brace(self, char):
        return char in ['(', '{', '[']
    
    def is_closing_brace(self, char):
        return char in [')', '}', ']']
    
    def opening_brace_of(self, char):
        return {')': '(', '}': '{', ']': '['}[char]
    
    def recent_opening_brace(self):
        return self.stack.pop() if self.stack else None

    def match_recent_opening_brace(self, char):
        return self.opening_brace_of(char) == self.recent_opening_brace()


if __name__ == '__main__':
    linter = Linter()
    linter.lint('( var x = {y: [1, 2, 3]) } )')
    print(linter.error)