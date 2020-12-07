'''比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
'''
import yaml
# 定义一个动物类，属性，方法
class Animal():
    name: str = ""
    color: str = ""
    age: int = 10
    gender: str = ""

    # 实例化
    def __init__(self, name, color, age, gender):
        self.age = age
        self.name = name
        self.color = color
        self.gender = gender

    def call(self):
        print("我会叫")

    def run(self):
        print("我会跑")

# 定义一个子类
class Cat(Animal):
    hair: str = ""

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        # 继承父类的属性
        super().__init__(name, color, age, gender)

    def Catch(self):
        print(f"我会抓老鼠")

    def call(self):
        print("我会喵喵叫")

        # 编写一个方法，输出全部结果
    def get_cat(self):
        print(f"我叫{self.name},颜色是{self.color},年龄是{self.age}，性别是{self.gender},{self.hair}")
        self.Catch()

    ## 定义一个狗子类
class Dog(Animal):
    hair: str = ""

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def home(self):
        print("我会看家")

    def call(self):
        print("我会汪汪叫")

    def get_dog(self):
        print(f"我叫{self.name},颜色是{self.color},年龄是{self.age}，性别是{self.gender},{self.hair}")

# 调用方法，运行结果
if __name__ == '__main__':
    ncat = Cat("短毛", "球球", "白色", 2, "公")
    # print(ncat.hair)
    ncat.Catch()
    ncat.get_cat()
    ndog = Dog("长毛", "花花", "黑色", 3, "母")
    ndog.home()
    ndog.get_dog()
    print("----------------------------------------------------------------------")

# yaml方法
with open("Animal.yml", encoding="utf-8") as f:
    datas=yaml.safe_load(f)  ##从yaml读取文件
    hair = datas['cat']['hair']
    name = datas['cat']['name']
    color = datas['cat']['color']
    age = datas['cat']['age']
    gender = datas['cat']['gender']
    ncat = Cat(hair, name, color, age, gender)
    ncat.Catch()
    ncat.get_cat()
    # 定义狗属性 从yml文件中获取值
    hair = datas['dog']['hair']
    name = datas['dog']['name']
    color = datas['dog']['color']
    age = datas['dog']['age']
    gender = datas['dog']['gender']
    ndog = Dog(hair, name, color, age, gender)
    ndog.home()
    ndog.get_dog()