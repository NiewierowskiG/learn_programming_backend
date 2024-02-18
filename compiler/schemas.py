from typing import Union, Optional, Literal
from pydantic import BaseModel


class CompilerSchema(BaseModel):
    text: str
    language_name: str


class LanguageCompileData(BaseModel):
    compile_code: str
    expected_result: str
    language: Literal['js', 'python', 'c']


class LanguageCompileDataResponse(BaseModel):
    error: bool
    message: str
