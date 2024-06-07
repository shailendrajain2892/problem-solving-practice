def best_time_to_buy_sell(numbers:list) -> int:
    maxProfit=0
    curProfit=0
    mini=numbers[0]
    for num in numbers[1:]:
        profit = num - mini
        if profit < 0:
            mini = num
        elif profit > 0:
            if profit > curProfit:
                curProfit = profit
            if curProfit > maxProfit:
                maxProfit = curProfit
    return maxProfit

numbers = [7, 1, 5, 3, 6, 4, 0, 4]
print(best_time_to_buy_sell(numbers))
    