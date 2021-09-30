#! /usr/bin/env python3

import abc  # abstract base class


def main():
    Observer()
    steve = Llama('Steve')
    print(steve.friend_names())
    waluama = Llama('Waluama')
    print(steve.friend_names())


class LlamaFarm:
    def __init__(self):
        self._llamas = []
        # TASK: Add a container for subscribers.
        self._observers = set()

    @staticmethod
    def get():
        if LlamaFarm._instance is None:
            LlamaFarm._instance = LlamaFarm()

        return LlamaFarm._instance

    _instance = None

    def subscribe(self, observer):
        # TASK: Register the new subscriber.
        self._observers.add(observer)

    def unsubscribe(self, observer):
        # TASK: Un-register the subscriber
        self._observers.remove(observer)

    def add_llama(self, llama):
        self._llamas.append(llama)
        # TASK: Push the new llama to all subscribers.
        for observer in self._observers:
            observer.update_new_llama(llama)

    def num_llamas(self):
        return len(self._llamas)


class Observer(abc.ABC):
    def update_new_llama(self, new_llama):
        # Update methods do nothing by default
        pass


class Llama(Observer):
    def __init__(self, name):
        self.name = name
        # TASK: Add a container for friends.
        self._friends = set()
        LlamaFarm.get().add_llama(self)
        # TASK: Register this Llama as a subscriber.
        LlamaFarm.get().subscribe(self)

    def friend_names(self):
        return [friend.name for friend in self._friends]

    def update_new_llama(self, llama):
        # TASK: Store the new Llama as a friend.
        self._friends.add(llama)


if __name__ == '__main__':
    main()
