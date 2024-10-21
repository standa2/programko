class Student():
    def __init__(self, name, school, colour):
        self.name = name
        self.school = school
        self.fav_colour = colour
    def speak(self, pozdrav):
        print(f"{pozdrav}moje oblibena barva je {self.fav_colour}")

class Zak(Student):
    def __init__(self, name, school, colour):
        super().__init__(name, school, colour)


venca = Student("Venca", "Trebesin", "blue")

print(venca.fav_colour)
venca.speak("Ahoj ")

zdena = Student("Zdena", "Trebesin", "black")
zdena.speak("Čůs ")

vlado = Zak("Vlado","Ukraijna", "ptal tebe")
vlado.speak("Čeeeeeeeuuu ")
