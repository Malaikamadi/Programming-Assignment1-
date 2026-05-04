import asyncio
from typing import Dict

# database
books: Dict[int, Dict] = {
    1: {"title": "Python Basics", "available": True},
    2: {"title": "Data Science 101", "available": True},
    3: {"title": "Fast API 1.0", "available": True},
    4: {"title": "Object-oriented Programming", "available": True},
    5: {"title": "Software Engineering", "available": True}
}

borrowed_books: Dict[int, int] = {}  # book_id -> user_id


# Borrow book (ASYNC)
async def borrow_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)  # simulate delay

    if book_id not in books:
        return f"User {user_id}: Book does not exist"

    if not books[book_id]["available"]:
        return f"User {user_id}: Book not available"

    books[book_id]["available"] = False
    borrowed_books[book_id] = user_id

    return f"User {user_id} borrowed '{books[book_id]['title']}'"


# Return book (ASYNC)
async def return_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)

    if book_id not in borrowed_books:
        return f"User {user_id}: Book was not borrowed"

    if borrowed_books[book_id] != user_id:
        return f"User {user_id}: Not your book"

    books[book_id]["available"] = True
    del borrowed_books[book_id]

    return f"User {user_id} returned '{books[book_id]['title']}'"


# Simulate multiple users
async def main():
    tasks = [
        borrow_book(101, 1),
        borrow_book(102, 1),  
        return_book(101, 1),
        borrow_book(102, 1)   
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)



asyncio.run(main())