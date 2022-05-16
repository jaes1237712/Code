from vpython import*
fd = 120
resistance = 30
inductance = 200E-3
capacitance = 20E-6
t = 0
dt = 1.0/(fd*5000)

scene1 = graph(align = 'left', xtitle = 'T', ytitle = 'i(A) blue/v(100V) red', background = vec(0.2,0.6,0.8))
scene2 = graph(align = 'left', xtitle = 'T', ytitle = 'Energy(J)', background = vec(0.2,0.6,0.8))
i_t = gcurve(color = color.blue, graph = scene1)
v_t = gcurve(color = color.red, graph = scene1)
E_t = gcurve(color = color.red, graph = scene2)

v,v_c,v_i = 0,0,0
i = 0
energy = 0

prev_i = 0
prev_prev_i = 0
maxcount = 0
nineth_imax_T = 0
nineth_imax_Mag = 0

E_10percent_t = 0
E_10percent_Mag = 0

while t <= (20/fd):
	rate(5000)

	if t<(12/fd): v = 36*sin(2*pi*fd*t)
	else: v = 0

	v_l = v - v_c - i*resistance
	i += (v_l/inductance) * dt
	v_c += (i/capacitance) * dt
	energy = 0.5*capacitance*v_c**2 + 0.5*inductance*i**2
	t += dt

	if(maxcount < 9):
		if(prev_i - i > 0 and prev_i - prev_prev_i > 0):
			maxcount += 1

		if(maxcount==9):
			nineth_imax_T = (t-dt)*fd
			nineth_imax_Mag = prev_i
			print("Magnitude of i")
			print("Numerical:", nineth_imax_Mag, "Theoretical:", 36/sqrt(30**2+(48*pi-10000/(48*pi))**2))
			print('	')
			

			print("Phase constant of i")
			print("Numerical:", 2*pi*(floor(nineth_imax_T)+0.25- nineth_imax_T), "Theoretical:", atan(-(48*pi-10000/(48*pi))/30))
			print('	')

		prev_prev_i = prev_i
		prev_i = i

	if t >= (12/fd):
		if E_10percent_Mag == 0:
			E_10percent_Mag = 0.1*energy
		if energy <= E_10percent_Mag and (E_10percent_t == 0):
			E_10percent_t = t
			print("THe energy drops below 0.1 E(T=12) at t=", t*fd, "T")

	v_t.plot(pos=(t*fd, v/100))
	i_t.plot(pos=(t*fd,i))
	E_t.plot(pos=(t*fd,energy))