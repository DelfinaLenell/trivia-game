
import random


def introduction():
    intro = input("Welcome to Trivia Game!\nWould you like to play?\n")
    if intro == "yes":
        welcome_msg = print("Let the game begin!\nYou'll have to answer al sorts of questions.\nIf you get them right you'll aquire points.\nOnce you reach 25 points, you win!\nIf you answer incorrectly points will be taken away.\nBe careful and good luck!")
        player1.game(questions)
        return welcome_msg




class Question:

    def __init__(self, subject, questions, answers, correct_answer):
        self.subject = subject
        self.questions = questions
        self.answers = answers
        self.correct_ans = correct_answer
    
    def __repr__(self):
        return("\n{question} \n{answers}".format(question = self.questions, answers = self.answers))
        
 

            
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
    
    
    def game(self, question):
        #answer_question = input()
        for i in question:
            print(i)
            answer_question = input()
            if answer_question == i.correct_ans:
                print("Correct Answer!")
                if self.score <= 25:
                    self.score += 2
                    print("You're current score is {score}".format(score = self.score))
                else:
                    print("You've won the game!")
            else:
                self.score -= 2
                print("Incorrect answer!\nYou're score is {score}".format(score = self.score))
                if self.score < 0:
                    print("You have lost the game.\nTry again next time!")
                    break
                
                

question1_history = Question("History", "Who was president of the united states in 1962?", ["a : Jonh F Kennedy", "b : Richard Nixon", "c : Harry H Truman", "d : George W Bush"], "a")
question2_history = Question("History", "What was the name of the group formed to mantain peace after WW1?", ["a : United Nations", "b : League of Nations", "c : NATO", "d : Commonwealth of Nations"], "b")
question3_history = Question("History", "Who was the last Tsar of Russia?", ["a : Peter II", "b : Alexander II", "c : Nicholas II", "d : Ivan II"], "c")
question4_history = Question("History", "Who is attributed with creation of the Atomic Bomb?", ["a : Albert Einstein", "b : Richard Feynman", "c : Robert J Oppenheimer", "d : Edward Teller"], "c")
question5_history = Question("History", "Which country was the first one to be invaded by Japan?", ["a : Hong Kong", "b : Manchuria", "c : French Indochina", "d : Korea"], "d")
question6_history = Question("History", "What year did the Cold War start?", ["a : 1945", "b : 1955", "c : 1947", "d : 1951"], "c")
question1_films = Question("Films", "Who directed the film Apocolypse Now?", ["a : Stanley Kubrick", "b : Francis Ford Coppola", "c : Oliver Stone", "d : Martin Scorsese"], "b")
question2_films = Question("Films", "What movie was the first film by director Steven Spielberg?", ["a : Jaws", "b : Close Encounters of the Third Kind", "c : Duel", "d : Not on this list"], "c")
question3_films = Question("Films", "For which of these movies did Jack Nicholson won the Oscar?", ["a : As Good as It Gets", "b : Chinatown", "c : The Shining", "d : The Departed"], "a")
question4_films = Question("Films", "Which of the following actors has won the most amount of Academy Awards?", ["a : Jack Nicholson", "b : Marlon Brando", "c : Ingrid Bergman", "d : Kathrine Hepburn"], "d")
question5_films = Question("Films", "Which of the following films won best original screenplay in the 2015 Orcars?", ["a : Nightcrawler", "b : Boyhood", "c : Birdman", "d : THe Grand Budapest Hotel"], "c")
question6_films = Question("Films", "Which of these films are not part of Takashi Miike's filmography?", ["a : Blade of the Immortal", "b : Harakiri", "c : 13 Assasins", "d : Audition"], "b")
question1_geography = Question("Geography", "What country was not a part of the Soviet Union?", ["a : Armenia", "b : Belarus", "c : Yugoslavia", "d : Latvia"], "c")
question2_geography = Question("Geography", "Which directions do latitud lines run on a globe?", ["a : West to East", "b : North to South", "c : South to North", "d : East to West"], "d")
question3_geography = Question("Geography", "How many time zones does Australia have?", ["a : 1", "b : 3", "c : 4", "d : 5"], "b")
question4_geography = Question("Geography", "What's the smallest country in the world?", ["a : Monaco", "b : Vatican", "c : Palau", "d : Nauru"], "b")
question5_geography = Question("Geography", "What's the tallest mountain in Europe?", ["a : Mount Elbrus", "b : Mont Blanc", "c : Mount Shkhara", "d : Monte Rosa"], "a")
question6_geography = Question("Geography", "Which of these countries border with Equatorial Guinea", ["a : Reoublic of Congo", "b : Malawi", "c : Papua New Guinea", "d : Gabon"], "d")

questions = [question1_history, question1_films, question1_geography, question2_history, question2_films, question2_geography, question3_history, question3_films, question3_geography, question4_history, question4_films, question4_geography, question5_history, question5_films, question5_geography, question6_history, question6_films, question6_geography]
#random_questions = random.choice(questions)
player1 = Player("Leo")
introduction()


