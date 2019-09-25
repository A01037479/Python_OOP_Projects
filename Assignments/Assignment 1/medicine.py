class Medicine:
    medicine_dict = {'1': 'Essence of Nightshade',
                     '2': 'Milk of the poppy',
                     '3': 'Shade of the Evening'}

    @staticmethod
    def feed(pet):
        pet.reset_health()
        pet.recover_health_status()
