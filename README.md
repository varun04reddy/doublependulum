
# Double Pendulum - Study of Chaos

## Equations of Motion

The dynamics of the double pendulum can be described by the following equations:

### Angular Accelerations

$$
\alpha_1 = \frac{-g (2 m_1 + m_2) \sin(\theta_1) - m_2 g \sin(\theta_1 - 2 \theta_2) - 2 \sin(\theta_1 - \theta_2) m_2 \left( \dot{\theta_2}^2 l_2 + \dot{\theta_1}^2 l_1 \cos(\theta_1 - \theta_2) \right)}{l_1 \left( 2 m_1 + m_2 - m_2 \cos(2 \theta_1 - 2 \theta_2) \right)}
$$

$$
\alpha_2 = \frac{2 \sin(\theta_1 - \theta_2) \left( \dot{\theta_1}^2 l_1 (m_1 + m_2) + g (m_1 + m_2) \cos(\theta_1) + \dot{\theta_2}^2 l_2 m_2 \cos(\theta_1 - \theta_2) \right)}{l_2 \left( 2 m_1 + m_2 - m_2 \cos(2 \theta_1 - 2 \theta_2) \right)}
$$

### Runge-Kutta Method (RK4)

To numerically solve the equations of motion, we use the Runge-Kutta method:

$$
\mathbf{k}_1 = f(\mathbf{y}, t)
$$

$$
\mathbf{k}_2 = f\left(\mathbf{y} + \frac{h}{2} \mathbf{k}_1, t + \frac{h}{2}\right)
$$

$$
\mathbf{k}_3 = f\left(\mathbf{y} + \frac{h}{2} \mathbf{k}_2, t + \frac{h}{2}\right)
$$

$$
\mathbf{k}_4 = f(\mathbf{y} + h \mathbf{k}_3, t + h)
$$

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + \frac{h}{6} (\mathbf{k}_1 + 2 \mathbf{k}_2 + 2 \mathbf{k}_3 + \mathbf{k}_4)
$$

## Initial Conditions and Parameters

Set the initial angles and angular velocities:

$$
\theta_1 = \frac{\pi}{2}, \quad \theta_2 = \frac{\pi}{2}
$$

$$
\dot{\theta}_1 = 0, \quad \dot{\theta}_2 = 1
$$

## Visualization

The pendulum's motion is visualized using Matplotlib, with traces to show the paths of the pendulum masses.

## Important Concepts

### Pendulum Positions

The positions of the masses are given by:

$$
x_1 = l_1 \sin(\theta_1)
$$

$$
y_1 = -l_1 \cos(\theta_1)
$$

$$
x_2 = x_1 + l_2 \sin(\theta_2)
$$

$$
y_2 = y_1 - l_2 \cos(\theta_2)
$$

### Trace Path

The trace path of the second pendulum mass is recorded and displayed to show its trajectory over time.

Save this README file as `README.md` in your project directory. It provides a clear and concise summary of the mathematical and physical principles behind the double pendulum project, including the equations of motion, numerical solution method, and visualization approach.