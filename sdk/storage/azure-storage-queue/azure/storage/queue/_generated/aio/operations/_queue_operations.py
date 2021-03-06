# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class QueueOperations:
    """QueueOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.storage.queue.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create(
        self,
        timeout: Optional[int] = None,
        metadata: Optional[str] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs
    ) -> None:
        """creates a new queue under the given account.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param metadata: Optional. Include this parameter to specify that the queue's metadata be
         returned as part of the response body. Note that metadata requested with this parameter must be
         stored in accordance with the naming restrictions imposed by the 2009-09-19 version of the
         Queue service. Beginning with this version, all metadata names must adhere to the naming
         conventions for C# identifiers.
        :type metadata: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/xml"

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 201:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
            response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if response.status_code == 204:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
            response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    create.metadata = {'url': '/{queueName}'}  # type: ignore

    async def delete(
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs
    ) -> None:
        """operation permanently deletes the specified queue.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/xml"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/{queueName}'}  # type: ignore

    async def get_properties(
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs
    ) -> None:
        """Retrieves user-defined metadata and queue properties on the specified queue. Metadata is
        associated with the queue as name-values pairs.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        comp = "metadata"
        accept = "application/xml"

        # Construct URL
        url = self.get_properties.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-meta']=self._deserialize('str', response.headers.get('x-ms-meta'))
        response_headers['x-ms-approximate-messages-count']=self._deserialize('int', response.headers.get('x-ms-approximate-messages-count'))
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_properties.metadata = {'url': '/{queueName}'}  # type: ignore

    async def set_metadata(
        self,
        timeout: Optional[int] = None,
        metadata: Optional[str] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs
    ) -> None:
        """sets user-defined metadata on the specified queue. Metadata is associated with the queue as
        name-value pairs.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param metadata: Optional. Include this parameter to specify that the queue's metadata be
         returned as part of the response body. Note that metadata requested with this parameter must be
         stored in accordance with the naming restrictions imposed by the 2009-09-19 version of the
         Queue service. Beginning with this version, all metadata names must adhere to the naming
         conventions for C# identifiers.
        :type metadata: str
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        comp = "metadata"
        accept = "application/xml"

        # Construct URL
        url = self.set_metadata.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_metadata.metadata = {'url': '/{queueName}'}  # type: ignore

    async def get_access_policy(
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs
    ) -> List["_models.SignedIdentifier"]:
        """returns details about any stored access policies specified on the queue that may be used with
        Shared Access Signatures.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of SignedIdentifier, or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.SignedIdentifier]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.SignedIdentifier"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        comp = "acl"
        accept = "application/xml"

        # Construct URL
        url = self.get_access_policy.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        deserialized = self._deserialize('[SignedIdentifier]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_access_policy.metadata = {'url': '/{queueName}'}  # type: ignore

    async def set_access_policy(
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        queue_acl: Optional[List["_models.SignedIdentifier"]] = None,
        **kwargs
    ) -> None:
        """sets stored access policies for the queue that may be used with Shared Access Signatures.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param queue_acl: the acls for the queue.
        :type queue_acl: list[~azure.storage.queue.models.SignedIdentifier]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        comp = "acl"
        content_type = kwargs.pop("content_type", "application/xml")
        accept = "application/xml"

        # Construct URL
        url = self.set_access_policy.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        serialization_ctxt = {'xml': {'name': 'SignedIdentifiers', 'wrapped': True}}
        if queue_acl is not None:
            body_content = self._serialize.body(queue_acl, '[SignedIdentifier]', is_xml=True, serialization_ctxt=serialization_ctxt)
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_access_policy.metadata = {'url': '/{queueName}'}  # type: ignore
