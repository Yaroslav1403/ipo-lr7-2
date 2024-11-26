#Подключение модуля json
import json

#Имя файла, из которого будут загружены данные
file = 'dump.json'  
#Просим dпользователя ввести номер квалификации
qualification_code_input = str(input("Введите номер квалификации: "))
#Переменная, которая будет использоваться для отслеживания, была ли найдена квалификация
skills_found = False

#Открываем файл для чтения и его сод ержимое загружается в переменную content
with open(file, 'r', encoding='utf-8') as file: 
    content = json.load(file) 
    #Проходимся по каждому элементу в content
    for skill in content:
        #Проверяем, представляет ли собой модель "data.skill" элемент
        if skill.get("model") == "data.skill":
            #Проверяем, совпадает ли код квалификации с введённым кодом пользователя
            if skill["fields"].get("code") == qualification_code_input: 
                #Сохраняем код квалификации в переменную code_of_qualification
                code_of_qualification = skill["fields"].get("code")
                #Сохраняем название квалификации в переменную qualification_title
                qualification_title = skill["fields"].get("title")
                #Переменная skills устанавливается в True
                skills_found = True
            
                #После того, как нашли код квалификации, снова проходимся по данным, чтобы найти специальность
                for profession in content:
                    #Проверяем, представляет ли собой модель "data.specialty" элемент
                    if profession.get("model") == "data.specialty":
                        code_of_speciality = profession["fields"].get("code")
                        #Проверяем, содержится ли код специальности в коде квалификации
                        if code_of_speciality in qualification_code_input:  
                            #Сохраняем 
                            name_of_speciality = profession["fields"].get("title")
                            speciality_educational = profession["fields"].get("c_type")
                            break
                break  

#Проверяем, была ли найдена квалификация.
if not skills_found:
   #Если квалификация не найдена, выводится сообщение "Не Найдено"
   print("=============== Не Найдено ===============") 
else:
   #Если квалификация найдена, выводится сообщение "Найдено"
   print("=============== Найдено ===============") 
   #Вывод информации о квалификации
   print(f"{code_of_speciality} >> Специальность {name_of_speciality} , {speciality_educational}")
   print(f"{code_of_qualification} >> Квалификация {qualification_title}")

