from old.nbp_api import NBPAPI
import nbp_api
import seaborn as sns
import numpy as np

class root:
    def __init__(self) -> None:
        self.nbp = nbp_api.NBPAPI

    def predict_to_tomorrow(self):
        self.rates_lst = np.array(self.nbp.get_last_10_rates())
        sns.scatterplot(self.rates_lst)
        print(self.rates_lst)



if __name__ == '__main__':
    root = root()
    root.predict_to_tomorrow()
