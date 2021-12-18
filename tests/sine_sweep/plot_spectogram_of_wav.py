
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from tkinter import filedialog
from tkinter import *


def get_path_to_file():
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return path


def main(path_to_file_):
    sample_rate, samples = wavfile.read(path_to_file_)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times.data, frequencies.data, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()


if __name__ == "__main__":
    path_to_file = get_path_to_file()
    main(path_to_file)
