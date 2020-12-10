from turtle import Turtle

class Announcer(Turtle):
	"""A class to announce when a player scores."""

	def __init__(self):
		"""Initialize announcer."""
		super().__init__()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 0)

	def announce_point(self):
		"""Announce that a player scored."""
		self.write("Point!", align="center", font=("Courier", 24, "normal"))

	def announce_dominating(self):
		"""Announce that a player is dominating."""
		self.write("Dominating!", align="center", font=("Courier", 24, "normal"))

	def clear_announcement(self):
		"""Clear announcement."""
		self.clear()
