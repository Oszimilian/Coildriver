def create_linear_pwm(file, tstart, tend, voltage, start_dutycycle, period):
    num_steps = int((tend - tstart) / period)

    while num_steps > 0:
        tstart += period
        num_steps -= 1
        if start_dutycycle < 1:
            file.write(f"{round(tstart,2)} 0.0\n")
            file.write(f"{round(tstart + start_dutycycle * period, 2)} 0.0\n")
        file.write(f"{round(tstart + start_dutycycle * period, 2)} {voltage}.0\n")
        file.write(f"{round(tstart + period,2)} {voltage}.0 \n")


def create_pwl_file(name):
    with open(name, "w") as file:
        create_linear_pwm(file, 0, 1, 5, 0.9, 0.1)

create_pwl_file("Test.txt")