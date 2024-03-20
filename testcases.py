"""
Checks that the zodiac compatibility program works as expected 
"""

import unittest #Include the pyUnit unittest framework
import zodiac    #The file tested

# Class in which all functions will be ran by unittest
class ZodiacTestP1(unittest.TestCase):

    #Tests that the sign matches the birthday
    def test_get_zodiac_sign(self):
        self.assertEqual(zodiac.get_zodiac_sign(1,10), "Capricorn")
        self.assertEqual(zodiac.get_zodiac_sign(11,9), "Scorpio")
        self.assertEqual(zodiac.get_zodiac_sign(7,22), "Cancer")

    #Tests that the elemental compatibility is accurate
    def test_elemental_compatibility(self):
        fire = ["Aries", "Leo", "Sagittarius"]
        earth = ["Taurus", "Virgo", "Capricorn"]
        air = ["Gemini", "Libra", "Aquarius"]
        water = ["Cancer", "Scorpio", "Pisces"]
        self.assertEqual(zodiac.elemental_compatibility(fire, "Leo", "Sagittarius"), True)
        self.assertEqual(zodiac.elemental_compatibility(earth, "Taurus", "Virgo"), True)
        self.assertEqual(zodiac.elemental_compatibility(water, "Pisces", "Gemini"), False)
    
    #Tests that the power couple matches are correct
    def test_power_couple(self):
        self.assertEqual(zodiac.power_couple("Libra", "Capricorn", "Capricorn", "Libra"), True)
        self.assertEqual(zodiac.power_couple("Aquarius", "Pisces", "Aquarius", "Aries"), False)
        self.assertEqual(zodiac.power_couple("Leo", "Leo", "Gemini", "Taurus"), False)
    
    #Tests that the danger couple matches are correct
    def test_danger_couple(self):
         self.assertEqual(zodiac.danger_couple("Aquarius", "Taurus", "Libra", "Virgo"), False)
         self.assertEqual(zodiac.danger_couple("Pisces", "Leo", "Pisces", "Pisces"), False)
         self.assertEqual(zodiac.danger_couple("Cancer", "Aries", "Aries", "Cancer"), True)
#Main
if __name__=='__main__':
    unittest.main(exit=False)
