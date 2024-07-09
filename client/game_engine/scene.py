from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def update(self, dt: float) -> None:
        pass
