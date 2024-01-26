import heapq


def get_min_cable_cost(cables):
    total = 0

    heapq.heapify(cables)

    while len(cables) > 1:
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)

        sum_length = first_cable + second_cable
        total += sum_length

        heapq.heappush(cables, sum_length)

    return total


cables = [4, 6, 8, 12, 15]
result = get_min_cable_cost(cables)
print("Сума:", result)
