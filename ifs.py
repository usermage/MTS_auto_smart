def drive_safe(pain):
    #получать данные с устройства отслеживания состояния, когда выдает предупреждение
    print("Вы устали! Необходим отдых! Продолжать движение опасно!")
    # если указано что у пользователя проблемы со здоровьем
    if (pain==1):
        print("Возможен риск здоровью!")
        #вызов скорой автоматически при необходимости

def climat():
    #получить данные от термометра или пользователя
    temp="cold" #hot
    if(temp=="cold"):
        print("Включается подогрев сидений")
    if (temp == "hot"):
        print("Включается кондиционер")

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

def diagn():
    print("results diagnostik")

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
        if i==0:
            break
