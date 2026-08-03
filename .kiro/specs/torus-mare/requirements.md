# Requirements Document

## Introduction

Torus Mare is an exploration game set on a torus-shaped ocean planet. The primary educational goal is to teach middle school students (ages 11–14) how to communicate with a stateless HTTP server using the Python `requests` library. The game world is a rectangular grid that wraps horizontally and vertically, forming the topology of a torus. Students write client-side Python code to send HTTP requests to a remote server, which maintains the game state and responds with information about their surroundings. The server runs as an AWS VM or Lambda function; the client renders the grid visually.

## Glossary

- **Server**: The stateless HTTP backend deployed as an AWS Lambda function (zip packaging, Python 3.10+ runtime) fronted by API Gateway. The server process holds no in-memory state between requests; all persistent data (player positions, grid, features) resides in DynamoDB.
- **Client**: The student-written Python application that sends HTTP requests to the Server and renders the grid
- **Grid**: A two-dimensional rectangular array of cells representing the ocean planet surface
- **Cell**: A single square in the Grid, identified by integer column and row coordinates
- **Torus_Topology**: The wrapping property where the Grid's left edge connects to its right edge and the top edge connects to the bottom edge
- **Player**: A named entity occupying a single Cell on the Grid, controlled by a student via the Client
- **Requests_Library**: The Python `requests` package used by the Client to send HTTP requests to the Server
- **Viewport**: The rectangular portion of the Grid visible to the Player at any given time
- **Game_Session**: A named interaction context identified by a seven-digit Player ID (PID). The session is not held in server memory; it is a logical construct whose state (player position, registration status) is stored in the external data store and looked up on each request using the PID provided in the request body.
- **Move_Action**: An HTTP request that changes the Player position by one Cell in a cardinal direction (north, south, east, west)
- **Look_Action**: An HTTP request that retrieves information about Cells surrounding the Player
- **Feature**: A point of interest on the Grid (island, reef, whirlpool, or other landmark) that the Player can discover
- **PID**: A randomly generated seven-digit numeric Player ID issued upon solving the registration puzzle. Used to identify a Player in all subsequent requests without exposing student names.
- **AID**: A longer numeric Admin ID (exact value TBD) included in a request to invoke Admin mode operations.
- **Anonymous_Mode**: The default API mode for unauthenticated users. Allows only the number-guessing registration puzzle.
- **Player_Mode**: The API mode activated when a request includes a valid PID. Allows gameplay actions (move, look, etc.).
- **Admin_Mode**: The API mode activated when a request includes a valid AID. Allows administrative operations not available to Players.
- **Registration_Puzzle**: A "guess the number" game that a student must solve to receive a PID and join the player roster.
- **Player_Roster**: The set of all issued PIDs. Capped at 200 entries; once full, no new registrations are accepted.

## Requirements

### Requirement 1: Player Registration via Puzzle

**User Story:** As a student, I want to solve a number-guessing puzzle to earn my Player ID, so that I can join the game without giving my real name.

#### Acceptance Criteria

1. WHEN a student sends a registration request in Anonymous_Mode, THE Server SHALL initiate a Registration_Puzzle by selecting a secret integer and returning a prompt indicating the valid range
2. WHEN the student submits a guess, THE Server SHALL respond with "too high", "too low", or "correct" feedback
3. WHEN the student guesses correctly, THE Server SHALL generate a random seven-digit PID, store it in the Player_Roster in the external data store, assign the Player a random unoccupied starting Cell, and return the PID and starting position
4. THE Server SHALL generate PIDs as random seven-digit numbers (1000000–9999999) that do not collide with any existing PID in the Player_Roster
5. IF the Player_Roster already contains 200 entries when a correct guess is submitted, THEN THE Server SHALL return an error response indicating the player roster is full and no new registrations are accepted
6. THE Server SHALL not store any student names; the PID is the sole identifier for a Player in the external data store

### Requirement 2: API Access Modes

**User Story:** As a club leader, I want three access levels (Anonymous, Player, Admin), so that students can register safely, play the game, and I can manage the system.

#### Acceptance Criteria

1. WHEN a request contains no PID and no AID fields, THE Server SHALL treat the request as Anonymous_Mode and only permit Registration_Puzzle interactions
2. WHEN a request contains a valid PID field, THE Server SHALL treat the request as Player_Mode and permit gameplay actions (move, look)
3. WHEN a request contains a valid AID field, THE Server SHALL treat the request as Admin_Mode and permit administrative operations
4. IF a request contains a PID that does not exist in the Player_Roster, THEN THE Server SHALL return an error response indicating the Player ID is not recognized
5. IF a request contains an AID that does not match the configured Admin ID, THEN THE Server SHALL return an error response indicating the Admin ID is invalid
6. IF a request in Anonymous_Mode attempts a gameplay or admin action, THEN THE Server SHALL return an error response indicating that a PID or AID is required
7. IF a request contains both a PID and an AID, THE Server SHALL treat it as Admin_Mode

