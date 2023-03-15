from re import match


class Validator:
	@staticmethod
	def username(username) -> bool:
		username = username.replace(" ", "").replace("\n", "")
		if match('^[a-zA-Z0-9._]*$', username) is None:
			return False
		return True
