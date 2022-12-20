from typing import Optional, List
from pydantic import BaseModel


class ExplorerRigelRequest(BaseModel):
    input_text: str
    max_questions: int
