orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]


def solution(orders, course):
    answer = []

    for c in range(0, len(course)):
        print(course[c])
        for order in orders:
            print(order)

    return answer


print(solution(orders, course))
