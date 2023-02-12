# order_extractor.py
```
from sys import argv
```
import argv to read the argument used
```
class Order:
    def __init__(self, line):
        self._parse_line(line)
```
create the class
```
    def _parse_line(self, line):
```
get directly a line from the csv, this method should be modified, either directly or throug inheritance to allow to parse other format
```
        elements = line.strip().split(";")
```
split the line
```
        self.id = int(elements[0])
        self.customer = elements[1].strip()
        self.items = {elements[x]:int(elements[x+1]) for x in range(2,len(elements)-1,2)}
```
parse the content
items are stored as a dict created using a comprehension
```
    def __str__(self):
        return f"{{'Order Number': {self.id}, 'Customer': '{self.customer}', 'Items': {self.items}}}"
```
allow to print in the format asked
```  
if __name__ == "__main__": 
    with open(argv[1]) as f:
        orders = map(Order, f.readlines())
```
open the file, map each line to an Order
```
    for order in orders:
        print(order)
```
print each orders

# fake_content.py
```
from faker import Faker
```
faker allow to easily create fake data like name or word
```
if __name__ == "__main__":
    filename = "test_data.csv"
    quantity = 1000
    start_id = 123
    fake = Faker()
```
initialize the faking by giving the filename created, the quantity of data created the id_start and initialize faker
```
    with open(filename, "w") as f:
        for i in range(quantity):
            values = [str(start_id+i)]
            values.append(fake.name())
            for x in range(fake.random_int(1,10)):
                values.append(fake.word())
                values.append(str(fake.random_int(1,1000)))
            print(";".join(values), file=f)
```
create and print to file the datas, rand could have been used instead for Faker.rand_int but would have requirer one more import for the same result
