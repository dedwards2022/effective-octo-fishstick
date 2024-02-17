# function to calculate points earned based on number of books purchased
def points(purchased_books):
    if purchased_books == 0:
        return 0
    elif purchased_books == 2:
        return 5
    elif purchased_books == 4:
        return 15
    elif purchased_books == 6:
        return 30
    elif purchased_books >= 8:
        return 60
    else:
        return -1

# main function to prompt user for number of books purchased and display points earned        
def main():
    books = int(input("How many books have you purchased this month?\t"))
    earned = points(books)
    
    # If "earned" is greater than or equal to 0 print the number of points earned
    if earned >= 0:
        print(f"\nYou have {earned} points this month.")
    else:
        print("\nPlease enter a supported number of books.")

# Call main function        
if __name__ == "__main__":
    main()