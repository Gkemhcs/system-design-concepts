from file_system_node import FileSystemNode
from directory import DirectoryNode 
from file import FileNode
from errors import InvalidPathError, MalformedPathError, PathAlreadyExistsError, FileNotExistError, InvalidFileFormat, InvalidNodeNameError, InvalidContentError

class FileSystem:
    def __init__(self):
        self.root:FileSystemNode=DirectoryNode("/")
    
    def valid_path(self,path:str):
        # Enhanced path validation
        if not path or not isinstance(path, str):
            return False
        if len(path) > 4096:  # Reasonable path length limit
            return False
        if not path.startswith("/"):
            return False
        # Check for invalid characters (basic validation)
        invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
        if any(char in path for char in invalid_chars):
            return False
        return True
    
    def create_path(self,path:str): 
        if not self.valid_path(path):
            raise InvalidPathError("Invalid file or directory path. Path must start with /, be a valid string, and not contain invalid characters")
        
        path_parts=path.split("/")
        # Remove empty strings from splitting
        path_parts = [part for part in path_parts if part]
        
        # Validate path components
        for part in path_parts:
            if not part or len(part) > 255:  # Standard filename length limit
                raise InvalidPathError("Path components cannot be empty or longer than 255 characters")
            if part in ['.', '..']:
                raise InvalidPathError("Path cannot contain '.' or '..' components")
        
        n=len(path_parts)
        node=self.root 
        
        # Create intermediate directories
        for i in range(n-1):
            if node.is_file():
                raise MalformedPathError("Cannot create path: intermediate component is a file")
            if not node.has_child_node(path_parts[i]):
                # Create a new directory node for intermediate paths
                new_dir = DirectoryNode(path_parts[i])
                node.add_child_node(new_dir)
            node=node.get_child_node(path_parts[i])
        
        # Check if final component already exists
        if node.has_child_node(path_parts[-1]):
            raise PathAlreadyExistsError(f"Path '{path}' already exists")
        
        # Create the final component (file or directory)
        if "." in path_parts[-1]:
            # Create a file node for the final component if it has an extension
            new_file = FileNode(path_parts[-1])
            node.add_child_node(new_file)
        else:
            # Create a directory node for the final component if it doesn't have an extension
            new_dir = DirectoryNode(path_parts[-1])
            node.add_child_node(new_dir)
    
    def display(self):
        self.root.display(0)
    
    def display_with_sizes(self):
        """Display the file system with size information"""
        print("File System with Sizes:")
        self._display_node_with_size(self.root, 0)
    
    def _display_node_with_size(self, node, depth):
        """Helper method to display nodes with their sizes"""
        indent = " " * (depth * 2)
        if node.is_file():
            print(f"{indent} File📄: {node.name} (Size: {node.size} bytes)")
        else:
            size = node.get_size()  # This will call update_size() recursively
            print(f"{indent} Directory📁: {node.name} (Size: {size} bytes)")
            for child in node.child_nodes.values():
                self._display_node_with_size(child, depth + 1)
    
    def add_content(self,path:str,content:str):
        if not self.valid_path(path):
            raise InvalidPathError("Invalid file or directory path. Path must start with /, be a valid string, and not contain invalid characters")
        
        if not isinstance(content, str):
            raise InvalidContentError("Content must be a string")
        
        paths=path.split("/")
        # Remove empty strings from splitting
        paths = [part for part in paths if part]
        
        if not paths:
            raise InvalidPathError("Path cannot be empty")
        
        if "." not in paths[-1]:
            raise InvalidFileFormat("Cannot add content: target must be a file with an extension")
        
        node=self.root
        for i in range(len(paths)):
            if not node.has_child_node(paths[i]):
                raise FileNotExistError(f"Path component '{paths[i]}' does not exist")
            node=node.get_child_node(paths[i])
        
        if node.is_file():
            node.set_content(content)
        else:
            raise InvalidFileFormat("Cannot add content to a directory")
    
    def read_content(self,path):
        if not self.valid_path(path):
            raise InvalidPathError("Invalid file or directory path. Path must start with /, be a valid string, and not contain invalid characters")
        
        paths=path.split("/")
        # Remove empty strings from splitting
        paths = [part for part in paths if part]
        
        if not paths:
            raise InvalidPathError("Path cannot be empty")
        
        if "." not in paths[-1]:
            raise InvalidFileFormat("Cannot read content: target must be a file with an extension")
        
        node=self.root
        for i in range(len(paths)):
            if not node.has_child_node(paths[i]):
                raise FileNotExistError(f"Path component '{paths[i]}' does not exist")
            node=node.get_child_node(paths[i])
        
        if node.is_file():
            print("content is:-",node.get_content())
        else:
            raise InvalidFileFormat("Cannot read content from a directory")
    
    def update_content(self,path, content):
        return self.add_content(path, content)
    
    def remove_path(self,path):
        if not self.valid_path(path):
            raise InvalidPathError("Invalid file or directory path. Path must start with /, be a valid string, and not contain invalid characters")
        
        paths=path.split("/")
        path_parts=[path for path in paths if path]
        
        if not path_parts:
            raise InvalidPathError("Cannot remove root directory")
        
        node=self.root 
        for i in range(len(path_parts)-1):
            if not node.has_child_node(path_parts[i]):
                raise FileNotExistError(f"Path component '{path_parts[i]}' does not exist")
            node=node.get_child_node(path_parts[i])
      
        if not node.has_child_node(path_parts[-1]):
            raise FileNotExistError(f"Path '{path_parts[-1]}' does not exist")
        else:
            node.remove_child_node(path_parts[-1])
        print("successfully removed path")



            
