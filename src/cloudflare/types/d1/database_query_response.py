# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .query_result import QueryResult

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DatabaseQueryResponse"]

DatabaseQueryResponse: TypeAlias = List[QueryResult]
