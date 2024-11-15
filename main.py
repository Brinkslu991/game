# Lucas Brinks
# 11/15/24
# guessing game
def ask_questions(question, answer):
    user_answer = input(question + ' ')
    if user_answer.lower() == answer.lower():
        return True
    else:
        return False

def run_quiz():
    questions = [
        ('what is the longest medical term?','Pneumonoultramicroscopicsilicovolcanoconiosis'),
        ('where is the largest volcano in the solar system?','Mars'),
        ('how many earths can fit in the sun?','1,300,000'),
        ('how many presidents have had a mind blowing expeiriance?','2')
    ]

    score = 0
    for q in questions:
        if ask_questions(q[0],q[1]):
            print('Correct')
            score += 1
        else:
            print('Worng')
    
    print(f'\nYour final score is: {score}/{len(questions)}')
    percentage = (score/len(questions)) * 100
    print(f'You scored: {percentage:.1f}%')
    print('Goodbye')

def main():
    print('Welcome to my quiz game')
    run_quiz()

if __name__ == '__main__':
    main()