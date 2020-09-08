import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(2):
    quizfile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerkeyfile = open('capitals_answers%s.txt' % (quizNum + 1), 'w')

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for quesnum in range(50):
        correct = capitals[states[quesnum]]
        wrong = list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong,3)
        answeroption = wrong + [correct]
        random.shuffle(answeroption)

        quizfile.write('%s.what is the capital of %s? \n' % (quesnum + 1,states[quesnum]))
        for i in range(4):
            quizfile.write('  %s. %s\n' % ('ABCD'[i], answeroption[i]))
        quizfile.write('\n')

        answerkeyfile.write('%s. %s\n' % (quesnum + 1 , 'ABCD'[answeroption.index(correct)]))
    quizfile.close()
    answerkeyfile.close()