from abc import ABC,abstractmethod
import time 
class FileSystemNode(ABC):

    def __init__(self,name:str,permissions:str,is_file:bool=False,content="",file_type=""):

        self._is_file=is_file
        self.child_nodes:dict[str:"FileSystemNode"]={}
        self.name=name 
        self.createTime=time.time()
        self.modifyTime=time.time()
        self.size=len(content)
        self.permissions=permissions 
        self.content=content
        self.file_type=file_type
    @abstractmethod
    def add_child_node(self,node:"FileSystemNode"):
        pass 
    @abstractmethod
    def has_child_node(self,name):
       pass 
    @abstractmethod 
    def get_child_node(self,name)->"FileSystemNode":
       pass 
    @abstractmethod
    def remove_child_node(self,name):
        pass

    @abstractmethod
    def display(self,depth):
        pass 

    def update_size(self,size):
        self.size+=size
    def get_name(self)->str:
        return self.name 
    
    def  set_content(self,content:str):
        self.content=content
        self.modifyTime=time.time()
        self.size=len(content)
    def get_content(self)->str:
        return self.content
    def get_permissions(self)->str:
        return self.permissions
    def is_file(self)->bool:
        return self._is_file