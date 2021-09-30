#! /usr/bin/env python3


def main():
    print(LlamaFarm.get().num_llamas())
    steve = Llama('Steve')
    waluama = Llama('Waluama')
    print(LlamaFarm.get().num_llamas())


class LlamaFarm:
    def __init__(self):
        # TASK: Add a container to store Llamas.
        self._llamas = []

    @staticmethod
    def get():
        # TASK: Implement this method.
        if LlamaFarm._instance is None:
            LlamaFarm._instance = LlamaFarm()

        return LlamaFarm._instance

    _instance = None

    def add_llama(self, llama):
        self._llamas.append(llama)

    def num_llamas(self):
        return len(self._llamas)


class Llama:
    def __init__(self, name):
        self.name = name
        # TASK: Add the Llama to the LlamaFarm
        LlamaFarm.get().add_llama(self)


if __name__ == '__main__':
    main()
