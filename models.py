# Path: models.py
from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl

class DefinedTerm(BaseModel):
    name: str
    inDefinedTermSet: str
    url: Optional[HttpUrl]
    termCode: Optional[str]

class Identifier(BaseModel):
    identifier: Union[str, HttpUrl]

class Dataset(BaseModel):
    name: str
    description: str
    url: HttpUrl
    sameAs: Optional[HttpUrl]
    version: Optional[str]
    isAccessibleForFree: Optional[bool]
    keywords: List[Union[str, DefinedTerm]]
    identifier: Optional[Identifier]
    variableMeasured: Optional[str]
