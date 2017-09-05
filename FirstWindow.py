import MoneyTools
import tkinter
from tkinter import ttk
from MainWindow import MainWindow


def done(country_str, cbb_str):
    country = MoneyTools.country_map.get(country_str)
    cbb = MoneyTools.cbb_map.get(cbb_str)

    if country is not None and cbb is not None:
        window = MainWindow(country, cbb, country_str, cbb_str)


def main():
    """
    Control for the graphical application CoinSlotter
    :return:
    """

    '''
    cs = CoinSlot(0.50, True)
    cs.num_coins = 0
    print(cs.get_total())
    '''

    root = tkinter.Tk()
    root.title("Welcome to CoinSlotterPy")

    country_box = ttk.Combobox(root, state="readonly", values=list(MoneyTools.country_map.keys()))
    country_box.set("Select Country")
    country_box.pack()

    cbb_box = ttk.Combobox(root, state="readonly", values=list(MoneyTools.cbb_map.keys()))
    cbb_box.set("Select Denominations")
    cbb_box.pack()

    done_button = ttk.Button(root, text="Done", command=lambda: done(country_box.get(), cbb_box.get()))
    done_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
