# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.addressing import (
    RegionalHostnameGetResponse,
    RegionalHostnameEditResponse,
    RegionalHostnameListResponse,
    RegionalHostnameCreateResponse,
    RegionalHostnameDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegionalHostnames:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        regional_hostname = client.addressing.regional_hostnames.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        )
        assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addressing.regional_hostnames.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = response.parse()
        assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addressing.regional_hostnames.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = response.parse()
            assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.create(
                zone_id="",
                hostname="foo.example.com",
                region_key="ca",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        regional_hostname = client.addressing.regional_hostnames.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.regional_hostnames.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = response.parse()
        assert_matches_type(SyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.regional_hostnames.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = response.parse()
            assert_matches_type(SyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        regional_hostname = client.addressing.regional_hostnames.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.regional_hostnames.with_raw_response.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = response.parse()
        assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.regional_hostnames.with_streaming_response.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = response.parse()
            assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.delete(
                hostname="foo.example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.delete(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        regional_hostname = client.addressing.regional_hostnames.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        )
        assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.regional_hostnames.with_raw_response.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = response.parse()
        assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.regional_hostnames.with_streaming_response.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = response.parse()
            assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.edit(
                hostname="foo.example.com",
                zone_id="",
                region_key="ca",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.edit(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                region_key="ca",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        regional_hostname = client.addressing.regional_hostnames.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.regional_hostnames.with_raw_response.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = response.parse()
        assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.regional_hostnames.with_streaming_response.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = response.parse()
            assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.get(
                hostname="foo.example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            client.addressing.regional_hostnames.with_raw_response.get(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRegionalHostnames:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        regional_hostname = await async_client.addressing.regional_hostnames.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        )
        assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.regional_hostnames.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = await response.parse()
        assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.regional_hostnames.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="foo.example.com",
            region_key="ca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = await response.parse()
            assert_matches_type(Optional[RegionalHostnameCreateResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.create(
                zone_id="",
                hostname="foo.example.com",
                region_key="ca",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        regional_hostname = await async_client.addressing.regional_hostnames.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.regional_hostnames.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = await response.parse()
        assert_matches_type(AsyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.regional_hostnames.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = await response.parse()
            assert_matches_type(AsyncSinglePage[RegionalHostnameListResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        regional_hostname = await async_client.addressing.regional_hostnames.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.regional_hostnames.with_raw_response.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = await response.parse()
        assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.regional_hostnames.with_streaming_response.delete(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = await response.parse()
            assert_matches_type(RegionalHostnameDeleteResponse, regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.delete(
                hostname="foo.example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.delete(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        regional_hostname = await async_client.addressing.regional_hostnames.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        )
        assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.regional_hostnames.with_raw_response.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = await response.parse()
        assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.regional_hostnames.with_streaming_response.edit(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="ca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = await response.parse()
            assert_matches_type(Optional[RegionalHostnameEditResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.edit(
                hostname="foo.example.com",
                zone_id="",
                region_key="ca",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.edit(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                region_key="ca",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        regional_hostname = await async_client.addressing.regional_hostnames.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.regional_hostnames.with_raw_response.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regional_hostname = await response.parse()
        assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.regional_hostnames.with_streaming_response.get(
            hostname="foo.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regional_hostname = await response.parse()
            assert_matches_type(Optional[RegionalHostnameGetResponse], regional_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.get(
                hostname="foo.example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            await async_client.addressing.regional_hostnames.with_raw_response.get(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
