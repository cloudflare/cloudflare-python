# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.intel import DNSGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dns = client.intel.dns.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        dns = client.intel.dns.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            ipv4="string",
            page=1,
            per_page=20,
            start_end_params={
                "end": parse_date("2021-04-30"),
                "start": parse_date("2021-04-01"),
            },
        )
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.intel.dns.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.intel.dns.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSGetResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.dns.with_raw_response.get(
                "",
            )


class TestAsyncDNS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.intel.dns.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.intel.dns.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            ipv4="string",
            page=1,
            per_page=20,
            start_end_params={
                "end": parse_date("2021-04-30"),
                "start": parse_date("2021-04-01"),
            },
        )
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.dns.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSGetResponse, dns, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.dns.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSGetResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.dns.with_raw_response.get(
                "",
            )
