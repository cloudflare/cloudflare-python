# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.intels import WhoisWhoisRecordGetWhoisRecordResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intels import whois_whois_record_get_whois_record_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhois:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_whois_record_get_whois_record(self, client: Cloudflare) -> None:
        whois = client.intels.whois.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_whois_record_get_whois_record_with_all_params(self, client: Cloudflare) -> None:
        whois = client.intels.whois.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domain="string",
        )
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_whois_record_get_whois_record(self, client: Cloudflare) -> None:
        response = client.intels.whois.with_raw_response.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whois = response.parse()
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_whois_record_get_whois_record(self, client: Cloudflare) -> None:
        with client.intels.whois.with_streaming_response.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whois = response.parse()
            assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_whois_record_get_whois_record(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intels.whois.with_raw_response.whois_record_get_whois_record(
                "",
            )


class TestAsyncWhois:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_whois_record_get_whois_record(self, async_client: AsyncCloudflare) -> None:
        whois = await async_client.intels.whois.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_whois_record_get_whois_record_with_all_params(self, async_client: AsyncCloudflare) -> None:
        whois = await async_client.intels.whois.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domain="string",
        )
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_whois_record_get_whois_record(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intels.whois.with_raw_response.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whois = await response.parse()
        assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_whois_record_get_whois_record(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intels.whois.with_streaming_response.whois_record_get_whois_record(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whois = await response.parse()
            assert_matches_type(WhoisWhoisRecordGetWhoisRecordResponse, whois, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_whois_record_get_whois_record(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intels.whois.with_raw_response.whois_record_get_whois_record(
                "",
            )
