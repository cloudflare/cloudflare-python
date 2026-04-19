# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.browser_rendering.devtools.browser import (
    TargetGetResponse,
    TargetListResponse,
    TargetCreateResponse,
    TargetActivateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTargets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        target = client.browser_rendering.devtools.browser.targets.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        target = client.browser_rendering.devtools.browser.targets.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            url="https://example.com",
        )
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.targets.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.targets.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetCreateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.create(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.create(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        target = client.browser_rendering.devtools.browser.targets.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.targets.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetListResponse, target, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.targets.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetListResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.list(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.list(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_activate(self, client: Cloudflare) -> None:
        target = client.browser_rendering.devtools.browser.targets.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TargetActivateResponse, target, path=["response"])

    @parametrize
    def test_raw_response_activate(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetActivateResponse, target, path=["response"])

    @parametrize
    def test_streaming_response_activate(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.targets.with_streaming_response.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetActivateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        target = client.browser_rendering.devtools.browser.targets.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TargetGetResponse, target, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.browser_rendering.devtools.browser.targets.with_raw_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetGetResponse, target, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.browser_rendering.devtools.browser.targets.with_streaming_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetGetResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTargets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.browser_rendering.devtools.browser.targets.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.browser_rendering.devtools.browser.targets.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            url="https://example.com",
        )
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.targets.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetCreateResponse, target, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.targets.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetCreateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.create(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.create(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.browser_rendering.devtools.browser.targets.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.targets.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetListResponse, target, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.targets.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetListResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.list(
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.list(
                session_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_activate(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.browser_rendering.devtools.browser.targets.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TargetActivateResponse, target, path=["response"])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetActivateResponse, target, path=["response"])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.targets.with_streaming_response.activate(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetActivateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.activate(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.browser_rendering.devtools.browser.targets.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TargetGetResponse, target, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.devtools.browser.targets.with_raw_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetGetResponse, target, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.devtools.browser.targets.with_streaming_response.get(
            target_id="target_id",
            account_id="account_id",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetGetResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="target_id",
                account_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="target_id",
                account_id="account_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.browser_rendering.devtools.browser.targets.with_raw_response.get(
                target_id="",
                account_id="account_id",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
