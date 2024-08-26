# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["ResultWrapper"]

_T = TypeVar("_T")


class ResultWrapper(GenericModel, Generic[_T]):
    result: _T

    @staticmethod
    def _unwrapper(obj: "ResultWrapper[_T]") -> _T:
        return obj.result
