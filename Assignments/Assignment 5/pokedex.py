"""
The module simulates a pokedex that takes in requests from user to retrieve
information of Pokemon, Ability or Move.
"""
import argparse
import asyncio
import string
import aiohttp
from data_models import Pokemon, Ability, Move, Stat


class PokemonDataParser:
    """
    PokemonDataParser is responsible to make requests based on user's inputs
    to retrieve information of Pokemon, Ability or Move and create corresponding
    objects.
    """
    @staticmethod
    def build_url(mode, name_or_id):
        """
        Helps forming url that make request to the pokemon api.
        :param mode:  string
        :param name_or_id: string
        :return: string
        """
        return "https://pokeapi.co/api/v2/{}/{}/".format(mode, name_or_id)

    @staticmethod
    async def get_data(request: string,
                       session: aiohttp.ClientSession) -> dict:
        """
        Retrieves data asynchronously in form of json dictionary based on a
        string request.
        :param request: string
        :param session: aiohttp.ClientSession
        :return: dict
        """
        try:
            response = await session.request(method="GET", url=request)
            json_dict = await response.json()
        except aiohttp.ContentTypeError:
            return {'invalid': True}
        else:
            json_dict['invalid'] = False
            return json_dict

    @staticmethod
    async def process_requests_tasks(requests: list) -> list:
        """
        Processes a list of requests asynchronously and return a list of
        corresponding responses.
        :param requests: list
        :return: list
        """
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(
                PokemonDataParser.get_data(request, session))
                for request in requests]
            responses = await asyncio.gather(*tasks)
            return responses

    @staticmethod
    def create_pokemon(response, is_expanded):
        """
        Creates a pokemon object based on a response retrieved.
        Pokemon object has two versions: expanded and non-expanded.
        Non-expanded version contains limited information of pokemon's move,
        ability and stats while expanded version provides more comprehensive
        information.
        :param response: dict
        :param is_expanded: boolean
        :return: Pokemon
        """
        if response['invalid'] is True:
            return '--------Invalid Pokemon--------\n'
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
            for i in range(len(stats_responses)):
                stats_responses[i]['base_stat'] = response['stats'][i][
                    'base_stat']
            for i in range(len(moves_responses)):
                moves_responses[i]['level_learned_at'] \
                    = response['moves'][i]["version_group_details"][0][
                    'level_learned_at']
            kwargs['stats'] = [PokemonDataParser.create_stat(stat)
                               for stat in stats_responses]
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
        """
        Creates an Ability object based on the response retrieved.
        :param response: dict
        :return: Ability
        """
        if response['invalid'] is True:
            return '--------Invalid Ability--------\n'
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
        """
        Creates an Move object based on the response retrieved.
        :param response: dict
        :return: Move
        """
        if response['invalid'] is True:
            return '--------Invalid Move--------\n'
        kwargs = {'id': response['id'], 'name': response['name'],
                  'generation': response['generation']['name'],
                  'accuracy': response['accuracy'], 'pp': response['pp'],
                  'power': response['power'], 'type': response['type']['name'],
                  'damage_class': response['damage_class']['name'],
                  'level_learned_at': response['level_learned_at']
                  }
        for effect_entry in response['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                kwargs['short_effect'] = effect_entry['short_effect']
        return Move(**kwargs)

    @staticmethod
    def create_stat(response):
        """
        Creates a Stat object based on the response retrieved.
        :param response: dict
        :return: Stat
        """
        kwargs = {'id': response['id'], 'name': response['name'],
                  'is_battle_only': response['is_battle_only'],
                  'base_stat': response['base_stat']
                  }
        return Stat(**kwargs)


class Request:
    """
    Request represents all the information of command line user input.
    mode is mandatory argument that user picks from 'pokemon', 'ability' or
    'move'.
    name_or_id is a mandatory argument that represents a name or id of a
    pokemon, ability or move.
    output_file is an optional argument that specify the path of output file.
    expanded is a boolean that specify if the pokemon information is expanded.
    """
    def __init__(self):
        self.mode = None
        self.name_or_id = None
        self.output_file = None
        self.expanded = None


class RequestHandler:
    """
    RequestHandler contains a Request and corresponding response.
    It retrieves user input from command line and process requests accordingly
    and execute the response.
    """
    def __init__(self):
        self.request = Request()
        self.response = None

    def get_request(self):
        """
        Retrieves request from commandline user inputs.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('mode', choices=("pokemon", "ability", "move"),
                            help='The mode to run the program, api request '
                                 'will be made base on mode.')
        parser.add_argument('name_or_id', help='Input of the program, either a'
                                               'string that represents a name'
                                               ' or id of a mode, or a file '
                                               'path that contains name or id '
                                               'information.')
        parser.add_argument('-e', '--expanded', action='store_true',
                            help='The argument to specify if the api response'
                                 ' is return in expanded context.')
        parser.add_argument('-o', '--output',
                            help='Output of the program, it is '
                                 'specified when a output file is requested.')

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

    def process_request(self):
        """
        Process the requests by making pokemon api requests and save results
        to responses.
        """
        if self.request.name_or_id.lower().endswith('.txt'):
            # read from input file
            with open(self.request.name_or_id, 'r') as file:
                names_or_ids = file.readlines()
                urls = [PokemonDataParser.build_url(
                    self.request.mode, name_or_id.strip('\n')).lower()
                        for name_or_id in names_or_ids]
        else:
            # read from input string
            urls = [PokemonDataParser.build_url(self.request.mode,
                                                self.request.name_or_id)]
        responses = asyncio.run(PokemonDataParser.process_requests_tasks(urls))
        self.response = responses

    def execute_response(self):
        """
        Prints response to console or write response to file based on requests.
        """
        for response in self.response:
            output = None
            if self.request.mode.lower() == 'ability':
                output = PokemonDataParser.create_ability(response)
            elif self.request.mode.lower() == 'pokemon':
                output = PokemonDataParser.create_pokemon \
                    (response, self.request.expanded)
            elif self.request.mode.lower() == 'move':
                output = PokemonDataParser.create_move(response)
            if not self.request.output_file:
                # print to console
                print(output)
            elif self.request.output_file.lower().endswith('txt'):
                # write to an output file
                with open(self.request.output_file, 'a') as file:
                    file.write(str(output))
            else:
                raise ValueError('Output file should be a text file.(.txt)')


def main():
    """
    Main method drives the program and simulates functionality of pokedex.
    """
    try:
        request_handler = RequestHandler()
        request_handler.get_request()
        request_handler.process_request()
        request_handler.execute_response()
    except aiohttp.ClientConnectionError:
        print(f'Internet not available.')
    except FileNotFoundError as e:
        print(f'File {e.filename} can not be found')
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
