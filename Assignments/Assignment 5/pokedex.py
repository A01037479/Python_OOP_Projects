import argparse
import asyncio
import string

import aiohttp
from data_models import Pokemon, Ability, Move, Stats


class PokemonDataParser:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/{}/{}/"

    async def get_data(self, data_model_name: string, request_name: string,
                       session: aiohttp.ClientSession) -> dict:
        target_url = self.url.format(data_model_name, request_name)
        response = await session.request(method="GET", url=target_url)
        json_dict = await response.json()
        return json_dict

    # async def process_single_request_task(self, data_model_name: string,
    #                                       request_name: string) -> list:
    #     async with aiohttp.ClientSession() as session:
    #         coroutine = self.get_data(data_model_name, request_name, session)
    #         async_task = asyncio.create_task(coroutine)
    #         response = await async_task
    #         return response

    async def process_requests_tasks(self, requests: list) -> list:
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.get_data(*request, session))
                     for request in requests]
            responses = await asyncio.gather(*tasks)
            return responses

    def create_pokemon(self, response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': None,
                  'height': response['height'], 'weight': response['weight'],
                  'stats': [Stats(stat['stat']['name'], stat['base_stat'],
                                  stat['stat']['url']) for stat in
                            response['stats']],
                  'types': [type['type']['name'] for type in
                            response['types']],
                  'abilities': [self.create_ability(
                      self.process_single_request_task('ability',
                                                       ability['ability'][
                                                           'name'])) for
                      ability in response['abilities']],
                  'moves': [self.create_move(
                      self.process_single_request_task('move',
                                                       move['move']['name']))
                      for move in response['moves']]}
        return Pokemon(**kwargs)

    def create_ability(self, response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'pokemon': [pokemon['pokemon']['name'] for pokemon in
                              response['pokemon']]}
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['effect'] = effect_entry['effect']
                kwargs['short_effect'] = effect_entry['short_effect']
        return Ability(**kwargs)

    def create_move(self, response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'accuracy': response['accuracy'], 'pp': response['pp'],
                  'power': response['power'], 'type': response['type']['name'],
                  'damage_class': response['damage_class']['name']
                  }
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['short_effect'] = effect_entry['short_effect']
        return Move(**kwargs)


class InputArgs:
    def __init__(self):
        self.mode = None
        self.name_or_id = None
        self.output_file = None
        self.expanded = None

    def __str__(self):
        return f'{self.mode}, {self.name_or_id}, {self.expanded}, {self.output_file}.'


class IOHandler:
    def __init__(self):
        self.input_args = InputArgs()

    def get_commandline_inputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('mode', choices=("pokemon", "ability", "move"))
        parser.add_argument('name_or_id')
        parser.add_argument('--expanded', action='store_true')
        parser.add_argument('--output')

        try:
            args = parser.parse_args()
            input_args = InputArgs()
            input_args.mode = args.mode
            input_args.name_or_id = args.name_or_id
            input_args.expanded = args.expanded
            input_args.output_file = args.output
            self.input_args = input_args
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()

    def execute_output(self):
        try:
            data_parser = PokemonDataParser()
            requests = []
            if not self.input_args.name_or_id.endswith('.txt'):
                # read from input string
                requests.append([self.input_args.mode,
                                 self.input_args.name_or_id])
            else:
                # read from input file
                pass
            responses = asyncio.run(
                data_parser.process_requests_tasks(requests))
            for response in responses:
                output = None
                if self.input_args.mode == 'ability':
                    output = data_parser.create_ability(response)
                elif self.input_args.mode == 'pokemon':
                    output = data_parser.create_pokemon(response)
                elif self.input_args.mode == 'move':
                    output = data_parser.create_move(response)
                if not self.input_args.output_file:
                    # print to console
                    print(output)
                else:
                    # write to file
                    pass
        except aiohttp.client_exceptions.ContentTypeError:
            print('Invalid input.')
            quit()


def main():
    io_handler = IOHandler()
    io_handler.get_commandline_inputs()
    print(io_handler.input_args)
    io_handler.execute_output()


if __name__ == '__main__':
    main()
