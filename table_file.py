def find_interval(onset: str, end: str) -> tuple:
    "функция поиска интервала между элементами списка"
    onset_index, end_index = 0, 0
    for i in range(len(list_goods)):
        if list_goods[i] == str(onset):
            onset_index = i
        if list_goods[i] == str(end):
            end_index = i
    return (onset_index, end_index)

def find_char(onset: str, end: str) -> str:
    "функция возвращает строку между начальным и конечным элементом списка"
    interval = find_interval(onset, end)
    onset_index, end_index = interval[0], interval[1]
    result = ''
    for i in range(onset_index + 1, end_index):
        result = result + str(list_goods[i]) + "\n"
    return result

list_goods = []
with open('table_good.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        list_goods.append(line[:-1])
print(len(list_goods))
print(list_goods)
processor = list_goods[2].split(",")[0] + list_goods[2].split(',')[1][:3] + " ядер"
screen = list_goods[37].split(' ')[0] + " " +  list_goods[37].split(' ')[2][1:-1]
oper_sist = list_goods[54]
ddr = list_goods[8][:4]
hdd = " ".join(str(x) for x in list_goods[14].split(' ')[:3]) # тут я распаковываю список из первых трех элементов строки, соединяя их пробелом
videocard, videocard_full = str, str
if list_goods[4].split(' ')[:1][0] == "Integrated":
    videocard = 'встроенная'
    videocard_full = list_goods[4][11:]
else:
    videocard = "дискретная"
    videocard_full = list_goods[4]
matrix = list_goods[37].split(' ')[3]
fingerprint = list_goods[72]
keyboard_backlit = str
if list_goods[41].split(' ')[:1][0] == 'Non-backlit,':
    keyboard_backlit = 'без подсветки'
else:
    keyboard_backlit = list_goods[41]
case_material = str
if list_goods[47][:2] == 'PC':
    case_material = 'пластик'
else:
    case_material = list_goods[47]
sensor_screen = list_goods[39]
case_color = list_goods[43]
weight = list_goods[51]
wdh = list_goods[49]
proc_freq = list_goods[2].split(' ')[12]
ddr_type = list_goods[8][16:20]
ddr_freq = list_goods[8][-4:]
storage_configuration = list_goods[14].split(' ')[1]
interfaces = str
# print(find_interval("Standard Ports", "Security Chip"))
find_char("Standard Ports", "Security Chip")




print(interfaces)
