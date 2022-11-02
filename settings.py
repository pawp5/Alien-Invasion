class Settings:
	"""A class to store all setings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game settings."""
		# Screen settings
		self.screen_width = 1280
		self.screen_height = 650
		self.bg_color = (230, 230, 230)
	
		# Ship setting
		self.ship_speed = 1.5
		self.ship_limit = 3
		
		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 100
		# fleet direction 1 reps right; -1 reps left.
		self.fleet_direction = 1