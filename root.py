from old.nbp_api import NBPAPI
import nbp_api
import seaborn as sns
import numpy as np

class root:
    def __init__(self) -> None:
        self._nbp = nbp_api.NBPAPI


    def get_pln_rate(self) -> str:
        rate = input("Względem jakiej waluty chcesz otrzymać kurs: ").upper()
        result = self._nbp.get_rate_to_pln(rate)
        return f'1 PLN --> {result} {rate}'

    def get_current_rate(self):
        rate_a = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ")
        rate_b = input("Wpisz symbol waluty która posiadasz: ")
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_a)
        result = round(rate_a_value / rate_b_value, 4)
        return f"\n{result} {rate_b} / 1 {rate_a}\n"


    def predict_to_tomorrow(self):
        self.rates_lst = np.array(self._nbp.get_last_10_rates('eur', 10))
        return self.rates_lst



if __name__ == '__main__':
    root = root()
    print(root.predict_to_tomorrow())
    print(root.get_pln_rate())
