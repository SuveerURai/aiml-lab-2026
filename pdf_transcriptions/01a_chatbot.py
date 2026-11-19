# Question: Demonstrate a simple Chabot with minimum 10 conversations.
# Transcribed from the manual; indentation restored for Python readability.
from nltk.chat.util import Chat, reflections

pairs = [
    ['myname is (.*)', ['Hello! %1']],
    ['(hi|hello|hey|holla|hola)', ['Heythere!', 'Hithere!', 'Hey!']],
    ['(.*) your name?', ['Mynameis Geeky']],
    ['(.*) do youdo ?', ['Weprovideaplatform fortechenthusiasts, awide rangeof options !']],
    ['(.*) createdyou?', ['Geeksforgeeks createdmeusingpythonandNLTK !']],
]

chat = Chat(pairs, reflections)
chat.converse()
