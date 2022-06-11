
from vpython import *
from numpy import *


const = 1E-7

#parameters
R = 0.12
r = 0.06
h = 0.1
I = 1
Ns = 1

#m ,n parts of small loops
m, n = 200, 200


def get_inductance(r1, r2, h1, h2):
    total_flux = 0
    for i in range(m):
        inner_radius = (r2 / m) * i
        outer_radius = (r2 / m) * (i + 1)
        p = vec((inner_radius + outer_radius) / 2, 0, h2)

        B = vec(0, 0, 0)
        for j in range(n):
            theta = 2 * pi / n
            ds_position = vec(r1 * cos(theta * j), r1 * sin(theta * j), h1)
            ds_direction = vec(-r1 * theta * sin(theta * j), r1 * theta * cos(theta * j), 0)
            r_vector = p - ds_position
            B += const * I * ds_direction.cross(r_vector) / (mag(r_vector) ** 3)
        dA = (outer_radius ** 2 - inner_radius ** 2) * pi * vec(0, 0, 1)
        total_flux += B.dot(dA)

    inductance = Ns * total_flux / I
    return inductance

# print inductance
print(get_inductance(R, r, 0, h))
print(get_inductance(r, R, h, 0))
print("diff:",get_inductance(R, r, 0, h) - get_inductance(r, R, h, 0))