# coding: utf-8

from __future__ import absolute_import

import logging
import unittest

from flask import json
from six import BytesIO

from openapi_server.models import Model
from openapi_server.test import BaseTestCase

MINT_USERNAME = "mint@isi.edu"

class TestModel(BaseTestCase):
    """Model integration test stubs"""
    logger = logging.getLogger("TestModel")

    def test_models_get(self):
        """Test case for models_get

        List all Model entities
        """
        query_string = [('username', self.get_username)] 
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/modelconfigurations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.json)
        for _item in response.json:
            keys = _item.keys()
            for key in keys:
                print(key)
                self.assertFalse('http://' in key)
                self.assertFalse('https://' in key)
        

    def test_model_custom_index_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'flooding')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/models/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_intervention_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'Fertilizer')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/model/intervention',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_region_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'baro')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/model/region',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        for _item in response.json:
            keys = _item.keys()
            for key in keys:
                print(key)
                self.assertFalse('http://' in key)
                self.assertFalse('https://' in key)

    def test_model_custom_variable_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/models/variable',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_model_custom_standard_variable_get(self):
        """Test case for model_get

        List all Models entities
        """
        query_string = [('username', MINT_USERNAME),
                        ('label', 'crop')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.8.0/custom/models/standard_variable',
            method='GET',
            headers=headers,
            query_string=query_string)

        self.logger.info("Response length {}".format(len(response.json)))
        for item in response.json:
            self.assertIsInstance(Model.from_dict(item), Model)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        for _item in response.json:
            keys = _item.keys()
            for key in keys:
                print(key)
                self.assertFalse('http://' in key)
                self.assertFalse('https://' in key)

if __name__ == '__main__':
    unittest.main()
