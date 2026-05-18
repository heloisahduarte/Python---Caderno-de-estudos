# Permite encrever comentários
"""
Para entender melhor o DOCSTRING
ler o documento em markdown da pasta
"""
#print(1 + 1);

# Aula - strings

#Aspas simples
#print('abc');

#Aspas duplas
#print("abc");

#String
#print("Heloisa Duarte");

#Uso do escape
#print("Heloisa \"Duarte\"");
#print('Heloisa \'Duarte\'');

#r
#print(r"Heloisa \"Duarte\"");
#print(r'Heloisa \'Duarte\'');

#Truque das aspas
#print('Heloisa "Duarte"');
#print("Heloisa 'Duarte'")


#Aula - int e float

#int
#print(11);
#print(-11);

# float
#print(1.1);
#print(-10.11);

# type
#print(type("Heloisa"), type(0));
#print(type(9.8));

#Aula - boolean
#print(10 == 10);
#print(10 == 11);

#Aula - Coerção de tipos

#Polimorfismo
print(1 + 1);
print("a" + "b");

#Coerção
print("1", type("1"));
# 1 <class 'str'> no terminal

print(int("1"), type(int("1")));
# 1 <class 'int'> no terminal

print(float("1") + 1);
#2.0 no terminal