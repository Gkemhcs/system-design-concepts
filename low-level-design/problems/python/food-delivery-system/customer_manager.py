from core_classes.customer import Customer


class CustomerManager:

    def __init__(self):
        self.__customers:dict[int,Customer]={}
        self.customer_id_counter=1
    def create_customer(self,name:str,email:str,phone_number:int,location)->Customer:
        customer_id=self.customer_id_counter
        customer=Customer(customer_id,name,email,phone_number,location)
        self.__customers[customer_id]=customer
        self.customer_id_counter+=1
        print(f"customer {name} created successfully")
        return customer
    def get_customer(self,id:int)->Customer:
        if id not in self.__customers:
            raise Exception("sorry the customer doesnt exist")
        else:
            return self.__customers.get(id,None)
    def get_customers(self)->list[Customer]:
        customers=list(self.__customers.values())
        return customers