import time
#
import Number_Ladder_lib as lib

# start, end = input().split()
# starttime = time.time()
# start, end = 26, 61
# end = lib.num_to_str(end)


def get_ans(start, end):
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
                    thing = tuple(lib.str_to_array(k))
                    if thing not in dicti:
                        tempdict[thing] = moves + 1
    #                     print(tempdict)
        moves += 1
    #     print(tempdict)
        dicti.update(tempdict)
    #     print(dicti)

    # if not ended:
    return None
highest_record = 0
count = 0
starttime1 = time.time()

for i in range(100, 1000):
    print(i)
    starttime2 = time.time()
    for j in range(i,
                   1000):
        if i != j:
            boolean = True
            for k in str(i):
                for h in str(j):
                    if k == h:
                        boolean = False
            if boolean:
                thing = get_ans(i, lib.num_to_str(j))
                if thing > highest_record:
                    highest_record = thing
                    count = 1
                elif thing == highest_record:
                    count += 1
    print(f"Total time amassed: {time.time() - starttime1}")
    print(f"This iteration took: {time.time() - starttime2}")
print(count)
# count = 0
# for i in range(100, 1000):
#     if "0" in str(i):
#         count += 1
#         print(i)
# print(count)

# # print(funct(tuple(lib.str_to_array(lib.num_to_str(start))), tuple(lib.str_to_array(lib.num_to_str(end))), 1))
