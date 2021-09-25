from root import Root

import numpy as np
import matplotlib.pyplot as plt

class WrongWayException(Exception):
    pass
class WrongRateNameException(Exception):
    pass


class CLI:

    def __init__(self):
        self._root = Root()
        self.print_welcome()
        self.main_loop()

    @staticmethod
    def print_welcome():
        print("Witaj!, co robimy?\n")

    @staticmethod
    def print_menu():
        print("1. Wyświetl aktualny kurs wybranej waluty względem innej")
        print("2. Przelicz kwotę aktualnego kursu wybranej waluty na inny")
        print("3. Przelicz archiwalną kwotę wybranego kursu na inny")
        print("4. Zapisz do pliku CSV kurs wybranej waluty z wybieranego zakresu")
        print("5. Predykcja wybranego kursu waluty na kolejny dzień")
        print()
        print("0. Wyjdź z programu")

    @staticmethod
    def print_enter_to_continue(final_result):
        print(final_result)
        input("\nAby przejść dalej wciśnij enter\n")

    def main_loop(self):
        still_work = True

        while still_work == True:

            self.print_menu()
            to_do = input("Co robimy?: ")

            if to_do == "1":
                rate_a = input("Wpisz symbol waluty która posiadasz: ").upper()
                rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ").upper()
                result = self._root.get_current_rate(rate_a, rate_b)
                final_result = f"\n{result} {rate_a} / 1 {rate_b}\n"
                self.print_enter_to_continue(final_result)

            elif to_do == "2":
                rate_a = input("Wpisz symbol waluty która posiadasz: ").upper()
                amount = float(input("Wpisz kwotę do przeliczenia: "))
                rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ").upper()
                result = self._root.rate_from_value(rate_a, amount, rate_b)
                final_result = f'{amount} {rate_a} --> {result} {rate_b}'
                self.print_enter_to_continue(final_result)

            elif to_do == "3":
                rate_a = input("Wpisz symbol waluty która posiadasz: ")
                rate_b = input("Wpisz symbol waluty, na którą chcesz przeliczyć: ")
                date = input("Data (RRRR-MM-DD): ")
                result = self.get_archive_rate_date(rate_a, rate_b, date)
                final_result = f"{rate_a} w {date} był wart {result} {rate_b}"
                self.print_enter_to_continue(final_result)

            elif to_do == "4":
                rate = input("Wpisz symbol waluty która cię interesuję: ")
                date_a = input("Podaj początkową datę (RRRR-MM-DD): ")
                date_b = input("Podaj datę końcową okresu (RRRR-MM-DD): ")
                final_result = self._root.get_archive_rate_spread(rate, date_a, date_b)
                self.print_enter_to_continue(final_result)

            elif to_do == "5":
                rate = input("Wpisz symbol waluty która cię interesuję: ").lower()
                pred_df, _ = self._root.predict_to_tomorrow(rate)
                final_result = f'{pred_df}'
                self.print_enter_to_continue(final_result)

            elif to_do == '6':
                rate = input("Wpisz symbol waluty która cię interesuję: ").lower()
                pred_df, result = self._root.predict_to_tomorrow(rate)
                final_result = f'{pred_df}\nSzacowane:   {round(result, 4)}'
                self.print_enter_to_continue(final_result)
                

            if to_do == "7":
                rate = input("Względem jakiej waluty chcesz otrzymać kurs: ").upper()
                result, rate = self._root.get_pln_rate(rate)
                final_result = f'1 PLN --> {result} {rate}'
                self.print_enter_to_continue(final_result)

            elif to_do == "0":
                still_work = False

            else:
                print("Spróbuj jeszcze raz!")
                print()
                raise WrongWayException(self.main_loop())








