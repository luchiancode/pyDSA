class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        if len(tokens) == 1: return int(tokens[0])

        while(tokens):
            current = tokens.pop(0)
   
            if((current in operators)):
                no2, no1 = stack.pop(), stack.pop()
                if(current == '+'):
                    stack.append(no1+no2)
                        
                if(current == '-'):
                    stack.append(no1 - no2)

                if(current == '*'):

                    stack.append(no1 * no2)

                if(current == '/'):
                    stack.append(int(no1 / no2))


            else:
                stack.append(int(current))

            
        return int(stack[0])