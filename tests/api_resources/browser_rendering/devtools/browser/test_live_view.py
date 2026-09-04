# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.browser_rendering.devtools.browser import LiveViewCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveView:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        live_view = client.browser_rendering.devtools.browser.live_view.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        live_view = client.browser_rendering.devtools.browser.live_view.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            expires_in_ms=60000,
            guardrails={"mode": "readonly"},
            mode="devtools",
            target_id="targetId",
        )
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_view = response.parse()
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.live_view.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_view = response.parse()
            assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
                session_id="",
                account_id="account_id",
            )


class TestAsyncLiveView:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        live_view = await async_client.browser_rendering.devtools.browser.live_view.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        live_view = await async_client.browser_rendering.devtools.browser.live_view.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            expires_in_ms=60000,
            guardrails={"mode": "readonly"},
            mode="devtools",
            target_id="targetId",
        )
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_view = await response.parse()
        assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.live_view.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_view = await response.parse()
            assert_matches_type(LiveViewCreateResponse, live_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.live_view.with_raw_response.create(
                session_id="",
                account_id="account_id",
            )
