import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m1 = 1
m2 = 1
g = 10
l1 = 1
l2 = 1
dt = 0.01

def angular_acceleration1(theta1, theta2, omega1, omega2):
    num = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * m2 * np.sin(theta1 - theta2) * (l2 * omega2 ** 2 + l1 * omega1 ** 2 * np.cos(theta1 - theta2))
    den = l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    return num / den

def angular_acceleration2(theta1, theta2, omega1, omega2):
    num = 2 * np.sin(theta1 - theta2) * (l1 * omega1 ** 2 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + l2 * omega2 ** 2 * m2 * np.cos(theta1 - theta2))
    den = l2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    return num / den

def rk4_step(derivatives, theta1, theta2, omega1, omega2, t, dt):
    k1 = derivatives(theta1, theta2, omega1, omega2)
    k2 = derivatives(theta1 + dt / 2 * k1[0], theta2 + dt / 2 * k1[1], omega1 + dt / 2 * k1[2], omega2 + dt / 2 * k1[3])
    k3 = derivatives(theta1 + dt / 2 * k2[0], theta2 + dt / 2 * k2[1], omega1 + dt / 2 * k2[2], omega2 + dt / 2 * k2[3])
    k4 = derivatives(theta1 + dt * k3[0], theta2 + dt * k3[1], omega1 + dt * k3[2], omega2 + dt * k3[3])
    theta1 += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    theta2 += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    omega1 += dt / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
    omega2 += dt / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
    t += dt
    return theta1, theta2, omega1, omega2, t

def derivatives(theta1, theta2, omega1, omega2):
    theta1_dot = omega1
    theta2_dot = omega2
    omega1_dot = angular_acceleration1(theta1, theta2, omega1, omega2)
    omega2_dot = angular_acceleration2(theta1, theta2, omega1, omega2)
    return np.array([theta1_dot, theta2_dot, omega1_dot, omega2_dot])

theta1 = np.pi / 2
theta2 = np.pi / 2
omega1 = 0
omega2 = 1
t = 0
steps = 10000
trace_length = 100

pendulum1_x = []
pendulum1_y = []
pendulum2_x = []
pendulum2_y = []

for _ in range(steps):
    theta1, theta2, omega1, omega2, t = rk4_step(derivatives, theta1, theta2, omega1, omega2, t, dt)
    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)
    pendulum1_x.append(x1)
    pendulum1_y.append(y1)
    pendulum2_x.append(x2)
    pendulum2_y.append(y2)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw=2, color='mediumvioletred')
trace, = ax.plot([], [], lw=1, color='gray')
trace2, = ax.plot([], [], lw=1, color='lightgray')

def init():
    line.set_data([], [])
    trace.set_data([], [])
    trace2.set_data([], [])
    return line, trace, trace2

def animate(i):
    if i < trace_length:
        trace.set_data(pendulum2_x[:i], pendulum2_y[:i])
        trace2.set_data(pendulum1_x[:i], pendulum1_y[:i])
    else:
        trace.set_data(pendulum2_x[i - trace_length:i], pendulum2_y[i - trace_length:i])
        trace2.set_data(pendulum1_x[i - trace_length:i], pendulum1_y[i - trace_length:i])
    x = [0, pendulum1_x[i], pendulum2_x[i]]
    y = [0, pendulum1_y[i], pendulum2_y[i]]
    line.set_data(x, y)
    return line, trace, trace2

ani = FuncAnimation(fig, animate, frames=steps, interval=1, blit=True, init_func=init)
plt.show()
