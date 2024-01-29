# -*- coding: utf-8 -*-

from bowling import Bowling, FirstThrow, FirstThrowNewRules
from utils import data_checking
import logging

format_write = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logfile_error = 'logfile_error.log'
logger = logging.getLogger('logger_errors')
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler(logfile_error, encoding='utf8')
file_handler.setFormatter(format_write)
logger.addHandler(file_handler)


def run(tournament, result_tournament):
    tour = []
    stats = {}
    with open(file=tournament, mode='r', encoding='utf8') as opened_file:
        for line in opened_file:
            if not line.isspace():
                tour.append(line)
            else:
                participants, winner = formatter(tour, result_tournament)
                tour.clear()
                for player in participants:
                    if player in stats:
                        stats[player]['game'] += 1
                    else:
                        stats[player] = {'game': 1, 'win': 0}
                if winner:
                    stats[winner]['win'] += 1

    console_output(stats)


def formatter(tour, result_tournament):
    winner = None
    current_score = 0
    leader_score = 0
    participants = []
    _tour = []
    for line in tour:
        if line.startswith('winner'):
            if not winner:
                continue
            line = line.replace('.........', winner) + '\n'
            _tour.append(line)
        elif line.startswith('###'):
            _tour.append(line)
        else:
            result = line.split()[1]
            name = line.split()[0]
            participants.append(name)
            try:
                current_score = get_score_new_rules(result)
            except ValueError as exc:
                logger.error(exc.args)
            line = line.rstrip() + '    ' + str(current_score) + '\n'
            if current_score > 0:
                _tour.append(line)
            if current_score > leader_score:
                leader_score = current_score
                winner = name
            current_score = 0
    for line in _tour:
        if winner:
            write_in_file(line, result_tournament)
    return participants, winner


def count_games_and_wins(tour):
    stats = {}
    for player in tour:
        name = player.split()[0]
        if name == 'winner':
            stats['winner'] = player.split()[2]
            continue
        if not player.startswith('#'):
            stats[name] = 1
    print(stats)


def write_in_file(line, result_tournament):
    with open(file=result_tournament, mode='a', encoding='utf8') as file:
        file.write(line)


def get_score_new_rules(result):
    result = list(data_checking(result))
    context = Bowling(FirstThrowNewRules(), result)
    while context.result:
        context.first_throw()
        context.second_throw()
    return context.score


def console_output(stats):
    print(f'+-------------+----------------------+-------------------+')
    print(f'|    игрок    |    сыграно матчей    |    всего побед    |')
    print(f'+-------------+----------------------+-------------------+')
    for elem in stats:
        print(f'|  {elem:9s}  |{stats[elem]["game"]:^18d}    |   {stats[elem]["win"]:^14d}  |')
    print(f'+-------------+----------------------+-------------------+')
