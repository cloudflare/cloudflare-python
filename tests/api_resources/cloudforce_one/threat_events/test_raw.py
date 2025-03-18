# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import RawGetResponse, RawEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRaw:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        raw = client.cloudforce_one.threat_events.raw.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        raw = client.cloudforce_one.threat_events.raw.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
            data={},
            source="example.com",
            tlp="amber",
        )
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.raw.with_raw_response.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.raw.with_streaming_response.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(RawEditResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.raw.with_raw_response.edit(
                raw_id="raw_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `raw_id` but received ''"):
            client.cloudforce_one.threat_events.raw.with_raw_response.edit(
                raw_id="",
                account_id=0,
                event_id="event_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        raw = client.cloudforce_one.threat_events.raw.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(RawGetResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.raw.with_raw_response.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(RawGetResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.raw.with_streaming_response.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(RawGetResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.raw.with_raw_response.get(
                raw_id="raw_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `raw_id` but received ''"):
            client.cloudforce_one.threat_events.raw.with_raw_response.get(
                raw_id="",
                account_id=0,
                event_id="event_id",
            )


class TestAsyncRaw:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        raw = await async_client.cloudforce_one.threat_events.raw.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        raw = await async_client.cloudforce_one.threat_events.raw.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
            data={},
            source="example.com",
            tlp="amber",
        )
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.raw.with_raw_response.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(RawEditResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.raw.with_streaming_response.edit(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(RawEditResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.raw.with_raw_response.edit(
                raw_id="raw_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `raw_id` but received ''"):
            await async_client.cloudforce_one.threat_events.raw.with_raw_response.edit(
                raw_id="",
                account_id=0,
                event_id="event_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        raw = await async_client.cloudforce_one.threat_events.raw.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )
        assert_matches_type(RawGetResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.raw.with_raw_response.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(RawGetResponse, raw, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.raw.with_streaming_response.get(
            raw_id="raw_id",
            account_id=0,
            event_id="event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(RawGetResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.raw.with_raw_response.get(
                raw_id="raw_id",
                account_id=0,
                event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `raw_id` but received ''"):
            await async_client.cloudforce_one.threat_events.raw.with_raw_response.get(
                raw_id="",
                account_id=0,
                event_id="event_id",
            )
