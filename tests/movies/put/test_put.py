try:
    from app import app
    import unittest
    import json

except Exception as e:
    print("Some Modules are Missing {}".format(e))

directors_id = input("\nMasukkan ID Directors yang ingin diget: ")
movies_id = input("\nMasukkan ID Movies yang ingin diget: ")
class PostTest(unittest.TestCase):
    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.put(f'http://h8ocbc2-milestone1-013.herokuapp.com/api/directors/{directors_id}/movies/{movies_id}',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps({"budget": 100,
                                "original_title": "EDITED",
                                "overview": "EDITED",
                                "popularity": 5,
                                "release_date": "2021-12-27",
                                "revenue": 200,
                                "tagline": "EDITED",
                                "title": "EDITED",
                                "uid": 1112222,
                                "vote_average": 8.5,
                                "vote_count": 10
                                }))
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

if __name__ == "__main__":
    unittest.main()