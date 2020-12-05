# given a diagram of the tennic court with areas
# given labels, use an input string of events
# to determine game results

# Rule
# • Game always starts with Server on H1 side (lower side in the image)
# • Serve changes after every game is won
# • On 'Serve' ball should hit on any 'Q' part of the other side. Hitting on 'H' part will be considered a fault
# • While serving, if the server makes a double fault (ball should fall on his side or outside region twice), the server loses one I
# • Points scored by the current server are mentioned first, for example if server wins the first point score will be 15-0
# • At the end of a set a changeover happens ie players change sides of the court.
# • In case of game score 40-40, display Deuce. In case of Server's Advantage, display Advantage Server In case of Receiver's Advantage, display "Advantage Receiver
# • Number of sets played may not exceed 5
# In case a set is complete a set score of 7-5 will be denoted as
# 70 (first player set score)
# 50 (second player set score)
# Since the second set is about to start a score of 00 is displayed. Please read these scores vertically
# Display 0 - 0 for a new game

# +--+----------------------------+--+
# |  |             O2             |  |
# +--+----------------------------+--+
# |  |                            |  |
# |  |             H2             |  |
# |  |                            |  |
# |O2+--------------+-------------+O2|
# |  |              |             |  |
# |  |      Q3      |      Q4     |  |
# |  |              |             |  |
# |================NET===============|
# |  |              |             |  |
# |  |      Q1      |      Q2     |  |
# |  |              |             |  |
# |O1+--------------+-------------+O1|
# |  |                            |  |
# |  |             H1             |  |
# |  |                            |  |
# +--+----------------------------+--+
# |  |             O1             |  |
# +--+----------------------------+--+

# ex. Q1 Q1 means 0-15 because of two invalid
# serves in a row

# ex. Q1 Q1 Q3 Q3 Q1 Q1 Q3 Q3 Q1 Q1 Q3 Q3
# means duece because both sides continually
# missed serves
