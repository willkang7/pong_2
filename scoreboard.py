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
		self.write("Player A: 0  Player B: 0", align="center",
			font=("Courier", 24, "normal"))
		self.score_a = 0
		self.score_b = 0

	def increment_a(self):
		"""Give point to player a."""
		self.score_a += 1
		self._update_score()

	def increment_b(self):
		"""Give point to player b."""
		self.score_b += 1
		self._update_score()

	def _update_score(self):
		"""Update score on screen."""
		self.clear()
		self.write("Player A: {}  Player B: {}".format(self.score_a,
			self.score_b), align="center", font=("Courier", 24, "normal"))
