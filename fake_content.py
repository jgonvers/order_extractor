from faker import Faker

if __name__ == "__main__":
    filename = "test_data.csv"
    quantity = 1000
    start_id = 123
    fake = Faker()
    with open(filename, "w") as f:
        for i in range(quantity):
            values = [str(start_id+i)]
            values.append(fake.name())
            for x in range(fake.random_int(1,10)):
                values.append(fake.word())
                values.append(str(fake.random_int(1,1000)))
            print(";".join(values), file=f)