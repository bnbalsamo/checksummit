import unittest
import json
from os import environ

# Defer any configuration to the tests setUp()
environ['CHECKSUMMIT_DEFER_CONFIG'] = "True"

import checksummit


class Tests(unittest.TestCase):
    def setUp(self):
        # Perform any setup that should occur
        # before every test
        checksummit.blueprint.BLUEPRINT.config['DISALLOWED_ALGOS'] = []
        self.app = checksummit.app.test_client()

    def tearDown(self):
        # Perform any tear down that should
        # occur after every test
        pass

    def testPass(self):
        self.assertEqual(True, True)

    def testVersionAvailable(self):
        x = getattr(checksummit, "__version__", None)
        self.assertTrue(x is not None)

    def testVersion(self):
        version_response = self.app.get("/version")
        self.assertEqual(version_response.status_code, 200)
        version_json = json.loads(version_response.data.decode())
        api_reported_version = version_json['version']
        self.assertEqual(
            checksummit.blueprint.__version__,
            api_reported_version
        )

    def testAvailableAlgos(self):
        r = self.app.get("/available")
        self.assertEqual(r.status_code, 200)
        x = json.loads(r.data.decode())
        self.assertTrue(isinstance(x, list))


if __name__ == "__main__":
    unittest.main()
