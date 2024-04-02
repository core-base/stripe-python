# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Configuration(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A portal configuration describes the functionality and behavior of a portal session.
    """

    OBJECT_NAME = "billing_portal.configuration"
