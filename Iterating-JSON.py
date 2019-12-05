import json

lista = ["XXXX", "YYYY"]

json_data = '{"vs":[{"XXXX":["1234", "56789", "101112"],"YYYY":["4321", "56789", "121110"]}]}' 

parsed_json = (json.loads(json_data))

for i in range (0, len (parsed_json["vs"])):
	for element in lista:
		for j in range (0, len (parsed_json["vs"][i][element])):
			print parsed_json["vs"][i][element][j]
