from python_code.Calc import Calculator
import pytest
import yaml

with open('calculator.yaml', encoding='utf-8') as f:
      datas = yaml.safe_load(f)
      datas_add = datas['add']
      add_data = datas_add['datas']
      add_ids = datas_add['add_yam']
      datas_div = datas['div']
      div_data = datas_div['div_yam']
# 定义测试类
class Test_Calculator:

    def setup_class(self):
            # 使局部变量cale变成一个实例变量
            self.calc = Calculator()
            print("开始计算")

    @pytest.mark.parametrize('a, b, expe', add_data, ids=add_ids)
    def test_add(self, a, b, expe):
            result = self.calc.add(a, b)
            if isinstance(result, float):
                result = round(result, 2)
            assert result == expe

    @pytest.mark.parametrize('a, b , expe', div_ids, ids=div_ids)
    def test_div(self, a, b, expe):
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
            if b == 0:
                print("除数不能为0")
                return
            assert result == expe

    def teardown_class(self):
        print("计算结束")

   # def test_add1(self):
   #      # 实例化计算器类
   #      self.calc = Calculator()
   #       调用add方法
   #      result = self.calc.add(0.1, 0.1)
   #      # 得到结果后需要些断言
   #     assert result == 0.2
   #  def test_add2(self):
   #      # 实例化计算器类
   #     calc = Calculator()
   #      # 调用add方法
   #    result = self.calc.add(-1, -1)
   #      # 得到结果后需要些断言
   #     assert result == -2

