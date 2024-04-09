# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.shared import UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846
from cloudflare.types.cloudforce_one.requests import (
    Message,
    MessageGetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="Can you elaborate on the type of DoS that occurred?",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.message.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.message.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.message.with_raw_response.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.message.with_streaming_response.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.update(
                0,
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.update(
                0,
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.message.with_raw_response.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.message.with_streaming_response.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.delete(
                0,
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.delete(
                0,
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        message = client.cloudforce_one.requests.message.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
            after=parse_datetime("2022-01-01T00:00:00Z"),
            before=parse_datetime("2024-01-01T00:00:00Z"),
            sort_by="created",
            sort_order="asc",
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.message.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.message.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                page=0,
                per_page=10,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.message.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=0,
                per_page=10,
            )


class TestAsyncMessage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="Can you elaborate on the type of DoS that occurred?",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.message.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.message.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            content="What regions were most effected by the recent DoS?",
            priority="routine",
            request_type="Victomology",
            summary="DoS attack",
            tlp="clear",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.message.with_raw_response.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.message.with_streaming_response.update(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.update(
                0,
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.update(
                0,
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.message.with_raw_response.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.message.with_streaming_response.delete(
            0,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.delete(
                0,
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.delete(
                0,
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        message = await async_client.cloudforce_one.requests.message.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
            after=parse_datetime("2022-01-01T00:00:00Z"),
            before=parse_datetime("2024-01-01T00:00:00Z"),
            sort_by="created",
            sort_order="asc",
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.message.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.message.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                page=0,
                per_page=10,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.message.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=0,
                per_page=10,
            )
