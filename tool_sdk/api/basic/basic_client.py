# -*- coding: utf-8 -*-
import os
import sys


import tool_sdk.api.basic.batch_get_tool_detail_pb2

import tool_sdk.api.basic.batch_update_tool_permission_pb2

import tool_sdk.model.tool.tool_pb2

import tool_sdk.api.basic.create_tool_pb2

import tool_sdk.api.basic.delete_tool_pb2

import google.protobuf.empty_pb2

import tool_sdk.api.basic.disable_tool_pb2

import tool_sdk.api.basic.get_reference_tool_object_pb2

import tool_sdk.api.basic.get_reference_tool_object_by_vId_pb2

import tool_sdk.api.basic.get_tool_pb2

import tool_sdk.api.basic.get_tool_categories_pb2

import tool_sdk.api.basic.get_tool_global_config_pb2

import tool_sdk.api.basic.list_tool_pb2

import tool_sdk.api.basic.tool_approval_pb2

import tool_sdk.utils.http_util
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

    
    def batch_get_tool_detail(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.batch_get_tool_detail_pb2.BatchGetToolDetailRequest, int, str, int) -> tool_sdk.api.basic.batch_get_tool_detail_pb2.BatchGetToolDetailResponse
        """
        通过工具id批量获取工具详细信息
        :param request: batch_get_tool_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.batch_get_tool_detail_pb2.BatchGetToolDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.BatchGetToolDetail"
        uri = "/tools/batch/{toolIds}".format(
            toolIds=request.toolIds,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.batch_get_tool_detail_pb2.BatchGetToolDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def batch_update_tool_permission(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.batch_update_tool_permission_pb2.BatchUpdateToolPermissionRequest, int, str, int) -> tool_sdk.api.basic.batch_update_tool_permission_pb2.BatchUpdateToolPermissionResponse
        """
        批量修改工具权限
        :param request: batch_update_tool_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.batch_update_tool_permission_pb2.BatchUpdateToolPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.BatchUpdateToolPermission"
        uri = "/tools/batch/permission"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.batch_update_tool_permission_pb2.BatchUpdateToolPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.model.tool.tool_pb2.Tool, int, str, int) -> tool_sdk.api.basic.create_tool_pb2.CreateToolResponse
        """
        创建工具
        :param request: create_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.create_tool_pb2.CreateToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.CreateTool"
        uri = "/tools"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.create_tool_pb2.CreateToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.delete_tool_pb2.DeleteToolRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除工具
        :param request: delete_tool请求
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
            route_name = "easyops.api.tool.basic.DeleteTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.tool_sdk",
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
    
    def disable_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.disable_tool_pb2.DisableToolRequest, int, str, int) -> tool_sdk.api.basic.disable_tool_pb2.DisableToolResponse
        """
        禁用工具开关
        :param request: disable_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.disable_tool_pb2.DisableToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.DisableTool"
        uri = "/tools/{toolId}/disable".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.disable_tool_pb2.DisableToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_reference_tool_object(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.get_reference_tool_object_pb2.GetReferenceToolObjectRequest, int, str, int) -> tool_sdk.api.basic.get_reference_tool_object_pb2.GetReferenceToolObjectResponse
        """
        通过版本id获取引用工具对象列表
        :param request: get_reference_tool_object请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.get_reference_tool_object_pb2.GetReferenceToolObjectResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetReferenceToolObject"
        uri = "/referenceToolObject/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.get_reference_tool_object_pb2.GetReferenceToolObjectResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_reference_tool_object_by_vid(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.get_reference_tool_object_by_vId_pb2.GetReferenceToolObjectByVidRequest, int, str, int) -> tool_sdk.api.basic.get_reference_tool_object_by_vId_pb2.GetReferenceToolObjectByVidResponse
        """
        获取引用工具对象列表
        :param request: get_reference_tool_object_by_vid请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.get_reference_tool_object_by_vId_pb2.GetReferenceToolObjectByVidResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetReferenceToolObjectByVid"
        uri = "/referenceToolObject/{toolId}//version/{vId}".format(
            toolId=request.toolId,
            vId=request.vId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.get_reference_tool_object_by_vId_pb2.GetReferenceToolObjectByVidResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.get_tool_pb2.GetToolRequest, int, str, int) -> tool_sdk.model.tool.tool_pb2.Tool
        """
        获取工具信息
        :param request: get_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.tool_pb2.Tool
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.tool_pb2.Tool()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_tool_categories(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> tool_sdk.api.basic.get_tool_categories_pb2.GetToolCategoriesResponse
        """
        批量获取工具分类
        :param request: get_tool_categories请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.get_tool_categories_pb2.GetToolCategoriesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetToolCategories"
        uri = "/tool_categories"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.get_tool_categories_pb2.GetToolCategoriesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_tool_global_config(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> tool_sdk.api.basic.get_tool_global_config_pb2.GetToolGlobalConfigResponse
        """
        获取工具全局配置
        :param request: get_tool_global_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.get_tool_global_config_pb2.GetToolGlobalConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.GetToolGlobalConfig"
        uri = "/toolsGlobalConfig"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.get_tool_global_config_pb2.GetToolGlobalConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.list_tool_pb2.ListToolRequest, int, str, int) -> tool_sdk.api.basic.list_tool_pb2.ListToolResponse
        """
        批量获取工具信息
        :param request: list_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.list_tool_pb2.ListToolResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.ListTool"
        uri = "/tools"
        
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.list_tool_pb2.ListToolResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def tool_approval(self, request, org, user, timeout=10):
        # type: (tool_sdk.api.basic.tool_approval_pb2.ToolApprovalRequest, int, str, int) -> tool_sdk.api.basic.tool_approval_pb2.ToolApprovalResponse
        """
        工具审批
        :param request: tool_approval请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.api.basic.tool_approval_pb2.ToolApprovalResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.ToolApproval"
        uri = "/tools/{toolId}/changeEnvType".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.api.basic.tool_approval_pb2.ToolApprovalResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_tool(self, request, org, user, timeout=10):
        # type: (tool_sdk.model.tool.tool_pb2.Tool, int, str, int) -> tool_sdk.model.tool.tool_pb2.Tool
        """
        修改工具
        :param request: update_tool请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: tool_sdk.model.tool.tool_pb2.Tool
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.tool.basic.UpdateTool"
        uri = "/tools/{toolId}".format(
            toolId=request.toolId,
        )
        requestParam = request
        
        rsp_obj = tool_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.tool_sdk",
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
        rsp = tool_sdk.model.tool.tool_pb2.Tool()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
