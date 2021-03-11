import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def add_mean_results_to_csv(out_file, in_file, algo):
    df = pd.read_csv(in_file)
    k = df.mean(axis=0).values.astype(str)
    with open(out_file, 'a') as fd:
        fd.write(algo + "," + ",".join(k.tolist()) + "\n")


def get_row(df, algo):
    res = df.loc[df["Algorithm"] == algo]
    res.reindex()
    return res.columns[1:].astype(int), res.values[0][1:].astype(float)


def draw_plot(x_label, y_label, title, patch="#B0C4DE"):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title(title, color='black', size=25, fontweight='bold', pad=30)
    ax.set_ylabel(y_label, size=15, fontweight='bold')
    ax.set_xlabel(x_label, size=15, fontweight='bold')
    ax.patch.set_facecolor(patch)
    fig.patch.set_facecolor('#154360')
    plt.grid(zorder=0)


def draw_polygon(x, yy, algos, title, colors, im_name):
    draw_plot("N", "Time", title)
    for i in range(len(yy)):
        plt.plot(x, yy[i], color=colors[i], linewidth=3, markersize=12)
    plt.legend(algos, loc='upper left')
    plt.xticks(x[::10])
    plt.savefig(im_name)


def get_4cols(time, indexes = np.array([1, 9, 19, 49])):
    k = time[indexes]
    return k


def draw_hists(bars1, bars2, bars3, bars4, im_name):
    draw_plot("Algorithms", "Time", "")
    plt.grid(axis='x')
    barWidth = 0.10

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    plt.bar(r1, bars1, color='#89CFEF', width=barWidth, edgecolor='white', label='randInt %2', zorder=3)
    plt.bar(r2, bars2, color='#4682B4', width=barWidth, edgecolor='white', label='randInt %10', zorder=3)
    plt.bar(r3, bars3, color='#0E4C92', width=barWidth, edgecolor='white', label='randInt %50', zorder=3)
    plt.bar(r4, bars4, color='#003151', width=barWidth, edgecolor='white', label='randInt %250', zorder=3)

    plt.xticks([r + 1.5 * barWidth for r in range(len(bars1))], ['GnomeRandom', 'BubleSort', 'InsertSort', 'SelectionSort'])

    plt.legend()
    plt.savefig(im_name)


def compareLanguages(n, times, colors, legends, im_name):
    draw_plot("N", "Time", "")

    for i in range(len(n)):
        plt.plot(n[i], times[i], color=colors[i], linewidth=3, markersize=12)

    plt.legend(legends, loc='upper left')
    plt.xticks(n[0][::10])
    plt.savefig(im_name)


def compare_Gnome():
    n1, time1 = get_row(df, "GnomeSorted")
    n2, time2 = get_row(df, "GnomeRandom")
    n3, time3 = get_row(df, "GnomeReverseSorted")

    draw_polygon(n2, [time1], ["Sorted array time"], "Gnome Sorted", ["#FF4500"], "compare_Gnome1.png")
    draw_polygon(n1, [time1, time2, time3], ["Sorted array time", "Random array time", "Reverse sorted array time"], "Order comparison", ["#FF4500", "#1E90FF", "#008000"],  "compare_Gnome2.png")


def compare_algos_small():
    _, time2 = get_row(df, "GnomeRandom")
    _, time4 = get_row(df, "BubleSort")
    _, time5 = get_row(df, "InsertSort")
    _, time6 = get_row(df, "SelectionSort")
    n2 = np.array(np.array([500, 1000, 1500, 2000, 2500]))

    draw_polygon(n2, [time2[:5], time4[:5], time5[:5], time6[:5]], ["GnomeRandom", "BubleSort", "InsertSort", "SelectionSort"], "",
                 ["#FF4500", "#FFA500", "#FFD700", "#3CB371"], "AlgosSmall.png")


def compare_algos():
    n2, time2 = get_row(df, "GnomeRandom")
    n4, time4 = get_row(df, "BubleSort")
    n5, time5 = get_row(df, "InsertSort")
    n6, time6 = get_row(df, "SelectionSort")

    draw_polygon(n2, [time2, time4, time5, time6], ["GnomeRandom", "BubleSort", "InsertSort", "SelectionSort"], "",
                 ["#FF4500", "#FFA500", "#FFD700", "#3CB371"],  "Algos.png")


if __name__ == "__main__":
    df = pd.read_csv("/Users/sophiyca/CLionProjects/GnomeResearch/results/TimeResults.csv")
    compare_Gnome()
