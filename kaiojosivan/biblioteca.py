dic = { 
    "josivan": "professor",
    "arthur": "estudante"
}

di = dict([("josivan","professor"),("arthur","estudante")])
print(dic["josivan"])
print(dic.get("josivan"))
print("josivan" in di)
if "bruno" in di:
    print("bruno existe")
else:
    print("bruno não existe")

if "professor" in di.values():
    print("professor existe")
else:
    print("professor não existe")
dic["josivan"] = "programador de jogos"
print(dic["josivan"])
dic["negativo"] = "oi"
print(dic)
del dic["negativo"]
print(len(dic))
dic.update(di)

robôs = {
    "robo1":{
        "peso":12.4,
        "consumo":5,
        "categoria":"defesa"},
    "robo2":{
        "peso":6.5,
        "consumo":12,
        "categoria":"ataque"},
    "robo3":{
        "peso":10.0,
        "consumo":16,
        "categoria":"suporte"}


}
def mostrarinfo(dicionario, nome):
    print(dicionario[nome])

mostrarinfo(robôs,"robo2")

