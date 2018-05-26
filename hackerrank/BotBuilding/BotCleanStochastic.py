#!/usr/bin/python

# Head ends here
ar = 0
ac = 0
nr = 0
nc = 0
flag = -1
def IsThisClean(x,y,flag):
    if board[x][y] == 'd':
        print('CLEAN')
        

def next_move(posr, posc, board):
    k_min = 9999
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 'd':
                nr = posr - i
                nc = posc - j
                dist = abs(nr) + abs(nc)
                if k_min > dist :
                    k_min = dist
                    ar = i
                    ac = j
                    

    return ar,ac,nr,nc


def myway(kr,kc,kdr,kdc,x,y,flag,board):
    IsThisClean(x,y,flag)
    
    if board[x][y] != 'd':
        if abs(kdr) > abs(kdc):
            if kdr > 0 :
                print('UP')
            else :
                print('DOWN')
        else :
            if kdc > 0:
                print('LEFT')
            else :
                print('RIGHT')
    else :
        return 0
            
    
            
            

            

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    flag = -1
    kr,kc,kdr,kdc = next_move(pos[0], pos[1], board)
    myway(kr,kc,kdr,kdc,pos[0],pos[1],flag,board)
            
    
            
