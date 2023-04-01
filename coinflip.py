import numpy as np

probability = 0.5
n = 10

fullResults = np.arange(n)


def CoinFlip(self):
    result = np.random.binomial(1, 0.5)  # one flip, 50 percent chance

    return result


for i in range(0, n):
    fullResults[i] = CoinFlip(probability)
    i += 1

print("Heads = 1, Tails = 0: ", fullResults)

print("Head Count: ", np.count_nonzero(fullResults == 1))
print("Tails Count: ", np.count_nonzero(fullResults == 0))
