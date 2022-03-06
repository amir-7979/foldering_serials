import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

current_path = filedialog.askdirectory()
os.chdir(current_path)
series_names = []
all_files = os.listdir()
for file in all_files:
    series_format1 = re.search("(.+)[._]S\d+E\d+[._]", file)
    if series_format1:
        serial_name = series_format1.group(1).replace('.', ' ').replace('_', ' ')
        if not os.path.exists(os.path.join(current_path, serial_name)):
            os.makedirs(os.path.join(current_path, serial_name))
        os.rename(os.path.join(current_path, file), os.path.join(current_path, serial_name, file))
