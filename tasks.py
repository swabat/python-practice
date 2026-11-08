#from collections import Counter

total = 0
for i in range(1, 11):
    total += i
print(total)


def find_max(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num


#def letters_count(word):
#    return Counter(word)


def letters_count(word):

    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts


def not_archived(notes):
    return [task["title"] for task in notes if not task["archived"]]