# localization/message_factory.py
from .en_msg import EnMessage
from .ko_msg import KoMessage


class MessageFactory:
    def __init__(self, language: str, rounds_count: int) -> None:
        """
        Initializes a MessageFactory instatnce.

        Args:
            language: The language code for the game messages (e.g., 'en', 'ko').
            rounds_count: The number of rounds played.
        """
        # Assign the message language
        if language == "en":
            self.current_language = EnMessage(rounds_count)
        else:
            # Default to Korean
            self.current_language = KoMessage(rounds_count)
