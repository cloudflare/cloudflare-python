# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    "CursorLimitPaginationResultInfo",
    "SyncCursorLimitPagination",
    "AsyncCursorLimitPagination",
    "SyncSinglePage",
    "AsyncSinglePage",
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
            if self.result.items is not None:
                items = self.result.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncV4PagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: Optional[V4PagePaginationResult[_T]] = None
    result_info: Optional[V4PagePaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = None
        if self.result is not None:
            if self.result.items is not None:
                items = self.result.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


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
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


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
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class CursorPaginationResultInfo(BaseModel):
    count: Optional[int] = None

    cursor: Optional[str] = None

    per_page: Optional[int] = None


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[CursorPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            if self.result_info.cursor is not None:
                cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[CursorPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            if self.result_info.cursor is not None:
                cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class CursorLimitPaginationResultInfo(BaseModel):
    count: Optional[int] = None

    cursor: Optional[str] = None

    per_page: Optional[int] = None


class SyncCursorLimitPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[CursorLimitPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            if self.result_info.cursor is not None:
                cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorLimitPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    result_info: Optional[CursorLimitPaginationResultInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = None
        if self.result_info is not None:
            if self.result_info.cursor is not None:
                cursor = self.result_info.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class SyncSinglePage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncSinglePage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None
