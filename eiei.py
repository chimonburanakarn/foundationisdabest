def check_bearing_pressure(load_kN, footing_width, footing_length):
    area = footing_width * footing_length
    pressure = load_kN / area
    return pressure

# ตัวอย่าง
pressure = check_bearing_pressure(1000, 2.6, 2.6)

print(f"แรงกดดินจริง = {pressure:.2f} kN/m^2")
