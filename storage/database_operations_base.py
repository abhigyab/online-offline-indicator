from abc import ABC, abstractmethod

class DatabaseOperationsBase(ABC):
    """
    Abstract class for database operations
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_documents(self):
        pass

    @abstractmethod
    def get_document_by_id(self, document_id):
        pass

    @abstractmethod
    def create_document_by_id(self, document_id):
        pass

    @abstractmethod
    def update_document_by_id(self, document_id):
        pass

    @abstractmethod
    def mul_update_document_by_id(self, document_id):
        pass

    @abstractmethod
    def delete_document_by_id(self, document_id):
        pass

    @abstractmethod
    def delete_all_documents(self):
        pass