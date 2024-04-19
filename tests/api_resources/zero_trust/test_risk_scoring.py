# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust import RiskScoringGetResponse, RiskScoringResetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRiskScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        risk_scoring = client.zero_trust.risk_scoring.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        risk_scoring = client.zero_trust.risk_scoring.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order_by="timestamp",
            page=0,
            per_page=0,
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                "f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_reset(self, client: Cloudflare) -> None:
        risk_scoring = client.zero_trust.risk_scoring.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_reset(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_reset(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_reset(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                "f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRiskScoring:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order_by="timestamp",
            page=0,
            per_page=0,
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.get(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                "f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_reset(self, async_client: AsyncCloudflare) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.reset(
            "f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_reset(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                "f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
