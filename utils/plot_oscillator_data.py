__author__ = 'juancarlosfarah'

import pymongo
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi


def connect(database):
    host = "localhost"
    port = 27017
    mc = pymongo.MongoClient(host=host, port=port)
    return mc.get_database(database)


def plot_one(threshold):
    db = connect("individual_project")

    cursor = db.oscillator_simulation.find({"threshold": threshold})

    beta = []
    global_sync = []
    integrated_information = []

    for doc in cursor:
        beta.append(doc['beta'])
        global_sync.append(doc['global_sync'])
        integrated_information.append(doc['integrated_information_e'])

    fig = plt.figure()
    plt.scatter(global_sync, integrated_information)
    plt.xlabel("Global Synchrony")
    plt.ylabel("Integrated Information Empirical")
    plt.title("Integrated Information Empirical over Global Synchrony\n" +
              "Threshold = " + str(threshold))
    plt.show(fig)

    fig = plt.figure()
    plt.scatter(beta, integrated_information)
    plt.xlabel("Beta")
    plt.ylabel("Integrated Information Empirical")
    plt.title("Integrated Information Empirical over Beta\n" +
              "Threshold = " + str(threshold))
    plt.show(fig)

    return


def plot():
    db = connect("individual_project")

    cursors = {
        "0.9": db.oscillator_simulation.find({"threshold": 0.9}),
        "0.8": db.oscillator_simulation.find({"threshold": 0.8}),
        "0.7": db.oscillator_simulation.find({"threshold": 0.7}),
        "0.6": db.oscillator_simulation.find({"threshold": 0.6}),
        "0.5": db.oscillator_simulation.find({"threshold": 0.5})
    }

    beta = dict()
    global_sync = dict()
    integrated_information = dict()
    coalition_entropy = dict()
    chi = dict()
    lamda = dict()

    colors = {
        "0.9": "orange",
        "0.8": "red",
        "0.7": "blue",
        "0.6": "green",
        "0.5": "purple"
    }

    for key in cursors:
        beta[key] = []
        global_sync[key] = []
        chi[key] = []
        lamda[key] = []
        integrated_information[key] = []
        coalition_entropy[key] = []
        for doc in cursors[key]:
            beta[key].append(doc['beta'])
            global_sync[key].append(doc['global_sync'])
            lamda[key].append(doc['lambda'])
            chi[key].append(doc['chi'])
            integrated_information[key].append(doc['integrated_information_e'])
            coalition_entropy[key].append(doc['coalition_entropy'])

    fig1 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Global Synchrony")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Global Synchrony")
        handles.append(plt.scatter(global_sync[key],
                                   integrated_information[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig1)

    fig2 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Beta")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Beta")
        handles.append(plt.scatter(beta[key],
                                   integrated_information[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig2)

    fig3 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Beta")
        plt.ylabel("Chi")
        plt.title("Chi over Beta")
        handles.append(plt.scatter(beta[key],
                                   chi[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig3)

    fig4 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Beta")
        plt.ylabel("Lambda")
        plt.title("Lambda over Beta")
        handles.append(plt.scatter(beta[key],
                                   lamda[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig4)

    fig5 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Chi")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Chi")
        handles.append(plt.scatter(chi[key],
                                   integrated_information[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig5)

    fig6 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Lambda")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Lambda")
        handles.append(plt.scatter(lamda[key],
                                   integrated_information[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig6)

    fig7 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Beta")
        plt.ylabel("Coalition Entropy")
        plt.title("Coalition Entropy over Beta")
        handles.append(plt.scatter(beta[key],
                                   coalition_entropy[key],
                                   color=colors[key],
                                   label=key))
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig7)

    return


def plot_curves():
    db = connect("individual_project")

    cursors = {
        "0.9": db.oscillator_simulation.find({"threshold": 0.9}),
        "0.8": db.oscillator_simulation.find({"threshold": 0.8}),
        "0.7": db.oscillator_simulation.find({"threshold": 0.7}),
        "0.6": db.oscillator_simulation.find({"threshold": 0.6}),
        "0.5": db.oscillator_simulation.find({"threshold": 0.5})
    }

    beta = dict()
    global_sync = dict()
    integrated_information = dict()
    chi = dict()
    lamda = dict()

    colors = {
        "0.9": "orange",
        "0.8": "red",
        "0.7": "blue",
        "0.6": "green",
        "0.5": "purple"
    }

    for key in cursors:
        beta[key] = []
        global_sync[key] = []
        chi[key] = []
        lamda[key] = []
        integrated_information[key] = []
        for doc in cursors[key]:
            beta[key].append(doc['beta'])
            global_sync[key].append(doc['global_sync'])
            lamda[key].append(doc['lambda'])
            chi[key].append(doc['chi'])
            integrated_information[key].append(doc['integrated_information_e'])

    fig2 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Beta")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Beta")
        x = beta[key]
        y = integrated_information[key]

        # Combine lists into list of tuples.
        points = zip(x, y)

        # Sort list of tuples by x-value.
        points = sorted(points, key=lambda point: point[0])

        # Split list of tuples into two list of x values any y values.
        x, y = zip(*points)

        # Plot original points.
        plt.plot(x, y, 'ro', color=colors[key], label=key)

        x_new = np.linspace(min(x), max(x), 200)
        spline = spi.InterpolatedUnivariateSpline(x, y)
        spline.set_smoothing_factor(0.15)

        handles.append(plt.plot(x_new,
                                spline(x_new),
                                color=colors[key],
                                label=key))
    plt.ylim(-0.5, 1)
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig2)

    fig3 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Chi")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Chi")
        x = chi[key]
        y = integrated_information[key]

        # Combine lists into list of tuples.
        points = zip(x, y)

        # Sort list of tuples by x-value.
        points = sorted(points, key=lambda point: point[0])

        # Split list of tuples into two list of x values any y values.
        x, y = zip(*points)

        # Plot original points.
        plt.plot(x, y, 'ro', color=colors[key], label=key)

        x_new = np.linspace(min(x), max(x), 200)
        spline = spi.InterpolatedUnivariateSpline(x, y)
        spline.set_smoothing_factor(1.1)

        handles.append(plt.plot(x_new,
                                spline(x_new),
                                color=colors[key],
                                label=key))
    plt.ylim(-0.5, 1)
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig3)

    fig4 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Lambda")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Lambda")
        x = lamda[key]
        y = integrated_information[key]

        # Combine lists into list of tuples.
        points = zip(x, y)

        # Sort list of tuples by x-value.
        points = sorted(points, key=lambda point: point[0])

        # Split list of tuples into two list of x values any y values.
        x, y = zip(*points)

        # Plot original points.
        plt.plot(x, y, 'ro', color=colors[key], label=key)

        x_new = np.linspace(min(x), max(x), 200)
        spline = spi.InterpolatedUnivariateSpline(x, y)
        spline.set_smoothing_factor(1.1)

        handles.append(plt.plot(x_new,
                                spline(x_new),
                                color=colors[key],
                                label=key))
    plt.ylim(-0.5, 1)
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig4)

    fig5 = plt.figure()
    handles = []
    labels = []
    for key in cursors:
        labels.append(key)
        plt.xlabel("Global Synchrony")
        plt.ylabel("Integrated Information Empirical")
        plt.title("Integrated Information Empirical over Global Synchrony")
        x = global_sync[key]
        y = integrated_information[key]

        # Combine lists into list of tuples.
        points = zip(x, y)

        # Sort list of tuples by x-value.
        points = sorted(points, key=lambda point: point[0])

        # Split list of tuples into two list of x values any y values.
        x, y = zip(*points)

        # Plot original points.
        plt.plot(x, y, 'ro', color=colors[key], label=key)

        x_new = np.linspace(min(x), max(x), 200)
        spline = spi.InterpolatedUnivariateSpline(x, y)
        spline.set_smoothing_factor(0.2)

        handles.append(plt.plot(x_new,
                                spline(x_new),
                                color=colors[key],
                                label=key))
    plt.ylim(-0.5, 1)
    plt.legend(handles, labels, title="Threshold")
    plt.show(fig5)


if __name__ == "__main__":
    plot()
    # plot_curves()