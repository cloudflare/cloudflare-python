# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDOM:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dom = client.url_scanner.dom.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(str, dom, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.url_scanner.dom.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dom = response.parse()
        assert_matches_type(str, dom, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.url_scanner.dom.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dom = response.parse()
            assert_matches_type(str, dom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.dom.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.dom.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )


class TestAsyncDOM:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dom = await async_client.url_scanner.dom.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(str, dom, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.dom.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dom = await response.parse()
        assert_matches_type(str, dom, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.dom.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dom = await response.parse()
            assert_matches_type(str, dom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.dom.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.dom.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )
