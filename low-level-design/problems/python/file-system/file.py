from file_system_node import FileSystemNode
from errors import InvalidNodeNameError

class FileNode(FileSystemNode):

    def __init__(self,name,is_file=True,permissions="-rwxr-x---",content=""):
        if not name or not isinstance(name, str):
            raise InvalidNodeNameError("File name must be a non-empty string")
        if not isinstance(content, str):
            raise InvalidNodeNameError("Content must be a string")
        file_type=self.extract_extension(name)
        super().__init__(name,is_file=is_file,content=content,permissions=permissions,file_type=file_type)
    
    def get_child_node(self,name):
        # Files cannot have child nodes
        return None
    
    def add_child_node(self,node:"FileSystemNode"):
        # Files cannot have child nodes
        raise InvalidNodeNameError("Files cannot contain child nodes")
    
    def remove_child_node(self,name:str):
        # Files cannot have child nodes
        raise InvalidNodeNameError("Files cannot contain child nodes")
    
    def extract_extension(self,filename)->str:
        if not filename or not isinstance(filename, str):
            return ""
        parts = filename.split(".")
        return parts[1] if len(parts) > 1 else ""
    
    def has_child_node(self,name:str):
        # Files cannot have child nodes
        return False 
    
    def update_size(self):
        # For files, simply return the current size
        return self.size
    
    def display(self,depth):
        if depth < 0:
            depth = 0
        indent=" "*depth*2
        print(f"{indent} File name📄:{self.name}")
    