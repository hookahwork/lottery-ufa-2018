#!/usr/bin/env python3
import argparse
import random
from os import path

WINNERS_NUM = 10

def get_participants() -> [(str, float)]:
    dir_path = path.dirname(path.realpath(__file__))

    with open(path.join(dir_path, 'participants.csv')) as f:
        lines = f.readlines()
    ret = []
    # Skip header row.
    for line in lines[1:]:
        card, tickets = line.strip().split(',')
        ret.append((card, float(tickets)))
    return ret

class Participant(object):
    def __init__(self, card: str, tickets: float):
        self.card = card
        self.tickets = tickets

def main():
    parser = argparse.ArgumentParser()
    # Use a certain blockhash as the random seed.
    parser.add_argument('seed', type=str, help='Use a certain bitcoin hash as the random seed.')
    args = parser.parse_args()
    random.seed(args.seed)

    # Get participants from the file
    participants_data = get_participants()
    Participants = [
        Participant(card, tickets)
        for card, tickets in participants_data
    ]
    winners = []

    assert len(Participants) > WINNERS_NUM
    # Make sure the order is deterministic so it's reproducible.
    Participants.sort(key=lambda p: p.card)

    weights = [p.tickets for p in Participants]
    winners = random.choices(Participants, weights=weights, k=WINNERS_NUM)

    assert len(winners) == WINNERS_NUM
    for i, p in enumerate(winners):
        print(p.card, p.tickets)

if __name__ == '__main__':
    main()
