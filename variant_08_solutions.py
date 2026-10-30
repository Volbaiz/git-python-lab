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





data_of_temperatures = [12, 32, 45, 45, 0, 0, 0, 6, 5, 5.6, 5.6, 6]
def remove_consecutive_duplicates(data: list) -> list:
    final_data = []
    for i in data:
        if final_data and i == final_data[-1]:
            continue
        final_data.append(i)
    return final_data
        
print(remove_consecutive_duplicates(data_of_temperatures))  




data_of_G_forces = [12, 32, 45, 45, 0, 0, 0, 45.5, 5, 5.6, 5.6, 6]

def find_max_overload(g_list: list) -> tuple:
    max_g = g_list[0]
    max_time = 0

    for (time, i) in enumerate(g_list):
        if max_g < i:
            max_g = i
            max_time = time
    return(max_time, max_g)

print(find_max_overload(data_of_G_forces))