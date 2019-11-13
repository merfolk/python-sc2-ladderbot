import sc2


class ExampleBot(sc2.BotAI):
    def __init__(self):
        super().__init__()
        self.name: str = "ExampleBot"
        self.race: str = sc2.Race.Random
        self.ai = self

    async def on_step(self, iteration):
        # On first step, send all workers to attack enemy start location
        if iteration == 0:
            print("Game started")
            for worker in self.workers:
                self.do(worker.attack(self.enemy_start_locations[0]))

    def on_end(self, result):
        print("OnGameEnd() was called.")
