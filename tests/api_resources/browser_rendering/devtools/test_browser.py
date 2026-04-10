# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.browser_rendering.devtools import (
    BrowserCreateResponse,
    BrowserDeleteResponse,
    BrowserVersionResponse,
    BrowserProtocolResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.create(
            account_id="account_id",
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.create(
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
            targets=True,
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.delete(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.delete(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_connect(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert browser is None

    @parametrize
    def test_method_connect_with_all_params(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
        )
        assert browser is None

    @parametrize
    def test_raw_response_connect(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @parametrize
    def test_streaming_response_connect(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.connect(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.connect(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_launch(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.launch(
            account_id="account_id",
        )
        assert browser is None

    @parametrize
    def test_method_launch_with_all_params(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.launch(
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
        )
        assert browser is None

    @parametrize
    def test_raw_response_launch(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.launch(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @parametrize
    def test_streaming_response_launch(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.launch(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_launch(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.launch(
                account_id="",
            )

    @parametrize
    def test_method_protocol(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

    @parametrize
    def test_raw_response_protocol(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

    @parametrize
    def test_streaming_response_protocol(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_protocol(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.protocol(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.protocol(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_version(self, client: Cloudflare) -> None:
        browser = client.browser_rendering.devtools.browser.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserVersionResponse, browser, path=["response"])

    @parametrize
    def test_raw_response_version(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.with_raw_response.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserVersionResponse, browser, path=["response"])

    @parametrize
    def test_streaming_response_version(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.with_streaming_response.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserVersionResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_version(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.version(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.with_raw_response.version(
                session_id="",
                account_id="account_id",
            )


class TestAsyncBrowser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.create(
            account_id="account_id",
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.create(
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
            targets=True,
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.delete(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserDeleteResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.delete(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.delete(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert browser is None

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
        )
        assert browser is None

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.connect(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.connect(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.connect(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_launch(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.launch(
            account_id="account_id",
        )
        assert browser is None

    @parametrize
    async def test_method_launch_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.launch(
            account_id="account_id",
            keep_alive=10000,
            lab=True,
            recording=True,
        )
        assert browser is None

    @parametrize
    async def test_raw_response_launch(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.launch(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @parametrize
    async def test_streaming_response_launch(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.launch(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_launch(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.launch(
                account_id="",
            )

    @parametrize
    async def test_method_protocol(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

    @parametrize
    async def test_raw_response_protocol(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

    @parametrize
    async def test_streaming_response_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.protocol(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserProtocolResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_protocol(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.protocol(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.protocol(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_version(self, async_client: AsyncCloudflare) -> None:
        browser = await async_client.browser_rendering.devtools.browser.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(BrowserVersionResponse, browser, path=["response"])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.with_raw_response.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserVersionResponse, browser, path=["response"])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.with_streaming_response.version(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserVersionResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_version(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.version(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.with_raw_response.version(
                session_id="",
                account_id="account_id",
            )
