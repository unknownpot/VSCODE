def paranthesis(openCount, closeCount, n, output = []):
    if closeCount == n:
        print(''.join(output))
        return
    
    else:
        if (openCount > closeCount):
            output.append(')')
            paranthesis(openCount, closeCount+1, n, output)
            output.pop()

        if (openCount < n):
            output.append('(')
            paranthesis(openCount+1, closeCount, n, output)
            output.pop()
    return

x = int(input())
paranthesis(0, 0, x)
