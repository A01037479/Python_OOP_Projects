class Medicine:
    @staticmethod
    def feed(pet):
        pet.reset_health()
        pet.recover_health_status()