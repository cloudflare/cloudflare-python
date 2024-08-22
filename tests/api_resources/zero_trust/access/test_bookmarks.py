# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.zero_trust.access import Bookmark, BookmarkDeleteResponse

from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access import bookmark_create_params
from cloudflare.types.zero_trust.access import bookmark_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestBookmarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        bookmark = client.zero_trust.access.bookmarks.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.zero_trust.access.bookmarks.with_raw_response.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.bookmarks.with_streaming_response.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.create(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
              body={},
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.create(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
              body={},
          )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        bookmark = client.zero_trust.access.bookmarks.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.zero_trust.access.bookmarks.with_raw_response.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.bookmarks.with_streaming_response.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.update(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
              body={},
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.update(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
              body={},
          )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        bookmark = client.zero_trust.access.bookmarks.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.zero_trust.access.bookmarks.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = response.parse()
        assert_matches_type(SyncSinglePage[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.bookmarks.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = response.parse()
            assert_matches_type(SyncSinglePage[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.list(
              account_id="",
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        bookmark = client.zero_trust.access.bookmarks.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.zero_trust.access.bookmarks.with_raw_response.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = response.parse()
        assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.bookmarks.with_streaming_response.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = response.parse()
            assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.delete(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.delete(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bookmark = client.zero_trust.access.bookmarks.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.zero_trust.access.bookmarks.with_raw_response.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.bookmarks.with_streaming_response.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.get(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          client.zero_trust.access.bookmarks.with_raw_response.get(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
          )
class TestAsyncBookmarks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.zero_trust.access.bookmarks.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.access.bookmarks.with_raw_response.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = await response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.bookmarks.with_streaming_response.create(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = await response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.create(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
              body={},
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.create(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
              body={},
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.zero_trust.access.bookmarks.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.access.bookmarks.with_raw_response.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = await response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.bookmarks.with_streaming_response.update(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = await response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.update(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
              body={},
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.update(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
              body={},
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.zero_trust.access.bookmarks.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.access.bookmarks.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = await response.parse()
        assert_matches_type(AsyncSinglePage[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.bookmarks.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = await response.parse()
            assert_matches_type(AsyncSinglePage[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.list(
              account_id="",
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.zero_trust.access.bookmarks.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.access.bookmarks.with_raw_response.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = await response.parse()
        assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.bookmarks.with_streaming_response.delete(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = await response.parse()
            assert_matches_type(Optional[BookmarkDeleteResponse], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.delete(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.delete(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bookmark = await async_client.zero_trust.access.bookmarks.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.access.bookmarks.with_raw_response.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        bookmark = await response.parse()
        assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.bookmarks.with_streaming_response.get(
            bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            bookmark = await response.parse()
            assert_matches_type(Optional[Bookmark], bookmark, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.get(
              bookmark_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookmark_id` but received ''"):
          await async_client.zero_trust.access.bookmarks.with_raw_response.get(
              bookmark_id="",
              account_id="699d98642c564d2e855e9661899b7252",
          )