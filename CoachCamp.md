# PBytes2026

## The Python picture from English

We are here to learn about rhinoceroses and sandwiches
(and on the way: tools and skills).
Let's begin with matching: The familiar World of stories to the new World of computer programming.


| Human | Computer |
| --- | --- |
| Story | Program |
| Sentences | Code |
| English | Python |
| Side Remark | Comment |
| Recipe | Function (`def`: more later) |
| Storyteller | Me/You |
| Audience | Me/You again! |


There is one more item (invisible). Human ear + brain: translates a sequence of sounds to something we understand: "The rhinoceros walked west on Elm street." Computer side: the Python interpreter. It tells us when our attempt to speak Python comes out right or not quite.


This is enough to begin with.


And now let us pick a story that begins... with a sandwich.



## Code Camp Agenda


- `https://github.com/robfatland/othermathclub`
    - Curriculum and Resources
        - Curr: `projects`
        - Curr: `syntax`
    - R: A jumble (Rob to sort)
- Review registration
    - Number of students
    - Number of classrooms?
- Start-up logistics
    - Everyone's accessible working email address...
    - Instructions for installing VSCode + Python
        - How to add a library like `matplotlib`
- Club operating logistics
    - Prep
        - Who owns the narrative?
            - OR...
                - Split the session up into section
                - lists example: paper model (fruit); indexing
                - then back on computers
        - Who owns the take home sheet?
            - Possibly multiple version > Linda the night before
    - Access to the building (Tyee admin, janitorial staff)
        - No key, too much responsibility; worked out for now
    - Student incentives: TBD
    - In-class and roving projectors
    - Post-club huddle
    - Set up the parents
    - Settle, close lids, connect
        - Touch on names, the past week, NBDProjects
    - Kinesthetics
        - Four bugs problem
    - Formal lesson
    - Code
        - Code-along
            - Need to engage their creativity
            - Example: Multiplayer was too hard; so code-along > hard part; then they have room to be creative
            - Class consensus alternative to code-along: Errors show up? Great! Let's debug
        - Intervention
        - No Big Deal Project
            - Need better guidelines
            - Resort to AI for complicated projects
            - Alternative: "Everybody"
- Coaching principles
    - Linda, Jeffrey, Matthew, Sameer, Nora, Manas
        - Demotivation happens; so the periodic walk-around
        - "The more technical help the better!"
        - Middle School kids become frustrated easily... and hints can be ineffective
        - They do not understand when they do not understand -- whatchamacallit syndrome
        - Momentum and room energy: How to make it funnier? Variations in information delivery!
        - Take a stretch break! Walk about! (Not minecraft, not YouTube)
        - J pushes back on breaks as much as "club is not burdensome": Keeping the fun means momentum.
    - Names
    - Parachute principle
    - WKWDKWYDK
- AI and other detractors
    - Thanks Matthew!
    - Do not police the students
- Celebrations
    - Early December
    - End of school year


## Rob's teaching principles


- Never ever lose your temper!
- Preparation and practice helps me understand what I am trying to communicate
- It is ok to repeat myself... in fact it is *necessary*
- 1:1 is effective
    - Engage: "Tell me your crazy plan here..."
        - Most common response is "I don't know..." 
            - Then I say "Let's come up with a crazy plan together..."
            - I can create a handwritten sheet to help the student keep going.



- Ms. Halfway
    - Introduce the `average()` function
    - Careful use of three markers: initialize h, d, x
    - x = average(h, d) skips over the non-intuitive sign changes
        - More intuitive to get to d = h and h = x
        - Order matters
    - Copy-paste to motivate loops
        - Pasting 10 times is plenty to imply 1/3
    - Where does Ms. 2/7 wind up?
    - Fibonacci is a reinforcing case of 3 variables
        - Bonus: Fib-ratios
    - Chaos Game
        - Prerequisite: turtle
        - Advanced: Follow all 3 possibilities
