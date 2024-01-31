import time

import Number_Ladder_lib as lib

start1, end1 = input().split()
end1 = lib.num_to_str(end1)
start2, end2 = input().split()
end2 = lib.num_to_str(end2)
start3, end3 = input().split()
end3 = lib.num_to_str(end3)

starttime = time.time()
# start, end = 26, 61


# def funct(num, goal, depth):
#     if num == goal:
#         return 0
#     if depth < 100:
#         arr = lib.transform(num)
#         if goal not in arr:
#             for i in arr:
# #                 print(depth + 1)
#                 print(i, arr)
#                 return funct(tuple(lib.str_to_array(i)), goal, depth + 1)
#         else:
#             return depth
#     return None

def get_ans(start: int, end: str):
    moves = 1
    # ended = False
    dicti = {tuple(lib.str_to_array(lib.num_to_str(start))): 1}

    for i in range(100):
        tempdict = {}
        for j in dicti:
            if dicti[j] == moves:
                # print("INPUT: ", j)
                for k in lib.transform(j):
    #                 print("result:", k, "end: ", end)
                    if k == end:
                        # ended = True
                        return moves
                    if tuple(lib.str_to_array(k)) not in dicti:
                        tempdict[tuple(lib.str_to_array(k))] = moves + 1
    #                     print(tempdict)
        moves += 1
    #     print(tempdict)
        dicti.update(tempdict)
    #     print(dicti)

    # if not ended:
    return None

# moves = 1
# ended = False
# dicti = {tuple(lib.str_to_array(lib.num_to_str(start))): 1}
#
# for i in range(100):
#     tempdict = {}
#     for j in dicti:
#         if dicti[j] == moves:
#             # print("INPUT: ", j)
#             for k in lib.transform(j):
# #                 print("result:", k, "end: ", end)
#                 if k == end:
#                     ended = True
#                     print(moves)
#                     break
#                 if tuple(lib.str_to_array(k)) not in dicti:
#                     tempdict[tuple(lib.str_to_array(k))] = moves + 1
# #                     print(tempdict)
#         if ended:
#             break
#     if ended:
#         break
#     moves += 1
# #     print(tempdict)
#     dicti.update(tempdict)
# #     print(dicti)
#
# if not ended:
#     print("not found")

print(get_ans(start1, end1))
print(get_ans(start2, end2))
print(get_ans(start3, end3))

print(time.time() - starttime)

# # print(funct(tuple(lib.str_to_array(lib.num_to_str(start))), tuple(lib.str_to_array(lib.num_to_str(end))), 1))
