----------------------------ReadMe----------------------------

The program takes in command line arguments:
{"pokemon" | "ability" | "move"} {"filename.txt" | "name or id'} [--expanded] [--output "filename.txt"]

Based on command line arguments, API calls are made at https://pokeapi.co/api/v2/

Program can be run in 3 modes: pokemon, ability, move.
Name or id of a pokemon, ability, move can be specified by a string or a txt file that contains them.
Pokemon has expanded mode which contains more comprehensive information on its ability, move, stat.
Output can be printed to console or written to a specified output txt file.