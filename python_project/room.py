rooms={
       "101":None,
       "102":None,
       "103":None,
       "104":None
}
occupied=set()
while True:
    print("1. Allocated Room:")
    print("2. Vacent Room:")
    print("3. Room info:")
    print("4. Exit:")

    choice=input("enter what you choose in that option:")

    if choice =="1":
        name=input("enter the student name:")
        for room in rooms:
            if rooms[room] is None:
              rooms[room]=name
              print("rooms{room},allocated to {name}")
              break
            else:
               print("no room avalable:")
    elif choice=="2":
       room=int(input("enter the number of vacant room:"))
       if room in rooms and rooms[room]is None:
            rooms[room]=None
            print("{room}is vacant sucesfully:")
       else:
             print("{room} is not allocated")
    elif choice=="3":
           print("\nroom statuse is that:")
           for room, name in rooms.items():
               state=f"Occupied by {name}" if name else "Vacant"
               print(f"Room {room}:{state}")
    elif choice=="4":
        print("exit thank u come again ")
        break
    else:
        print("invald choice chose again bro")