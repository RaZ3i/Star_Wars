class Utils:
    @classmethod
    def get_items(cls, val: list) -> str:
        str = ""
        for i in val:
            if i == val[-1]:
                str += i
                break
            str += i + ", "
        return str

    @classmethod
    def chek_starships(cls, val: list):
        if len(val) == 0:
            return """"""
        else:
            return f"""
            <p>Starships: {Utils.get_items(val)}</p>
        """

    @classmethod
    def chek_vehicles(cls, val: list):
        if len(val) == 0:
            return """"""
        else:
            return f"""
            <p>Vehicles: {Utils.get_items(val)}</p>
        """
