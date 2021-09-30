#! /usr/bin/env python3

import abc  # abstract base class


def main():
    # FIXME: Create and run the controller


# Model
class LlamaFarm:
    def __init__(self):
        self._llamas = []
        self._observers = set()

    @staticmethod
    def get():
        if LlamaFarm._instance is None:
            LlamaFarm._instance = LlamaFarm()

        return LlamaFarm._instance

    _instance = None

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def get_llama_list(self):
        return self._llamas

    def add_llama(self, llama):
        self._llamas.append(llama)
        for observer in self._observers:
            observer.update_new_llama(llama)

    def run_away(self, llama_name):
        self._llamas = [
            llama for llama in self._llamas if llama.name != llama_name]
        # FIXME: broadcast to subscribers

    def num_llamas(self):
        return len(self._llamas)


class Observer:
    def update_new_llama(self, new_llama):
        # Update methods do nothing by default,
        # the observer is ignoring the pushed data.
        pass

    # FIXME: Add update for llama run away


class Llama(Observer):
    def __init__(self, name):
        self.name = name
        self._friends = set()
        # FIXME: We'll do these actions in the Controller
        LlamaFarm.get().add_llama(self)
        LlamaFarm.get().subscribe(self)

    def friend_names(self):
        return [friend.name for friend in self._friends]

    def update_new_llama(self, llama):
        self._friends.add(llama)

    # Note: Llama is only paying attention to new llama updates.


# FIXME: Add View base class


class LlamaView(View):

    def show(self):
        print('----------------------------------------------------')
        for llama in LlamaFarm.get().get_llama_list():
            print(llama.name, 'has', len(llama.friend_names()), 'friend(s)')

        print(len(self._ran_away), 'llamas have run away:')
        if len(self._ran_away):
            print(self._ran_away)

    # FIXME: Override update_llama_ran_away


class Controller:
    def __init__(self):
        # FIXME: Initialize view to None

    def run(self):
        # FIXME: Create view, subscribe to it

        while True:
            try:
                self._view.show()
                cmd = input('Enter a command: ')
                cmd = [item.strip() for item in cmd.split()]
                if cmd[0] == 'add_llama':
                    # FIXME: Add llama command
                if cmd[0] == 'run_away':
                    # FIXME: Add run away command
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
