list_goods = []
with open('table_good.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        list_goods.append(line[:-1])
print(list_goods)
processor = list_goods[2].split(",")[0] + list_goods[2].split(',')[1][:3] + " ядер"
screen = list_goods[128].split(' ')[0] + " " +  list_goods[128].split(' ')[2][1:-1]
oper_sist = list_goods[54]
ddr = list_goods[8]
hdd = " ".join(str(x) for x in list_goods[14].split(' ')[:3]) # тут я распаковываю список из первых трех элементов строки, соединяя их пробелом
videocard = str
if list_goods[4].split(' ')[:1][0] == "Integrated":
    videocard = 'встроенная'
else:
    videocard = list_goods[4]
matrix = list_goods[128].split(' ')[3]
fingerprint = list_goods[72]
keyboard_backlit = str
if list_goods[132].split(' ')[:1][0] == 'Non-backlit,':
    keyboard_backlit = 'без подсветки'
else:
    keyboard_backlit = list_goods[132]
case_material = str
if list_goods[138][:2] == 'PC':
    case_material = 'пластик'
else:
    case_material = list_goods[138]

print(case_material)
print(list_goods[128])