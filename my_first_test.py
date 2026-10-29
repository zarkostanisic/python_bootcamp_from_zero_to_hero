from unittest import TestCase, main

value = 1
class Evaluate(TestCase):
    def test_exercise(self):
        self.assertEqual(1, value, 'Not Equal')

# Standardni ulaz za pokretanje unittest-a u čistom Python-u
if __name__ == '__main__':
    main()