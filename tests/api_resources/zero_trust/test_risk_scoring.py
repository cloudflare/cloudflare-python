# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust import RiskScoringGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRiskScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        risk_scoring = client.zero_trust.risk_scoring.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_reset(self, client: Cloudflare) -> None:
        risk_scoring = client.zero_trust.risk_scoring.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, risk_scoring, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(object, risk_scoring, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(object, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="",
                account_id="account_id",
            )


class TestAsyncRiskScoring:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.get(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(Optional[RiskScoringGetResponse], risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncCloudflare) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(object, risk_scoring, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(object, risk_scoring, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.reset(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(object, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="",
                account_id="account_id",
            )
