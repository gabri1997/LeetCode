"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

def maxProfit(prices):
    
    # Generator expression: prices[i] >= prices[i+1] for i in range(len(prices) - 1)
    # A differenza della list comprehension [prices[i] >= prices[i+1] for i in range(len(prices) - 1)] restituisce un oggetto generatore che può essere iterato
    # La list comprehension crea invece una lista in memoria
    # La funzione all() consuma il generatore e restituisce True solo se tutti i valori restituiti dal generatore sono True
    if all(prices[i] >= prices[i+1] for i in range(len(prices) - 1)):
           return 0
    profit = 0
    for i in range(len(prices) -1):
        if prices[i] < prices[i+1]:
             profit += prices[i+1] - prices[i]
    return profit            
    
if __name__ == '__main__':

    prices = [7,1,5,3,6,4]
    profit = maxProfit(prices)
    print('Profit: ', profit)