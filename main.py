#Импорт модуля json
import json

#Имя файла, из которого будут загружены данные
file = 'dump.json'  
#Просим пользователя ввести номер квалификации
input_qualification_code = str(input("Введите код квалификации: "))
#Инициализируем переменную, которая изменится на True, если квалификация будет найдена
found_skills = False

#Открываем файл для чтения и его содержимое загружается в переменную content
with open(file, 'r', encoding = 'utf-8') as file: 
    content = json.load(file) 
    
    #Проходимся по каждому элементу в content
    for skill in content:
        #Проверяем, соответствует ли модель элемента значению "data.skill" 
        if skill.get("model") == "data.skill":
            #Проверяем, совпадает ли код квалификации с введённым кодом пользователя
            if skill["fields"].get("code") == input_qualification_code: 
                #Сохраняем код квалификации в переменную code_of_qualification
                code_of_qualification = skill["fields"].get("code")
                #Сохраняем название квалификации в переменную qualification_title
                title_of_qualification = skill["fields"].get("title")
                #Сохраняем специальность в переменную specialty
                specialty = skill["fields"].get("specialty")
                #Переменная found_skills устанавливается в True
                found_skills = True
            
                #После того, как нашли код квалификации, снова проходимся по данным, чтобы найти соответствующую специальность
                for profession in content:
                    #Проверяем, соответствует ли модель элемента значению "data.specialty"
                    if profession.get("model") == "data.specialty":
                        #Сохраняем код специальности в переменную code_of_specialty
                        code_of_specialty = profession["fields"].get("code")
                        #Сохраняем первичный ключ квалификации в переменную pk_of_specialty
                        pk_of_specialty = profession["pk"]
                        #Проверяем, совпадает ли идентификатор специальности с первичным ключом текущей специальности
                        if specialty == pk_of_specialty:  
                            #Сохраняем информацию о специальности и об образовании
                            title_of_specialty = profession["fields"].get("title")
                            specialty_educational = profession["fields"].get("c_type")
                            break
                break  

#Проверяем, была ли найдена квалификация
if not found_skills:
   #Если квалификация не найдена, выводится сообщение: "Не Найдено"
   print("=============== Не Найдено ===============") 
else:
   #Если квалификация найдена, выводится сообщение: "Найдено"
   print("=============== Найдено ===============") 
   #Вывод информации о квалификации
   print(f"{code_of_specialty} >> Специальность: {title_of_specialty} , {specialty_educational}")
   print(f"{code_of_qualification} >> Квалификация: {title_of_qualification}")

