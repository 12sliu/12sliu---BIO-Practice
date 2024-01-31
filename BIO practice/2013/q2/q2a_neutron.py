from neutron_lib import Board

# board = Board([5,2,4,1,3]
# ,[1,4,2,3,5])
# board = Board([1,3,5,4,2]
# ,[4,1,2,5,3])
board = Board([int(x) for x in input().split()], [int(x) for x in input().split()])
thing = 0
turn = 0

while thing == 0:
    thing = board.update()
    # print(f"thing is {thing}")
    turn += 1
    # if turn == 1 or turn == 2:
    board.print_state()

board.print_state()
