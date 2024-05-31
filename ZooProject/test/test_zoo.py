import unittest
from unittest import TestCase
from src.zoo import Zoo,ZooKeeper,Animal,Fence


class TestZoo(TestCase):
    def setUp(self) -> None:
        self.zoo_1: Zoo = Zoo(Fence,ZooKeeper)
        self.zookeeper_1 : ZooKeeper = ZooKeeper(nome ="Filippo",cognome= "rossi",id=1)
        self.fence_1 : Fence = Fence(area=100, temperature= 25.0 ,habitat= "Savana", id=1)
        self.animal_1 : Animal = Animal(id=1,name="Leone",species="licaone",age = 5,height=300.00,width=1.0,preferred_habitat="Savana") 

    def test_animal_dimension(self):
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result : int = len(self.fence_1.animals)
        message :str = f"errorfunction"

        self.assertEqual(result,0,message)

    def test_animal_pesoanimale(self):
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result : int = len(self.fence_1.animals)
        message :str = f" non è in linea"

        self.assertEqual(result,0,message)
        
        
    def test_animal_health(self):
        result_2 : int = self.animal_1.health
        self.zookeeper_1.feed(self.animal_1, self.fence_1)
        result : int = self.animal_1.health
        message :str = f" è in salute "

        self.assertEqual(result,result_2,message)   
    

    def test_1(self):
        pass

if __name__=="__main__":    
    unittest.main()
