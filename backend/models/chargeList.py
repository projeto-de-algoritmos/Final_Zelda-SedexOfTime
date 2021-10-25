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

    def compareItems(self,itemA, itemB):
        return itemA.get_value_per_weight() > itemB.get_value_per_weight()

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i,j,k = (0, 0, 0)

            while i < len(left) and j < len(right):
                if self.compareItems(left[i], right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def knapsack(self):
        self.mergeSort(self.charge_list)
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
