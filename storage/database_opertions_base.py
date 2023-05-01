from abc import ABC, abstractmethod

class DatabaseOperationsBase(ABC):
    """
    Abstract class for database operations
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __get_all_documents(self):
        pass

    @abstractmethod
    def __get_document_by_id(self, document_id):
        pass

    @abstractmethod
    def __create_document_by_id(self, document_id):
        pass

    @abstractmethod
    def __update_document_by_id(self, document_id):
        pass

    @abstractmethod
    def __mul_update_document_by_id(self, document_id):
        pass

    @abstractmethod
    def __delete_document_by_id(self, document_id):
        pass

    @abstractmethod
    def __delete_all_documents(self):
        pass