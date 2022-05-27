class Cars:
    types="automobile"
    brand="audi"
    def __init__(self,model,exshowroomprice,variants,mileage,color):
        self.model=model
        self.exshowroomprice=exshowroomprice
        self.variants=variants
        self.mileage=mileage
        self.color=color
a6=Cars("audi6",100000,"sedan",500,"blue")
a3=Cars("audi3",200000,"suv",100,"green")
print("a6 is a {} of brand{}".format(a6.__class__.types,a6.__class__.brand))
print("a3 is a {} of brand{}".format(a3.__class__.types,a3.__class__.brand))
print("{} has price {} of variant {} has mileage{} of color{}".format(a6.model,a6.exshowroomprice,a6.variants,a6.mileage,a6.color))
print("{} has price {} of variant {} has mileage{} of color{}".format(a3.model,a3.exshowroomprice,a3.variants,a3.mileage,a3.color))