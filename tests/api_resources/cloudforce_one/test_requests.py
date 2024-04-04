# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.shared import UnnamedSchemaRef171
from cloudflare.types.cloudforce_one import (
    CloudforceOneQuota,
    CloudforceOneRequestItem,
    CloudforceOneRequestTypes,
    CloudforceOneRequestListItem,
    CloudforceOneRequestConstants,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(SyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
            completed_after=parse_datetime("2022-01-01T00:00:00Z"),
            completed_before=parse_datetime("2024-01-01T00:00:00Z"),
            created_after=parse_datetime("2022-01-01T00:00:00Z"),
            created_before=parse_datetime("2024-01-01T00:00:00Z"),
            request_type="Victomology",
            sort_by="created",
            sort_order="asc",
            status="open",
        )
        assert_matches_type(SyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.list(
                "",
                page=0,
                per_page=10,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_constants(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_constants(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_constants(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_constants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.constants(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_quota(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneQuota, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_quota(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneQuota, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_quota(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneQuota, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_quota(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.quota(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_types(self, client: Cloudflare) -> None:
        request = client.cloudforce_one.requests.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_types(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.with_raw_response.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_types(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.with_streaming_response.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_types(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.with_raw_response.types(
                "",
            )


class TestAsyncRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(AsyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
            completed_after=parse_datetime("2022-01-01T00:00:00Z"),
            completed_before=parse_datetime("2024-01-01T00:00:00Z"),
            created_after=parse_datetime("2022-01-01T00:00:00Z"),
            created_before=parse_datetime("2024-01-01T00:00:00Z"),
            request_type="Victomology",
            sort_by="created",
            sort_order="asc",
            status="open",
        )
        assert_matches_type(AsyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[CloudforceOneRequestListItem], request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.list(
                "",
                page=0,
                per_page=10,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(UnnamedSchemaRef171, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_constants(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_constants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_constants(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.constants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneRequestConstants, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_constants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.constants(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneRequestItem, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_quota(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneQuota, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_quota(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneQuota, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_quota(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneQuota, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_quota(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.quota(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_types(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.cloudforce_one.requests.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_types(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.with_raw_response.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_types(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.with_streaming_response.types(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(CloudforceOneRequestTypes, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_types(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.with_raw_response.types(
                "",
            )
