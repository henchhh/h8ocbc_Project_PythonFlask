try:
    from app import app
    import unittest
    import json

except Exception as e:
    print("Some Modules are Missing {}".format(e))

class PostTest(unittest.TestCase):
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        input_id = input("\nMasukkan id Directors yang ingin dihapus : ")
        response = tester.delete(f'http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{input_id}',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({},))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

if __name__ == "__main__":
    unittest.main()