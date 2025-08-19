from facade import AzureFacade,GCPFacade



def main():
    gcp_facade = GCPFacade()
    azure_facade = AzureFacade()
    print("\n creating gcp resources \n")
    gcp_facade.create()
    print("\n creating azure resources \n")
    azure_facade.create()
    print("\n destroying gcp resources \n")
    gcp_facade.destroy()
    print("\n destroying  azure resources \n")
    azure_facade.destroy()

if __name__ == "__main__":
    main()