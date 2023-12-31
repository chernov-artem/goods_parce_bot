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
    "функция возвращает строку между начальным и конечным элементом списка. Входные данные содержание строчек(не индексы)"
    interval = find_interval(onset, end)
    onset_index, end_index = interval[0], interval[1]
    result = ''
    for i in range(onset_index + 1, end_index):
        result = result + str(list_goods[i]) + "\n"
    return result

def find_parametr(name: str) -> int:
    "ищет параметр в файле, возвращает индекс следующей строки"
    i = 0
    with open('table_good.txt', 'r', encoding='utf-8') as file:

        while True:
            line = file.readline()
            i += 1
            if not line:
                break
            if line == name + "\n":
                return i

list_goods = []
with open('table_good.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        list_goods.append(line[:-1])
print(len(list_goods))
print(list_goods)
item1 = list_goods[37]
item2 = list_goods[2]
item3 = list_goods[53] + ' ' + list_goods[64]
item4 = list_goods[12]
item5 = list_goods[14]
item6 = list_goods[3] + ' ' + list_goods[4]
item7 = 'тип матрицы' + list_goods[37]
item8 = 'количество ядер (cores): ' + list_goods[2].split(' ')[3]
item9 =  list_goods[71] + ': ' + list_goods[72]
item10 = list_goods[40] + ': ' + list_goods[41]
item11 =  list_goods[46] + ': ' + list_goods[47]
item12 =  list_goods[38] + ': ' + list_goods[39]
item13 =  'частота обновления экрана: нет данных, скорее всего 60Гц'
item14 =  list_goods[42] + ': ' + list_goods[43]
item15 =  list_goods[50] + ': ' + list_goods[51]
item16 =  list_goods[2]
item17 =  item6
item18 =  'тип памяти: ' + list_goods[8].split(' ')[2][2:6]
item19 =  'частота памяти: ' +  list_goods[8].split(' ')[2][7:]
item20 =  list_goods[15] + ': ' + list_goods[16]
item21 = find_char('CONNECTIVITY', 'SERVICE')
item22 = 'беспроводная связь: ' + list_goods[60]
item23 =  list_goods[61].split(', ')[0]
item24 =  list_goods[61].split(' ')[-1]
item25 = list_goods[0]
item26 = list_goods[21] + ': ' + list_goods[22]
item27 = 'ширина: ' +  str(list_goods[49].split(' ')[0])
item28 = 'глубина: ' +  str(list_goods[49].split(' ')[2])
item29 = 'толщина: ' +  str(list_goods[49].split(' ')[4])
item30 = list_goods[0]


print('item = ', item29)


# item6 = list_goods[] + ' ' +  list_goods[]
# item7 =list_goods[] + ' ' +  list_goods[]
# item8 = list_goods[] + ' ' +  list_goods[]
# item9 = list_goods[] + ' ' +  list_goods[]
# item10 = list_goods[] + ' ' +  list_goods[]
# item11 = list_goods[] + ' ' +  list_goods[]
# item12 = list_goods[] + ' ' +  list_goods[]
# item13 = list_goods[] + ' ' +  list_goods[]
# item14 = list_goods[] + ' ' +  list_goods[]
# item15 = list_goods[] + ' ' +  list_goods[]
# item16 = list_goods[] + ' ' +  list_goods[]
# item17 = list_goods[] + ' ' +  list_goods[]
# item18 = list_goods[] + ' ' +  list_goods[]
# item19 = list_goods[] + ' ' +  list_goods[]
# item20 = list_goods[] + ' ' +  list_goods[]
# item21 = list_goods[] + ' ' +  list_goods[]
# item22 = list_goods[] + ' ' +  list_goods[]
# item23 = list_goods[] + ' ' +  list_goods[]
# item24 = list_goods[] + ' ' +  list_goods[]
# item25 = list_goods[] + ' ' +  list_goods[]
# item2 = list_goods[] + ' ' +  list_goods[]



# tmp_ind = find_parametr('Processor')
# processor = list_goods[tmp_ind].split(",")[0] + list_goods[tmp_ind].split(',')[1][:3] + " ядер"
# tmp_ind = find_parametr('Display')
# screen = list_goods[tmp_ind].split(' ')[0] + " " +  list_goods[tmp_ind].split(' ')[2][1:-1]
# tmp_ind = find_parametr('Operating System')
# oper_sist = list_goods[tmp_ind]
# tmp_ind = find_parametr('Memory')
# ddr = ' '.join(str(x) for x in list_goods[tmp_ind].split(' ')[:2])
# tmp_ind = find_parametr('Storage')
# hdd = " ".join(str(x) for x in list_goods[tmp_ind].split(' ')[:3]) # тут я распаковываю список из первых трех элементов строки, соединяя их пробелом
# tmp_ind = find_parametr('Graphics')
# videocard, videocard_full = str, str
# if list_goods[tmp_ind].split(' ')[:1][0] == "Integrated":
#     videocard = 'встроенная'
#     videocard_full = list_goods[4][11:]
# else:
#     videocard = "дискретная"
#     videocard_full = list_goods[4]
# tmp_ind = find_parametr('Display')
# matrix = list_goods[tmp_ind].split(' ')[3]
# tmp_ind = find_parametr('Fingerprint Reader')
# fingerprint = list_goods[tmp_ind]
# tmp_ind = find_parametr('Keyboard')
# keyboard_backlit = str
# if list_goods[tmp_ind].split(' ')[:1][0] == 'Non-backlit,':
#     keyboard_backlit = 'без подсветки'
# else:
#     keyboard_backlit = list_goods[41]
# tmp_ind = find_parametr('Case Material')
# case_material = str
# if list_goods[tmp_ind][:2] == 'PC':
#     case_material = 'пластик'
# else:
#     case_material = list_goods[47]
# tmp_ind = find_parametr('Touchscreen')
# sensor_screen = list_goods[tmp_ind]
# tmp_ind = find_parametr('Case Color')
# case_color = list_goods[tmp_ind]
# tmp_ind = find_parametr('Weight')
# weight = list_goods[tmp_ind]
# tmp_ind = find_parametr('Dimensions (WxDxH)')
# wdh = list_goods[tmp_ind]
# tmp_ind = find_parametr('Processor')
# proc_freq = list_goods[tmp_ind].split(' ')[12][:-1]
# tmp_ind = find_parametr('Memory')
# ddr_type = list_goods[tmp_ind][16:20]
# ddr_freq = list_goods[tmp_ind][-4:]
# tmp_ind = find_parametr('Storage')
# storage_configuration = list_goods[tmp_ind].split(' ')[1]
# interfaces = find_char("Standard Ports", "Security Chip")
# tmp_ind = find_parametr('WLAN + Bluetooth')
# wireless_connection = list_goods[tmp_ind]
# wifi = " ".join(x for x in list_goods[tmp_ind].split(' ')[:2])[:-1] #распаковка списка, соединенная пробелом
# bluetooth = list_goods[tmp_ind].split(' ')[-1]
# tmp_ind = find_parametr('Optical')
# optical = list_goods[tmp_ind]
# width = str(round(float(wdh.split(' ')[0]) / 10, 1)) + " см" # сделал сокращение до 1 знака после запятой
# depth = str(round(float(wdh.split(' ')[2]) / 10, 1)) + " см" # сделал сокращение до 1 знака после запятой
# height = str(round(float(wdh.split(' ')[4]) / 10, 1)) + " см" # сделал сокращение до 1 знака после запятой
# wdn_cm = width + ' ' + depth + ' ' + height


