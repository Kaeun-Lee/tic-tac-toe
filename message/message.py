from .english import English
from .korean import Korean


class Message:
    def __init__(self, language: str) -> None:
        """
        Initializes a MessageFactory instatnce.

        Arg:
            language: Language code for the game messages (e.g., 'en', 'ko').
        """
        # Assign the message language
        if language == "en":
            self.current_language = English()
        else:
            # Default to Korean
            self.current_language = Korean()
