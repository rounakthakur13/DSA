def countDistinctIntegers(n,m=-1,board=[]):
    if m>=n:
        return board
    for i in range(1,n):
        if n%i ==  1:
            if (n-i) not in board:
                board.append(n-i)
    m +=1
    if board[m] > 1:
        countDistinctIntegers(board[m],m,board)
    board.append(n)
    return len(set(board))
print(countDistinctIntegers(1000))