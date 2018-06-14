p1accept = [20,20]
p1deny = [80,40]
p1scores = 0

p2accept = [40,80]
p2deny = [60,60]
p2scores = 0

roundnumber = 5
currentround = 1

p1strats = ['accept','accept','accept','deny']
p2strats = ['deny','accept','accept','accept']


while currentround != roundnumber:


    # Round begins with strategy

    p1r1 = p1strats[currentround - 1]
    p2r1 = p2strats[currentround - 1]


    # Execute Round...... Fight! 

    if p1r1 == 'accept':
        p1scores += p1accept[0]
        p2scores += p1accept[1]
    else:
        # Player 1 denies
        p1scores += p1deny[0]
        p2scores += p1deny[1]


    if p2r1 == 'accept':
        p1scores += p2accept[0]
        p2scores += p2accept[1]
    else:
        # Player 2 denies
        p1scores += p2deny[0]
        p2scores += p2deny[1]


    # Display scores

    print(p1scores, p2scores)

    currentround = currentround + 1






    
'''

# Round 2

p1r1 = 'accept'
p2r1 = 'accept'


# Execute Round 2...... Fight! 

if p1r1 == 'accept':
    p1scores += p1accept[0]
    p2scores += p1accept[1]
else:
    # Player 1 denies
    p1scores += p1deny[0]
    p2scores += p1deny[1]


if p2r1 == 'accept':
    p1scores += p2accept[0]
    p2scores += p2accept[1]
else:
    # Player 2 denies
    p1scores += p2deny[0]
    p2scores += p2deny[1]


# Display scores

print(p1scores, p2scores)

'''





'''
# Round 2

p1r2 = 'deny'
p2r2 = 'accept'

# Execute Round 2...... Fight! 

if p1r2 == 'accept':
    p1scores = p1scores + p1accept[0]
    p2scores = p2scores + p2accept[1]
else:
    # Player 1 denies
    p1scores = p1scores + p1deny[0]
    p2scores = p2scores + p2deny[1]


if p2r2 == 'accept':
    p1scores = p1scores + p1accept[0]
    p2scores = p2scores + p2accept[1]
else:
    # Player 2 denies
    p1scores = p1scores + p1deny[0]
    p2scores = p2scores + p2deny[1]

    
# Display scores

print(p1scores, p2scores)

'''
