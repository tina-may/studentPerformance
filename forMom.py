#starter python code for Mommy

#import modules at the very top of your code:
import csv

#import data from CSV file
x = open('Desktop/CA Grade 5 ELA Assessment Henriquez.csv', 'rb')
yy = open('Desktop/scrap','w')
xreader = csv.reader(x, delimiter=',', quotechar='"')

def sortKids(kids):
  kidList = []
  for key, value in kids.iteritems():
    temp = (value,key)
    kidList.append(temp)
  kidList.sort(reverse=True)
  return kidList


#make a dictionary for looking up question levels:
d = {'RL5.9': [53,59], 'RL5.1': [3, 6, 15, 20, 38, 51, 54], 'RL5.2': [5, 22, 40, 52], 'RL5.3': [2, 17, 21, 50, 55], 'RL5.4': [4, 16, 18, 37, 41], 'RL5.5': [1, 36], 'RL5.6': [7, 19, 42], 'RL5.7': [39], 'RI5.7': [28, 34, 35, 46], 'RI5.5': [58], 'RI5.4': [12, 27, 30, 43], 'RI5.3': [11, 26, 33, 45], 'RI5.2': [8, 14, 25, 29, 48, 49, 56], 'RI5.1': [9, 10, 23, 24, 31, 32, 47], 'RI5.9': [59], 'RI5.8': [13, 44, 57]}
points = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 2, 51: 2, 52: 2, 53: 4, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 4}
y = d.keys()[:]
y.sort()

students = list(xreader)[2:-2]
for topic in y:
  kids_who_got_wrong = {}
  class_tot_wrong = 0
  tot_topic_questions = 0
  for student in students:
    kidname = student[0]
    i = 0
    for column in student[2:]:
      #print column + '&&'
      i += 1
      if i in d[topic] and column not in ['', ' ']:
        tot_topic_questions += 1*points[i]
        if column in ['A','B','C','D']:
          class_tot_wrong += 1
          if kidname not in kids_who_got_wrong:
            kids_who_got_wrong[kidname] = 1
          else:
            kids_who_got_wrong[kidname] += 1*points[i]
        elif points[i] > 1 and points[i] != int(column):
          class_tot_wrong += points[i] - int(column)
          if kidname not in kids_who_got_wrong:
            kids_who_got_wrong[kidname] = points[i] - int(column)
          else:
            kids_who_got_wrong[kidname] += points[i] - int(column)


  topic_percent_wrong = float(class_tot_wrong)/tot_topic_questions
  yy.write (topic + ':\n')
  yy.write ('% of indicator points answered wrong (class): ' + str(100*topic_percent_wrong) + '\n')
  yy.write('({0} points missed)/({1} total points)'.format(class_tot_wrong,tot_topic_questions) + '\n')
  for kid in sortKids(kids_who_got_wrong):
    yy.write ('  ' + kid[1] + '(' + str(kid[0]) +' points)\n')
  yy.write('\n\n\n')




x.close()
yy.close()