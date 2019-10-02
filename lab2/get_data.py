import pandas as pd
import matplotlib.pyplot as plt
def get_name():
    name = "Susanne"
    return name


#call the function
name = get_name()
print(name)


def get_spectrum(table):
    #table = pd.read_csv(file_name)
    frequency = table ["frequency"].values
    amplitude = table ["amplitude"]. values
    return frequency, amplitude

def label():
    x_label = "frequency"
    y_label = "amplitude"
    return x_label, y_label

#call the function
if __name__ == '__main__':
    file_name = "frequency_spectrum.csv"
    table = pd.read_csv(file_name)
    frequency, amplitude = get_spectrum(table)
    plt.plot(frequency, amplitude)
    plt.show()
