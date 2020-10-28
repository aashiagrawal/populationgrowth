import matplotlib.pyplot as plt

def func1 (lam, t):
    #func1 = x(t) = x(t-1) * lambda

    x_0 = 100
    x_vals = []
    x_vals.append(x_0)
    for i in range(1, t):
        x_vals.append(x_vals[-1]*lam)

    return x_vals

def func2 (lam, t):
    #func2 = x(t) = x(t-1) * lambda - y(t)

    x_0 = 100
    x_vals = []
    x_vals.append(x_0)
    for i in range(1, t):
        indicator = 1 if (i > 20 and i < 40) else 0
        x_vals.append(x_vals[-1]*lam + (-10)*indicator)
        # if (i > 20 and i < 40):
        #     x_vals.append(x_vals[-1]*lam - 10)
        # else:
        #     x_vals.append(x_vals[-1]*lam)

    return x_vals

def func3 (lam, t):
    #func3 = x(t) = x(t-1) * lambda + .9(x(t))

    x_0 = 100
    x_vals = []
    x_vals.append(x_0)
    for i in range(1, t):
        indicator = 1 if (i > 20 and i < 40) else 0
        x_vals.append(x_vals[-1]*lam - (.9 * x_vals[-1])*indicator)
    return x_vals

def func4 (penalty_vals, lam, t):
    for i in (penalty_vals):
        x_0 = 100
        x_vals = []
        x_vals.append(x_0)
        for j in range(1, t):
            indicator = 1 if (j > 20 and j < 40) else 0
            x_vals.append(x_vals[-1]*lam - (i * x_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x_vals))], x_vals)

def func5 (penalty_vals, lam, t):
    for i in (penalty_vals):
        x_0 = 100
        x_vals = []
        x_vals.append(x_0)
        for j in range(1, t):
            indicator = 1 if (j > 20 and j < 40) else 0
            x_vals.append(x_vals[-1]*lam - (i * x_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x_vals))], x_vals)
    for i in (penalty_vals):
        x_0 = 100
        x_vals = []
        x_vals.append(x_0)
        for j in range(1, t):
            indicator = 1 if (j > 20 and j < 30) else 0
            x_vals.append(x_vals[-1]*lam - (i * x_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x_vals))], x_vals)
    for i in (penalty_vals):
        x_0 = 100
        x_vals = []
        x_vals.append(x_0)
        for j in range(1, t):
            indicator = 1 if (j > 35 and j < 40) else 0
            x_vals.append(x_vals[-1]*lam - (i * x_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x_vals))], x_vals)
    plt.show()

def func6 (penalty_vals, lam1, lam2, t):
    for i in (penalty_vals):
            x1_0 = 100
            x1_vals = []
            x1_vals.append(x1_0)
            for j in range(1, t):
                indicator = 1 if (j > 20 and j < 40) else 0
                x1_vals.append(x1_vals[-1]*lam1 - (i * x1_vals[-1])*indicator)
            plt.plot ([i for i in range(len(x1_vals))], x1_vals)
    for i in (penalty_vals):
        x1_0 = 100
        x1_vals = []
        x1_vals.append(x1_0)
        for j in range(1, t):
            indicator = 1 if (j > 20 and j < 30) else 0
            x1_vals.append(x1_vals[-1]*lam1 - (i * x1_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x1_vals))], x1_vals)
    for i in (penalty_vals):
        x1_0 = 100
        x1_vals = []
        x1_vals.append(x1_0)
        for j in range(1, t):
            indicator = 1 if (j > 35 and j < 40) else 0
            x1_vals.append(x1_vals[-1]*lam1 - (i * x1_vals[-1])*indicator)
        plt.plot ([i for i in range(len(x1_vals))], x1_vals)

    x2_0 = 100
    x2_vals = []
    x2_vals.append(x2_0)
    for j in range(1, t):
        x2_vals.append(x2_vals[-1]*lam2)
    plt.plot ([i for i in range(len(x2_vals))], x2_vals)

    plt.show()    


def plot (x_vals, title):
    plt.plot ([i for i in range(len(x_vals))], x_vals)
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.title(title)
    plt.show()

def main ():
    #print(func1(1.05, 50))
    #results1 = func1(1.05, 50)
    #plot(results1, "func1")

    #results2 = func2(1.05, 50)
    #print(results2)
    #plot(results2, "func2")

    #results3 = func3(1.05, 50)
    #print(results3)
    #plot(results3, "func3")

    #func4([.5, .6, .7, .8, .9], 1.05, 50)
    #func5([.5, .6, .7, .8, .9], 1.05, 50)
    func6([.5, .6, .7, .8, .9], 1.05, 1.03, 50)

if __name__ == "__main__":
    main()