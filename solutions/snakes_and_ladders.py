class SnakesLadders:

    def __init__(self):
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
        self.snakes = {99: 80, 95: 75, 92: 88, 89: 68, 74: 53, 64: 60, 62: 19, 49: 11, 46: 25, 16: 6}
        self.p_1_pos = 0
        self.p_2_pos = 0
        self.turn = "p_1"

    def play(self, die1, die2):
        if self.p_1_pos == 100 or self.p_2_pos == 100:
            return "Game over!"
        if self.turn == "p_1":
            self.p_1_turn(die1, die2)
            if self.p_1_pos == 100:
                return "Player 1 Wins!"
            return f"Player 1 is on square {self.p_1_pos}"
        elif self.turn == "p_2":
            self.p_2_turn(die1, die2)
            if self.p_2_pos == 100:
                return "Player 2 Wins!"
            return f"Player 2 is on square {self.p_2_pos}"

    def p_1_turn(self, die1, die2):
        self.p_1_move(die1, die2)
        if die1 != die2:
            self.turn = "p_2"

    def p_1_move(self, die1, die2):
        self.p_1_pos += die1 + die2
        if self.p_1_pos > 100:
            self.p_1_pos = 200 - self.p_1_pos
        self.p_1_check_position_modifiers()

    def p_1_check_position_modifiers(self):
        if self.p_1_pos in self.ladders.keys():
            self.p_1_pos = self.ladders.get(self.p_1_pos)
        if self.p_1_pos in self.snakes.keys():
            self.p_1_pos = self.snakes.get(self.p_1_pos)

    def p_2_turn(self, die1, die2):
        self.p_2_move(die1, die2)
        if die1 != die2:
            self.turn = "p_1"

    def p_2_move(self, die1, die2):
        self.p_2_pos += die1 + die2
        if self.p_2_pos > 100:
            self.p_2_pos = 200 - self.p_2_pos
        self.p_2_check_position_modifiers()

    def p_2_check_position_modifiers(self):
        if self.p_2_pos in self.ladders.keys():
            self.p_2_pos = self.ladders.get(self.p_2_pos)
        if self.p_2_pos in self.snakes.keys():
            self.p_2_pos = self.snakes.get(self.p_2_pos)
