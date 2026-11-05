# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.zero_trust.access.user_populations import (
    UserGetResponse,
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
    UserReplaceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            active=True,
            display_name="displayName",
            emails=[
                {
                    "primary": True,
                    "type": "type",
                    "value": "value",
                }
            ],
            external_id="externalId",
            meta={
                "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                "location": "https://example.com",
                "resource_type": "resourceType",
                "version": "version",
            },
            name={
                "family_name": "familyName",
                "formatted": "formatted",
                "given_name": "givenName",
                "honorific_prefix": "honorificPrefix",
                "honorific_suffix": "honorificSuffix",
                "middle_name": "middleName",
            },
            schemas=["string"],
            user_name="userName",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.create(
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.create(
                user_population_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[
                {
                    "op": "add",
                    "path": "path",
                    "value": "string",
                }
            ],
            schemas=["string"],
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                operations=[{"op": "add"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
                operations=[{"op": "add"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                operations=[{"op": "add"}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            attributes="attributes",
            count=0,
            excluded_attributes="excludedAttributes",
            filter="filter",
            start_index=1,
        )
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.list(
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.list(
                user_population_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            attributes="attributes",
            excluded_attributes="excludedAttributes",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserGetResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_replace(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.user_populations.users.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            active=True,
            display_name="displayName",
            emails=[
                {
                    "primary": True,
                    "type": "type",
                    "value": "value",
                }
            ],
            external_id="externalId",
            meta={
                "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                "location": "https://example.com",
                "resource_type": "resourceType",
                "version": "version",
            },
            name={
                "family_name": "familyName",
                "formatted": "formatted",
                "given_name": "givenName",
                "honorific_prefix": "honorificPrefix",
                "honorific_suffix": "honorificSuffix",
                "middle_name": "middleName",
            },
            schemas=["string"],
            user_name="userName",
        )
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.user_populations.users.with_raw_response.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Cloudflare) -> None:
        with client.zero_trust.access.user_populations.users.with_streaming_response.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            active=True,
            display_name="displayName",
            emails=[
                {
                    "primary": True,
                    "type": "type",
                    "value": "value",
                }
            ],
            external_id="externalId",
            meta={
                "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                "location": "https://example.com",
                "resource_type": "resourceType",
                "version": "version",
            },
            name={
                "family_name": "familyName",
                "formatted": "formatted",
                "given_name": "givenName",
                "honorific_prefix": "honorificPrefix",
                "honorific_suffix": "honorificSuffix",
                "middle_name": "middleName",
            },
            schemas=["string"],
            user_name="userName",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.create(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.create(
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.create(
                user_population_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[
                {
                    "op": "add",
                    "path": "path",
                    "value": "string",
                }
            ],
            schemas=["string"],
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.update(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            operations=[{"op": "add"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                operations=[{"op": "add"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
                operations=[{"op": "add"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.update(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                operations=[{"op": "add"}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            attributes="attributes",
            count=0,
            excluded_attributes="excludedAttributes",
            filter="filter",
            start_index=1,
        )
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserListResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.list(
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.list(
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.list(
                user_population_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.delete(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.delete(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            attributes="attributes",
            excluded_attributes="excludedAttributes",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.get(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserGetResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.get(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.user_populations.users.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            active=True,
            display_name="displayName",
            emails=[
                {
                    "primary": True,
                    "type": "type",
                    "value": "value",
                }
            ],
            external_id="externalId",
            meta={
                "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                "location": "https://example.com",
                "resource_type": "resourceType",
                "version": "version",
            },
            name={
                "family_name": "familyName",
                "formatted": "formatted",
                "given_name": "givenName",
                "honorific_prefix": "honorificPrefix",
                "honorific_suffix": "honorificSuffix",
                "middle_name": "middleName",
            },
            schemas=["string"],
            user_name="userName",
        )
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.user_populations.users.with_raw_response.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.user_populations.users.with_streaming_response.replace(
            user_id="user_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserReplaceResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="user_id",
                account_id="",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_population_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="user_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.user_populations.users.with_raw_response.replace(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_population_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )
