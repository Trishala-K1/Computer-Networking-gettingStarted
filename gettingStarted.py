def welcome_assignment_answers(question):
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mTCP"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking'":
        answer = "883c13da6a24949c9a23231b60119e2ace58459da4f8bbdd812cc37764548bdd"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else:
        # you should understand why this else case should be included
        # what happens if there is a typo in one of the questions?
        # maybe put something here to flag an issue
        answer = " "
    return (answer)

if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What is the SHA256 hashing value to the following message: 'NYU Computer Networking'"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question))

