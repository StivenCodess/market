from Model import User, Validator


class LoginController:

	@staticmethod
	def login(username, password):
		if not Validator.username(username):
			print("invalid username")
			return False
		if not User.login(username, password):
			print("incorrect username or password")
			return False
		print(f"Logged: {username}")
		return True


class RegisterController:

	@classmethod
	def register(username, password):
		if not Validator.username(username):
			print("invalid username")
			return False
		if User.exists(username):
			print("Username already exists")
			return False
		if not User.register(username, password):
			print("Error in database")
			return False
		print("register with exit")
		return True
