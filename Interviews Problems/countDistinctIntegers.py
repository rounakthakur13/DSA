def countDistinctIntegers(n,m=-1,board=[]):
    if n == 1:
        return n
    if m>=n:
        return (len(set(board)))
    for i in range(1,n):
        if n%i ==  1:
            if (n-i) not in board:
                print(i)
                board.append(n-i)
    m +=1
    if board[m] > 1:
        countDistinctIntegers(board[m],m,board)
    board.append(n)
    print(sorted(board))
    return (len(set(board)))
print(countDistinctIntegers(133))