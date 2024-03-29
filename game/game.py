import random
import uuid
from dixit.models import Player
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

class Game:
    guid = 1

    def __init__(self, creator_id, player_limit):
        self.game_id = self.guid
        Game.guid += 1
        self.creator_id = creator_id
        self.players = [{"id": creator_id, "score": 0, "streak": 0, "hand": []}]
        self.player_limit = player_limit
        self.card_iterator = 0
        tmp = list(range(1, 85))
        random.shuffle(tmp)
        self.deck = []
        for i in range(0, 84):
            self.deck.append(tmp[i])
        self.has_started = False
        self.has_ended = False
        self.player_turn = 0
        self.turn_details = {
            'stage': 'WAITING_FOR_START',
            'keyword': '',
            'right-card': -1,
            'other-cards': dict(),
            'votes': dict()
        }

    def already_joined(self, player_id):
        for player in self.players:
            if player['id'] == player_id:
                return True
        return False

    def add_player(self, player_id):
        if self.turn_details['stage'] == 'WAITING_FOR_START':
            if (len(self.players) == self.player_limit):
                return False
            else:
                self.players.append({"id": player_id, "score": 0, "streak": 0, "hand": []})
                print("add",len(self.players), self.player_limit)
                if len(self.players) == self.player_limit:
                    self.start_game()
        return True

    def get_participants(self):
        participants = []
        for player in self.players:
            participants.append(Player.objects.get(id=player['id']))
        return participants

    def get_stage(self):
        return self.turn_details['stage']

    def get_started(self):
        return self.has_started

    def start_game(self):
        print("start_game")
        self.has_started = True
        self.turn_details['stage'] = 'WAITING_FOR_MOVE'
        channel_layer = get_channel_layer()
        print("started")
        async_to_sync(channel_layer.group_send)(
            f'game_{self.game_id}',
            {
                "type": "game_update",
                "message" : json.dumps({"message":"message"})
            }
        )

    def is_available(self):
        return (self.turn_details['stage'] == 'WAITING_FOR_START') and self.player_limit > len(self.players)

    def get_initial_cards(self):
        cards = list()
        for i in range(self.card_iterator, self.card_iterator + 6):
            cards += self.deck[i]
        self.card_iterator += 6
        return cards

    def get_next_card(self):
        card = self.deck[self.card_iterator]
        self.card_iterator += 1
        if (self.card_iterator == 84):
            self.has_ended = True
        return card

    def make_move(self, player_id, card, keyword):
        if (self.turn_details['stage'] == 'WAITING_FOR_MOVE') and self.player_turn == player_id:
            self.turn_details['stage'] = 'WAITING_FOR_OTHER_CARDS'
            self.turn_details['keyword'] = keyword
            self.turn_details['right-card'] = card
            self.turn_details['other-cards'] = dict()

    def make_move_others(self, player_id, card):
        if (self.turn_details['stage'] == 'WAITING_FOR_OTHER_CARDS') and (self.turn_details['other-cards'] != 0):
            self.turn_details['other-cards'][card] = player_id
            if len(self.turn_details['other-cards']) == self.player_limit - 1:
                self.turn_details['stage'] = 'WAITING_FOR_VOTES'
                return True
        return False

    def vote(self, player_id, card):
        if (self.turn_details['stage'] == 'WAITING_FOR_VOTES') and (
            self.turn_details['other-cards'][card] != player_id) and (self.turn_details['votes'][player_id] != 0):
            self.turn_details['votes'][player_id] = card
        else:
            return False

    def get_scoreboard(self):
        scoreboard = dict()
        for i in range(0, self.player_limit):
            scoreboard[self.players[i][0]] = self.players[i][1]
        return scoreboard

    def get_cards_after_move(self):
        if self.turn_details['stage'] == 'TURN_RESULTS_OVERVIEW':
            cards = self.turn_details['other-cards']
            cards[self.player_turn] = self.turn_details['right-card']
            return cards
        return False

    def calc_scores(self):
        if self.turn_details['stage'] == 'TURN_RESULTS_OVERVIEW':
            addedPoints = {}
            answerSum = dict()  # TODO proveri jel treba inicijalizovati
            for vote in self.turn_details['votes']:
                answerSum[vote] += 1

            if answerSum[self.turn_details['right-card']] > 0 and answerSum[
                self.turn_details['right-card']] < self.player_limit - 1:
                self.players[self.player_turn][1] += 3
                addedPoints[self.player_turn] = 3
                if self.players[self.player_turn][1] >= 30:
                    self.turn_details['stage'] = 'GAME_OVER'

            for i in range(0, self.player_limit):
                if i == self.player_turn:
                    continue
                if self.turn_details['vote'][i] == self.turn_details['right-card']:
                    self.players[i][1] += 3
                    self.players[i][2] += 1
                    addedPoints[i] += 3
                else:
                    self.players[self.turn_details['other-cards'][self.turn_details['vote'][i]]][1] += 1
                    self.players[i][2] = 0
                    addedPoints[self.turn_details['other-cards'][self.turn_details['vote'][i]]] += 1

                if self.players[i][1] >= 30:
                    self.turn_details['stage'] = 'GAME_OVER'
            self.player_turn = (self.player_turn + 1) % self.player_limit
            return addedPoints
