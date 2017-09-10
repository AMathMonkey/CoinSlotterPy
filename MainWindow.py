from CoinSlot import CoinSlot
import MoneyTools
from MoneyTools import format_100cents
from MoneyTools import get_int
import tkinter as tk
from PIL import ImageTk, Image


class MainWindow(object):
    def __init__(self, country, cbb, country_str, cbb_str):

        self.coin_slots = []
        self.denom_labels = []
        self.input_boxes = []
        self.input_string_vars = []
        self.plus_buttons = []
        self.minus_buttons = []
        self.value_labels = []
        self.value_string_vars = []
        self.total_label = None

        self.root = tk.Toplevel()
        self.root.title("CoinSlotterPy - " + country_str + " - " + cbb_str)
        # self.background_image = ImageTk.PhotoImage(Image.open("resources/Background.png"))
        # self.background_label = tk.Label(self.root, image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        if country is not None and cbb is not None:
            files = MoneyTools.return_files(country, cbb)
            for file in files:
                for line in file:
                    line_data = line.split()
                    self.coin_slots.append(CoinSlot(float(line_data[0]), line_data[1].lower() == "true"))
                file.close()

            i = 0
            for i, coin_slot in enumerate(self.coin_slots):
                self.denom_labels.append(tk.Label(self.root, text="$" + str(format_100cents(coin_slot.value))
                                                                       + (" coins" if coin_slot.is_coin else " bills")))
                self.denom_labels[i].grid(row=i, column=0)

                self.input_string_vars.append(tk.StringVar())
                self.input_string_vars[i].trace("w", lambda name, index, mode, i=i: self.update_total_and_value(i))

                vcmd = (self.root.register(self.validate),
                        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

                self.input_boxes.append(
                    tk.Entry(self.root,textvariable=self.input_string_vars[i],validate='key', validatecommand=vcmd)
                )
                self.input_boxes[i].grid(row=i, column=1)

                self.plus_buttons.append(tk.Button(self.root, command=lambda i=i: self.plus(i), text="+"))
                self.plus_buttons[i].grid(row=i, column=2)

                self.minus_buttons.append(tk.Button(self.root, command=lambda i=i: self.minus(i), text="-"))
                self.minus_buttons[i].grid(row=i, column=3)

                self.value_string_vars.append(tk.StringVar())
                self.value_string_vars[i].set("$0.00")

                self.value_labels.append(tk.Label(self.root, textvariable=self.value_string_vars[i]))
                self.value_labels[i].grid(row=i, column=4)

                self.total_string_var = tk.StringVar()
                self.total_string_var.set("$0.00")
                self.total_label = tk.Label(self.root, textvariable=self.total_string_var, font=("helvetica", 16))
                self.total_label.grid(row=i + 1, columnspan=5)

    def plus(self, row):
        try:
            i = get_int(self.input_string_vars[row].get())
            self.input_string_vars[row].set(i + 1)
        except ValueError:
            self.input_string_vars[row].set(1)

    def minus(self, row):
        try:
            i = get_int(self.input_string_vars[row].get())
            if i > 0:
                self.input_string_vars[row].set(i - 1)
        except ValueError:
            self.input_string_vars[row].set(0)

    def update_total_and_value(self, row):
        try:
            i = get_int(self.input_string_vars[row].get())
            self.coin_slots[row].num_coins = i
            self.value_string_vars[row].set("$" + str(self.coin_slots[row].get_total()))
            total = 0
            for coin_slot in self.coin_slots:
                total += coin_slot.get_total()
                self.total_string_var.set("$" + str(total))
        except ValueError:
            return

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            try:
                get_int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

