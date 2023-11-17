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

print(hdd)
print(list_goods[128])