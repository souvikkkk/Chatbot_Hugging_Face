class ChatMemory:
    def __init__(self, max_turns=5):
        self.history = []
        self.max_turns = max_turns

    def add(self, speaker, text):
        self.history.append(f"{speaker}: {text}")
        if len(self.history) > self.max_turns * 2:  # user + bot = 2 per turn
            self.history = self.history[-self.max_turns*2:]

    def get_context(self):
        return "\n".join(self.history)
