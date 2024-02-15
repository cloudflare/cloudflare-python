# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    BookmarkGetResponse,
    BookmarkDeleteResponse,
    BookmarkUpdateResponse,
    BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookmarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        bookmark = client.access.bookmarks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.bookmarks.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.bookmarks.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.bookmarks.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        bookmark = client.access.bookmarks.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.bookmarks.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.bookmarks.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.bookmarks.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, client: Cloudflare
    ) -> None:
        bookmark = client.access.bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            bookmark,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, client: Cloudflare
    ) -> None:
        response = client.access.bookmarks.with_raw_response.access_bookmark_applications_deprecated_list_bookmark_applications(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(
            Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            bookmark,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, client: Cloudflare
    ) -> None:
        with client.access.bookmarks.with_streaming_response.access_bookmark_applications_deprecated_list_bookmark_applications(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(
                Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
                bookmark,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bookmark = client.access.bookmarks.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.bookmarks.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.bookmarks.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.bookmarks.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncBookmarks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.access.bookmarks.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.bookmarks.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.bookmarks.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkUpdateResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.bookmarks.with_raw_response.update(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.access.bookmarks.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.bookmarks.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.bookmarks.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.bookmarks.with_raw_response.delete(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        bookmark = (
            await async_client.access.bookmarks.access_bookmark_applications_deprecated_list_bookmark_applications(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            bookmark,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.bookmarks.with_raw_response.access_bookmark_applications_deprecated_list_bookmark_applications(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(
            Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
            bookmark,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_bookmark_applications_deprecated_list_bookmark_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.bookmarks.with_streaming_response.access_bookmark_applications_deprecated_list_bookmark_applications(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(
                Optional[BookmarkAccessBookmarkApplicationsDeprecatedListBookmarkApplicationsResponse],
                bookmark,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.access.bookmarks.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.bookmarks.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.bookmarks.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkGetResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.bookmarks.with_raw_response.get(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )
