from dotenv import load_dotenv
import os
import requests
import urllib.parse
import argparse


def shorten_link(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    params = {"long_url": bitlink, "domain": "bit.ly"}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=params
    )
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'unit': 'week', 'units': '-1'}
    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}",
        headers=headers
    )
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Создаёт Битлинк")
    parser.add_argument('url', help='Ваша ссылка')
    args = parser.parse_args()
    bitly_token = os.getenv("BITLY_TOKEN")
    url_parts = urllib.parse.urlparse(args.url)
    extracted_link = f'{url_parts.netloc}{url_parts.path}'
    try:
        if is_bitlink(bitly_token, extracted_link):
            print(
                'Количество кликов по bit.ly ссылке:',
                count_clicks(bitly_token, extracted_link)
            )
        else:
            print('Битлинк:', shorten_link(bitly_token, args.url))
    except requests.exceptions.HTTPError:
        print('Ошибка: requests.exceptions.HTTPError')


if __name__ == "__main__":
    main()
