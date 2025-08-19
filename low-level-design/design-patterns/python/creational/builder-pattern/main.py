from vm_builder import VMBuilder


def main():
    builder=VMBuilder("VM1")
    vm=(
     builder.add_cpu(2)
    .add_network("network-1").add_memory(16).add_datadisk("disk-1",100).add_datadisk("disk-2",200).build()
    )
    
   

if __name__ == "__main__":
    main()
