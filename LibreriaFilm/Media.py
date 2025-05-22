class Media:

    def __init(self, name:str, y:int) ->None:

        self.title: str = name
        self.year:int = y

    
    def get_info(self) ->str:

        return f"{self.title} ({self.year})"
    


class Movie(Media):


    def __init(self, name:str, y:int, duration:int) ->None:
        super().__init(name, y)
    
        self.duration = duration


    def get_info(self) ->str:

        return f"[FILM]{super().get_info()} - Durata: {self.duration}"
    


class SerieTV(Media):

    def __init(self, name:str, y:int, seasons:int) ->None:
        super().__init(name, y)

        self.seasons = seasons


    def get_info(self) ->str:

        return f"[SERIETV]{super().get_info()} - stagioni: {self.seasons}"