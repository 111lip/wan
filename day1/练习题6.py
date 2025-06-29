# 练习题 1：定义 Car 类
class Car:
    def __init__(self, brand, speed):
        """
        初始化 Car 类的属性
        :param brand: 汽车品牌
        :param speed: 初始速度
        """
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        """
        加速方法，速度增加 m 次，每次增加 10
        :param m: 加速次数
        """
        self.speed += m * 10

    def brake(self, n):
        """
        刹车方法，速度减少 n 次，每次减少 10，且不低于 0
        :param n: 刹车次数
        """
        self.speed = max(self.speed - n * 10, 0)

# 练习题 2：创建 Car 类实例并调用方法
car_instance = Car("Toyota", 50)
print(f"初始速度: {car_instance.speed}")

car_instance.accelerate(3)
print(f"加速 3 次后速度: {car_instance.speed}")

car_instance.brake(2)
print(f"刹车 2 次后速度: {car_instance.speed}")

# 练习题 3：定义 ElectricCar 子类继承 Car
class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        """
        初始化 ElectricCar 类的属性，调用父类构造方法
        :param brand: 汽车品牌
        :param speed: 初始速度
        :param battery: 初始电量
        """
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        """
        充电方法，电量增加 20，不超过 100
        """
        self.battery = min(self.battery + 20, 100)

# 测试 ElectricCar 子类
electric_car_instance = ElectricCar("Tesla", 60, 50)
print(f"\n电动汽车初始速度: {electric_car_instance.speed}, 初始电量: {electric_car_instance.battery}")

electric_car_instance.accelerate(2)
print(f"加速 2 次后速度: {electric_car_instance.speed}")

electric_car_instance.charge()
print(f"充电后电量: {electric_car_instance.battery}")