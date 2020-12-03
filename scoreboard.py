from turtle import Turtle

class Scoreboard(Turtle):
	"""A class to report scoring information."""

	def __init__(self):
		"""Initialize scoreboard."""
		super().__init__()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 260)
		self.write("0  0", align="center", font=("Courier", 24, "normal"))
		self.score_a = 0
		self.score_b = 0
		self.consecutive_points = {
			'a': 0,
			'b': 0,
			}

	def increment_a(self):
		"""Give point to player a."""
		self.score_a += 1
		self._update_score()
		self._update_consecutive_points('a')

	def increment_b(self):
		"""Give point to player b."""
		self.score_b += 1
		self._update_score()
		self._update_consecutive_points('b')

	def _update_score(self):
		"""Update score on screen."""
		self.clear()
		self.write("{}  {}".format(self.score_a, self.score_b),
			align="center", font=("Courier", 24, "normal"))

	def _update_consecutive_points(self, player):
		"""Count the consecutive points."""
		if player == 'a':
			self.consecutive_points['a'] += 1
			self.consecutive_points['b'] = 0
		elif player == 'b':
			self.consecutive_points['a'] = 0
			self.consecutive_points['b'] += 1

	def get_consecutive_points(self):
		"""Return the current consecutive points."""
		for points in self.consecutive_points.values():
			if points:
				return points
		return 0
