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

def on_click(event):
    global theta1, theta2, omega1, omega2, simulation_started
    if event.xdata is not None and event.ydata is not None:
        theta1 = np.arctan2(event.ydata, event.xdata)
        theta2 = np.pi / 2
        omega1 = 0
        omega2 = 0
        simulation_started = True

def on_move(event):
    global hover_x, hover_y
    if event.xdata is not None and event.ydata is not None:
        hover_x = event.xdata
        hover_y = event.ydata

theta1 = np.pi / 2
theta2 = np.pi / 2
omega1 = 0
omega2 = 0
t = 0
steps = 10000
trace_length = 100

pendulum1_x = []
pendulum1_y = []
pendulum2_x = []
pendulum2_y = []

simulation_started = False
hover_x = hover_y = None

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw=2, color='mediumvioletred')
trace, = ax.plot([], [], lw=1, color='gray')
trace2, = ax.plot([], [], lw=1, color='lightgray')
hover_line, = ax.plot([], [], 'o-', lw=2, color='lightpink')

fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('motion_notify_event', on_move)

def init():
    line.set_data([], [])
    trace.set_data([], [])
    trace2.set_data([], [])
    hover_line.set_data([], [])
    return line, trace, trace2, hover_line

def animate(i):
    if hover_x is not None and hover_y is not None and not simulation_started:
        hover_theta1 = np.arctan2(hover_y, hover_x)
        hover_theta2 = np.pi / 2
        hover_x1 = l1 * np.sin(hover_theta1)
        hover_y1 = -l1 * np.cos(hover_theta1)
        hover_x2 = hover_x1 + l2 * np.sin(hover_theta2)
        hover_y2 = hover_y1 - l2 * np.cos(hover_theta2)
        hover_x_coords = [0, hover_x1, hover_x2]
        hover_y_coords = [0, hover_y1, hover_y2]
        hover_line.set_data(hover_x_coords, hover_y_coords)
    
    if not simulation_started:
        return line, trace, trace2, hover_line
    
    global theta1, theta2, omega1, omega2, t
    theta1, theta2, omega1, omega2, t = rk4_step(derivatives, theta1, theta2, omega1, omega2, t, dt)
    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)
    pendulum1_x.append(x1)
    pendulum1_y.append(y1)
    pendulum2_x.append(x2)
    pendulum2_y.append(y2)

    if i < trace_length:
        trace.set_data(pendulum2_x[:i], pendulum2_y[:i])
        trace2.set_data(pendulum1_x[:i], pendulum1_y[:i])
    else:
        trace.set_data(pendulum2_x[i - trace_length:i], pendulum2_y[i - trace_length:i])
        trace2.set_data(pendulum1_x[i - trace_length:i], pendulum1_y[i - trace_length:i])
    x = [0, x1, x2]
    y = [0, y1, y2]
    line.set_data(x, y)
    return line, trace, trace2, hover_line

ani = FuncAnimation(fig, animate, frames=steps, interval=1, blit=True, init_func=init)
plt.show()




# https://www.sciencedirect.com/science/article/pii/S1877705816001971

# thank you to this paper for the math behind the double pendulum https://www.math.uwaterloo.ca/~sdalessi/EJP2023.pdf