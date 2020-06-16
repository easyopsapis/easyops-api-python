# -*- coding: utf-8 -*-
import os
import sys


import flow_sdk.api.basic.batch_update_permission_pb2

import google.protobuf.struct_pb2

import flow_sdk.model.flow.flow_pb2

import flow_sdk.api.basic.delete_pb2

import flow_sdk.api.basic.get_pb2

import google.protobuf.empty_pb2

import flow_sdk.api.basic.get_categories_pb2

import flow_sdk.api.basic.get_version_list_pb2

import flow_sdk.api.basic.list_pb2

import flow_sdk.utils.http_util
import google.protobuf.json_format


class BasicClient(object):
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

    
    def update_batch_permission(self, request, org, user, timeout=10):
        # type: (flow_sdk.api.basic.batch_update_permission_pb2.UpdateBatchPermissionRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        批量更新流程权限
        :param request: update_batch_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.struct_pb2.Struct
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.UpdateBatchPermission"
        uri = "/flows/batch/permission"
        
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flow_sdk",
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_flow(self, request, org, user, timeout=10):
        # type: (flow_sdk.model.flow.flow_pb2.Flow, int, str, int) -> flow_sdk.model.flow.flow_pb2.Flow
        """
        创建流程
        :param request: create_flow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.model.flow.flow_pb2.Flow
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.CreateFlow"
        uri = "/flows"
        
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.model.flow.flow_pb2.Flow()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_flow(self, request, org, user, timeout=10):
        # type: (flow_sdk.api.basic.delete_pb2.DeleteFlowRequest, int, str, int) -> flow_sdk.api.basic.delete_pb2.DeleteFlowResponse
        """
        删除流程
        :param request: delete_flow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.api.basic.delete_pb2.DeleteFlowResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.DeleteFlow"
        uri = "/flows/{flowId}".format(
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.api.basic.delete_pb2.DeleteFlowResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_flow_info(self, request, org, user, timeout=10):
        # type: (flow_sdk.api.basic.get_pb2.GetFlowInfoRequest, int, str, int) -> flow_sdk.model.flow.flow_pb2.Flow
        """
        获取流程信息
        :param request: get_flow_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.model.flow.flow_pb2.Flow
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.GetFlowInfo"
        uri = "/flows/{flowId}".format(
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.model.flow.flow_pb2.Flow()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_flow_categories(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> flow_sdk.api.basic.get_categories_pb2.GetFlowCategoriesResponse
        """
        查询流程分类
        :param request: get_flow_categories请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.api.basic.get_categories_pb2.GetFlowCategoriesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.GetFlowCategories"
        uri = "/flow_categories"
        
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.api.basic.get_categories_pb2.GetFlowCategoriesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_version_list(self, request, org, user, timeout=10):
        # type: (flow_sdk.api.basic.get_version_list_pb2.GetVersionListRequest, int, str, int) -> flow_sdk.api.basic.get_version_list_pb2.GetVersionListResponse
        """
        获取流程版本列表
        :param request: get_version_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.api.basic.get_version_list_pb2.GetVersionListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.GetVersionList"
        uri = "/flows/{flowId}/versions".format(
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.api.basic.get_version_list_pb2.GetVersionListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_flow_list(self, request, org, user, timeout=10):
        # type: (flow_sdk.api.basic.list_pb2.GetFlowListRequest, int, str, int) -> flow_sdk.api.basic.list_pb2.GetFlowListResponse
        """
        获取流程列表
        :param request: get_flow_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.api.basic.list_pb2.GetFlowListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.GetFlowList"
        uri = "/flows"
        
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.api.basic.list_pb2.GetFlowListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_flow(self, request, org, user, timeout=10):
        # type: (flow_sdk.model.flow.flow_pb2.Flow, int, str, int) -> flow_sdk.model.flow.flow_pb2.Flow
        """
        更新流程
        :param request: update_flow请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flow_sdk.model.flow.flow_pb2.Flow
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flow.basic.UpdateFlow"
        uri = "/flows/{flowId}".format(
            flowId=request.flowId,
        )
        requestParam = request
        
        rsp_obj = flow_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flow_sdk",
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
        rsp = flow_sdk.model.flow.flow_pb2.Flow()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
