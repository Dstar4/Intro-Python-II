class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __repr(self):
        return f'Item: {self.item_name}'

    def on_take(self, item):
        # player.take_item(item)
        return f'You have picked up {item}. Behold its glory.'

    def on_drop(self, item):
        return f'You have dropped {item}.'
