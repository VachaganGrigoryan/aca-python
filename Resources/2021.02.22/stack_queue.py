from typing import Iterable, Any
from abc import ABC, abstractmethod


class AbstractStack(ABC):

    def __init__(self, items: Iterable = None):
        super().__init__()
        self._data = list(items) if items else []

    @abstractmethod
    def push(self, item: Any):
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass


class Stack(AbstractStack):

    def __repr__(self) -> str:
        return f'Stack({self._data})'

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, item: Any) -> bool:
        return item in self._data

    def __add__(self, other):
        if not isinstance(other, Stack):
            raise TypeError(f'Instance of Stack expected {type(other)} found')
        return Stack(self._data + other._data)

    def push(self, item: Any):
        self._data.append(item)

    def pop(self) -> Any:
        return self._data.pop()


class Queue:

    def __init__(self, items: Iterable = None):
        super().__init__()
        self._data = list(items) if items else []

    def __repr__(self) -> str:
        return f'Queue({self._data})'

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, item: Any) -> bool:
        return item in self._data

    def enqueue(self, item: Any):
        """ Enqueue method of generic queue object which accepts any object

        Parameters
        ----------
        item : any object

        Returns
        -------
        None

        """
        self._data.insert(0, item)

    def dequeue(self) -> Any:
        return self._data.pop()


class LimitedQueue(Queue):
    """ Generic queue implementation with limited number of items

    """
    def __init__(self, limit: int, items: Iterable = None):
        # TODO: validate length of initialization items
        super().__init__(items)
        self._limit = limit

    def enqueue(self, item: Any) -> bool:
        """

        Parameters
        ----------
        item : Any

        Returns
        -------
        bool

        Raises
        ------
        QueueLimitReachedError

        """
        if len(self) == self._limit:
            return False

        super().enqueue(item)
        return True


if __name__ == '__main__':
    empty_stack = Stack()
    prefilled = Stack((10, 20 ,30))

    empty_stack.push('message')
    empty_stack.push(['hello', 'there'])
    print('>>>', prefilled.pop())
    print('Length of prefilled stack =', len(prefilled))

    combined = empty_stack + prefilled  # empty_stack.__add__(prefilled)

    print(empty_stack)
    print(prefilled)
    print(combined)
    print('message' in combined)

    queue = Queue([-1, -2, -3])
    queue.enqueue(-4)
    print(queue)
    print(queue.dequeue())
    help(Queue.enqueue)
