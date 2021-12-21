import random

def random_sampling(k, A):
    # rando_list = []
    for i in range(k):
        # generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
        # rando_list.append(A[r])
    return A



exo = random_sampling(3, [3, 7, 5, 11])
print(exo)