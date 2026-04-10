# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        page = client.browser_rendering.devtools.browser.page.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert page is None

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.page.with_raw_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert page is None

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.page.with_streaming_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        page = await async_client.browser_rendering.devtools.browser.page.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert page is None

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.page.with_raw_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert page is None

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.page.with_streaming_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.page.with_raw_response.get(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
