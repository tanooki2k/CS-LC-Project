from abc import abstractmethod
from Tools.ObserverDesignPattern import Observer


class FileManager(Observer):
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self, record):
        pass
    
    @abstractmethod
    def delete(self):
        pass
    