### Requirement 3: Admin Operations

**User Story:** As a club leader, I want administrative commands to monitor and manage the game, so that I can support students and maintain the system.

#### Acceptance Criteria

1. WHEN an Admin_Mode request is sent with imperative "nplayers", THE Server SHALL return the number of registered Players currently in the Player_Roster
2. WHEN an Admin_Mode request is sent with imperative "reset", THE Server SHALL clear the Player_Roster and regenerate the Grid, removing all player state from the external data store
3. WHEN an Admin_Mode request is sent with imperative "listplayers", THE Server SHALL return an array of all PIDs and their current positions
4. WHEN an Admin_Mode request is sent with an unrecognized imperative, THE Server SHALL return an error response listing the valid imperative values
5. THE Server SHALL validate the AID before executing any administrative imperative

### Requirement 4: Player Movement

**User Story:** As a student, I want to move my player in cardinal directions, so that I can explore the ocean grid.

#### Acceptance Criteria

1. WHEN a Move_Action specifying a direction (north, south, east, or west) is sent to the Server, THE Server SHALL update the Player position by one Cell in the specified direction and return the new position, where north decreases the row index by 1, south increases the row index by 1, west decreases the column index by 1, and east increases the column index by 1
2. WHILE the Player is at the eastern edge of the Grid, THE Server SHALL wrap a Move_Action in the east direction to the western edge of the same row (Torus_Topology), setting the column index to 0
3. WHILE the Player is at the western edge of the Grid, THE Server SHALL wrap a Move_Action in the west direction to the eastern edge of the same row (Torus_Topology), setting the column index to the maximum column index
4. WHILE the Player is at the northern edge of the Grid, THE Server SHALL wrap a Move_Action in the north direction to the southern edge of the same column (Torus_Topology), setting the row index to the maximum row index
5. WHILE the Player is at the southern edge of the Grid, THE Server SHALL wrap a Move_Action in the south direction to the northern edge of the same column (Torus_Topology), setting the row index to 0
6. WHEN a Move_Action is sent without a valid PID, THE Server SHALL return an error response indicating the Player ID is not recognized
7. IF a Move_Action specifies a direction value that is not one of north, south, east, or west, THEN THE Server SHALL return an error response indicating the direction is invalid

### Requirement 5: Look Around

**User Story:** As a student, I want to see what is near my player, so that I can discover features and plan my route.

#### Acceptance Criteria

1. WHEN a Look_Action is sent to the Server, THE Server SHALL return the contents of all Cells within a 11-column by 11-row Viewport centered on the Player position
2. THE Server SHALL include in the Look_Action response: cell coordinates, cell terrain type, and any Features present in each visible Cell, using a null value for the feature field when no Feature is present
3. WHILE the Viewport extends beyond a Grid edge, THE Server SHALL wrap the visible area using Torus_Topology so that the Viewport is always fully populated with exactly 121 Cells
4. THE Server SHALL return Viewport data as a JSON array of cell objects, each containing column, row, terrain, and feature fields
5. WHEN a Look_Action is sent without a valid PID, THE Server SHALL return an error response indicating the Player ID is not recognized

### Requirement 6: Grid and World Configuration

**User Story:** As a student, I want the ocean world to have interesting features to find, so that exploration feels rewarding.

#### Acceptance Criteria

1. THE Server SHALL maintain a Grid of at least 32 columns by 32 rows
2. THE Server SHALL populate the Grid with at least 10 Features distributed across the Grid
3. THE Server SHALL assign each Cell exactly one terrain type from the set: deep_ocean, shallow_water, reef, island
4. THE Server SHALL ensure that at least 5 percent of Grid Cells are non-deep_ocean terrain

### Requirement 7: HTTP API Format

**User Story:** As a student, I want a simple and consistent HTTP interface, so that I can learn how HTTP requests and responses work.

#### Acceptance Criteria

1. THE Server SHALL expose all game actions as HTTP POST endpoints with JSON request and response bodies
2. THE Server SHALL return HTTP status code 200 for successful requests
3. WHEN a request contains a body that is not valid JSON or is missing required fields, THE Server SHALL return HTTP status code 400 and a JSON body containing an error_message field indicating the specific validation problem
4. WHEN a request references a Game_Session that does not exist, THE Server SHALL return HTTP status code 404 and a JSON body containing an error_message field
5. THE Server SHALL include a Content-Type header of application/json in all responses
6. WHEN a request is sent using an HTTP method other than POST to a game action endpoint, THE Server SHALL return HTTP status code 405 and a JSON body containing an error_message field indicating that only POST is supported
7. WHEN a request contains JSON fields not recognized by the endpoint, THE Server SHALL ignore the unrecognized fields and process the request using only the recognized fields
8. THE Server SHALL reject any request whose body exceeds 4096 bytes with HTTP status code 400 and a JSON body containing an error_message field indicating the size limit

