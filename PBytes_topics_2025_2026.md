# From the 2025/2026 school year


MS abbreviates "middle school"
SM abbreviates "Stand-up Maths"
MP is Meru Prastarah, also known as the Pascale Triangle
SG is the Serpienski Gasket


## From Idea To Calculation To Code to Experiment to Project


Some of these resonate with material in the "Puzzles" section.


- Ms. Halfway
    - Careful use of three markers: initialize h = 0, m0 = 0, m1 = 1
    - 1/2-arrival is the average of m0 and m1 (teach as an aside, then apply)
    - The last aspect is getting the update order correct
        - h should be the average of m0 and m1
        - m1 should be updated before m0: Why?
            - m0 will be updated to be h: m0 = h
            - The concept of m1 actually depends on (new) h and (old) m0...
                - ...so calculate m1 before changing m0
        - Where does Ms. 2/7 wind up? Ms. a/b?
    - Leads to Chaos Game
        - With an interesting underlying explanation
        - Advanced coding: Roll all 3 possibilities (All The Myriad Ways)
        - Hausdorf dimension
- Draw the XOR universe (turtle)
    - This is probably easier to do starting with 3 cells > 1 cell
        - It avoids the jiggle back and forth finesse; maybe saves time
- `requests`
- `music21`


## Coding Mechanics


### Coding unto itself


- Execution flow is top down; but sometimes this rule breaks
    - Loops break this
    - Conditional logic breaks this
    - Functions are read but not run until called
    - Indented code blocks are called just that: *blocks* or (formally) a *suite*.
- Indentation syntax ~ multiple lines as a group activity
    - This suggests functions
- The turtle library cheat sheet
    - `turtle.Screen`
    - `tracer(0, 0)` and `update()`
    - `turtle.Turtle()`
    - `t.towards(x, y)` and `t[0].towards(t[1])`
    - `t.setheading(direction)` and composition `(randint(etc))`
    - `t.dot(25)`, `t.penup()`, `t.pendown()`
    - `t.pencolor("blue")`
    - turtle.done() is the means of avoiding blip-draw-gone syndrome


### Short exercises that emphasize code mechanics and syntax


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
- What is the graph of the state space of a hexahexaflexagon?
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

    
