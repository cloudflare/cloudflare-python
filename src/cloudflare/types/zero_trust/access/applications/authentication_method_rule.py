# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["AuthenticationMethodRule", "AuthMethod"]


class AuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method
    https://datatracker.ietf.org/doc/html/rfc8176#section-2.
    """


class AuthenticationMethodRule(BaseModel):
    auth_method: AuthMethod
