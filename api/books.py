from fastapi import APIRouter


class BooksController:
    def __init__(self):
        self.router = APIRouter()

        @self.router.get("/book/{book_id}")
        def get_item(book_id: str):
            return book_id
