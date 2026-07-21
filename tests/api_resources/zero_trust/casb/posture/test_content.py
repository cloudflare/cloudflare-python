# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture import (
    ContentListResponse,
    ContentExportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        content = client.zero_trust.casb.posture.content.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        content = client.zero_trust.casb.posture.content.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            direction="asc",
            dlp_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="asset_name",
            page=0,
            per_page=0,
            search="search",
            vendor="GOOGLE_WORKSPACE",
        )
        assert_matches_type(SyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.content.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.content.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.content.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        content = client.zero_trust.casb.posture.content.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        )
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Cloudflare) -> None:
        content = client.zero_trust.casb.posture.content.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
            dlp_profile_id=["e91a2360-da51-4fdf-9711-bcdecd462614"],
            integration_id=["c416bc38-75dc-425f-ae25-c37b5df5c37f"],
            max_affliction_date=parse_datetime("2024-01-01T00:00:00Z"),
            min_affliction_date=parse_datetime("2023-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "asset_name",
                }
            ],
            search="sensitive",
            vendors=["GOOGLE_WORKSPACE"],
        )
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.content.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.content.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.content.with_raw_response.export(
                account_id="",
                dlp_profile_information=[
                    {
                        "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        "entries": [
                            {
                                "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                                "name": "Credit Card Numbers",
                                "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                            }
                        ],
                        "name": "Financial Information",
                    }
                ],
            )


class TestAsyncContent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.zero_trust.casb.posture.content.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.zero_trust.casb.posture.content.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            direction="asc",
            dlp_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="asset_name",
            page=0,
            per_page=0,
            search="search",
            vendor="GOOGLE_WORKSPACE",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.content.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.content.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ContentListResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.content.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.zero_trust.casb.posture.content.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        )
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.zero_trust.casb.posture.content.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
            dlp_profile_id=["e91a2360-da51-4fdf-9711-bcdecd462614"],
            integration_id=["c416bc38-75dc-425f-ae25-c37b5df5c37f"],
            max_affliction_date=parse_datetime("2024-01-01T00:00:00Z"),
            min_affliction_date=parse_datetime("2023-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "asset_name",
                }
            ],
            search="sensitive",
            vendors=["GOOGLE_WORKSPACE"],
        )
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.content.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.content.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            dlp_profile_information=[
                {
                    "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                    "entries": [
                        {
                            "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                            "name": "Credit Card Numbers",
                            "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        }
                    ],
                    "name": "Financial Information",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(Optional[ContentExportResponse], content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.content.with_raw_response.export(
                account_id="",
                dlp_profile_information=[
                    {
                        "id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                        "entries": [
                            {
                                "id": "55ba2c6c-8ef4-4b2e-9148-e75e8b6ccac1",
                                "name": "Credit Card Numbers",
                                "profile_id": "e91a2360-da51-4fdf-9711-bcdecd462614",
                            }
                        ],
                        "name": "Financial Information",
                    }
                ],
            )
