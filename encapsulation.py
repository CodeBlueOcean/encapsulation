# Encapsulation ( 4 pilliars of oop)

# 1 encapsulation  

class PlayerCharacter:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        return self

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100) 
# player1.speak()
#'hello'. 
print(player1.name)
print(player1.age)

player2 = {'name': 'andrei', 'age': 100}
print(player2['name'])
print(player2['age'])




