# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture import (
    FindingTypeGetResponse,
    FindingTypeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindingTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            page=0,
            per_page=0,
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )


class TestAsyncFindingTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            page=0,
            per_page=0,
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )
