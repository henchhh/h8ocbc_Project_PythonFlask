try:
    from app import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {}".format(e))

class HomeTest(unittest.TestCase):
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #Check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Database' in response.data)

if __name__ == "__main__":
    unittest.main()