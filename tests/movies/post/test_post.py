try:
    from app import app
    import unittest
    import json

except Exception as e:
    print("Some Modules are Missing {}".format(e))

directors_id = input("\nMasukkan ID Directors yang ingin dipost: ")
class PostTest(unittest.TestCase):
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.post(f'http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{directors_id}/movies',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({"budget": 100000,
                                "id": 1234,
                                "original_title": "Movie Test Post",
                                "overview": "Test Post",
                                "popularity": 100,
                                "release_date": "2021-12-28",
                                "revenue": 2000000,
                                "tagline": "Test Post",
                                "title": "Movie Test Post",
                                "uid": 111222,
                                "vote_average": 8,
                                "vote_count": 1000
                                }))
        statuscode = response.status_code
        self.assertEqual(statuscode,201)

if __name__ == "__main__":
    unittest.main()