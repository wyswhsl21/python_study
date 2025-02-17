class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("이 메서드는 서브클래스에서 구현해야 합니다.")


class Dog(Animal):

    def speak(self):
        return f"{self.name}가 멍멍 짖습니다."


class Cat(Animal):

    def speak(self):
        return f"{self.name}가 야옹거립니다."


# 객체 생성
dog = Dog("바둑이")
cat = Cat("나비")

print(dog.speak())  # 출력: 바둑이가 멍멍 짖습니다.
print(cat.speak())  # 출력: 나비가 야옹거립니다.
