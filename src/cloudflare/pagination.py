# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "V4PagePaginationResult",
    "V4PagePaginationResultInfo",
    "SyncV4PagePagination",
    "AsyncV4PagePagination",
    "V4PagePaginationArrayResultInfo",
    "SyncV4PagePaginationArray",
    "AsyncV4PagePaginationArray",
    "CursorPaginationResultInfo",
    "SyncCursorPagination",
    "AsyncCursorPagination",
]

_T = TypeVar("_T")


class V4PagePaginationResult(GenericModel, Generic[_T]):
    items: Optional[List[_T]] = None


class V4PagePaginationResultInfo(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None


class SyncV4PagePagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: Optional[V4PagePaginationResult[_T]] = None
    result_info: Optional[V4PagePaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = None
        if self.result is not None:
            items = self.result.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = cast("int | None", self._options.params.get("page"))
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncV4PagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: Optional[V4PagePaginationResult[_T]] = None
    result_info: Optional[V4PagePaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = None
        if self.result is not None:
            items = self.result.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = cast("int | None", self._options.params.get("page"))
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})


class V4PagePaginationArrayResultInfo(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = None


class SyncV4PagePaginationArray(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[V4PagePaginationArrayResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = cast("int | None", self._options.params.get("page"))
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncV4PagePaginationArray(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[V4PagePaginationArrayResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = cast("int | None", self._options.params.get("page"))
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})


class CursorPaginationResultInfo(BaseModel):
    count: Optional[int] = None

    cursor: Optional[str] = None

    per_page: Optional[int] = None


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: Optional[object] = None
    result_info: Optional[CursorPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: Optional[object] = None
    result_info: Optional[CursorPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})
