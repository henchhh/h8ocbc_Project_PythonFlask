try:
    from app import app
    import unittest
    import json

except Exception as e:
    print("Some Modules are Missing {}".format(e))

# client = connex_app.test_client()

class PostTest(unittest.TestCase):    
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.post('http://h8ocbc2-milestone1-013.herokuapp.com/api/directors',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({"department": "Test",
                                                 "gender": 2,
                                                 "id": 123,
                                                 "name": "Dean Test",
                                                 "uid": 11111111}))
        statuscode = response.status_code
        self.assertEqual(statuscode,201)

if __name__ == "__main__":
    unittest.main()