import requests
import numpy as np

Array = np.array([float])

class NBPAPI:

    @staticmethod
    def get_rate_to_pln(rate_name: str) -> float:
        if rate_name == 'PLN':
            return 1
        url = f'http://api.nbp.pl/api/exchangerates/rates/a/{rate_name}'
        rate = requests.get(url).json()['rates'][0]['mid']
        return rate

    @staticmethod
    def get_archive_rate_to_pln(rate_name: str, date: str) -> float:
        if rate_name == 'PLN':
            return 1
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{rate_name}/{date}"
        rate = requests.get(url).json()['rates'][0]['mid']
        
        return rate

    @staticmethod
    def get_archive_rate_to_pln_spread(rate_name: str, start_date: str, end_date: str) -> Array:
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{rate_name}/{start_date}/{end_date}"
        rates = requests.get(url).json()['rates']
        data = np.array([rate['mid'] for rate in rates])
        dates = np.array([date['effectiveDate'] for date in rates])
        return data, dates

    @staticmethod
    def get_last_10_rates(code: str, topCount: int) -> Array:
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{code.lower()}/last/{str(topCount)}/?format=json"
        rates = requests.get(url).json()['rates']
        data = np.array([rate['mid'] for rate in rates])
        dates = np.array([date['effectiveDate'] for date in rates])
        return data, dates
