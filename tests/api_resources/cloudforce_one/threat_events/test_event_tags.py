# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    EventTagCreateResponse,
    EventTagDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        event_tag = client.cloudforce_one.threat_events.event_tags.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        )
        assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.event_tags.with_raw_response.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_tag = response.parse()
        assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.event_tags.with_streaming_response.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_tag = response.parse()
            assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.event_tags.with_raw_response.create(
                event_id="",
                account_id=0,
                tags=["botnet"],
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        event_tag = client.cloudforce_one.threat_events.event_tags.delete(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.event_tags.with_raw_response.delete(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_tag = response.parse()
        assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.event_tags.with_streaming_response.delete(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_tag = response.parse()
            assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.event_tags.with_raw_response.delete(
                event_id="",
                account_id=0,
            )


class TestAsyncEventTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        event_tag = await async_client.cloudforce_one.threat_events.event_tags.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        )
        assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.event_tags.with_raw_response.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_tag = await response.parse()
        assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.event_tags.with_streaming_response.create(
            event_id="event_id",
            account_id=0,
            tags=["botnet"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_tag = await response.parse()
            assert_matches_type(EventTagCreateResponse, event_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.event_tags.with_raw_response.create(
                event_id="",
                account_id=0,
                tags=["botnet"],
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        event_tag = await async_client.cloudforce_one.threat_events.event_tags.delete(
            event_id="event_id",
            account_id=0,
        )
        assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.event_tags.with_raw_response.delete(
            event_id="event_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_tag = await response.parse()
        assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.event_tags.with_streaming_response.delete(
            event_id="event_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_tag = await response.parse()
            assert_matches_type(EventTagDeleteResponse, event_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.event_tags.with_raw_response.delete(
                event_id="",
                account_id=0,
            )
