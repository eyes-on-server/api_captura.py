from abc import ABC, abstractmethod


class Executavel(ABC):

    @abstractmethod
    def executar(self):
        pass
