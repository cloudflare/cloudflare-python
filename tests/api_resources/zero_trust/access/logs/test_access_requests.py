# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.zero_trust.access.logs import AccessRequestListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        access_request = client.zero_trust.access.logs.access_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        access_request = client.zero_trust.access.logs.access_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            limit=0,
            since=parse_datetime("2020-07-01T05:20:00Z"),
            until=parse_datetime("2020-10-01T05:20:00Z"),
        )
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.logs.access_requests.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_request = response.parse()
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.logs.access_requests.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_request = response.parse()
            assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.logs.access_requests.with_raw_response.list(
                account_id="",
            )


class TestAsyncAccessRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        access_request = await async_client.zero_trust.access.logs.access_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_request = await async_client.zero_trust.access.logs.access_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            limit=0,
            since=parse_datetime("2020-07-01T05:20:00Z"),
            until=parse_datetime("2020-10-01T05:20:00Z"),
        )
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.logs.access_requests.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_request = await response.parse()
        assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.logs.access_requests.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_request = await response.parse()
            assert_matches_type(Optional[AccessRequestListResponse], access_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.logs.access_requests.with_raw_response.list(
                account_id="",
            )
