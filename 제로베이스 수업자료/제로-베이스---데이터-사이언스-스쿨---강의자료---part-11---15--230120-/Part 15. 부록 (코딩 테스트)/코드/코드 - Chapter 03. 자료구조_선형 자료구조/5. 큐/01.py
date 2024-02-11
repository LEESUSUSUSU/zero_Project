# Python에서 큐 사용하기 (리스트 응용)

queue = []
for i in range(1, 11):
    queue.append(i)  # put()은 append()를 이용
print(queue)

print(queue[0])  # peek()는 [0]를 이용

for i in range(1, 11):
    val = queue.pop(0)  # get()은 pop(0)을 이용
    print(val, end=' ')
print()


# Python 에서 큐 사용하기 (queue 패키지 사용)
from queue import Queue

queue = Queue()
for i in range(1, 11):
    queue.put(i)

# print(queue.peek())  # peek()는 미구현

for i in range(1, 11):
    val = queue.get()
    print(val, end=' ')
print()

