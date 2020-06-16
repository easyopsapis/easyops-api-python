# -*- coding: utf-8 -*-
import os
import sys


import collector_center_sdk.api.collection_config.create_collection_config_pb2

import collector_center_sdk.api.collection_config.debug_collection_config_pb2

import collector_center_sdk.api.collection_config.debug_collection_config_callback_pb2

import collector_center_sdk.api.collection_config.delete_collection_config_pb2

import collector_center_sdk.api.collection_config.detail_collection_config_pb2

import collector_center_sdk.api.collection_config.detail_collection_config_debug_pb2

import collector_center_sdk.api.collection_config.disable_collection_config_pb2

import collector_center_sdk.api.collection_config.list_collection_config_pb2

import collector_center_sdk.api.collection_config.list_collection_config_job_pb2

import collector_center_sdk.api.collection_config.maintain_collection_config_job_pb2

import collector_center_sdk.api.collection_config.update_collection_config_pb2

import collector_center_sdk.utils.http_util
import google.protobuf.json_format


class CollectionConfigClient(object):
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

    
    def create_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.create_collection_config_pb2.CreateCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.create_collection_config_pb2.CreateCollectionConfigResponse
        """
        创建采集配置
        :param request: create_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.create_collection_config_pb2.CreateCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.CreateCollectionConfig"
        uri = "/api/v1/collection_config"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.create_collection_config_pb2.CreateCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def debug_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.debug_collection_config_pb2.DebugCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.debug_collection_config_pb2.DebugCollectionConfigResponse
        """
        调试采集配置
        :param request: debug_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.debug_collection_config_pb2.DebugCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DebugCollectionConfig"
        uri = "/api/v1/collection_config/debug"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.debug_collection_config_pb2.DebugCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def debug_collection_config_callback(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.debug_collection_config_callback_pb2.DebugCollectionConfigCallbackRequest, int, str, int) -> collector_center_sdk.api.collection_config.debug_collection_config_callback_pb2.DebugCollectionConfigCallbackResponse
        """
        接收command回调
        :param request: debug_collection_config_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.debug_collection_config_callback_pb2.DebugCollectionConfigCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DebugCollectionConfigCallback"
        uri = "/api/v1/debug/cmd/callback"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.debug_collection_config_callback_pb2.DebugCollectionConfigCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.delete_collection_config_pb2.DeleteCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.delete_collection_config_pb2.DeleteCollectionConfigResponse
        """
        删除采集配置
        :param request: delete_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.delete_collection_config_pb2.DeleteCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DeleteCollectionConfig"
        uri = "/api/v1/collection_config/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.delete_collection_config_pb2.DeleteCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.detail_collection_config_pb2.DetailCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.detail_collection_config_pb2.DetailCollectionConfigResponse
        """
        查看采集配置
        :param request: detail_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.detail_collection_config_pb2.DetailCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DetailCollectionConfig"
        uri = "/api/v1/collection_config/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.detail_collection_config_pb2.DetailCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def detail_collection_config_debug(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.detail_collection_config_debug_pb2.DetailCollectionConfigDebugRequest, int, str, int) -> collector_center_sdk.api.collection_config.detail_collection_config_debug_pb2.DetailCollectionConfigDebugResponse
        """
        查看采集配置调试结果
        :param request: detail_collection_config_debug请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.detail_collection_config_debug_pb2.DetailCollectionConfigDebugResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DetailCollectionConfigDebug"
        uri = "/api/v1/debug/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.detail_collection_config_debug_pb2.DetailCollectionConfigDebugResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def disable_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.disable_collection_config_pb2.DisableCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.disable_collection_config_pb2.DisableCollectionConfigResponse
        """
        启禁用采集配置
        :param request: disable_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.disable_collection_config_pb2.DisableCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.DisableCollectionConfig"
        uri = "/api/v1/collection_config/{id}/disabled".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.disable_collection_config_pb2.DisableCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.list_collection_config_pb2.ListCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.list_collection_config_pb2.ListCollectionConfigResponse
        """
        查看采集配置列表
        :param request: list_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.list_collection_config_pb2.ListCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.ListCollectionConfig"
        uri = "/api/v1/collection_config"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.list_collection_config_pb2.ListCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_collection_config_jobs(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.list_collection_config_job_pb2.ListCollectionConfigJobsRequest, int, str, int) -> collector_center_sdk.api.collection_config.list_collection_config_job_pb2.ListCollectionConfigJobsResponse
        """
        查看单个采集配置的任务
        :param request: list_collection_config_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.list_collection_config_job_pb2.ListCollectionConfigJobsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.ListCollectionConfigJobs"
        uri = "/api/v1/collection_config/{confId}/jobs".format(
            confId=request.confId,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.list_collection_config_job_pb2.ListCollectionConfigJobsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def maintain_collection_config_job(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.maintain_collection_config_job_pb2.MaintainCollectionConfigJobRequest, int, str, int) -> collector_center_sdk.api.collection_config.maintain_collection_config_job_pb2.MaintainCollectionConfigJobResponse
        """
        维护配置生成任务
        :param request: maintain_collection_config_job请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.maintain_collection_config_job_pb2.MaintainCollectionConfigJobResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.MaintainCollectionConfigJob"
        uri = "/api/v1/collection_config/maintain_job"
        
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.maintain_collection_config_job_pb2.MaintainCollectionConfigJobResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_collection_config(self, request, org, user, timeout=10):
        # type: (collector_center_sdk.api.collection_config.update_collection_config_pb2.UpdateCollectionConfigRequest, int, str, int) -> collector_center_sdk.api.collection_config.update_collection_config_pb2.UpdateCollectionConfigResponse
        """
        更新采集配置
        :param request: update_collection_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: collector_center_sdk.api.collection_config.update_collection_config_pb2.UpdateCollectionConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.collector_center.collection_config.UpdateCollectionConfig"
        uri = "/api/v1/collection_config/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = collector_center_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.collector_center_sdk",
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
        rsp = collector_center_sdk.api.collection_config.update_collection_config_pb2.UpdateCollectionConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
