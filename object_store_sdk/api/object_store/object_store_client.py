# -*- coding: utf-8 -*-
import os
import sys


import object_store_sdk.api.object_store.createBucket_pb2

import google.protobuf.empty_pb2

import object_store_sdk.api.object_store.listBuckets_pb2

import object_store_sdk.api.object_store.listObjects_pb2

import object_store_sdk.api.object_store.putObject_pb2

import object_store_sdk.api.object_store.removeObject_pb2

import object_store_sdk.utils.http_util
import google.protobuf.json_format


class ObjectStoreClient(object):
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

    
    def create_bucket(self, request, org, user, timeout=10):
        # type: (object_store_sdk.api.object_store.createBucket_pb2.CreateBucketRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        创建对象存储桶
        :param request: create_bucket请求
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
            route_name = "easyops.api.object_store.object_store.CreateBucket"
        uri = "/api/v1/objectStore/bucket/{bucketName}".format(
            bucketName=request.bucketName,
        )
        requestParam = request
        
        rsp_obj = object_store_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.object_store_sdk",
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
    
    def list_buckets(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> object_store_sdk.api.object_store.listBuckets_pb2.ListBucketsResponse
        """
        列出所有对象存储桶
        :param request: list_buckets请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: object_store_sdk.api.object_store.listBuckets_pb2.ListBucketsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.object_store.object_store.ListBuckets"
        uri = "/api/v1/objectStore/bucket"
        
        requestParam = request
        
        rsp_obj = object_store_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.object_store_sdk",
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
        rsp = object_store_sdk.api.object_store.listBuckets_pb2.ListBucketsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_objects(self, request, org, user, timeout=10):
        # type: (object_store_sdk.api.object_store.listObjects_pb2.ListObjectsRequest, int, str, int) -> object_store_sdk.api.object_store.listObjects_pb2.ListObjectsResponse
        """
        列出对象存储桶中所有对象
        :param request: list_objects请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: object_store_sdk.api.object_store.listObjects_pb2.ListObjectsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.object_store.object_store.ListObjects"
        uri = "/api/v1/objectStore/bucket/{bucketName}/object".format(
            bucketName=request.bucketName,
        )
        requestParam = request
        
        rsp_obj = object_store_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.object_store_sdk",
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
        rsp = object_store_sdk.api.object_store.listObjects_pb2.ListObjectsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def put_object(self, request, org, user, timeout=10):
        # type: (object_store_sdk.api.object_store.putObject_pb2.PutObjectRequest, int, str, int) -> object_store_sdk.api.object_store.putObject_pb2.PutObjectResponse
        """
        上传对象
        :param request: put_object请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: object_store_sdk.api.object_store.putObject_pb2.PutObjectResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.object_store.object_store.PutObject"
        uri = "/api/v1/objectStore/bucket/{bucketName}/object".format(
            bucketName=request.bucketName,
        )
        requestParam = request
        
        rsp_obj = object_store_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.object_store_sdk",
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
        rsp = object_store_sdk.api.object_store.putObject_pb2.PutObjectResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def remove_object(self, request, org, user, timeout=10):
        # type: (object_store_sdk.api.object_store.removeObject_pb2.RemoveObjectRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除对象
        :param request: remove_object请求
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
            route_name = "easyops.api.object_store.object_store.RemoveObject"
        uri = "/api/v1/objectStore/bucket/{bucketName}/object/{objectName}".format(
            bucketName=request.bucketName,
            objectName=request.objectName,
        )
        requestParam = request
        
        rsp_obj = object_store_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.object_store_sdk",
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
    
