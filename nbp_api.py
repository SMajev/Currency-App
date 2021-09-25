import requests

class NBPAPI:

    @staticmethod
    def get_rate_to_pln(rate_name):
        if rate_name == 'PLN':
            return 1

        url = f'http://api.nbp.pl/api/exchangerates/rates/a/{rate_name}'
        rate = requests.get(url).json()['rates'][0]['mid']
        return rate

    @staticmethod

    @staticmethod
    def get_last_10_rates(code='eur', topCount=10):
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{code.lower()}/last/{str(topCount)}/?format=json"

        rates = requests.get(url).json()['rates']
        # print(type(rates))
        data = []
        for rate in rates:
            data.append(float(rate["mid"]))
        return data











if __name__ == '__main__':
    NBPAPI = NBPAPI()
    print(NBPAPI.get_rate_to_pln('eur'))