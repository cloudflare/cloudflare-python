# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .query_result import QueryResult

__all__ = ["DatabaseQueryResponse"]

DatabaseQueryResponse: TypeAlias = List[QueryResult]
