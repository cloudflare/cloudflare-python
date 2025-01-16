# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        response = client.url_scanner.responses.get(
            response_id="response_id",
            account_id="account_id",
        )
        assert_matches_type(str, response, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        http_response = client.url_scanner.responses.with_raw_response.get(
            response_id="response_id",
            account_id="account_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(str, response, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.url_scanner.responses.with_streaming_response.get(
            response_id="response_id",
            account_id="account_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(str, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.responses.with_raw_response.get(
                response_id="response_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.url_scanner.responses.with_raw_response.get(
                response_id="",
                account_id="account_id",
            )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.responses.get(
            response_id="response_id",
            account_id="account_id",
        )
        assert_matches_type(str, response, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        http_response = await async_client.url_scanner.responses.with_raw_response.get(
            response_id="response_id",
            account_id="account_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(str, response, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.responses.with_streaming_response.get(
            response_id="response_id",
            account_id="account_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(str, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.responses.with_raw_response.get(
                response_id="response_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.url_scanner.responses.with_raw_response.get(
                response_id="",
                account_id="account_id",
            )
