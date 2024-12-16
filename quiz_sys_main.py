class Account:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.gender = ""
        self.accountno = 0
        self.password = ""

class Quiz:
    accountcounter = 100  # Class variable

    def __init__(self):
        self.score = 0
        self.questions = []
        self.options = []
        self.correctAnswers = []
        self.acc = Account()

    def accountgenerate(self):
        Quiz.accountcounter += 1
        return Quiz.accountcounter

    def accountcreate(self):
        self.acc.accountno = self.accountgenerate()
        input()  # Clear buffer
        self.acc.name = input("Enter the name: ")
        self.acc.gender = input("Enter the Gender: ")
        self.acc.username = input("Enter Username: ")
        self.acc.password = input("Enter your Password: ")

        try:
            with open("accounts.txt", "w") as outFile:
                outFile.write(f"{self.acc.accountno},{self.acc.name},{self.acc.gender},"
                            f"{self.acc.username},{self.acc.password}\n")
        except IOError:
            print("Error opening file for writing!")
            return

        print(f"Account created successfully! Your account number is: {self.acc.accountno}")
        print(f"Thanks for creating account, {self.acc.username}")

    def login(self):
        enteredAccNo = int(input("Enter your Account Number: "))
        enteredPassword = input("Enter your Password: ")

        try:
            with open("accounts.txt", "r") as inFile:
                for line in inFile:
                    accountnoStr, name, gender, username, password = line.strip().split(',')
                    fileAccountNo = int(accountnoStr)

                    if fileAccountNo == enteredAccNo and password == enteredPassword:
                        print(f"Login successful! Welcome to the Quiz, {name}!")
                        return True
        except IOError:
            print("Error opening file for reading!")
            return False

        print("Invalid Account Number or Password!")
        return False

    def loadQuestions(self, questions):
        try:
            with open(questions, "r") as inFile:
                for line in inFile:
                    question, *options_and_answer = line.strip().split('|')
                    self.questions.append(question)
                    self.options.append(options_and_answer[:4])
                    self.correctAnswers.append(int(options_and_answer[4]))
        except IOError:
            print("Error: Could not open questions file!")

    def startQuiz(self):
        if not self.questions:
            print("No questions available. Please check the questions file.")
            return

        self.score = 0
        for i in range(len(self.questions)):
            print(f"Question {i + 1}: {self.questions[i]}")
            for j, option in enumerate(self.options[i], 1):
                print(f"{j}. {option}")

            userAnswer = int(input("Your answer (1-4): "))

            if userAnswer == self.correctAnswers[i]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: "
                      f"{self.correctAnswers[i]}. {self.options[i][self.correctAnswers[i] - 1]}\n")

        print(f"Quiz Over! Your total score: {self.score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    
    while True:
        print("\n1. Create Account\n2. Login and Start Quiz\n3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            quiz.accountcreate()
        elif choice == 2:
            if quiz.login():
                quiz.loadQuestions("questions.txt")
                quiz.startQuiz()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
