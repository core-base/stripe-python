# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Configuration(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A Configurations object represents how features should be configured for terminal readers.
    """

    OBJECT_NAME = "terminal.configuration"
