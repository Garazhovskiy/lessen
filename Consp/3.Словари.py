-----------------------------------------
slovar = {
    "name": "xiaomi",
    "model": "redmi note 5",             #словарь (ключ : значение)
    "prise": 120 
}
-----------------------------------------
slovar["root"] = "none" (True,False)     #добавляет ключь в словарь если его там нет (False)         
slovar["prise"] = 4                      #обновляет значение ключа 
-----------------------------------------
print(slovar["prise"])                   #выводит значение ключа
print(slovar.get("prise"))               #выводит значение ключа методом get

plus = slovar.get("name") + " " + slovar.get("model")
print(plus)                              #выводит и слаживает значение ключей

print(slovar.get("model","Такого телефона у нас нет!")) #выводит значение ключа 
                                                  #(если такого ключа нет то СООБЩЕНИЕ)
-----------------------------------------
"name" in slovar                         #есть ли такой ключ в словаре?
"name" not in slovar                     #нету ли такого ключа в каталоге?                                            
-----------------------------------------
slovar = {
    "name": "xiaomi",
    "model": "redmi note 5",         
    "prise": 120 
for key in slovar:
	print(key)                           #цыкл for по словарю slovar (по очереди кладется в переменную)
>>>name
   model
   prise
   root
-----------------------------------------
slovar = {
    "name": "xiaomi",
    "model": "redmi note 5",             #вывод пары ключ:значение
    "prise": 120
for key, value in slovar.items():
	print("{}: {}" .format(key, value))
-----------------------------------------
try:
    del slovar["name"]                       #удаление из словаря по ключу  
except KeyEror:                              #питаюсь удалить если такого ключа нет то ничего не делаю.
	pass
-----------------------------------------