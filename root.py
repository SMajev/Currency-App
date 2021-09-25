import nbp_api
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Array = np.array([float])

class root:
    def __init__(self) -> None:
        self._nbp = nbp_api.NBPAPI

    def get_pln_rate(self) -> str:
        rate = input("Względem jakiej waluty chcesz otrzymać kurs: ").upper()
        result = round(1 / self._nbp.get_rate_to_pln(rate), 2)
        # result = rate_a / rate_b
        return f'1 PLN --> {result} {rate}'

    def get_current_rate(self) -> str:
        rate_a = input("Wpisz symbol waluty która posiadasz: ")
        rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ")
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        return f"\n{result} {rate_a} / 1 {rate_b}\n"

    def rate_from_value(self) -> str:    
        rate_a = input("Wpisz symbol waluty która posiadasz: ").upper()
        amount = float(input("Wpisz kwotę do przeliczenia: "))
        rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ").upper()
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        final_result = round(result * amount, 2)
        return f'{amount} {rate_a} --> {final_result} {rate_b}'

    def get_archive_rate_date(self) -> str:
        rate_a = input("Wpisz symbol waluty która posiadasz: ")
        rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ")
        date = input("Data (RRRR-MM-DD): ")
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        return f"{rate_a} w {date} był wart {result} {rate_b}"

    def get_archive_rate_spread(self):
        rate = input("Wpisz symbol waluty która cię interesuję: ")
        date_a = input("Podaj początkową datę (RRRR-MM-DD): ")
        date_b = input("Podaj datę końcową okresu (RRRR-MM-DD): ")
        rates, dates = self._nbp.get_archive_rate_to_pln_spread(rate, date_a, date_b)
        result = pd.DataFrame(rates, index=dates)
        return result        

    def predict_to_tomorrow(self, x=11):
        rate = input("Wpisz symbol waluty która cię interesuję: ").lower()
        rates_lst, dates = self._nbp.get_last_10_rates(rate, 10)
        param = self._estimate_param(rates_lst)
        y_pred = param[0] * x + param[1]
        pred_df = pd.DataFrame({'Rates': rates_lst}, index=dates).rename_axis('Dates', axis=1)
        print(pred_df)
        return f'Szacowane:   {round(y_pred, 4)}'

    @staticmethod
    def _calculate_rate_to_rate(rate_a: float, rate_b: float, precision=2) -> float:
        result = rate_a / rate_b
        return round(result, precision)

    @staticmethod
    def _estimate_param(y: Array) -> tuple:
        n = len(y)
        x = np.array([1,2,3,4,5,6,7,8,9,10])        
        mx = np.mean(x)
        my = np.mean(y)
        ss_xy = np.sum(y*x) - n*my*mx
        ss_xx = np.sum(x*x) - n*mx*mx
        w = ss_xy / ss_xx
        b = my - w * mx
        return (w, b)


