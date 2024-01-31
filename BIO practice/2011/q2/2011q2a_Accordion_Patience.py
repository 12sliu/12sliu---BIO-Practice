import copy

from lib_Accordion_Patience import CardManager

nums = [int(x) for x in input().split()]
# nums = [1, 3, 5, 7, 2 ,4]

og = CardManager(nums)
print(og.cards[0],og.cards[-1])
# og.print_cards()
# print(len(og.piles))
# print()

cardmanager1 = copy.deepcopy(og)
cardmanager1.strat(cardmanager1.strat_one_update)
print(len(cardmanager1.piles), cardmanager1.piles[0].top)

cardmanager2 = copy.deepcopy(og)
cardmanager2.strat(cardmanager2.strat_two_update)
print(len(cardmanager2.piles), cardmanager2.piles[0].top)

cardmanager3 = copy.deepcopy(og)
cardmanager3.strat(cardmanager3.strat_three_update)
print(len(cardmanager3.piles), cardmanager3.piles[0].top)

# Test 2: 3/4
# Test 4: 3/4
# Test 5: 3/4

