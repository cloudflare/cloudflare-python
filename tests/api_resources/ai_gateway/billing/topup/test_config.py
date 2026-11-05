# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai_gateway.billing.topup import ConfigGetResponse, ConfigCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        config = client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.topup.config.with_raw_response.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.topup.config.with_streaming_response.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigCreateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.topup.config.with_raw_response.create(
                account_id="",
                amount=5000,
                threshold=500,
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        config = client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        config = client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
            setup_intent_id="seti_123",
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.topup.config.with_raw_response.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.topup.config.with_streaming_response.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigCreateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.topup.config.with_raw_response.create(
                account_id="",
                amount=5000,
                consent_version="auto-topup-v1",
                payment_method_id="pm_123",
                setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
                threshold=500,
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.ai_gateway.billing.topup.config.delete(
            account_id="account_id",
        )
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.topup.config.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.topup.config.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.topup.config.with_raw_response.delete(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.ai_gateway.billing.topup.config.get(
            account_id="account_id",
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.topup.config.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.topup.config.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.topup.config.with_raw_response.get(
                account_id="",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.topup.config.with_raw_response.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.topup.config.with_streaming_response.create(
            account_id="account_id",
            amount=5000,
            threshold=500,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigCreateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.topup.config.with_raw_response.create(
                account_id="",
                amount=5000,
                threshold=500,
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.ai_gateway.billing.topup.config.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
            setup_intent_id="seti_123",
        )
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.topup.config.with_raw_response.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigCreateResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.topup.config.with_streaming_response.create(
            account_id="account_id",
            amount=5000,
            consent_version="auto-topup-v1",
            payment_method_id="pm_123",
            setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
            threshold=500,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigCreateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.topup.config.with_raw_response.create(
                account_id="",
                amount=5000,
                consent_version="auto-topup-v1",
                payment_method_id="pm_123",
                setup_idempotency_key="f6af84c0-12d6-4c46-840d-2e4934df85e1",
                threshold=500,
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.ai_gateway.billing.topup.config.delete(
            account_id="account_id",
        )
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.topup.config.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.topup.config.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.topup.config.with_raw_response.delete(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.ai_gateway.billing.topup.config.get(
            account_id="account_id",
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.topup.config.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.topup.config.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.topup.config.with_raw_response.get(
                account_id="",
            )
