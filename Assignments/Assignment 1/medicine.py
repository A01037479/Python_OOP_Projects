class Medicine:
    """
    Static class that represents Medicine. It contains class variable:
     a dictionary of medicine types.
    """
    medicine_dict = {'1': 'Essence of Nightshade',
                     '2': 'Milk of the poppy',
                     '3': 'Shade of the Evening'}

    @staticmethod
    def feed(pet):
        """
        Takes in a Pet object.
        Restore pet's health back to 100/100 and update its health status
        back to 'Healthy'.
        :param pet: Pet (Fizz, Teemo, Yuumi)
        """
        pet.reset_health()
        pet.recover_health_status()
