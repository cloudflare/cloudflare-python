# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.risk_scoring import (
    BehaviourGetResponse,
    BehaviourUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBehaviours:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        behaviour = client.zero_trust.risk_scoring.behaviours.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        behaviour = client.zero_trust.risk_scoring.behaviours.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = response.parse()
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.behaviours.with_streaming_response.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = response.parse()
            assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
                account_identifier="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        behaviour = client.zero_trust.risk_scoring.behaviours.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = response.parse()
        assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.behaviours.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = response.parse()
            assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
                "",
            )


class TestAsyncBehaviours:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        behaviour = await async_client.zero_trust.risk_scoring.behaviours.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        behaviour = await async_client.zero_trust.risk_scoring.behaviours.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = await response.parse()
        assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.behaviours.with_streaming_response.update(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = await response.parse()
            assert_matches_type(BehaviourUpdateResponse, behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
                account_identifier="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        behaviour = await async_client.zero_trust.risk_scoring.behaviours.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = await response.parse()
        assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.behaviours.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = await response.parse()
            assert_matches_type(BehaviourGetResponse, behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
                "",
            )
