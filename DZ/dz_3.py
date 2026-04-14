# -*- coding: utf-8 -*-
# домашняя работа №2        Вриант №6



# задание №1
"""
Реализовать очередь на двух стеках.
"""
class Queue_2_Stacks:
    def __init__(self):
        self.push_stak = []
        self.pop_stak = []


    def enqueue(self, item):    # добавляем элемент в конец очереди (push_stak)
        self.push_stak.append(item)


    def dequeue(self):  # удяляем 1 элемент из очерди (1 для push_stak, но последний для pop.stak)
        if self.is_empty():
            raise IndexError("Очередь пуста")

        if not self.pop_stak:
            while self.push_stak:   # переносим из push_stak в pop_stak (теперь порядок правильный)
                perm = self.push_stak.pop()
                self.pop_stak.append(perm)

        return self.pop_stak.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")

        if not self.pop_stak:
            while self.push_stak:
                self.pop_stak.append(self.push_stack.pop())
        
        return self.pop_stak[-1]


    def is_empty(self):
        return len(self.push_stak) == 0 and len(self.pop_stak) == 0


    def size(self):     # мы ведь можем продолжить дописывать значения, поэтому суммируем длины обоих
        return len(self.push_stak) + len(self.pop_stak)



# задача №2
"""
Написать функцию для проверки корректности скобок с использованием очереди 
(по аналогии с тем что делали со стеком на лабах).
"""
from collections import deque

def is_valid_clovo(clovo):
    matching = {')': '(', ']': '[', '}': '{'}
    queue_stak = deque()

    for ch in clovo:
        if ch in "({[":
            queue_stak.append(ch)
        else:
            if not queue_stak or queue_stak[-1] != matching[ch]:
                return False
            queue_stak.pop()
    return len(queue_stak) == 0



# задача №3 (с литкода 232)
'''
232. Реализация очереди с использованием стеков.
Реализуйте очередь типа «первым вошел — первым вышел» (FIFO), 
используя всего два стека. Реализованная очередь должна поддерживать все 
функции обычной очереди ( push, peek, pop, и empty).
'''
# уже сделана, получается



# задача №4 (с литкода 622)
"""
Разработайте свою реализацию кольцевой очереди. Кольцевая очередь — это линейная структура данных, 
в которой операции выполняются по принципу FIFO (первым вошел — первым вышел), и 
последняя позиция соединяется с первой, образуя замкнутый круг. Её также называют «кольцевым буфером».

Одно из преимуществ кольцевой очереди заключается в возможности использования свободного места 
перед ней. В обычной очереди, как только она заполняется, мы не можем вставить следующий 
элемент, даже если перед ней есть свободное место. Но в кольцевой очереди мы можем использовать 
это пространство для хранения новых значений.

Реализуйте MyCircularQueueкласс:

MyCircularQueue(k)Инициализирует объект размером очереди, равным k.
int Front()Получает первый элемент из очереди. Если очередь пуста, возвращает значение -1.
int Rear()Получает последний элемент из очереди. Если очередь пуста, возвращает значение -1.
boolean enQueue(int value)Вставляет элемент в кольцевую очередь. Возвращает значение, true если операция выполнена успешно.
boolean deQueue()Удаляет элемент из кольцевой очереди. Возвращает значение, trueесли операция выполнена успешно.
boolean isEmpty()Проверяет, пуста ли кольцевая очередь.
boolean isFull()Проверяет, заполнена ли кольцевая очередь.
Вам необходимо решить задачу, не используя встроенную в ваш язык программирования структуру данных "очередь". 
"""

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.max_size = k
        self.rear = 0
        self.front = 0
        self.size = 0


    def enQueue(self, value):
        if self.isFull():   # при полной очереди не получится добавить
            return False

        self.queue[self.rear] = value   # при добавлении в конец смещаем правый указатель на 1 в пределах max_size
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

        return True


    def deQueue(self):
        if self.isEmpty():  # при пустой очереди не получится удалить
            return False
        
        self.front = (self.front + 1) % self.max_size   # попробую просто сдвинуть указатель с начала (началом станет следующий элемент)
        self.size -= 1

        return True


    def Front(self):
        if self.isEmpty():  # не можем ничего вывести, если она пустой
            return -1

        return self.queue[self.front]


    def Rear(self):
        if self.isEmpty():  # не можем ничего вывести, если она пустой
            return -1

        return self.queue[(self.rear - 1 + self.max_size) % self.max_size]
    # resr смотрит на (последний элмент + 1), чтобы записывать в него, так что я отнимаю 1
    # я добавляю max_size) % self.max_size, чтобы в ситуации, если rear смотрит на начало - мы сдвинулись на -1 элемент


    def isEmpty(self):
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.max_size



# задача №5 (с литкода 933)
"""
У вас есть RecentCounter класс, который подсчитывает количество недавних запросов за 
определенный период времени.

Реализуйте RecentCounterкласс:

RecentCounter()Инициализирует счетчик нулевым количеством недавних запросов.
int ping(int t)Добавляет новый запрос в момент времени t, где tпредставляет собой некоторое время в 
миллисекундах, и возвращает количество запросов, которые произошли за прошедшие 3000миллисекунды 
(включая новый запрос). В частности, возвращает количество запросов, которые произошли в указанном диапазоне [t - 3000, t].
Гарантируется , что каждый последующий вызов pingиспользует значение, строго большее, t чем значение, использованное в предыдущем вызове.
"""
class RecentCounter:
    def __init__(self):
        self.queue = deque()
#        self.kol = 0
#        self.front = 0

    def ping(self, t):
        self.queue.append(t)    # новый элемент добавили
#        kol += 1

        while self.queue[0] < t-3000: # старые почистили
            self.queue.popleft()

        return len(self.queue)

           



q = Queue_2_Stacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1 (должно быть)
print(q.dequeue())  # 2 (должно быть)
q.enqueue(4)
print(q.dequeue())  # 3 (должно быть)
print(q.dequeue())  # 4 (должно быть)
print(q.is_empty()) # True (должно быть)

print(is_valid_clovo("([]){}"))   # True (должно быть)
print(is_valid_clovo("([)]"))     # False (должно быть)

cq = MyCircularQueue(3)
print(cq.enQueue(1))  # True (должно быть)
print(cq.enQueue(2))  # True (должно быть)
print(cq.enQueue(3))  # True (должно быть)
print(cq.enQueue(4))  # False (должно быть)
print(cq.Rear())      # 3(должно быть)
print(cq.isFull())    # True (должно быть)
print(cq.deQueue())   # True (должно быть)
print(cq.enQueue(4))  # True (должно быть)
print(cq.Rear())      # 4 (должно быть)

rc = RecentCounter()
print(rc.ping(1))     # 1 (должно быть)
print(rc.ping(100))   # 2(должно быть)
print(rc.ping(3001))  # 3 (должно быть)
print(rc.ping(3002))  # 3 (должно быть)
















