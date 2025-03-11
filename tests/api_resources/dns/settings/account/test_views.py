# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.dns.settings.account import (
    ViewGetResponse,
    ViewEditResponse,
    ViewListResponse,
    ViewCreateResponse,
    ViewDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )
        assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns.settings.account.views.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns.settings.account.views.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.create(
                account_id="",
                name="my view",
                zones=["372e67954025e0ba6aaa6d586b9e0b59"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            match="any",
            name={
                "contains": "view",
                "endswith": "ew",
                "exact": "my view",
                "startswith": "my",
            },
            order="name",
            page=1,
            per_page=5,
            zone_id="ae29bea30e2e427ba9cd8d78b628177b",
            zone_name="www.example.com",
        )
        assert_matches_type(SyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns.settings.account.views.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns.settings.account.views.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns.settings.account.views.with_raw_response.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns.settings.account.views.with_streaming_response.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.delete(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.delete(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dns.settings.account.views.with_raw_response.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns.settings.account.views.with_streaming_response.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.edit(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.edit(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        view = client.dns.settings.account.views.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.settings.account.views.with_raw_response.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.settings.account.views.with_streaming_response.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.get(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.dns.settings.account.views.with_raw_response.get(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncViews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )
        assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.account.views.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.account.views.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(Optional[ViewCreateResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.create(
                account_id="",
                name="my view",
                zones=["372e67954025e0ba6aaa6d586b9e0b59"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            match="any",
            name={
                "contains": "view",
                "endswith": "ew",
                "exact": "my view",
                "startswith": "my",
            },
            order="name",
            page=1,
            per_page=5,
            zone_id="ae29bea30e2e427ba9cd8d78b628177b",
            zone_name="www.example.com",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.account.views.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.account.views.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ViewListResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.account.views.with_raw_response.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.account.views.with_streaming_response.delete(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(Optional[ViewDeleteResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.delete(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.delete(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my view",
            zones=["372e67954025e0ba6aaa6d586b9e0b59"],
        )
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.account.views.with_raw_response.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.account.views.with_streaming_response.edit(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(Optional[ViewEditResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.edit(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.edit(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        view = await async_client.dns.settings.account.views.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.account.views.with_raw_response.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.account.views.with_streaming_response.get(
            view_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(Optional[ViewGetResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.get(
                view_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.dns.settings.account.views.with_raw_response.get(
                view_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
