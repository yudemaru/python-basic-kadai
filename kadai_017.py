class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

humans = {
    "太郎": Human("太郎", 25),
    "花子": Human("花子", 18),
    "次郎": Human("次郎", 22),
    "三郎": Human("三郎", 15),
}

for human in humans.values():
    human.check_adult()
