# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    InsightGetResponse,
    InsightEditResponse,
    InsightCreateResponse,
    InsightDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insights.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insights.with_raw_response.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insights.with_streaming_response.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightCreateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.create(
                event_id="",
                account_id=0,
                content="Here is some additional context _in markdown_",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insights.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insights.with_raw_response.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insights.with_streaming_response.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.delete(
                insight_id="insight_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.delete(
                insight_id="",
                account_id=0,
                event_id="event_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insights.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightEditResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insights.with_raw_response.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightEditResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insights.with_streaming_response.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightEditResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.edit(
                insight_id="insight_id",
                account_id=0,
                event_id="",
                content="Updated: Here is some additional context _in markdown_",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.edit(
                insight_id="",
                account_id=0,
                event_id="event_id",
                content="Updated: Here is some additional context _in markdown_",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        insight = client.cloudforce_one.threat_events.insights.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.insights.with_raw_response.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.insights.with_streaming_response.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightGetResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.get(
                insight_id="insight_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.cloudforce_one.threat_events.insights.with_raw_response.get(
                insight_id="",
                account_id=0,
                event_id="event_id",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insights.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insights.with_raw_response.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insights.with_streaming_response.create(
            event_id="event_id",
            account_id=0,
            content="Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightCreateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.create(
                event_id="",
                account_id=0,
                content="Here is some additional context _in markdown_",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insights.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insights.with_raw_response.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insights.with_streaming_response.delete(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.delete(
                insight_id="insight_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.delete(
                insight_id="",
                account_id=0,
                event_id="event_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insights.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        )
        assert_matches_type(InsightEditResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insights.with_raw_response.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightEditResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insights.with_streaming_response.edit(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
            content="Updated: Here is some additional context _in markdown_",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightEditResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.edit(
                insight_id="insight_id",
                account_id=0,
                event_id="",
                content="Updated: Here is some additional context _in markdown_",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.edit(
                insight_id="",
                account_id=0,
                event_id="event_id",
                content="Updated: Here is some additional context _in markdown_",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        insight = await async_client.cloudforce_one.threat_events.insights.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.insights.with_raw_response.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightGetResponse, insight, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.insights.with_streaming_response.get(
            insight_id="insight_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightGetResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.get(
                insight_id="insight_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.cloudforce_one.threat_events.insights.with_raw_response.get(
                insight_id="",
                account_id=0,
                event_id="event_id",
            )
