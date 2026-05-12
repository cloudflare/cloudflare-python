# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai_gateway.billing import SpendingLimitGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpendingLimit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        spending_limit = client.ai_gateway.billing.spending_limit.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        )
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.spending_limit.with_raw_response.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = response.parse()
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.spending_limit.with_streaming_response.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = response.parse()
            assert_matches_type(object, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.spending_limit.with_raw_response.create(
                account_id="",
                amount=10000,
                duration="monthly",
                strategy="fixed",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        spending_limit = client.ai_gateway.billing.spending_limit.delete(
            account_id="account_id",
        )
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.spending_limit.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = response.parse()
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.spending_limit.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = response.parse()
            assert_matches_type(object, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.spending_limit.with_raw_response.delete(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        spending_limit = client.ai_gateway.billing.spending_limit.get(
            account_id="account_id",
        )
        assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.spending_limit.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = response.parse()
        assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.spending_limit.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = response.parse()
            assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.spending_limit.with_raw_response.get(
                account_id="",
            )


class TestAsyncSpendingLimit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        spending_limit = await async_client.ai_gateway.billing.spending_limit.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        )
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.spending_limit.with_raw_response.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = await response.parse()
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.spending_limit.with_streaming_response.create(
            account_id="account_id",
            amount=10000,
            duration="monthly",
            strategy="fixed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = await response.parse()
            assert_matches_type(object, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.spending_limit.with_raw_response.create(
                account_id="",
                amount=10000,
                duration="monthly",
                strategy="fixed",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        spending_limit = await async_client.ai_gateway.billing.spending_limit.delete(
            account_id="account_id",
        )
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.spending_limit.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = await response.parse()
        assert_matches_type(object, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.spending_limit.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = await response.parse()
            assert_matches_type(object, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.spending_limit.with_raw_response.delete(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        spending_limit = await async_client.ai_gateway.billing.spending_limit.get(
            account_id="account_id",
        )
        assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.spending_limit.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spending_limit = await response.parse()
        assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.spending_limit.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spending_limit = await response.parse()
            assert_matches_type(SpendingLimitGetResponse, spending_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.spending_limit.with_raw_response.get(
                account_id="",
            )
