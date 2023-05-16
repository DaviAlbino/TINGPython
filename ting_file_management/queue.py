from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        if self.queue == []:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index >= 0 and index <= len(self.queue) - 1:
            return self.queue[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
