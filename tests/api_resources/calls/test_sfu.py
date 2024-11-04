# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.calls import (
    SfuGetResponse,
    SfuListResponse,
    SfuCreateResponse,
    SfuDeleteResponse,
    SfuUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSfu:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.calls.sfu.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = response.parse()
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.calls.sfu.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = response.parse()
            assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.sfu.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.calls.sfu.with_raw_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = response.parse()
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.calls.sfu.with_streaming_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = response.parse()
            assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.sfu.with_raw_response.update(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.sfu.with_raw_response.update(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SfuListResponse], sfu, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.calls.sfu.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = response.parse()
        assert_matches_type(SyncSinglePage[SfuListResponse], sfu, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.calls.sfu.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = response.parse()
            assert_matches_type(SyncSinglePage[SfuListResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.sfu.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.calls.sfu.with_raw_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = response.parse()
        assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.calls.sfu.with_streaming_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = response.parse()
            assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.sfu.with_raw_response.delete(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.sfu.with_raw_response.delete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        sfu = client.calls.sfu.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.calls.sfu.with_raw_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = response.parse()
        assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.calls.sfu.with_streaming_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = response.parse()
            assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.sfu.with_raw_response.get(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.sfu.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSfu:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.calls.sfu.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = await response.parse()
        assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.calls.sfu.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = await response.parse()
            assert_matches_type(Optional[SfuCreateResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.calls.sfu.with_raw_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = await response.parse()
        assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.calls.sfu.with_streaming_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = await response.parse()
            assert_matches_type(Optional[SfuUpdateResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.update(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.update(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SfuListResponse], sfu, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.calls.sfu.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = await response.parse()
        assert_matches_type(AsyncSinglePage[SfuListResponse], sfu, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.calls.sfu.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = await response.parse()
            assert_matches_type(AsyncSinglePage[SfuListResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.calls.sfu.with_raw_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = await response.parse()
        assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.calls.sfu.with_streaming_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = await response.parse()
            assert_matches_type(Optional[SfuDeleteResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.delete(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.delete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        sfu = await async_client.calls.sfu.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.calls.sfu.with_raw_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sfu = await response.parse()
        assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.calls.sfu.with_streaming_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sfu = await response.parse()
            assert_matches_type(Optional[SfuGetResponse], sfu, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.get(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.sfu.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