### Requirement 8: Client Grid Rendering

**User Story:** As a student, I want to see a visual map of the ocean around my player, so that I can understand the torus world.

#### Acceptance Criteria

1. THE Client SHALL render the Viewport as a colored rectangular grid using matplotlib, with one rendered square per Cell
2. THE Client SHALL represent each terrain type with a distinct color: deep_ocean as dark blue, shallow_water as light blue, reef as orange, island as green
3. THE Client SHALL display the Player position by overlaying a marker symbol (distinct in shape from Feature symbols) on the Cell the Player occupies
4. THE Client SHALL display each Feature in the Viewport by rendering a text label showing the Feature type name within the corresponding Cell, using a symbol or annotation visually distinct from the terrain fill color
5. WHEN the Player moves, THE Client SHALL issue a Look_Action to retrieve the updated Viewport and re-render the grid within 2 seconds of receiving the Server response
6. IF the Server returns an error response or the Viewport data is missing required fields (col, row, terrain), THEN THE Client SHALL display an error message in place of the grid indicating the rendering data is unavailable

### Requirement 9: Client HTTP Communication

**User Story:** As a student, I want example code showing how to talk to the server, so that I can learn the requests library pattern.

#### Acceptance Criteria

1. THE Client SHALL use the Python Requests_Library exclusively for all HTTP communication with the Server
2. THE Client SHALL provide a helper function for each game action (register, move, and look) that accepts the required parameters for that action and returns the parsed JSON response body as a Python dictionary
3. IF an HTTP request to the Server fails with a network error or the Server does not respond within 10 seconds, THEN THE Client SHALL print an error message to stdout that includes the word "connection" and a description of which action was attempted
4. IF the Server returns an error response (HTTP status 400 or 404), THEN THE Client SHALL print the error_message value from the JSON response body to stdout
5. WHEN a helper function receives a successful response from the Server, THE Client SHALL return the parsed response as a Python dictionary without modifying the field names or values

### Requirement 10: Stateless Server Design

**User Story:** As a student, I want the server to work reliably without complex session management, so that I can focus on learning HTTP rather than debugging server state.

#### Acceptance Criteria

1. THE Server SHALL store all game state (Grid layout, Player positions, Player registration records, and Features) in DynamoDB; the Lambda function SHALL hold no player or game state in memory between invocations
2. THE Server SHALL treat each HTTP request independently, requiring no information from previous requests other than what is stored in DynamoDB and what is provided in the current request body; specifically, player identity is conveyed by the PID field in each request and resolved against DynamoDB
3. WHEN the Lambda function cold-starts, THE Server SHALL resume serving requests using DynamoDB within 30 seconds, with all previously stored game state (Player positions, Grid layout, and Features) intact
4. THE Server SHALL not require cookies or local session storage on the Client side; the Client SHALL identify itself by including the PID in each request body
5. IF DynamoDB is unavailable when processing a request, THEN THE Server SHALL return HTTP status code 503 and a JSON body containing an error_message field indicating the service is temporarily unavailable
6. THE Server SHALL ensure that concurrent requests from different Players do not corrupt shared game state; each request SHALL read and write only the state relevant to the requesting Player and the shared Grid

### Requirement 11: API Endpoint Discovery

**User Story:** As a student, I want a way to find out what endpoints the server supports, so that I can explore the API on my own.

#### Acceptance Criteria

1. WHEN a GET request is sent to the Server root path, THE Server SHALL return a JSON document listing all available endpoints with their paths, HTTP methods, and one-sentence descriptions
2. THE Server SHALL include example request and response bodies for each endpoint in the discovery document

### Requirement 12: Coordinate Serialization

**User Story:** As a student, I want coordinates to be represented consistently in all messages, so that I can write reliable parsing code.

#### Acceptance Criteria

1. THE Server SHALL represent all Cell positions as JSON objects with integer fields named "col" and "row"
2. THE Server SHALL use zero-based indexing for both col and row fields, where col ranges from 0 to grid width minus 1 and row ranges from 0 to grid height minus 1
3. THE Server SHALL ensure that serializing any valid Cell position to JSON and parsing it back produces a coordinate object with identical col and row integer values (round-trip property)
4. THE Client SHALL use the same JSON coordinate format when sending positions to the Server
5. IF the Client sends a coordinate with col or row values that are not integers or fall outside the valid Grid range, THEN THE Server SHALL return an error response indicating the coordinate values are invalid
