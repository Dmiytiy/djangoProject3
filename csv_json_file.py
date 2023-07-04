#преобразования данных из CSV-файла в формат JSON
import csv
import json
#Задаются константы DATA_ADS и JSON_ADS, которые представляют пути к исходному CSV-файлу и целевому JSON-файлу соответственно.
DATA_ADS = 'data/ads.csv'
JSON_ADS = 'ads.json'
DATA_CAT = 'data/categories.csv'
JSON_CAT = 'categories.json'

#Цикл for перебирает строки в CSV-файле с использованием csv.DictReader. csv.DictReader позволяет читать строки из CSV-файла и возвращать их в виде словаря, где ключами являются названия столбцов, а значениями — данные из соответствующих ячеек.
def convert_file(csv_file, model_name, json_file):
    result = []
    with open(csv_file, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add ={'model':model_name, 'pk':int(row['Id'] if 'Id' in row else row['id'])}

            if 'Id' in row:

                del row['Id']
            else:
                del row['id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True

                else:
                    row['is_published'] = False
            if 'price'  in row:
                row['price'] = int(row['price'])
            to_add['fields'] =row
            result.append(to_add)

    with open(json_file, "w", encoding='utf-8') as jsf:
        jsf.write(json.dumps(result, ensure_ascii=False))

#В каждой итерации цикла создается словарь to_add, который будет представлять отдельную запись в JSON-файле. В этом словаре устанавливаются два ключа: 'model' с значением model_name и 'pk' с значением, полученным из столбца 'Id' текущей строки CSV-файла (преобразованного в целое число с помощью int()).

#Удаляется ключ 'Id' из словаря row, так как он уже использован для формирования значения ключа 'pk'.

#Если значение столбца 'is_published' равно строке 'TRUE', то в словарь row для ключа 'is_published' устанавливается значение True. В противном случае, устанавливается значение False.
#Создается ключ 'fields' в словаре to_add, которому присваивается словарь row. Это позволяет сохранить все остальные поля строки CSV-файла внутри ключа 'fields' в JSON-файле.
#вызывается функция convert_file с передачей ей путей к исходному CSV-файлу DATA_ADS, названию модели 'ads.ad' и пути к целевому JSON-файлу JSON_ADS.
#convert_file(DATA_ADS, "ads.ad", JSON_ADS)
convert_file(DATA_CAT, "ads.category", JSON_CAT)