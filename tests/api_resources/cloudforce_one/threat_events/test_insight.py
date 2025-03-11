# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    InsightGetResponse,
    InsightCreatResponse,
    InsightDeleteResponse,
    InsightUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsight:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insight.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insight.with_raw_response.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insight.with_streaming_response.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightUpdateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.update(
                insight_id="insightId",
                account_id=0,
                event_id="",
                content="Updated: Here is some additional context _in markdown_",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.update(
                insight_id="",
                account_id=0,
                event_id="eventId",
                content="Updated: Here is some additional context _in markdown_",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insight.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insight.with_raw_response.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insight.with_streaming_response.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.delete(
                insight_id="insightId",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.delete(
                insight_id="",
                account_id=0,
                event_id="eventId",
            )

    @parametrize
    def test_method_creat(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insight.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightCreatResponse, insight, path=["response"])

    @parametrize
    def test_raw_response_creat(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insight.with_raw_response.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightCreatResponse, insight, path=["response"])

    @parametrize
    def test_streaming_response_creat(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insight.with_streaming_response.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightCreatResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_creat(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.creat(
                event_id="",
                account_id=0,
                content="Here is some additional context _in markdown_",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insight.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insight.with_raw_response.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insight.with_streaming_response.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightGetResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.get(
                insight_id="insightId",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insight.with_raw_response.get(
                insight_id="",
                account_id=0,
                event_id="eventId",
            )


class TestAsyncInsight:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insight.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insight.with_raw_response.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insight.with_streaming_response.update(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
            content="Updated: Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightUpdateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.update(
                insight_id="insightId",
                account_id=0,
                event_id="",
                content="Updated: Here is some additional context _in markdown_",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.update(
                insight_id="",
                account_id=0,
                event_id="eventId",
                content="Updated: Here is some additional context _in markdown_",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insight.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insight.with_raw_response.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insight.with_streaming_response.delete(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.delete(
                insight_id="insightId",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.delete(
                insight_id="",
                account_id=0,
                event_id="eventId",
            )

    @parametrize
    async def test_method_creat(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insight.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightCreatResponse, insight, path=["response"])

    @parametrize
    async def test_raw_response_creat(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insight.with_raw_response.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightCreatResponse, insight, path=["response"])

    @parametrize
    async def test_streaming_response_creat(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insight.with_streaming_response.creat(
            event_id="eventId",
            account_id=0,
            content="Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightCreatResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_creat(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.creat(
                event_id="",
                account_id=0,
                content="Here is some additional context _in markdown_",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insight.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insight.with_raw_response.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insight.with_streaming_response.get(
            insight_id="insightId",
            account_id=0,
            event_id="eventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightGetResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.get(
                insight_id="insightId",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insight.with_raw_response.get(
                insight_id="",
                account_id=0,
                event_id="eventId",
            )
