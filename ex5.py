colors = ["Blue", "Yellow", "Pink", "Red", "Orange"] # Danh sách màu mẫu
fav = input("What is your favorite color? ")

if fav in colors:
    print(f"Your colod is at index {colors.index(fav)} in my list")
else:
    print("Sorry, I could not find your color")