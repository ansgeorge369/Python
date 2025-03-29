# This Python script implements a **Timed Quiz Game** on Indian history.
# Players must answer multiple-choice questions within a **10-second limit** per question.
#
# Key Features:
# 1. **Threading for Timed Input**: A separate thread runs a countdown timer.
# 2. **Randomized Questions**: Questions appear in a random order.
# 3. **Input Validation**: Ensures users enter a valid answer (A, B, C, or D).
# 4. **Automatic Time Expiry Handling**: If the player fails to answer in time, the answer is marked incorrect.
# 5. **Scoring System**: Displays the total score and correct answers after the quiz.
# 6. **Replay Option**: Players can choose to play again.
#
# Use Cases:
# - Can be adapted for **educational quizzes** and **learning platforms**.
# - Suitable for **competitive timed exams** or **trivia games**.
# - A **fun Python project** to practice threading, input handling, and randomization.

# Import necessary modules
import random  # For shuffling questions
import time  # For timing functions
import threading  # For running the countdown timer in a separate thread

# Define a time limit for each question
TIME_LIMIT = 10

# Flag to track if time has expired
timer_expired = False

# Event object to control input timing
input_active = threading.Event()

def countdown_timer():
    """Live countdown timer for answering the question."""
    global timer_expired  # Access the global variable
    
    # Loop from TIME_LIMIT down to 1
    for i in range(TIME_LIMIT, 0, -1):
        if timer_expired:  # Stop countdown if the user answers early
            break
        if not input_active.is_set():  # Only show countdown when input is NOT active
            print(f"\r⏳ Time remaining: {i} seconds... ", end='', flush=True)
        time.sleep(1)  # Wait for 1 second
    
    # If timer was not stopped, time has expired
    if not timer_expired:
        print("\n⏳ Time's up! Moving to the next question...")

def new_game():
    """Start a new quiz session."""
    global timer_expired  # Access the global flag
    
    # Store player's guesses
    guesses = []
    correct_guesses = 0

    # Shuffle questions randomly
    shuffled_questions = list(questions.items())
    random.shuffle(shuffled_questions)

    # Iterate through all shuffled questions
    for index, (question, answer) in enumerate(shuffled_questions):
        print("\n--------------------------------------------------------------")
        print(f"Question {index + 1}: {question}")  # Print the question

        # Get the original index to match options
        original_index = list(questions.keys()).index(question)

        # Display the multiple-choice options
        for option in options[original_index]:
            print(option)

        # Reset the timer flag
        timer_expired = False

        # Start the countdown timer in a separate thread
        timer_thread = threading.Thread(target=countdown_timer)
        timer_thread.start()

        # Enable input event to avoid interfering with countdown
        input_active.set()
        start_time = time.time()  # Record the start time
        
        # Take player's input
        guess = input("\nEnter your answer (A, B, C, D) within 10 seconds: ").upper()
        
        # Allow countdown updates again
        input_active.clear()

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Stop the countdown timer
        timer_expired = True
        timer_thread.join()  # Ensure the timer thread stops before proceeding

        # If the player took too long, their answer is marked as incorrect
        if elapsed_time > TIME_LIMIT:
            print("\n⏳ Time's up! Moving to the next question...")
            guess = "X"  # Mark as incorrect due to timeout

        # Store the player's answer
        guesses.append(guess)

        # Check if the answer is correct and update the score
        correct_guesses += check_answer(answer, guess)

        # Display the current score after each question
        print(f"⭐ Current Score: {correct_guesses}/{index + 1}")

    # Display final results after all questions
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    """Check if the given answer is correct."""
    if guess == answer:
        print("✅ Correct!")
        return 1  # Increase score by 1
    elif guess == "X":
        print("⏳ You ran out of time!")
        return 0
    else:
        print("❌ Incorrect!")
        return 0

def display_score(correct_guesses, guesses):
    """Display the final quiz score and results."""
    print("\n--------------------------------------------------------------")
    print("📝 RESULTS")
    print("--------------------------------------------------------------")

    # Show correct answers
    print("✅ Correct Answers: ", end="")
    for key in questions:
        print(questions[key], end="  ")
    print()

    # Show the user's guesses
    print("🧐 Your Guesses:  ", end="")
    for guess in guesses:
        print(guess, end="  ")
    print()

    # Calculate and display final score
    score = int((correct_guesses / len(questions)) * 100)
    print(f"\n🏆 Your Final Score: {score}%")

def play_again():
    """Ask the player if they want to play again."""
    response = input("\nWould you like to play again? (Y/N): ").upper()
    return response == 'Y'  # Returns True if 'Y', False otherwise

# Dictionary storing questions and their correct answers
questions = {
    "1. When did India gain independence from British rule?": "C",
    "2. Which movement was launched by Mahatma Gandhi in 1942 demanding an end to British rule?": "C",
    "3. Who was the last Viceroy of British India?": "A",
    "4. Which freedom fighter is known as the 'Iron Man of India'?": "B",
    "5. What was the main objective of the Simon Commission (1927)?": "A",
    "6. Which event marked the beginning of direct British rule in India?": "A",
    "7. Who was the first Prime Minister of independent India?": "B",
    "8. Which session of the Indian National Congress declared ‘Purna Swaraj’ (Complete Independence)?": "A",
    "9. Which Act was passed by the British in response to the Civil Disobedience Movement?": "A",
    "10. Who was the founder of the Indian National Army (INA)?": "B"
}

# Multiple-choice options for each question
options = [
    ["A. 15th August 1945", "B. 26th January 1947", "C. 15th August 1947", "D. 2nd October 1947"],
    ["A. Civil Disobedience Movement", "B. Non-Cooperation Movement", "C. Quit India Movement", "D. Swadeshi Movement"],
    ["A. Lord Mountbatten", "B. Lord Curzon", "C. Lord Wavell", "D. Lord Linlithgow"],
    ["A. Mahatma Gandhi", "B. Sardar Vallabhbhai Patel", "C. Subhas Chandra Bose", "D. Jawaharlal Nehru"],
    ["A. To propose constitutional reforms in India", "B. To divide India into two nations", "C. To negotiate with Indian leaders for independence", "D. To introduce new taxes"],
    ["A. First War of Independence (1857)", "B. Partition of Bengal (1905)", "C. Jallianwala Bagh Massacre (1919)", "D. Formation of the Indian National Congress (1885)"],
    ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. Dr. B.R. Ambedkar"],
    ["A. Lahore Session (1929)", "B. Surat Session (1907)", "C. Lucknow Session (1916)", "D. Nagpur Session (1920)"],
    ["A. Rowlatt Act (1919)", "B. Government of India Act (1935)", "C. Indian Councils Act (1909)", "D. Regulating Act (1773)"],
    ["A. Bal Gangadhar Tilak", "B. Subhas Chandra Bose", "C. Bhagat Singh", "D. Lala Lajpat Rai"]
]

# Start the game
new_game()

# Loop to allow replaying the game
while play_again():
    new_game()

print('Thanks for playing! 🎉')
