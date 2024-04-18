class Message:
    def __init__(self, category: str, message: str):
        self.allowed_categories = ['info', 'error', 'warning', 'io']
        if category not in self.allowed_categories:
            raise ValueError(f'Category must be one of {self.allowed_categories}')
        self.type = category
        self.message = message
        self.display()

    def display(self):
        category_color = '\033[94m' if self.type == 'io' else ''  # Blue color for 'IO'
        reset_color = '\033[0m'  # Reset color to default

        print(f'{category_color}[{self.type.upper()}]{reset_color}: {self.message}')
