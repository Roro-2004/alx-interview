#!/usr/bin/python3
"""
Main file
"""


def makeChange(coins, total):
    """
    make change of coins
    """
    if total <= 0:
        return 0
    remainder = total
    coins_needed = 0
    coin_index = 0
    sorted_coins_list = sorted(coins, reverse=True)
    list_len = len(coins)
    while remainder > 0:
        if coin_index >= list_len:
            return -1
        if remainder - sorted_coins_list[coin_index] >= 0:
            remainder -= sorted_coins_list[coin_index]
            coins_needed += 1
        else:
            coin_index += 1
    return coins_needed
