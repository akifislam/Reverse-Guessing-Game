from welcome_screen import show_welcome_screen
from userclue import get_user_clue

show_welcome_screen()

start = int(1)
end = int(999)

total_chances = 9

while(total_chances>=0):
    mid = start + (end - start) // 2
    # print(f"{start} {mid} {end}")
    print(f"Is the number {mid} ?")
    user_clue = get_user_clue()
    print("Chances Left : ",total_chances)
    total_chances-=1
    if (user_clue=="H"):
        start = mid+1
    elif (user_clue=="L"):
        end = mid - 1
    else:
        print("Thanks for Playing :) ")
        break

