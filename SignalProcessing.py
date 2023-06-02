import numpy
from scipy import signal, fft
import matplotlib.pyplot as plt
from os.path import dirname, join

frequencyMax = 27  # Максимальна частота сигналу
fs = 1000  # Частота дискретизації
n = 500  # Довжина сигналу у відліках

signals_generation = numpy.random.normal(0, 10, n)  # Генерація сигналу
counting_time = numpy.arange(n) / fs  # Визначення відліків часу

w = frequencyMax / (fs / 2)  # Розрахунок параметрів фільтру

parameters_filter = signal.butter(3, w, 'low', output='sos')
signal_filtered = signal.sosfiltfilt(parameters_filter, signals_generation)

# counting spectrum
signal_spectrum = fft.fft(signal_filtered)
modular_value = numpy.abs(fft.fftshift(signal_spectrum))
frequency_readings = fft.fftfreq(n, 1 / n)
centering = fft.fftshift(frequency_readings)

grapg_title = input('Enter fig title: ')
spectrum_title = input('Enter spectrum fig title: ')


def graph(x, y, x_title, y_title, main_title, title):
    fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
    ax.plot(x, y, linewidth=1)
    ax.set_xlabel(y_title, fontsize=14)
    ax.set_ylabel(x_title, fontsize=14)
    plt.title(main_title, fontsize=14)

    current_dir = dirname(__file__)
    file_path = join(current_dir, 'figures', title + '.png')

    fig.savefig(file_path, dpi=600)

#1
print(graph(counting_time, signal_filtered, "Амплітуда сигналу", "Час(секунди)",
            "Сигнал з максимальною частотою F-max = " + str(frequencyMax) + "Гц", grapg_title))
print(graph(centering, modular_value, 'Амплітуда спектру', 'Частота(Гц)', 'Спектр сигналу з максимальною частотою F-max = ' + str(frequencyMax) + 'Гц', spectrum_title))
