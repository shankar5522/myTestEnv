# from behave import given, when, then
#
#
# @given(u'my example')
# def test_myexampl():
#     # raise NotImplementedError(u'STEP: Given my example')
#     print('My Example1111111')
#
#
# @when(u'my action')
# def test_myacti():
#     # raise NotImplementedError(u'STEP: When my action')
#     print('my myaction')
#
#
# @then(u'my validation')
# def test_myvalidation():
#     # raise NotImplementedError(u'STEP: Then my validation')
#     print('my myvalidation')

import requests
import pytest


def test_git():
    username = 'shankar5522'
    token = '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'
    login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username, token))
    print('abs')

git();
