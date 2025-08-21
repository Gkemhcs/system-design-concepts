from file_system_node import FileSystemNode
from errors import NodeAlreadyExistsError, NodeNotFoundError, InvalidNodeNameError

class DirectoryNode(FileSystemNode):
    def __init__(self,name,permissions="drwxr-x---"):
        if not name or not isinstance(name, str):
            raise InvalidNodeNameError("Directory name must be a non-empty string")
        super().__init__(name,permissions)
    
    def add_child_node(self,node:"FileSystemNode"):
        if not node or not isinstance(node, FileSystemNode):
            raise InvalidNodeNameError("Node must be a valid FileSystemNode")
        if not node.name or not isinstance(node.name, str):
            raise InvalidNodeNameError("Node name must be a non-empty string")
        if node.name in self.child_nodes:
            raise NodeAlreadyExistsError(f"Node '{node.name}' already exists in directory '{self.name}'")
        else:
            self.child_nodes[node.name]=node 
    
    def remove_child_node(self,name):
        if not name or not isinstance(name, str):
            raise InvalidNodeNameError("Node name must be a non-empty string")
        if name in self.child_nodes:
            del self.child_nodes[name]
        else:
            raise NodeNotFoundError(f"Node '{name}' is not present in directory '{self.name}'")
    
    def has_child_node(self, name)->bool:
        if not name or not isinstance(name, str):
            return False
        if name in self.child_nodes:
            return True 
        return False 
    
    def display(self,depth):
        if depth < 0:
            depth = 0
        indent=" "*(depth*2)
        print(f"{indent} Directory📁:{self.get_name()}")
        for node in self.child_nodes.values():
            node.display(depth+1)
    
    def get_size(self):
        # Always calculate fresh size when getting directory size
        return self.update_size()
    
    def update_size(self):
        # Simple and consistent: iterate through all child nodes, add their sizes
        total_size = 0
        for node in self.child_nodes.values():
            if node.is_file():
                # For files, just add their current size
                total_size += node.size
            else:
                # For directories, recursively call update_size to get their total size
                total_size += node.update_size()
        
        self.size = total_size
        return self.size
    
    def get_child_node(self,name)->"FileSystemNode":
        if not name or not isinstance(name, str):
            raise InvalidNodeNameError("Node name must be a non-empty string")
        if name not in self.child_nodes:
            raise NodeNotFoundError(f"Node '{name}' not found in directory '{self.name}'")
        return self.child_nodes[name]
    
