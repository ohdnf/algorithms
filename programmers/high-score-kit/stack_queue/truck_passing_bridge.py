import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


# 내 풀이

# from collections import deque as dq


# def sum_of(bridge):
#     return sum([w for w, s in bridge])

# def solution(bridge_length, weight, truck_weights):
#     answer = 0

#     passed = []
#     bridge = dq()
#     remains = dq(truck_weights)
    
#     while bridge or remains:
#         count = 0
#         for truck in bridge:
#             if truck[1] == bridge_length:
#                 count += 1
#             else:
#                 truck[1] += 1
#         while count:
#             passed.append(bridge.popleft()[0])
#             count -= 1
        
#         if remains and weight - sum_of(bridge) >= remains[0]:
#             bridge.append([remains.popleft(), 1])
#         answer += 1
#         print(answer, bridge, remains)
    
#     return answer


# if __name__ == '__main__':
#     b = 2
#     w = 10
#     tw = [7, 4, 5, 6]
#     a = solution(b, w, tw)
#     print(a)