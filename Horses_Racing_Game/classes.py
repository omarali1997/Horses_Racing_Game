class HorsesRacing:
    '''
    A class contains 
    1. setters to update attributes : 
        1.1 horse name
        1.2 horse breed
        1.3 horse points
    2. getter to get all pervious attributes.
    3. static method "win_lose" that takes two arguments : Horse and Contender
        and determine the winner depending on the breed of each them;depending on Win-lose matrix.
    4. method to increase the point of horse until it reaches 100 it will be full.
    5. racing method that takes two arguments horse of user and its contender and call win_lose method 
        and specify the result if this racing.
    6. class attribute "round_number" that counts the number of racing by increasing it inside racing method. 
    7. class method "get_round_numbers" to get the number of rounds.
    8. also __str__ and __repr__ 
    '''

    def __init__(self):
        self.name = None
        self.Breed = None  
        self.high_point = 100
        self.point = 50

    #Setters 

    def set_name(self, name):
        self.name = name

    def set_Breed(self, Breed):
        self.Breed = Breed

    def set_point(self, point):
        self.point = point

    #Getters

    def get_name(self):
        return self.name

    def get_Breed(self):
        return self.Breed

    def get_point(self):
        return self.point

    @staticmethod
    def win_lose(horse, contender):
        result_map = {0 : "lose", 1 : "win", -1 : "tie"}
        game_map = {"american": 0,"arabian": 1,  "thoroughbred": 2,'gypsy':3,'andalusian':4}
        # Win-lose matrix
        rps_table = [
            [-1, 1, 0, 1, -1], # American
            [0, -1, 1, 0, 1],  # Arabian
            [1, 0, -1, -1, 1], # Thoroughbred
            [0, 1, 0, -1, 1],  # Gypsy
            [-1, 0, 1, 0, -1]  # Andalusian
        ]
        result = rps_table[game_map[horse]][game_map[contender]]
        return result_map[result]
    
    
    def Point(self):
        if self.point < self.high_point:
            self.point += 10
            # print(f"{self.name} recovered 10 points.")
            return f"{self.name} recovered 10 points."
        else:
            # print(f"{self.name} is full.")
            return f"{self.name} is full."


    round_number=0 # Number of rounds
    def racing(self, other):
        HorsesRacing.round_number+=1
        result = self.win_lose(self.Breed, other.Breed)
        if result == 'lose':
            self.point = 0
            if other.point < other.high_point:
                other.point += 10
            else:
                print(f"{other.name} is full.")
            return f"{self.name} fainted!"
        elif result == 'tie':
            if self.point>0:
                self.point -= 10
            if other.point>0:
                other.point -= 10
            return f"{self.name} and {other.name} battled hard. It's a tie."

        elif result == 'win':
            if self.point < self.high_point:
                self.point += 10
            else:
                print(f"{self.name} is full.")
            other.point = 0
            return f"{self.name} won. Congratulations!"
        


    @classmethod
    def get_round_numbers(cls):
        return HorsesRacing.round_number

    def __str__(self):
        return f"{self.name} ({self.Breed}): {self.point}/{self.high_point}"


    def __repr__(self):
        return f"name= {self.name}, Breed= {self.Breed} point= {self.point}, high_point= {self.high_point}"