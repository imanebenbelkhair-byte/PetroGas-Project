import numpy as np
import matplotlib.pyplot as plt

def calculate_pressure(T_celsius, n=1, V=10):
    R = 0.0821  # L.atm/(mol.K)
    T_kelvin = T_celsius + 273.15
    P = (n * R * T_kelvin) / V
    return P

def show_plot():
    # اختيار مجال درجات الحرارة (مثلاً من 0 إلى 100 مئوية)
    temperatures = np.linspace(0, 100, 100)
    pressures = calculate_pressure(temperatures)

    # إنشاء الرسم البياني مع المقاييس
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, pressures, label='Ideal Gas (PV=nRT)', color='red', linewidth=2)

    # إضافة العناوين والمقاييس (هنا الأهم)
    plt.title('Gas Pressure vs Temperature Analysis', fontsize=14)
    plt.xlabel('Temperature (°C)', fontsize=12) # مقياس الحرارة
    plt.ylabel('Pressure (atm)', fontsize=12)    # مقياس الضغط
    
    # إضافة الشبكة لتسهيل قراءة القيم
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # إضافة وسيلة الإيضاح
    plt.legend()

    # إظهار الرسم
    plt.show()

if __name__ == "__main__":
    show_plot()