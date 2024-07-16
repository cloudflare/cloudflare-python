# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one import Item, Quota
from cloudflare.types.cloudforce_one.requests import (
    Priority,
    PriorityDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPriority:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        priority = client.cloudforce_one.requests.priority.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )
        assert_matches_type(Optional[Priority], priority, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.priority.with_raw_response.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = response.parse()
        assert_matches_type(Optional[Priority], priority, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.priority.with_streaming_response.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = response.parse()
            assert_matches_type(Optional[Priority], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.create(
                account_identifier="",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        priority = client.cloudforce_one.requests.priority.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.priority.with_raw_response.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = response.parse()
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.priority.with_streaming_response.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = response.parse()
            assert_matches_type(Optional[Item], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.update(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.update(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        priority = client.cloudforce_one.requests.priority.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.priority.with_raw_response.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = response.parse()
        assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.priority.with_streaming_response.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = response.parse()
            assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.delete(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.delete(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        priority = client.cloudforce_one.requests.priority.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.priority.with_raw_response.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = response.parse()
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.priority.with_streaming_response.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = response.parse()
            assert_matches_type(Optional[Item], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.get(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.get(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_quota(self, client: Cloudflare) -> None:
        priority = client.cloudforce_one.requests.priority.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Quota], priority, path=["response"])

    @parametrize
    def test_raw_response_quota(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.priority.with_raw_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = response.parse()
        assert_matches_type(Optional[Quota], priority, path=["response"])

    @parametrize
    def test_streaming_response_quota(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.priority.with_streaming_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = response.parse()
            assert_matches_type(Optional[Quota], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_quota(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.priority.with_raw_response.quota(
                "",
            )


class TestAsyncPriority:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        priority = await async_client.cloudforce_one.requests.priority.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )
        assert_matches_type(Optional[Priority], priority, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.priority.with_raw_response.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = await response.parse()
        assert_matches_type(Optional[Priority], priority, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.priority.with_streaming_response.create(
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = await response.parse()
            assert_matches_type(Optional[Priority], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.create(
                account_identifier="",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        priority = await async_client.cloudforce_one.requests.priority.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.priority.with_raw_response.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = await response.parse()
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.priority.with_streaming_response.update(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            labels=["DoS", "CVE"],
            priority=1,
            requirement="DoS attacks carried out by CVEs",
            tlp="clear",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = await response.parse()
            assert_matches_type(Optional[Item], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.update(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.update(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                labels=["DoS", "CVE"],
                priority=1,
                requirement="DoS attacks carried out by CVEs",
                tlp="clear",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        priority = await async_client.cloudforce_one.requests.priority.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.priority.with_raw_response.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = await response.parse()
        assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.priority.with_streaming_response.delete(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = await response.parse()
            assert_matches_type(PriorityDeleteResponse, priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.delete(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.delete(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        priority = await async_client.cloudforce_one.requests.priority.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.priority.with_raw_response.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = await response.parse()
        assert_matches_type(Optional[Item], priority, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.priority.with_streaming_response.get(
            priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = await response.parse()
            assert_matches_type(Optional[Item], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.get(
                priority_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `priority_identifer` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.get(
                priority_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_quota(self, async_client: AsyncCloudflare) -> None:
        priority = await async_client.cloudforce_one.requests.priority.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Quota], priority, path=["response"])

    @parametrize
    async def test_raw_response_quota(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.priority.with_raw_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        priority = await response.parse()
        assert_matches_type(Optional[Quota], priority, path=["response"])

    @parametrize
    async def test_streaming_response_quota(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.priority.with_streaming_response.quota(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            priority = await response.parse()
            assert_matches_type(Optional[Quota], priority, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_quota(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.priority.with_raw_response.quota(
                "",
            )