- XOR universe
    - Use 3 cells (not 2 with stagger)


## Flow of control


- Execution is top down and discrete...
    - Then we learn exceptions
        - Loops
        - Conditional logic
        - Functions are read but not run until called
        - Indented code *blocks* are a *suite*.
- Indentation syntax



## Short exercises emphasize code mechanics and syntax


- Input gives a string but we want an integer
- Remainder function %
- Is a number even?
- Is a number divisible by n?
- Is a number prime?
- What is n!
- Alternating sign sequence
- Printing a triangle where the start location moves backwards
- Use sleep to instill some interactivity interest
- Use time to see how long something took


## Puzzles and enlightening solutions


- Look and Say
    - "1... What is the next number?"
- Duck and Wolf
    - For MS the inner radius calculation tends to be too much
    - To this end an alternative is to match the shadow to the wolf...
        - ...where this gives us r/4 from the center
        - ...and then we can move "one feather towards the center"
            - ...now the shadow moves faster than the wolf
        - ...so it becomes a bit Argument by Enthusiasm
- Boring Worm
- Poker chip
- Gold Key
- Flipping locks
- 4 Hats and other prisoner/hat variants
- What is the graph of state space of hexahexaflexagons?
- Cellular automata
    - Begin in one dimension plus time
    - The AND, OR and XOR Universes
    - For a bit more fun make the universe closed on itself
    - There is a 3 > 1 rule that can be described using 8 bits
        - Therefore there are 256 possible rules
        - Which are interesting?
- Chocolate bar problem
    - n pieces = a cuts + 1
- Various expressions for pi
    - 1/1 - 1/3 + 1/5 - 1/7 ...
    - Average of flips until heads exceeds tails (SM)
    - Dart board unit square / unit circle
        - Speed up by not needing to use square root (see time function)
- Five foot copper pipe
    - how to work in a magnet?
    - extrapolation of dimension... what size for a 100-dimensional box?
- What is the Name of this Book?
    - Lion and Unicorn
        - Lion: Yesterday was one of my lying days. Unicorn: Me too!
        - Lion: I lied yesterday. I will lie again 2 days after tomorrow.
        - Lion: I lied yesterday. I will lie again tomorrow. (nope)
        - Lion: I lied yesterday and I will lie again tomorrow. (yep)
    - Knights and Knaves
- Knights
    - The Tour (and Reentrant)
    - The Trapped Knight (spiral board square numbering)
- Fibonacci
    - Generate the series
    - Generate the ratios: To what do they converge?
    - Generate the spiral
    - Generate Meru Prastarah and produce Fibonacci
    - Back-propagate MP + F
    - Even-odd mask of MP is the SG
    - Also matches the XOR Universe
    - What about a 2D CA? Life? 2^9 possible rules (1/2 million)
- L-Systems
    - x, y, +, -
    - Suggestion: Start with an xy+- string and write the render turtle first
        - This gets to an intermediate punchline directly
        - Then we have a landing zone for the x > y + x + y; y > x - y - x recursion
- David Hilbert's hotel
    - Strangeness of infinity
    - Pi knows where you left your house key
- The circular ring of numbers problem
- Proofs book: 2^n-1 L-Domino tiling
    - to the nature of induction proof
- Four bugs
- Gargutron
- Eye color
- Mobius derision
- Planar graphs and Platonic solids


## Poetry and Philosophy


- Ladle Rat
- Twas brillig
- Strogatz on loving the problem
- "Gardnerian" as criteria for worthy problems
- Why do this? 
    - Remind... what is it Sagan had to say?
    - Satisfactory philosophy of ignorance
- Let's talk about AI for a moment
    - equivalence to "your mom does your homework"
- Work versus Distraction
- The Unreliable Narrator and the social contract of instruction


## Aspirational topics


- Music (with `music21` and possibly `midiano`)
- Server/Client Game (with `requests`)
- Physical actuator




