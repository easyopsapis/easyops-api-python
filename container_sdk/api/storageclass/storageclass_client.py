# -*- coding: utf-8 -*-
import os
import sys


import container_sdk.api.storageclass.create_pb2

import container_sdk.model.container.storage_class_pb2

import container_sdk.api.storageclass.delete_storageclass_pb2

import google.protobuf.empty_pb2

import container_sdk.api.storageclass.get_pb2

import container_sdk.api.storageclass.list_pb2

import container_sdk.api.storageclass.set_default_pb2

import container_sdk.api.storageclass.update_pb2

import container_sdk.utils.http_util
import google.protobuf.json_format


class StorageclassClient(object):
    def __init__(self, server_ip="", server_port=0, service_name="", host=""):
        """
        初始化client
        :param server_ip: 指定sdk请求的server_ip，为空时走名字服务路由
        :param server_port: 指定sdk请求的server_port，与server_ip一起使用, 为空时走名字服务路由
        :param service_name: 指定sdk请求的service_name, 为空时按契约名称路由。如果server_ip和service_name同时设置，server_ip优先级更高
        :param host: 指定sdk请求服务的host名称, 如cmdb.easyops-only.com
        """
        if server_ip == "" and server_port != 0 or server_ip != "" and server_port == 0:
            raise Exception("server_ip和server_port必须同时指定")
        self._server_ip = server_ip
        self._server_port = server_port
        self._service_name = service_name
        self._host = host

    
    def create(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.create_pb2.CreateRequest, int, str, int) -> container_sdk.model.container.storage_class_pb2.StorageClass
        """
        创建 StorageClass
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.storage_class_pb2.StorageClass
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.Create"
        uri = "/api/container/v1/storageclasses"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = container_sdk.model.container.storage_class_pb2.StorageClass()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_storage_class(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.delete_storageclass_pb2.DeleteStorageClassRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除 StorageClass
        :param request: delete_storage_class请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.DeleteStorageClass"
        uri = "/api/container/v1/storageclasses/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.get_pb2.GetRequest, int, str, int) -> container_sdk.api.storageclass.get_pb2.GetResponse
        """
        获取 StorageClass
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.storageclass.get_pb2.GetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.Get"
        uri = "/api/container/v1/storageclasses/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = container_sdk.api.storageclass.get_pb2.GetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.list_pb2.ListRequest, int, str, int) -> container_sdk.api.storageclass.list_pb2.ListResponse
        """
        获取 StorageClass 列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.storageclass.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.List"
        uri = "/api/container/v1/storageclasses"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = container_sdk.api.storageclass.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def set_default(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.set_default_pb2.SetDefaultRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        设置 StorageClass 为默认
        :param request: set_default请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.empty_pb2.Empty
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.SetDefault"
        uri = "/api/container/v1/storageclasses/{instanceId}/default".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (container_sdk.api.storageclass.update_pb2.UpdateRequest, int, str, int) -> container_sdk.model.container.storage_class_pb2.StorageClass
        """
        更新 StorageClass
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.storage_class_pb2.StorageClass
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.storageclass.Update"
        uri = "/api/container/v1/storageclasses/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=self._host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = container_sdk.model.container.storage_class_pb2.StorageClass()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
