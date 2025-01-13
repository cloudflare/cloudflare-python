# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.settings import (
    TrustedDomainGetResponse,
    TrustedDomainEditResponse,
    TrustedDomainListResponse,
    TrustedDomainCreateResponse,
    TrustedDomainDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrustedDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
            comments=None,
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.create(
                account_id="",
                is_recent=True,
                is_regex=False,
                is_similarity=False,
                pattern="example.com",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.create(
                account_id="",
                body=[
                    {
                        "is_recent": True,
                        "is_regex": False,
                        "is_similarity": False,
                        "pattern": "example.com",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_recent=True,
            is_similarity=True,
            order="pattern",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.delete(
                trusted_domain_id=2401,
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_recent=True,
            is_regex=True,
            is_similarity=True,
            pattern="x",
        )
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.edit(
                trusted_domain_id=2401,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        trusted_domain = client.email_security.settings.trusted_domains.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.settings.trusted_domains.with_raw_response.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = response.parse()
        assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.trusted_domains.with_streaming_response.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = response.parse()
            assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.trusted_domains.with_raw_response.get(
                trusted_domain_id=2401,
                account_id="",
            )


class TestAsyncTrustedDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
            comments=None,
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recent=True,
            is_regex=False,
            is_similarity=False,
            pattern="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.create(
                account_id="",
                is_recent=True,
                is_regex=False,
                is_similarity=False,
                pattern="example.com",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        )
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "is_recent": True,
                    "is_regex": False,
                    "is_similarity": False,
                    "pattern": "example.com",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(TrustedDomainCreateResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.create(
                account_id="",
                body=[
                    {
                        "is_recent": True,
                        "is_regex": False,
                        "is_similarity": False,
                        "pattern": "example.com",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_recent=True,
            is_similarity=True,
            order="pattern",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[TrustedDomainListResponse], trusted_domain, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.delete(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(TrustedDomainDeleteResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.delete(
                trusted_domain_id=2401,
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_recent=True,
            is_regex=True,
            is_similarity=True,
            pattern="x",
        )
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.edit(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(TrustedDomainEditResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.edit(
                trusted_domain_id=2401,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        trusted_domain = await async_client.email_security.settings.trusted_domains.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.trusted_domains.with_raw_response.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_domain = await response.parse()
        assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.trusted_domains.with_streaming_response.get(
            trusted_domain_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_domain = await response.parse()
            assert_matches_type(TrustedDomainGetResponse, trusted_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.trusted_domains.with_raw_response.get(
                trusted_domain_id=2401,
                account_id="",
            )
