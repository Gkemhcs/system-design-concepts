from file_system_singleton import FileSystemSingleton

def main():

    file_system=FileSystemSingleton.get_file_system()
    file_system.create_path("/lld")
    file_system.create_path("/hld")
    file_system.create_path("/python/design-patterns/singleton/main.py")
    try:
        file_system.create_path("/lld")
    except Exception as e:
        print(e)
    
    file_system.display()
    file_system.add_content("/python/design-patterns/singleton/main.py","i am here")
    file_system.read_content("/python/design-patterns/singleton/main.py")
    file_system.add_content("/python/design-patterns/singleton/main.py","i am there")
    file_system.read_content("/python/design-patterns/singleton/main.py")
    
    # Test size calculation
    print("\n=== Testing Size Calculation ===")
    file_system.display_with_sizes()
    
    file_system.remove_path("/hld")

    file_system.display()
    
    print("\n=== Final Size Calculation ===")
    file_system.display_with_sizes()

if __name__=="__main__":
    main()

