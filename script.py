import pyautogui
import time
import random

pyautogui.FAILSAFE = False

# Read words from a file into a list
with open('words.txt', 'r') as file:
    random_words = [line.strip() for line in file]
print('PC Searches started') 
# Function to perform a Bing search with a random word on Edge
def edge_search_with_random_word():
    # Get a random word from the list
    query = random.choice(random_words)
    
    #selects & clears the searchbar
    pyautogui.moveTo(200,55)
    time.sleep(1) 
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)

    # Type the random search query and press Enter
    pyautogui.write(query)
    pyautogui.press('enter')
 
 # Add random time delay between searches 
    delay_between_searches = random.uniform(3, 7)  # Random delay between 4 and 7 seconds
    time.sleep(delay_between_searches)

# Performs PC Searches
for _ in range(34):
    edge_search_with_random_word()

print('PC Searches Finished')

pyautogui.alert('Click OK to start Mobile searches') 

# Performs Mobile Searches
pyautogui.hotkey('ctrl', 'shift', 'i')  # switches to Mobile Mode
time.sleep(1)

print('  Switched to Mobile Search Mode') 

for _ in range(24):
    edge_search_with_random_word()