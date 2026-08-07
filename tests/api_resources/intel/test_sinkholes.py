# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.intel import Sinkhole

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSinkholes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            r2_bucket="r2_bucket",
            r2_id="r2_id",
            r2_secret="r2_secret",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = response.parse()
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = response.parse()
            assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.sinkholes.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            r2_bucket="r2_bucket",
            r2_id="r2_id",
            r2_secret="r2_secret",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.with_raw_response.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = response.parse()
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.with_streaming_response.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = response.parse()
            assert_matches_type(object, sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.sinkholes.with_raw_response.update(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.with_raw_response.update(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = response.parse()
        assert_matches_type(SyncSinglePage[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = response.parse()
            assert_matches_type(SyncSinglePage[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.sinkholes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.with_raw_response.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = response.parse()
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.with_streaming_response.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = response.parse()
            assert_matches_type(object, sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.sinkholes.with_raw_response.delete(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.with_raw_response.delete(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        sinkhole = client.intel.sinkholes.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.with_raw_response.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = response.parse()
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.with_streaming_response.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = response.parse()
            assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.sinkholes.with_raw_response.get(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.with_raw_response.get(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSinkholes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            r2_bucket="r2_bucket",
            r2_id="r2_id",
            r2_secret="r2_secret",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = await response.parse()
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = await response.parse()
            assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.create(
                account_id="",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            r2_bucket="r2_bucket",
            r2_id="r2_id",
            r2_secret="r2_secret",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.with_raw_response.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = await response.parse()
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.with_streaming_response.update(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = await response.parse()
            assert_matches_type(object, sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.update(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.update(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = await response.parse()
        assert_matches_type(AsyncSinglePage[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = await response.parse()
            assert_matches_type(AsyncSinglePage[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.with_raw_response.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = await response.parse()
        assert_matches_type(object, sinkhole, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.with_streaming_response.delete(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = await response.parse()
            assert_matches_type(object, sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.delete(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.delete(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        sinkhole = await async_client.intel.sinkholes.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.with_raw_response.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sinkhole = await response.parse()
        assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.with_streaming_response.get(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sinkhole = await response.parse()
            assert_matches_type(Optional[Sinkhole], sinkhole, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.get(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.with_raw_response.get(
                sinkhole_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
