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
