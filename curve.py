import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

def square(p):
    fig, ax = plt.subplots()
    ax.grid(True)
    major_ticks = np.arange(0, p + 1, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    result_x1, result_x2, result_y1, result_y2 = [], [], [], []
    for x in range (0, p + 1):
        set = False
        for y in range (0, p + 1):
            if ((x ** 3 + 11 - y ** 2) % p == 0):
                if (set == False):
                    result_y1.append(y)
                    result_x1.append(x)
                    set = True
                else :
                    result_y2.append(y)
                    result_x2.append(x)
    ax.plot(result_x1, result_y1)
    ax.plot(result_x2, result_y2)
    plt.show();

result = square(17)

#plt.savefig('t.png')
