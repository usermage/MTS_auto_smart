import user 
from threading import Thread
import time
import socket
import requests

#1
def climat():
    #получить данные от термометра или пользователя
    temp="cold" #hot
    if(temp=="cold"):
        print("Включается подогрев сидений")
    if (temp == "hot"):
        print("Включается кондиционер")
		
#2
def drive_safe(pain):
    #получать данные с устройства отслеживания состояния, когда выдает предупреждение
    print("Вы устали! Необходим отдых! Продолжать движение опасно!")
    # если указано что у пользователя проблемы со здоровьем
    if (pain==1):
        print("Возможен риск здоровью!")
        #вызов скорой автоматически при необходимости

#3
def whereavto():
    #от машины данные, получаем лог
    res=1
    #машина где-то стоит
    if res==1:
        print("Координаты : на карте")
    #мотор выключен, машина движется
    if res==2:
        print("Машину эвакуируют")
    # машина едет, но в ней не владелец
    if res ==3:
        print("Машину угнали. Давай позвоним в полицию")

#4
def diagn():
#отправка результатов диагностики
    print(getr('Diagnostik'))
	
#5
 def ugon():
 #меня угнали
    print(getr('stolen_car'))   

#6	
def safety():
#check safety sensors
	print(getr('Car_safety_results'))

#7	
def driving_quality():
	res = 0
	#вождение опасно
	if res == 1:
		print(getr('danger_driver'))
		#Ваше вождение может быть опасным и повлечь ДТП
	#нормальная манера вождения
	if res == 0:
		print (getr('good_driver'))
	
	
#Запрос к МТС
def getr(command):
    x = requests.get('http://127.0.0.1:5000/1/'+command)
    return x.text
    
    



if __name__=='__main__':
    while True:
        print("Введите запрос:")
        i = int(input())
        
            
        if i == 1:
            print("Включаю климат контроль")
            climat()

        if i==2:
            print("Включаю поддержка водителя в дороге")
            drive_safe(0)
			
        if i==3:
            print("Включаю поиск автомобиля")
            #программа возвращает геопозицию машины
            whereavto()

        if i==4:
            print("Включаю диагностику автомобиля")
            # возвращает состояние машины, коды и описание проблем, выдает ближайшие адреса сервисов при необходимости
            diagn()
		
		if i == 5:
			print ("Отправляю ообщение об угоне машины")
			ugon()
		
		if i == 6:
			print ("Проверка датчиков безопасности")
			safety()
		
		if i == 7:
			print ("Проверка качества вождения и отправка результатов")
			driving_quality()
		
		
        if i==0:
            break
