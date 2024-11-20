# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security import SubmissionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        submission = client.email_security.submissions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        submission = client.email_security.submissions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=1,
            per_page=1,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            submission_id="submission_id",
            type="TEAM",
        )
        assert_matches_type(SyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.submissions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.submissions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.submissions.with_raw_response.list(
                account_id="",
            )


class TestAsyncSubmissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        submission = await async_client.email_security.submissions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        submission = await async_client.email_security.submissions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=1,
            per_page=1,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            submission_id="submission_id",
            type="TEAM",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.submissions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.submissions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[SubmissionListResponse], submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.submissions.with_raw_response.list(
                account_id="",
            )
