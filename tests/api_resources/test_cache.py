# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import (
    CachePurgeResponse,
    CacheInvalidateResponse,
    CachePurgeEnvironmentResponse,
    CacheInvalidateEnvironmentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_invalidate_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_1(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_1(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    def test_method_invalidate_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_2(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_2(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    def test_method_invalidate_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_3(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_3(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    def test_method_invalidate_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_4(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_4(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    def test_method_invalidate_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_5(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_5(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    def test_method_invalidate_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_method_invalidate_with_all_params_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_invalidate_overload_6(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_invalidate_overload_6(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invalidate_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_1(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_1(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_2(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_2(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_3(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_3(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_4(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_4(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_5(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_5(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_invalidate_environment_with_all_params_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_invalidate_environment_overload_6(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_invalidate_environment_overload_6(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_invalidate_environment_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_purge_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_1(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_1(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_2(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_2(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_3(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_3(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_4(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_4(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_5(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_5(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_6(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_6(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_1(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_1(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_2(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_2(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_3(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_3(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_4(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_4(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_5(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_5(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_purge_environment_with_all_params_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_purge_environment_overload_6(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_purge_environment_overload_6(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_purge_environment_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCache:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_invalidate_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    async def test_method_invalidate_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    async def test_method_invalidate_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    async def test_method_invalidate_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    async def test_method_invalidate_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @parametrize
    async def test_method_invalidate_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_method_invalidate_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_invalidate_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_invalidate_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invalidate_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_5(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_invalidate_environment_with_all_params_overload_6(
        self, async_client: AsyncCloudflare
    ) -> None:
        cache = await async_client.cache.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_invalidate_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_invalidate_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.invalidate_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CacheInvalidateEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_invalidate_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.invalidate_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            tags=["product-1234", "homepage"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefixes=["www.example.com/blog/", "images.example.com/avatars/"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=["https://www.example.com/css/styles.css", "https://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_purge_environment_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "https://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "DE",
                    },
                    "url": "https://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_purge_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_purge_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge_environment(
            environment_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeEnvironmentResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_purge_environment_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.cache.with_raw_response.purge_environment(
                environment_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
