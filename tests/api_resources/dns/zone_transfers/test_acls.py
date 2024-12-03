# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.dns.zone_transfers import ACL, ACLDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACLs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        acl = client.dns.zone_transfers.acls.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.acls.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.acls.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.create(
                account_id="",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        acl = client.dns.zone_transfers.acls.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.acls.with_raw_response.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.acls.with_streaming_response.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.update(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.update(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        acl = client.dns.zone_transfers.acls.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.acls.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.acls.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        acl = client.dns.zone_transfers.acls.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.acls.with_raw_response.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.acls.with_streaming_response.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.delete(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.delete(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        acl = client.dns.zone_transfers.acls.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.acls.with_raw_response.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.acls.with_streaming_response.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.get(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.dns.zone_transfers.acls.with_raw_response.get(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )


class TestAsyncACLs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.dns.zone_transfers.acls.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.acls.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.acls.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.create(
                account_id="",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.dns.zone_transfers.acls.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.acls.with_raw_response.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.acls.with_streaming_response.update(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.update(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.update(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                ip_range="192.0.2.53/28",
                name="my-acl-1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.dns.zone_transfers.acls.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.acls.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.acls.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.dns.zone_transfers.acls.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.acls.with_raw_response.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.acls.with_streaming_response.delete(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(Optional[ACLDeleteResponse], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.delete(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.delete(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.dns.zone_transfers.acls.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.acls.with_raw_response.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(Optional[ACL], acl, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.acls.with_streaming_response.get(
            acl_id="23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(Optional[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.get(
                acl_id="23ff594956f20c2a721606e94745a8aa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.dns.zone_transfers.acls.with_raw_response.get(
                acl_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )
