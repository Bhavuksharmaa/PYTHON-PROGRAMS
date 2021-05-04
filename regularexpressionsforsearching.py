import re
mystr = '''ar
Business Email
Business Letters
Business Reports
Business Writing Skills
Business Writing Tutoring and Coaching
PowerPoint + Training
 fiaoi@ajjf.com
Proofreading and Editing
Training Writing Trainers
Workshop PowerPoint
Writing Evaluations
Writing for Nonnative Speakers
Writing in Special Areas
ABOUT US
Testimonials
Our Clients, ueieiui@hfjaj.com
Awards and Recognition
About the Instructor
CONTACT US
Toll free: 800-827-3770
 961738539@gmail.com
Outside the U.S.: +1-309-452-2831 
Email: register@businesswriting.com'''
pattern = re.compile(r".com")
matches = pattern.finditer(mystr)

for match in matches:
    i = match.start()
    while True:
        i = i - 1
        if mystr[i] == (" "):
            with open("C:\\Users\\dell\\PycharmProjects\\emailfile", "a") as f :
                f.write("email is :")
                f.write(mystr[i:match.start()+4])
                print(mystr[i:match.start()+4])
                f.write("\n")

            break



