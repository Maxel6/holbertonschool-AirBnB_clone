#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertTrue(hasattr(self.model, "id"))
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save(self):
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.model, "to_dict"))
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()
