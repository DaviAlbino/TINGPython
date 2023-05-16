from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queues = PriorityQueue()
    queues.enqueue({"qtd_linhas": 3})
    queues.enqueue({"qtd_linhas": 4})
    queues.enqueue({"qtd_linhas": 7})
    queues.enqueue({"qtd_linhas": 6})
    queues.enqueue({"qtd_linhas": 2})

    assert queues.dequeue() == {"qtd_linhas": 3}
    assert len(queues) == 4

    queues.enqueue({"qtd_linhas": 1})
    assert queues.search(2) == {"qtd_linhas": 1}

    with pytest.raises(IndexError):
        queues.search(75)
