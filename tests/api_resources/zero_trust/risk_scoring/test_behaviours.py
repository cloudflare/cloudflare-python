# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

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
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )
        assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = response.parse()
        assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.behaviours.with_streaming_response.update(
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = response.parse()
            assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
                account_id="",
                behaviors={
                    "foo": {
                        "enabled": True,
                        "risk_level": "low",
                    }
                },
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        behaviour = client.zero_trust.risk_scoring.behaviours.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = response.parse()
        assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.risk_scoring.behaviours.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = response.parse()
            assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
                account_id="",
            )


class TestAsyncBehaviours:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        behaviour = await async_client.zero_trust.risk_scoring.behaviours.update(
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )
        assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = await response.parse()
        assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.behaviours.with_streaming_response.update(
            account_id="account_id",
            behaviors={
                "foo": {
                    "enabled": True,
                    "risk_level": "low",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = await response.parse()
            assert_matches_type(Optional[BehaviourUpdateResponse], behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.update(
                account_id="",
                behaviors={
                    "foo": {
                        "enabled": True,
                        "risk_level": "low",
                    }
                },
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        behaviour = await async_client.zero_trust.risk_scoring.behaviours.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        behaviour = await response.parse()
        assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.risk_scoring.behaviours.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            behaviour = await response.parse()
            assert_matches_type(Optional[BehaviourGetResponse], behaviour, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.risk_scoring.behaviours.with_raw_response.get(
                account_id="",
            )
