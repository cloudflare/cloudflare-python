# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.ct import (
    AuthorityGetResponse,
    AuthorityListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthorities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        authority = client.radar.ct.authorities.list()
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        authority = client.radar.ct.authorities.list(
            format="JSON",
            limit=1,
            offset=0,
        )
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.ct.authorities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authority = response.parse()
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.ct.authorities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authority = response.parse()
            assert_matches_type(AuthorityListResponse, authority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        authority = client.radar.ct.authorities.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        )
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        authority = client.radar.ct.authorities.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
            format="JSON",
        )
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.ct.authorities.with_raw_response.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authority = response.parse()
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.ct.authorities.with_streaming_response.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authority = response.parse()
            assert_matches_type(AuthorityGetResponse, authority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ca_slug` but received ''"):
            client.radar.ct.authorities.with_raw_response.get(
                ca_slug="",
            )


class TestAsyncAuthorities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        authority = await async_client.radar.ct.authorities.list()
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        authority = await async_client.radar.ct.authorities.list(
            format="JSON",
            limit=1,
            offset=0,
        )
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ct.authorities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authority = await response.parse()
        assert_matches_type(AuthorityListResponse, authority, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ct.authorities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authority = await response.parse()
            assert_matches_type(AuthorityListResponse, authority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        authority = await async_client.radar.ct.authorities.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        )
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        authority = await async_client.radar.ct.authorities.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
            format="JSON",
        )
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ct.authorities.with_raw_response.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authority = await response.parse()
        assert_matches_type(AuthorityGetResponse, authority, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ct.authorities.with_streaming_response.get(
            ca_slug="24EDD4E503A8D3FDB5FFB4AF66C887359901CBE687A5A0760D10A08EED99A7C3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authority = await response.parse()
            assert_matches_type(AuthorityGetResponse, authority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ca_slug` but received ''"):
            await async_client.radar.ct.authorities.with_raw_response.get(
                ca_slug="",
            )
