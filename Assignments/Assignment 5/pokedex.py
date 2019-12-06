import argparse
import asyncio
import string
import aiohttp
from data_models import Pokemon, Ability, Move, Stat


class PokemonDataParser:

    @staticmethod
    def build_url(mode, name_or_id):
        return "https://pokeapi.co/api/v2/{}/{}/".format(mode, name_or_id)

    @staticmethod
    async def get_data(request: string,
                       session: aiohttp.ClientSession) -> dict:
        response = await session.request(method="GET", url=request)
        json_dict = await response.json()
        return json_dict

    @staticmethod
    async def process_requests_tasks(requests: list) -> list:
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(
                PokemonDataParser.get_data(request, session))
                for request in requests]
            responses = await asyncio.gather(*tasks)
            return responses

    @staticmethod
    def create_pokemon(response, is_expanded):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'height': response['height'], 'weight': response['weight'],
                  'types': [type['type']['name'] for type in
                            response['types']]}
        if is_expanded:
            abilities_requests = [ability['ability']['url'] for
                                  ability in response['abilities']]
            abilities_responses = asyncio.run(
                PokemonDataParser.process_requests_tasks(abilities_requests))
            moves_requests = [move['move']['url'] for
                              move in response['moves']]
            moves_responses = asyncio.run(
                PokemonDataParser.process_requests_tasks(moves_requests))
            stats_requests = [stat['stat']['url'] for stat in
                              response['stats']]
            stats_responses = asyncio.run(
                PokemonDataParser.process_requests_tasks(stats_requests))
            kwargs['stats'] = [PokemonDataParser.create_stat(stat) for stat in
                               stats_responses]
            kwargs['abilities'] = [PokemonDataParser.create_ability(ability)
                                   for ability in abilities_responses]
            kwargs['moves'] = [PokemonDataParser.create_move(move) for move in
                               moves_responses]
        else:
            kwargs['stats'] = [f'{stat["stat"]["name"]}: {stat["base_stat"]}'
                               for stat in response['stats']]
            kwargs['abilities'] = [f'{ability["ability"]["name"]}'
                                   for ability in response['abilities']]
            kwargs['moves'] = [f'{move["move"]["name"]}: learnt at lvl ' \
                               f'{move["version_group_details"][0]["level_learned_at"]}'
                               for move in response['moves']]

        return Pokemon(**kwargs)

    @staticmethod
    def create_ability(response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'pokemon': [pokemon['pokemon']['name'] for pokemon in
                              response['pokemon']]
                  }
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['effect'] = effect_entry['effect']
                kwargs['short_effect'] = effect_entry['short_effect']
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
        return Move(**kwargs)

    @staticmethod
    def create_stat(response):
        kwargs = {'id': response['id'], 'name': response['name'],
                  'is_battle_only': response['is_battle_only'],
                  'base_stat': response["base_stat"]
                  }
        return Stat(**kwargs)


class Request:
    def __init__(self):
        self.mode = None
        self.name_or_id = None
        self.output_file = None
        self.expanded = None

    def __str__(self):
        return f'{self.mode}, {self.name_or_id}, {self.expanded}, {self.output_file}.'


class RequestHandler:
    def __init__(self):
        self.request = Request()
        self.response = None

    def get_request(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('mode', choices=("pokemon", "ability", "move"),
                            help='The mode to run the program, api request '
                                 'will be made base on mode.')
        parser.add_argument('name_or_id', help='Input of the program, either a'
                                               'string that represents a name'
                                               ' or id of a mode, or a file '
                                               'path that contains name or id '
                                               'information.')
        parser.add_argument('--expanded', action='store_true',
                            help='The argument to specify if the api response'
                                 ' is return in expanded context.')
        parser.add_argument('--output', help='Output of the program, it is '
                                             'specified when a output file is'
                                             ' requested.')

        try:
            args = parser.parse_args()
            request = Request()
            request.mode = args.mode
            request.name_or_id = args.name_or_id
            request.expanded = args.expanded
            request.output_file = args.output
            self.request = request
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()

    def process_request(self):
        if self.request.name_or_id.endswith('.txt'):
            # read from input file
            with open(self.request.name_or_id, 'r') as file:
                names_or_ids = file.readlines()
                urls = [PokemonDataParser.build_url(
                    self.request.mode, name_or_id.strip('\n')).lower()
                        for name_or_id in names_or_ids]
            print(urls)
        else:
            # read from input string
            urls = [PokemonDataParser.build_url(self.request.mode,
                                                self.request.name_or_id)]
        responses = asyncio.run(
            PokemonDataParser.process_requests_tasks(urls))
        self.response = responses

    def execute_response(self):
        for response in self.response:
            output = None
            if self.request.mode == 'ability':
                output = PokemonDataParser.create_ability(response)
            elif self.request.mode == 'pokemon':
                output = PokemonDataParser.create_pokemon \
                    (response, self.request.expanded)
            elif self.request.mode == 'move':
                output = PokemonDataParser.create_move(response)
            if not self.request.output_file:
                # print to console
                print(output)
            else:
                with open(self.request.output_file, 'a') as file:
                    file.write(str(output))


def main():
    try:
        request_handler = RequestHandler()
        request_handler.get_request()
        print(request_handler.request)
        request_handler.process_request()
        request_handler.execute_response()
    except aiohttp.client_exceptions.ContentTypeError:
        print('Invalid input.')
        quit()


if __name__ == '__main__':
    main()
