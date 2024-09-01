[This `README.md` file](https://github.com/robfatland/othermathclub/blob/master/README.md)
[Notes on teaching](https://github.com/robfatland/othermathclub/blob/master/python/teaching%20notes/Teaching.ipynb)


# The Other Math Club and Python Bytes


## Python Bytes


These are my ideas about Python Bytes for the 2024-2025 school year. I try to
motivate everything but I also consider it all open to discussion and improvement!


For an earlier version of this material see the `python/teaching notes` folder.


### A Starting Activity


> Ms. Halfway lives in a house that is one city block from the Post Office.
> She needs to mail a letter at the Post Office but she can be rather indecisive 
> at times. She begins walking from her house (at say `0.0`) towards the Post
> Office (at say `1.0`)... but she stops when she is just halfway there. Now 
> her location is `0.5`. She decides it is too far and she will return home.
> But wouldn't you know it, she only goes halfway there when she again comes
> to a stop. Now her location is `0.25`. She turns around (now looking towards
> the Post Office) and begins walking back towards `0.5` from `0.25`... but 
> of course stops once she gets halfway there. Now her location is `0.375`. 
> She turns back to face her home once again you see how the process keeps
> repeating. Each journey is shorter and shorter; and eventually it will become
> so short that she is in effect standing in place. When this comes to pass:
> What will her location be?


This little story illustrates a mathematical idea: We are describing a
plausible sequence of events that could continue forever but with a
practical end point. The idea has nothing to do with computer programming...
but it does become tedious to calculate (plus we might make a mistake). 
So it is perfectly reasonable to let the computer do the calculation.
In so doing we are able to learn a few programming ideas along the way. 
And once we have a working program: We can use it to explore related
questions. For example: Where might Mr. Two-thirds wind up?


### Bullet point planning thoughts


- Agree on the club philosophy of operation
    - I recommend the "ideas > calculation > code > experimentation" plan
    - Suggest Units: Four-week blocks devoted to a particular topic
    - Students tend to want to code up games but note these qualifiers:
        - Games that work properly tend to require a fair amount of coding skill
            - This means that a fun idea can become very frustrating
        - Games are potentially a good direction for advanced students
        - Intent on building a game? 
            - Coaches should be involved in the process
            - Start out by writing a simplest-possible game
                - For example: Guess a number from 1 to 100
                    - Write this from the number chooser side
                    - Write this from the number guesser side
                    -Everything good? Now turn to more complicated games


- Highschool Coaches
    - Recruit coaches: Reji knows the way!
        - The HS students are signing up for a number of responsibilities
            - Two workshops
                - Workshop 1: Curriculum and methods (more on this below)
                - Workshop 2: Developing your own curriculum
            - Manage the classroom
                - Dealing with technical issues
                - Dealing with behavior issues (see below on computer games)


- Advertise the club
    - Parent's night (zoom or in person)
        - Be sure to communicate the importance of the Code of Conduct
            - Why it exists
            - Patterns we have seen
            - Limitations of the club: One day per week, many skip weeks
            - Working away from the club
                - We do not expect this; it is not a class with homework
                - Work on your own is the best way to benefit
                - We will do our best to involve projects: You and your friends
                - At the end of the year: Our goal is your self-sufficiency
    - Policy on friends: Yes if possible, shuffle if necessary (see below)
    - What if student went through the club last year and wish to participate again?
        - This usually does not happen but if it does...
            - Create a separate advanced track
            - Get one or more HS coaches to sign up to teach
            - Do some planning; and run with it


- Onboard the students who sign up
    - Students will configure a working computer
        - Do this with your parents
        - Do this before the first club meeting
        - First meeting: We will test your installation to make sure you are good to go
        - Students need Python, a development environment and the turtle graphics module
        - Simplest: install the Python IDE from [python.org/downloads](https://www.python.org/downloads/)
        - Optional, more advanced: Install Visual Studio Code (VSCode) with Python extension
        - Not recommended: Use the school-provided laptop (too slow, too many restrictions)
        - Cloud option: Create an account on [replit](https://repl.it)
            - Advantage: Nothing to install on your computer (runs in a browser)
            - Disadvantage: Probably need your own WiFi hotspot; BSD does not support
        - See the test program section below on what should work properly after installing Python
    - Students sign a code of conduct
        - Seating as directed
        - Do not engage with anything else found in the classroom
        - Return the room to how we found it: Get the ok to leave from the coach
        - Do not leave any items or any sort of a mess in the room
        - Rules of the club concerning friends
        - We do not open our computers until directed
        - We do not play computer games at the club
            - If you really need to play computer games the club will invite you to do so at home
        - The club activities will include some moving and talking
            - You agree to participate with a positive attitude
        - You agree to bring your computer to the club fully charged


- Administrative
    - Get permission from Tyee and the PTSA for the POA
    - Maintain open lines of communication
    - Check in with the Tyee teacher responsible for Python: Any interest in the club?


- Workshop 1: Teaching method and starting curriculum
    - Name tags for everyone!!
    - Three hour session: Very full as we will cover: 
        - Philosophy: Ideas > Calculation > Code > Experiments 
        - Python mechanics
            - Taught using an "in passing" approach
            - The initial technical content includes the following:
                - Flow of execution, jumps, logic, logic-driven jumps
                - Variables having 3 attributes including a mutable value
                - Arithmetic with variables includeing the modulo `%` operator
                - Information is stable
                - Random numbers
                - Programs live in files
                - Coding is a step-by-step process, there are bugs
                - Two-way communication: `input()` and `print()`
                - Our first data structure is a `string`
        - Kinesthetics
        - Self-sufficiency approach, code-along approach, hybrid approach
        - Our initial curriculum includes 3 "for sure" items and a stretch item
            - Curriculum 1: Ms.Halfway
            - Curriculum 2: Four prisoners, five hats (no coding)
            - Curriculum 3: Many roads lead to π
                - Let's include some actual pie to celebrate
            - Stretch: Curriculum 4: `requests`
        - The most difficult thing about teaching
        - Pauses and silence
        - Responding to questions
        - Using the whiteboard
        - Back-up coaching: How to engage when you are a Guide on the Side
        - Start thinking about what you would like to teach: Prep for workshop 2!

       
- Club meeting number 1
    - Name tags for everyone!!
    - As a group (lunch area): Review the Code of Conduct
    - Group photo!
    - Split up into classrooms
        - Write names of each classroom's participants for reference
    - Create a student status spreadsheet 
        - 1 student per row, columns are status
            - Student name, email, parent name, parent email, emergency contact
            - Status: The student has attended in person
            - Student's computer has passed the basic program test (see below)
            - Has the student been playing computer games?
    - Once we get all of this taken care of: Begin with Ms. Halfway
        - Notice that much of this activity does not require a computer
        
     
- Club meetings: Before winter break
    - Need an adult or HS person to act as gatekeeper at the door
    - Typically we meet 3 or 4 times before the December break
    - Each classroom has a lead Coach and supporting Coaches
    - This will correspond to the "everyone on the same page" curriculum
    - We can call this "Unit 1"
    - The stretch topic "requests" may be introduced at the very end


- Workshop 2: Creating your curriculum
    - Discussion: How has it been going? 
    - Presenting "that moment when I realized..."
    - Presenting your ideas
    - Process: Choosing an idea to road test
        - Idea
        - Kinesthetics
        - Calculation
        - Coding
        - Experiment
        
        
- Club meetings: After winter break
    - Assessment: Coaches lead: How has it been going so far?
    - Assessment: Can students create a working program from scratch?
        - What are the obstacles?
    - Introduce Project 1
    - Begin Unit 2
    
    
- Course correction
    - Based on assessment we may need to change what we are doing


### Friends


Students are very enthusiastic about participating with their friends. This can be 
very productive as they will naturally want to help one another. However some
friends-together situations become distracting or worse. I suggest making this
very clear to the students and coaches. Example item in the Code of Conduct:


*"I understand that the club will try to support friends sitting together if possible.
In those cases it is my responsibility to manage the friends-together situation so
that we are engaged and contributing. If on the other hand the Coach sees that we 
are so focused on friends behavior that the club becomes secondary: The Coach may
feel it appropriate to move us apart and I will adhere to this decision."*



### Basic program test


Students should code up the following program and run it to verify their environment 
is working. We publish this in advance (since they are installing a Python IDE) but
we want to see it work in the club space.


```
# this is not complete just yet... (9/1/2024)
import requests
import turtle

t = turtle.Turtle()
t.forward(100)
input('Hit <enter> to halt')
```



### Skill tiers


The Python Bytes (non-competitive) computing club has run each year at Tyee
Middle School in Bellevue Washington from 2018 onward. Until last year (the 2023-24 
school year) the club placed students into two 'tiers': Tier 1 was intended to 
serve students who were completely new to coding and tier 2 was oriented towards 
students who already had some coding experience. 


In this most recent year the distinction was abandoned because it tended to 
dilute our limited teaching resources. It also sometimes divided friends 
(which they do not enjoy) and it deprived the tier 1 students of potential 
help in learning the material from their more experienced peers. In 2023 we 
ran with the idea focus and assumed all students are essentially beginning 
coders.


Getting more advanced students engaged -- including the possibility of 
returning students as mentioned above -- goes to "let's solve that problem 
if and when it comes up".


### Language


We learn a languages on multiple levels; and let's suppose we are 
motivated by some need to communicate so all those levels come together.
Python as a programming language follows this pattern; so the challenge in
the club is to combine motivating ideas with a process of learning the 
basics, the mechanics of coding. It is very challenging to do this in 
a limited club time of 75 minutes per week.


The first idea or approach is to have the fundamentals clearly in mind
as coaches so we can do little mini-lessons along the way. For example
I remember that variables have three attributes, three things 
that makes them variables; and so when we first need
variables I can "call time out" and do a little mini-lesson. It will
come to me that I need to mention the three ingredients; so the students
will be introduced to value, name and type. Then we can revisit this
multiple times until it becomes second nature. 


### Teaching ideas


As noted above we hope to begin with ideas that have nothing to do with
computers or `print` statements. From there we want to think about them,
try to understand them, and possibly we want to translate the ideas into
some sort of calculation. Then and only then do we open our Python
environment to begin writing code.


Once our code works we can hopefully understand the idea better; or perhaps
answer a question. In a spirit of exploration this is intended not as the
end of the story but rather the starting point for further exploration.


### Writing code


Here are five approaches to getting students writing useful code.

- code along: Instructor writes code on the whiteboard, student copies.
Explanations as we go. Good to get started and get a working result.
Does not get the students self-sufficient
- Do it yourself: The guide merely presents a coding objective.
This might be a many-steps / iterative process. Interactively we may
introduce or review certain commands. But the idea is the students are
putting a program together under their own power. Students may work 
together or individually. Coaches try and help students avoid "just copy
what Fred does".
- Socratic: Instructor chooses a student, asks them a high-level question.
Example: After introducing Ms. Halfway ask "Where does she end up?"
Assuming the student is not sure of the answer: We resort to small leading
questions directed to this student and to other students. By means of these
small steps we eventually arrive at a plan for code that solves the problem.
Very important: No coding until the algorithm is understood.
- Kinesthetic: Activities away from the computer that enact some part of
a source idea. These work well if there is some motion involved and if there
is an opportunity to reach a non-obvious conclusion. Coaches aim for
multiple iterations and as many participating students as possible. 
- Guide On The Side: A coach who is not the primary teacher circulates
in the classroom and observes progress on screens. Suppose a student 
seems "at pause": The coach grabs a chair, places it nearby, and asks
the student "How is it going?" From there the coach engages as seems
appropriate to get the student off and running. The results of this 
process might turn into a "common theme" announcement for the room.
 