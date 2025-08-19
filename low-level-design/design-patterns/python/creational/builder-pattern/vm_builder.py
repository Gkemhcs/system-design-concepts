from vm  import VM

class VMBuilder:
    def __init__(self,name:str):
      
        self.vm=VM(name)

    def add_cpu(self,cores:int):
        print(f"{cores} cores added")
        self.vm.cpu=cores
        return self
    
    def add_memory(self,memory:int):
        print(f"{memory} GB added")
        self.vm.memory=memory
        return self
    
    def add_datadisk(self,disk_name:str,size:int):
        print(f"{disk_name} with {size} GB added")
        self.vm.datadisks.append({"name":disk_name,"size":size})
        return self
    
    def add_network(self,network_name:str):
        print(f"{network_name} added")
        self.vm.network.append(network_name)
        return self


    def build(self):
        print("VM built")
        return self.vm


