from .charge import Charge


class ChargeList:
    def __init__(self, charge_list, max_weight):
        self.charge_list = [
            Charge(
                str(charge['nome']),
                int(charge['peso']),
                int(charge['valor']))
            for charge in charge_list]
        self.max_weight = int(max_weight)

    def bubbleSort_charge(self):
        for passnum in range(len(self.charge_list) - 1, 0, -1):
            for i in range(passnum):
                if self.charge_list[i].get_value_per_weight(
                ) < self.charge_list[i + 1].get_value_per_weight():
                    temp = self.charge_list[i]
                    self.charge_list[i] = self.charge_list[i + 1]
                    self.charge_list[i + 1] = temp

    def knapsack(self):
        self.bubbleSort_charge()
        selected = []
        for charge in self.charge_list:
            if self.max_weight == 0:
                return selected
            elif charge.get_weight() <= self.max_weight:
                selected.append({
                                 'nome': charge.get_name(),
                                 'peso': charge.get_weight(),
                                 'valor': charge.get_value(),
                                 'porcentagem': 1})
                self.max_weight -= charge.get_weight()
            elif self.max_weight > 0:
                variable = self.max_weight / charge.get_weight()
                selected.append({
                                 'nome': charge.get_name(),
                                 'peso': charge.get_weight(),
                                 'valor': charge.get_value(),
                                 'porcentagem': variable})
                self.max_weight = 0
        if self.max_weight >= 0:
            return selected
