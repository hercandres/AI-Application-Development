print("\n*** Campus FAQ Chatbot ***")
print("Type 'exit' to quit.\n")

# define intents
intents = { 
    "library_hours" : {
        "keywords" : ["library", "open", "hour", "close"],
        "response" : "The library is open from 8am to 11pm, Monday through Friday."
    },
    "office_hours" :{
        "keywords" : ["office", "professor", "hours"],
        "response" : "The faculty office hours are listed on the course syllabus."
    },
    "it_support" :{
        "keywords" : ["it","help","support","computer","wifi"],
        "response" : "You can contact IT at itsupport@niagara.edu."
    },
    "campus_location" :{
        "keywords" : ["where","location","building","map"],
        "response" : "You can find campus building locations using the online campus map."
    },
    "admissions" : {
        "keywords" : ["admissions","apply","application"],
        "response" : "You can apply through the university admissions portal online."
    },
    "faculty" : {
        "keywords" : ["faculty","office","hour","syllabus"],
        "response" : "Faculty office hours are listed on the course syllabus."
    }
}

# main loop
running = True

while running:
    user_input = input("You: ").lower()

    if user_input == "exit":
        running = False
        break

    user_words = user_input.split()

    coincidence_count = {}

    # count matches
    for intent_name in intents:
        coincidence_count[intent_name] = 0

        for keyword in intents[intent_name]["keywords"]:
            if keyword in user_words:
                coincidence_count[intent_name] += 1

    # find highest match number
    max_matches = 0
    for intent_name in coincidence_count:
        if coincidence_count[intent_name] > max_matches:
            max_matches = coincidence_count[intent_name]

    # if nothing matched
    if max_matches == 0:
        print("Bot: Sorry, I did not understand your question.")
    else:
        # collect all intents with highest matches
        best_intents = []
        for intent_name in coincidence_count:
            if coincidence_count[intent_name] == max_matches:
                best_intents.append(intent_name)

        print("Bot:")
        for intent_name in best_intents:
            print(intents[intent_name]["response"])
                

