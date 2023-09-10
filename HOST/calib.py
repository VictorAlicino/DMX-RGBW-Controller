import tkinter as tk
from tkinter import ttk
from PyDMX import PyDMX

class LEDCalibrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Calibration Tool")

        self.dmx = PyDMX('COM5', Cnumber=14)

        self.red_calibration = tk.DoubleVar(value=1.0)
        self.green_calibration = tk.DoubleVar(value=1.0)
        self.blue_calibration = tk.DoubleVar(value=1.0)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="LED Calibration Tool", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Red Calibration:").pack()
        tk.Scale(self.root, from_=0.1, to=2.0, resolution=0.01, variable=self.red_calibration, orient="horizontal").pack()

        tk.Label(self.root, text="Green Calibration:").pack()
        tk.Scale(self.root, from_=0.1, to=2.0, resolution=0.01, variable=self.green_calibration, orient="horizontal").pack()

        tk.Label(self.root, text="Blue Calibration:").pack()
        tk.Scale(self.root, from_=0.1, to=2.0, resolution=0.01, variable=self.blue_calibration, orient="horizontal").pack()

        ttk.Separator(self.root, orient="horizontal").pack(fill="both", pady=10)

        tk.Button(self.root, text="Apply Calibration", command=self.apply_calibration).pack()
        tk.Button(self.root, text="Quit", command=self.root.quit).pack(pady=10)

    def apply_calibration(self):
        print(f"Red Calibration: {self.red_calibration.get()}")
        print(f"Green Calibration: {self.green_calibration.get()}")
        print(f"Blue Calibration: {self.blue_calibration.get()}")
        print("Calibration values have been saved.")

def main():
    root = tk.Tk()
    app = LEDCalibrationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()