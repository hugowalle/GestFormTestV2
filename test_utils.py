import unittest

from utils import create_random_list,apply_gestform_processing_to_list


class TestUtils(unittest.TestCase):
    def test_create_random_list(self):                                        #Test vérifiant que la liste générée est de la bonne taille
        _length = 10
        self.assertEqual(
            len(create_random_list(_length)),
            _length,
            "incorrect length"
        )
    def test_create_random_list_input(self):                                  #Test vérifiant l'entrée de la fonction créant une liste aléatoire       
        self.assertRaises(TypeError,create_random_list,True)
        self.assertRaises(ValueError,create_random_list,-5)

    def test_apply_gestform_processing_to_list(self):                         #Test vérifiant le bon traitement d'une liste
        _list = [2,3,5,15,120]
        processed_list = "2, Geste, Forme, Gestform, Gestform"
        self.assertEqual(
            apply_gestform_processing_to_list(_list),
            processed_list,
            "incorrect list"
        )
    def test_apply_gestform_processing_to_list_input(self):                   #Test vérifiant l'entrée de la fonction traitant la liste aléatoire
        self.assertRaises(TypeError,apply_gestform_processing_to_list,True)
        self.assertRaises(TypeError,apply_gestform_processing_to_list,[-5,100,True])
    

if __name__ == '__main__':
    unittest.main()
