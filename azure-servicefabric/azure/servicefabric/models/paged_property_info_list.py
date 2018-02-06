# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PagedPropertyInfoList(Model):
    """The paged list of Service Fabric properties under a given name. The list is
    paged when all of the results cannot fit in a single message. The next set
    of results can be obtained by executing the same query with the
    continuation token provided in this list.

    :param continuation_token: The continuation token parameter is used to
     obtain next set of results. The continuation token is included in the
     response of the API when the results from the system do not fit in a
     single response. When this value is passed to the next API call, the API
     returns next set of results. If there are no further results then the
     continuation token is not included in the response.
    :type continuation_token: str
    :param is_consistent: Indicates whether any property under the given name
     has been modified during the enumeration. If there was a modification,
     this property value is false.
    :type is_consistent: bool
    :param properties: List of property information.
    :type properties: list[~azure.servicefabric.models.PropertyInfo]
    """

    _attribute_map = {
        'continuation_token': {'key': 'ContinuationToken', 'type': 'str'},
        'is_consistent': {'key': 'IsConsistent', 'type': 'bool'},
        'properties': {'key': 'Properties', 'type': '[PropertyInfo]'},
    }

    def __init__(self, continuation_token=None, is_consistent=None, properties=None):
        super(PagedPropertyInfoList, self).__init__()
        self.continuation_token = continuation_token
        self.is_consistent = is_consistent
        self.properties = properties
