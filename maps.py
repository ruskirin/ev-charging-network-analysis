import requests
import json
from decouple import config


URL_BASE = "https://maps.googleapis.com/maps/api/distancematrix/json"

def get_distance_coords(orig: tuple, dest: tuple):
    """
    Get best estimated travel distance and time from @orig to @dest based on
      historical data
    :param orig: tuple of origin (latitude, longitude)
    :param dest: tuple of destination (latitude, longitude)
    :return:
    """
    payload = {}
    headers = {}

    url = f'{URL_BASE}' \
          f'?origins={orig[0]}%2C{orig[1]}' \
          f'&destinations={dest[0]}%2C{dest[1]}' \
          f'&key={config("API_KEY")}'

    response = requests.get('GET', url, headers=headers, data=payload)
    return response.text
