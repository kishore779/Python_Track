class Mobile:
    def __init__(self, model : str, ram : int, storage : int):
        self.model = model
        self.ram = ram
        self.storage = storage
    
    def display_mobile(self):
        print(f"Model : {self.model} | RAM : {self.ram} | Storage : {self.storage}")
    

mobile1 = Mobile("readmi",16, 256)
mobile2 = Mobile("oppo", 12, 256)

mobile1.display_mobile()
mobile2.display_mobile()