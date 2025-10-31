# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.iam import (
    SSOGetResponse,
    SSOListResponse,
    SSOCreateResponse,
    SSODeleteResponse,
    SSOUpdateResponse,
    SSOBeginVerificationResponse,
)
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSSO:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        sso = client.iam.sso.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        )
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        sso = client.iam.sso.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
            begin_verification=True,
            use_fedramp_language=False,
        )
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.create(
                account_id="",
                email_domain="example.com",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        sso = client.iam.sso.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        sso = client.iam.sso.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            use_fedramp_language=False,
        )
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.update(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            client.iam.sso.with_raw_response.update(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        sso = client.iam.sso.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SSOListResponse], sso, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(SyncSinglePage[SSOListResponse], sso, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(SyncSinglePage[SSOListResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        sso = client.iam.sso.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.delete(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            client.iam.sso.with_raw_response.delete(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_begin_verification(self, client: Cloudflare) -> None:
        sso = client.iam.sso.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

    @parametrize
    def test_raw_response_begin_verification(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

    @parametrize
    def test_streaming_response_begin_verification(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_begin_verification(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.begin_verification(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            client.iam.sso.with_raw_response.begin_verification(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        sso = client.iam.sso.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.iam.sso.with_raw_response.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = response.parse()
        assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.iam.sso.with_streaming_response.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = response.parse()
            assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.sso.with_raw_response.get(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            client.iam.sso.with_raw_response.get(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSSO:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        )
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
            begin_verification=True,
            use_fedramp_language=False,
        )
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email_domain="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(Optional[SSOCreateResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.create(
                account_id="",
                email_domain="example.com",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            use_fedramp_language=False,
        )
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.update(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(Optional[SSOUpdateResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.update(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            await async_client.iam.sso.with_raw_response.update(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SSOListResponse], sso, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(AsyncSinglePage[SSOListResponse], sso, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(AsyncSinglePage[SSOListResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.delete(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(Optional[SSODeleteResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.delete(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            await async_client.iam.sso.with_raw_response.delete(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_begin_verification(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

    @parametrize
    async def test_raw_response_begin_verification(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

    @parametrize
    async def test_streaming_response_begin_verification(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.begin_verification(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(SSOBeginVerificationResponse, sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_begin_verification(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.begin_verification(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            await async_client.iam.sso.with_raw_response.begin_verification(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        sso = await async_client.iam.sso.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.sso.with_raw_response.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso = await response.parse()
        assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.sso.with_streaming_response.get(
            sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso = await response.parse()
            assert_matches_type(Optional[SSOGetResponse], sso, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.sso.with_raw_response.get(
                sso_connector_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sso_connector_id` but received ''"):
            await async_client.iam.sso.with_raw_response.get(
                sso_connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
