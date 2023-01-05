# Exercise 1

def countsort(l):
    freqs = [0] * (max(l) + 1)
    sorted_list = []
    for num in l:
        freqs[num] += 1

    for i in range(max(l) + 1):
        if freqs[i] != 0:
            sorted_list += [i] * freqs[i]

    return sorted_list


def main1():
    nl = [1, 4, 1, 11, 35, 2, 7, 5, 2, 3, 9, 8]
    print(f"Sorted list is: {countsort(nl)}")


# main1()


def rec_ins_sort(l, n):
    if n <= 1:
        return

    rec_ins_sort(l, n - 1)
    last = l[n - 1]
    j = n - 2
    while j >= 0 and l[j] > last:
        l[j + 1] = l[j]
        j -= 1

    l[j + 1] = last


def main2():
    nl = [1, 4, 1, 2, 7, 5, 2, 3, 9, 8]
    rec_ins_sort(nl, len(nl))
    print(f"Sorted list: {nl}")


main2()
