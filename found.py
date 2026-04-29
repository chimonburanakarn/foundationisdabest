import math

def calculate_footing_size(load_kN, soil_bearing_capacity_kN_per_m2):
    """
    load_kN: แรงจากเสา (kN)
    soil_bearing_capacity_kN_per_m2: กำลังรับน้ำหนักดิน (kN/m^2)
    """
    # พื้นที่ฐานรากที่ต้องการ
    required_area = load_kN / soil_bearing_capacity_kN_per_m2
    
    # สมมติฐานรากเป็นสี่เหลี่ยมจัตุรัส
    side_length = math.sqrt(required_area)
    
    return required_area, side_length

# ตัวอย่างการใช้งาน
load = 1000  # kN
soil_capacity = 150  # kN/m^2

area, size = calculate_footing_size(load, soil_capacity)

print(f"พื้นที่ฐานรากที่ต้องการ = {area:.2f} m^2")
print(f"ขนาดฐานราก (กว้าง x ยาว) ≈ {size:.2f} x {size:.2f} m")
