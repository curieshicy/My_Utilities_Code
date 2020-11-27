import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from pathlib import Path
# load data
# specify the file pathj
file_path = Path('DATA/MEC_data.txt')
data = np.loadtxt(file_path)
pure_M_x = data[:3, 0]
pure_M_290 = data[:3, 1]
pure_M_320 = data[:3, 2]
pure_M_285 = data[:3, 3]
part_M_x = data[3:, 0]
part_M_290 = data[3:, 1]
part_M_320 = data[3:, 2]
part_M_285 = data[3:, 3]

def linear_fit(x_array, y_array):
    # take in two arrays and return slope and intercept as tuple
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_array, y_array)
    return slope, intercept, r_value**2

def plot_subfigure(x_array, y_array, text, title):
    slope, intercept, r2 = linear_fit(x_array, y_array)
    plt.plot(x_array, y_array, 'bo', markersize = 12, label = text)
    plt.plot(x_array, slope*x_array + intercept, 'r-', lw=2)
    plt.xlabel('Concentration (M)', fontsize = 12)
    plt.ylabel('Absorbance (AU)', fontsize = 12)
    plt.title('In {} at {}'.format(title, text), fontsize = 12)
    plt.ticklabel_format(style = 'sci', axis = 'x', scilimits = (0,0))
    plt.text(np.max(x_array) * 0.5,
             np.max(y_array) * 0.9,
             'y = {:.2f}x + {:.5f} \n R$^2$ = {:.5f}'.format(slope, intercept, r2),
             ha = 'center',
             va = 'center'
             )
    plt.tight_layout()

# plot
plt.figure(figsize = (13, 7))
plt.subplot(231)
plot_subfigure(pure_M_x, pure_M_290, '290 nm', 'pure methanol')
plt.subplot(232)
plot_subfigure(pure_M_x, pure_M_320, '320 nm', 'pure methanol')
plt.subplot(233)
plot_subfigure(pure_M_x, pure_M_285, '285 nm', 'pure methanol')
plt.subplot(234)
plot_subfigure(part_M_x, part_M_290, '290 nm', '40% methanol/60% buffer')
plt.subplot(235)
plot_subfigure(part_M_x, part_M_320, '320 nm', '40% methanol/60% buffer')
plt.subplot(236)
plot_subfigure(part_M_x, part_M_285, '285 nm', '40% methanol/60% buffer')
plt.show()






