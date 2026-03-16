"""
The following code has been taken from: https://refactoring.guru/design-patterns/observer/python/example
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def notify(self, new_record: Dict[str, Any]) -> None:
        """
        Notify all observers about an event.
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, new_record: Dict[str, Any]) -> None:
        """
        Receive update from subject.
        """
        pass

class GraphObserver(Observer):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, new_record: Dict[str, Any]) -> None:
        """
        Receive update from subject.
        """
        pass

    @abstractmethod
    def show(self, can_save: bool = False, path:str =""):
        """
        Save graph plotted.
        """
        pass
