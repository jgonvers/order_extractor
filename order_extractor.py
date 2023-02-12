from sys import argv

class Order:
    def __init__(self, line):
        self._parse_line(line)
    
    def _parse_line(self, line):
        elements = line.strip().split(";")
        self.id = int(elements[0])
        self.customer = elements[1].strip()
        self.items = {elements[x]:int(elements[x+1]) for x in range(2,len(elements)-1,2)}
        
    def __str__(self):
        return f"{{'Order Number': {self.id}, 'Customer': '{self.customer}', 'Items': {self.items}}}"
    
    
if __name__ == "__main__": 
    line = "123;Jhon Pony;Item1;3;item2;14;item3;123"
    print(Order(line))
