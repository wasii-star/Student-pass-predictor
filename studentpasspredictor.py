from sklearn import tree

hours_spent_studying = int(input('Enter how many hours spent studying: '))
attendance_percentage = int(input('Enter attendance_percentage: '))
previous_score = int(input('Enter previous score: '))

new_entry = [[hours_spent_studying, attendance_percentage, previous_score]]

# Features: [hours_studied, attendance_percentage, previous_score]
X = [
    [2, 60, 45],
    [5, 75, 60],
    [8, 90, 85],
    [1, 40, 30],
    [6, 80, 70],
    [3, 65, 50],
    [10, 95, 90],
    [4, 70, 55],
    [7, 85, 75],
    [2, 50, 40],
    [9, 92, 88],
    [5, 78, 65]
]

#Labels
# 0 = Fail
# 1 = Pass

Y = [
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    1
]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)


prediction = clf.predict(new_entry)

if prediction[0] == 1:
    print('Pass')
else:    
    print('Fail')
