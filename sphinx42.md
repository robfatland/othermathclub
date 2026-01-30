# sphinx 42


This is a riddle game that emphasizes...


- basic input of strings
- formatting a web request (http POST)
- an infinite loop with an escape clause (conditional logic)
- using the `requests` library


## step 1: Create an Azure Function App


- This is done on the AWS console (or using the CLI)
- US WEST 2 is Washington state
- Sphinx refers to riddles and 42 refers to the ultimate answer to Life, the Universe and Everything


We begin by planning for 2 routes: `test` and `riddle`

- test will return a pointer to riddle
- riddle will accept a puzzle number and an answer, as in '7 Thursday'
