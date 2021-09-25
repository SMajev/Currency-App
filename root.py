import nbp_api
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

Array = np.array([float])
DataFrame = pd.DataFrame()

class Root:
    def __init__(self) -> None:
        self._nbp = nbp_api.NBPAPI

    def get_pln_rate(self, rate: float) -> str:
        '''Obecny kurs PLN.'''
        result = round(1 / self._nbp.get_rate_to_pln(rate), 2)
        return result, rate

    #  1. Kurs waluty względem innej.
    def get_current_rate(self, rate_a: str, rate_b: str) -> float:
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        return result

    # 2.
    def rate_from_value(self, rate_a: str, amount: float, rate_b:str) -> float:    
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        final_result = round(result * amount, 2)
        return final_result

    # 3.
    def get_archive_rate_date(self, rate_a: str, rate_b: str, date: str) -> float:
        rate_a_value = self._nbp.get_rate_to_pln(rate_a)
        rate_b_value = self._nbp.get_rate_to_pln(rate_b)
        result = self._calculate_rate_to_rate(rate_a_value, rate_b_value)
        return float

    # 4.
    def get_archive_rate_spread(self, rate: str, date_a: str, date_b: str) -> DataFrame:
        rates, dates = self._nbp.get_archive_rate_to_pln_spread(rate, date_a, date_b)
        result = pd.DataFrame({'Rates': rates}, index=dates).rename_axis('Dates', axis=1)
        return result

    # 5., 6.
    def predict_to_tomorrow(self, rate: str, x=11) -> DataFrame:
        rates_lst, dates = self._nbp.get_last_10_rates(rate, 10)
        param = self._estimate_param(rates_lst)
        y_pred = param[0] * x + param[1]
        pred_df = pd.DataFrame({'Rates': rates_lst}, index=dates).rename_axis('Dates', axis=1)
        return pred_df, y_pred
    
    
    @staticmethod
    def get_rate_to_csv(self, data):
        with open("Rate.csv", "w") as f1:
            write = csv.writer(f1, delimiter=",")
            write.writerow(data)

    
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


