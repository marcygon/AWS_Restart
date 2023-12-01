{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":11},"action":"insert","lines":["import csv","import copy"],"id":2}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":4}],[{"start":{"row":12,"column":1},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":10}],[{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":14}],[{"start":{"row":17,"column":20},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":39,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":16}],[{"start":{"row":39,"column":42},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":45},"action":"insert","lines":["currentVehicle = copy.deepcopy(myVehicle)"],"id":19}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":41,"column":41},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":43,"column":0},"end":{"row":46,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":22}]]},"ace":{"folds":[],"scrolltop":591,"scrollleft":0,"selection":{"start":{"row":46,"column":22},"end":{"row":46,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1701433175477,"hash":"cc0ab50a92df21fca80cae8a3ac02b70e9901f54"}