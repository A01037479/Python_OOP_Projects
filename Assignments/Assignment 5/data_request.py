import asyncio
import string

import aiohttp
from data_models import Pokemon, Ability, Move


class DataParser:
    url = "https://pokeapi.co/api/v2/{}/{}/"

    @classmethod
    async def get_data(cls, data_model_name: string, request_name: string,
                       session: aiohttp.ClientSession) -> dict:
        target_url = cls.url.format(data_model_name, request_name)
        response = await session.request(method="GET", url=target_url)
        # print("Response object from aiohttep:\n", response)
        # print("Response object type:\n", type(response))
        json_dict = await response.json()
        return json_dict

    @classmethod
    async def process_single_request_task(cls, data_model_name: string,
                                          request_name: string) -> list:
        async with aiohttp.ClientSession() as session:
            coroutine = cls.get_data(data_model_name, request_name, session)
            async_task = asyncio.create_task(coroutine)
            response = await async_task
            return response

    @classmethod
    async def process_requests_tasks(cls, requests: list) -> list:
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(cls.get_data(*request, session))
                     for request in requests]
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(response)
            return responses

    @staticmethod
    def create_pokemon(response):
        return Pokemon(**kwargs)

    @staticmethod
    def create_ability(response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'pokemon': [pokemon['pokemon']['name'] for pokemon in
                              response['pokemon']]}
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['effect'] = effect_entry['effect']
                kwargs['short_effect'] = effect_entry['short_effect']
        print(kwargs)
        return Ability(**kwargs)

    @staticmethod
    def create_move(response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'accuracy': response['accuracy'], 'pp': response['pp'],
                  'power': response['power'], 'type': response['type']['name'],
                  'damage_class': response['damage_class']['name']
                  }
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['short_effect'] = effect_entry['short_effect']
        print(kwargs)
        return Move(**kwargs)


def main():
    request = ['ability', 'magic-guard']
    response = asyncio.run(DataParser.process_single_request_task(*request))
    ability = DataParser.create_ability(response)
    print(ability)

    request = ['move', 'pound']
    response = asyncio.run(DataParser.process_single_request_task(*request))
    move = DataParser.create_move(response)
    print(move)

    requests = [['ability', 'magic-guard'], ['pokemon', 'ditto'],
                ['move', 'pound']]
    # responses = asyncio.run(DataRequester.process_requests_tasks(requests))


if __name__ == '__main__':
    main()
