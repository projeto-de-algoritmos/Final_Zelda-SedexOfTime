class Charge:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def get_name(self) -> str:
        return self.name

    def get_weight(self) -> int:
        return self.weight

    def get_value(self) -> int:
        return self.value

    def get_value_per_weight(self) -> float:
        return self.value / self.weight

    def __str__(self):
        return f"Charge(Weight: {self.get_weight()} Value: {self.get_value()})"
