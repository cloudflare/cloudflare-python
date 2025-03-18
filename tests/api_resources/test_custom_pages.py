# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.custom_pages import CustomPageGetResponse, CustomPageUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_pages.with_raw_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_pages.with_streaming_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.custom_pages.with_raw_response.update(
                identifier="",
                state="default",
                url="http://www.example.com",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                state="default",
                url="http://www.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                state="default",
                url="http://www.example.com",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.custom_pages.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(SyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.custom_pages.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(SyncSinglePage[object], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.custom_pages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_pages.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_pages.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.custom_pages.with_raw_response.get(
                identifier="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )


class TestAsyncCustomPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.with_raw_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.with_streaming_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            state="default",
            url="http://www.example.com",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageUpdateResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.custom_pages.with_raw_response.update(
                identifier="",
                state="default",
                url="http://www.example.com",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                state="default",
                url="http://www.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                state="default",
                url="http://www.example.com",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(AsyncSinglePage[object], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(AsyncSinglePage[object], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.custom_pages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageGetResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism failures")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.custom_pages.with_raw_response.get(
                identifier="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )
