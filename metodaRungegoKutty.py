def rk4(f, t0, y0, h, n):
    t = t0
    y = y0
    T = [t]
    Y = [y]

    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + 0.5*h, y + 0.5*h*k1)
        k3 = f(t + 0.5*h, y + 0.5*h*k2)
        k4 = f(t + h,     y + h*k3)

        y += (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
        t += h

        T.append(t)
        Y.append(y)

    return T, Y
f = lambda t, y: -y

t0 = 0.0
y0 = 1.0
h = 0.1
n = 100

T, Y = rk4(f, t0, y0, h, n)

for i in range(5):
    print(T[i], Y[i])