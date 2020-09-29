"""
Module for fetching trash holiday schedule
"""
import logging

from urllib.parse import urlparse
from aws_requests_auth.aws_auth import AWSRequestsAuth
from botocore.credentials import Credentials

import boto3
import requests


class TrashScheduleService:
    """
    TrashScheduleService is a service class that fetches the trash holiday schedule
    """

    def __init__(self, url):
        self.url = url

    @staticmethod
    def __get_credentials() -> Credentials:
        session = boto3.Session()
        credentials = session.get_credentials()
        return credentials.get_frozen_credentials()

    def _get_auth(self) -> AWSRequestsAuth:
        host = urlparse(self.url).netloc
        credentials = TrashScheduleService.__get_credentials()
        return AWSRequestsAuth(aws_access_key=credentials.access_key,
                               aws_secret_access_key=credentials.secret_key,
                               aws_token=credentials.token,
                               aws_host=host,
                               aws_region=boto3.Session().region_name,
                               aws_service='execute-api')

    def _fetch_schedule(self, auth: AWSRequestsAuth) -> requests.Response:
        logging.info('starting request to url=%s', self.url)
        response = requests.get(self.url, auth=auth)
        logging.info('response=%s', str({'statusCode': response.status_code, 'text': response.text}))
        return response

    def get_schedule(self) -> list:
        """
        fetches the trash holiday schedule from trash holiday service
        :return: a list of holidays and delay information
        """
        auth = self._get_auth()
        response = self._fetch_schedule(auth)
        return response.json()['data']
