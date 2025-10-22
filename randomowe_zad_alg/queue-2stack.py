class Queue:
    def __init__(self):
        self.inn = []
        self.out = []

    def put(self, value):
        self.inn.append(value)

    def get(self):
        if len(self.out)==0:
            while len(self.inn) > 0:
                self.out.append(self.inn.pop(-1))
        return self.out.pop(-1) if len(self.out) > 0 else None