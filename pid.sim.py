import matplotlib.pyplot as plt
Kp, Ki, Kd = 1, 0, 10   # coba ubah-ubah nilai ini
setpoint = 100.0              # kecepatan target
dt = 0.02                     # langkah waktu (detik)
tau = 0.3                     # kelambanan motor (model sederhana)
gain = 0.5                    # kecepatan akhir = gain x PWM
speed = 0.0
integral = 0.0
prev_error = 0.0
waktu, kecepatan, pwm = [], [], []
for i in range(500):
    error = setpoint - speed
    integral += error * dt
    derivative = (error - prev_error) / dt
    prev_error = error
    output = Kp * error + Ki * integral + Kd * derivative
    output = max(0, min(255, output))   # batas PWM Arduino 0-255
    speed += (gain * output - speed) / tau * dt   # model motor orde satu
    waktu.append(i * dt)
    kecepatan.append(speed)
    pwm.append(output)
plt.plot(waktu, kecepatan, label='Kecepatan')
plt.axhline(setpoint, color='red', linestyle='--', label='Setpoint')
plt.xlabel('Waktu (detik)')
plt.ylabel('Kecepatan')
plt.legend()
plt.title(f'PID: Kp={Kp}, Ki={Ki}, Kd={Kd}')
plt.savefig('pid_simulasi.png')
plt.show()