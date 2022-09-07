# Battle-Ship Game

The Battle-ship Game is a logic game that most people are familiar with that runs in the command-line interface. It allows a single user to play an opponent (computer) in the game of Battle_ship.

<img src = "documentation/full_battleship_game_display.png" alt="Screenshot of full battleship game">

## Design
I mapped out what I wanted to achieve with my functions on a flowchart

<img src = "documentation/project_3_flowchart.png" alt="Screenshot of Flowchart for game">

## Languages Used
The only language used on this project was Python.

## Features

## Existing Features

### Game board display
The game displays both a player board and and opponent board.
<ol>
 <li>
  Player Board
   <ul>
   <img src = "documentation/player_board.png" alt="Screenshot of player board from game">
    <li>
     The board is made up as a grid with rows labelled 1-8 and columns labelled A-H, This allows the user to see and determine where they want to strike.
    </li>
    <li>
     It displays the position of the users randomly placed ships with the "#" symbol.
    </li>
    <li>
     Shows the user where the opponent has already guessed, misses are displayed with a "-" symbol and hits are displayed with a "X" symbol.
    </li>
   </ul>
 </li>
 <li>
  Opponent Board
 </li>
  <ul>
  <img src = "documentation/opponents_board.png" alt="Screenshot of opponent board from game">
   <li>
    The Opponent board is created in the same way as the player board, the only difference is the random generated ships are hidden from the user.
   </li>
   <li>
    The board shows the user where they have guessed displaying a "-" symbol for a miss and a "X" symbol for a hit.
   </li>
  </ul>
</ol>

### User Inputs
There are 2 user inputs for the game, 1 for row selection and the other for column selection.
<ol>
 <li>
  Row Input
  <ul>
  <img src = "documentation/row_input.png" alt="Screenshot of player row input from game">
   <li>
    When the game is ran a row selection input is printed in the console for the user to type their selection.
   </li>
  </ul>
 </li>
 <li>
  Column Input
  <ul>
  <img src = "documentation/column_input.png" alt="Screenshot of player column input from game">
   <li>
    When the row selection has been made a column selection input is printed in the console for the user to type their selection.
   </li>
  </ul>
 </li>
</ol>
When both selections have been made the game will check to see if it's a hit or miss and the display whuch it is on the opponent board.

### Selection Outcome Display
<img src = "documentation/selection_outcome_display_1.png" alt="Screenshot of selection outcome display message of 'It's a hit!' 'It's a miss!' from game">

<img src = "documentation/selection_outcome_display_2.png" alt="Screenshot of selection outcome display message of 'Positioned already guessed!' from game">

When the player has made a selection of where to strike the game will display "It's a miss!", "It's a hit!" or "Positioned already guessed!" for both the player and the opponent.

### Hits counters
<img src = "documentation/hits_counters.png" alt="Screenshot of hits counters from game">

When the game is ran it will display a hit counter for both the player and the opponent so the player can see who has more hits at any given time during the game.

### Turns Counter
<img src = "documentation/turns_counter.png" alt="Screenshot of turns counter from game">

When the game is ran it will display a turns counter, this counter with start at the number of turns a player has and will show how many turns the player has remaining throughout the game.

### End of game message
<img src = "documentation/end_of_game_message.png" alt="Screenshot of End of game message from game">

When a player has used all of there turns a message will be printed to the console stating "Congratulations! You Win!", "You Lose!, Better luck next time." or "It's a Draw, Try again" depending on the outcome of the game.

## Possible Features to be implemented in the future:
<ul>
 <li>
  Allow the user to input grid size.
 </li>
 <li>
  Allow user to input ship sizes.
 </li>
 <li>
  Allow user to input number of turns game runs for.
 </li>
 <li>
  Improve on AI of the computer so the guesses are more logical instead of random.
 </li>
</ul>