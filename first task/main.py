from factory import USVehicycleFactory, EUVehicycleFactory

if __name__== "__main__":
    us_factory = USVehicycleFactory()
    eu_factory = EUVehicycleFactory()

    car_us = us_factory.create_car("Ford", "Mustang")
    car_us.start_engine()

    bike_us = us_factory.create_motorcycle("Harley-Davidson","Sportster")
    bike_us.start_engine()

    car_eu = us_factory.create_car("Volkswagen", "Golf")
    car_eu.start_engine()

    bike_eu = us_factory.create_motorcycle("BMW","R1250")
    bike_eu.start_engine()


     
