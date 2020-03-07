#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
d = np.array([0.0,0.0])
prev_d = d
heading = 0

v = 1
omega = 2*np.pi

t = 0
dt = 0.02

length = 0.01
while t <= 2:
    t += dt
    d[0] += v * np.cos(heading) * dt
    d[1] += v * np.sin(heading) * dt
    omega = np.random.random_sample() * 3 -1
    print(t)
    heading += omega * dt
    omega -= 0.1
    # for stopping simulation with the esc key.
    plt.gcf().canvas.mpl_connect(
        'key_release_event',
        lambda event: [exit(0) if event.key == 'escape' else None])
    plt.plot((prev_d[0],d[0]),(prev_d[1],d[1]))
    plt.arrow(d[0],d[1],length * np.cos(heading), length * np.sin(heading))
    plt.axis("equal")
    plt.grid(True)
    plt.pause(0.02)
    prev_d = np.copy(d)
plt.show()
