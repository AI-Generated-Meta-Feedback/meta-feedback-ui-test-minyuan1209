function sortBooks(bookList):
    # bookList is a list of (shelfNumber, returnOrder)
    
    for i from 1 to length(bookList) - 1:
        key = bookList[i]
        j = i - 1
        
        # Move elements that have greater shelfNumber than key.shelfNumber
        # one position ahead of their current position
        while j >= 0 and (
            bookList[j].shelfNumber > key.shelfNumber
        ):
            bookList[j + 1] = bookList[j]
            j = j - 1
        
        # Since we use a stable sort, we do not move books
        # with the same shelfNumber (preserves returnOrder)
        bookList[j + 1] = key
    
    return bookList

