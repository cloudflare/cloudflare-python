# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.d1.database import (
    TimeTravelRestoreResponse,
    TimeTravelGetBookmarkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeTravel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_bookmark(self, client: Cloudflare) -> None:
        time_travel = client.d1.database.time_travel.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    def test_method_get_bookmark_with_all_params(self, client: Cloudflare) -> None:
        time_travel = client.d1.database.time_travel.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            timestamp=parse_datetime("2024-01-15T12:00:00Z"),
        )
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    def test_raw_response_get_bookmark(self, client: Cloudflare) -> None:
        response = client.d1.database.time_travel.with_raw_response.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_travel = response.parse()
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    def test_streaming_response_get_bookmark(self, client: Cloudflare) -> None:
        with client.d1.database.time_travel.with_streaming_response.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_travel = response.parse()
            assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_bookmark(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.time_travel.with_raw_response.get_bookmark(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.time_travel.with_raw_response.get_bookmark(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_restore(self, client: Cloudflare) -> None:
        time_travel = client.d1.database.time_travel.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    def test_method_restore_with_all_params(self, client: Cloudflare) -> None:
        time_travel = client.d1.database.time_travel.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bookmark="00000001-00000002-00004e2f-0a83ea2fceebc654de0640c422be4653",
            timestamp=parse_datetime("2024-01-15T12:00:00Z"),
        )
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    def test_raw_response_restore(self, client: Cloudflare) -> None:
        response = client.d1.database.time_travel.with_raw_response.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_travel = response.parse()
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    def test_streaming_response_restore(self, client: Cloudflare) -> None:
        with client.d1.database.time_travel.with_streaming_response.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_travel = response.parse()
            assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restore(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.time_travel.with_raw_response.restore(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.time_travel.with_raw_response.restore(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTimeTravel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_bookmark(self, async_client: AsyncCloudflare) -> None:
        time_travel = await async_client.d1.database.time_travel.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    async def test_method_get_bookmark_with_all_params(self, async_client: AsyncCloudflare) -> None:
        time_travel = await async_client.d1.database.time_travel.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            timestamp=parse_datetime("2024-01-15T12:00:00Z"),
        )
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    async def test_raw_response_get_bookmark(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.time_travel.with_raw_response.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_travel = await response.parse()
        assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

    @parametrize
    async def test_streaming_response_get_bookmark(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.time_travel.with_streaming_response.get_bookmark(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_travel = await response.parse()
            assert_matches_type(TimeTravelGetBookmarkResponse, time_travel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_bookmark(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.time_travel.with_raw_response.get_bookmark(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.time_travel.with_raw_response.get_bookmark(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_restore(self, async_client: AsyncCloudflare) -> None:
        time_travel = await async_client.d1.database.time_travel.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncCloudflare) -> None:
        time_travel = await async_client.d1.database.time_travel.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bookmark="00000001-00000002-00004e2f-0a83ea2fceebc654de0640c422be4653",
            timestamp=parse_datetime("2024-01-15T12:00:00Z"),
        )
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.d1.database.time_travel.with_raw_response.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time_travel = await response.parse()
        assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncCloudflare) -> None:
        async with async_client.d1.database.time_travel.with_streaming_response.restore(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time_travel = await response.parse()
            assert_matches_type(TimeTravelRestoreResponse, time_travel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restore(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.time_travel.with_raw_response.restore(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.time_travel.with_raw_response.restore(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
