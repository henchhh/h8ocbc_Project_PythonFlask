try:
    from app import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {}".format(e))

directors_id = input("\nMasukkan ID Directors yang ingin diget: ")
movies_id = input("\nMasukkan ID Movies yang ingin diget: ")
class HomeTest(unittest.TestCase):
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get(f"http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{directors_id}/movies/{movies_id}")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #Check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get(f"http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{directors_id}/movies/{movies_id}")
        self.assertEqual(response.content_type,"application/json")

    #Check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get(f"http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{directors_id}/movies/{movies_id}")
        self.assertTrue(b'department' in response.data)

if __name__ == "__main__":
    unittest.main()