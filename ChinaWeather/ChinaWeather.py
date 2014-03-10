#!/usr/bin/env python
# coding:utf-8

import urllib
from bs4 import BeautifulSoup
import re
import json
import os
import functools


def cache(func):
    """cache the value in memory
    """
    table = func.cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = '{0}{1}'.format(args, kwargs)
        if key not in table:
            table[key] = func(*args, **kwargs)
        return table[key]
    return wrapper


@cache
def _get_weather_data(city):
    '''get weather data per hour for every city
    '''
    html_doc = urllib.urlopen(city).read()
    soup = BeautifulSoup(html_doc)
    alldata = {}
    for i in soup.find_all('div')[2:10]:
        tempdata = i.string.replace('\t', '').replace('\r\n', ' ').split(u'：')
        alldata[tempdata[0].strip()] = tempdata[1]
    return alldata


def get(city):
    if not city.startswith('http://'):
        city = 'http://' + city

    try:
        return _get_weather_data(city)
    except:
        return '错误： 请检查网址是否错误'
