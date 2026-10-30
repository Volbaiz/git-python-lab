"""
Лабораторна робота: Варіант 8
Студент: [Зяблов Нікіта]
Група: [2]
"""

def stall_warning(alpha: float) -> str:
    match True:
        case _ if alpha <= 10:
            return("Політ штатний")
        case _ if 10 < alpha <= 15:
            return("Увага: Наближення до критичного кута")
        case _:
            return "Попередження: Звалювання!"

angle_of_attack = float(input("Enter the angle of attack "))
print(stall_warning(angle_of_attack))


onboard_sensors = {
    'sensor': input("Enter the sensor name "), 
    'value': float(input("Enter the sensor\'s value ")), 
    'status': input("Enter the sensor\'s status ")
}

def process_sensor_response(response: dict) -> str:
    match response:
        case {'status': 'ERROR'}:
            return "Помилка"
        case {'sensor': 'ALTITUDE', 'value': val} if val < 0:
            return "Помилка висотоміра"
        case _:
            return "Політ штатний"

print(process_sensor_response(onboard_sensors))