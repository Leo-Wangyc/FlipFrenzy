class Game_card:
    def __init__(self, id, fruit):
        self._id = id
        self._value = fruit['value']
        self._text = fruit['text']
        self._is_click = False
        self._is_matched = False

    def __str__(self):
        return self._text

    def card_info(self):
        return {
            'id': self._id,
            'value': self._value,
            'text': self._text,
            'is_click': self._is_click,
            'is_matched': self._is_matched,
        }

    def flip_over(self):
        self._is_click = True

    def flip_down(self):
        self._is_click = False

    def card_matched(self):
        self._is_matched = True