# -*- coding: utf-8 -*-
import os
import sys


import permission_sdk.api.permission.batch_validate_cmdb_permission_pb2

import permission_sdk.api.permission.delete_permission_pb2

import permission_sdk.api.permission.get_permission_detail_pb2

import permission_sdk.api.permission.get_permission_list_pb2

import google.protobuf.empty_pb2

import permission_sdk.api.permission.put_permission_pb2

import permission_sdk.model.permission.permission_pb2

import permission_sdk.api.permission.save_permission_pb2

import permission_sdk.api.permission.user_register_pb2

import permission_sdk.api.permission.validate_artifact_permission_pb2

import permission_sdk.api.permission.validate_cmdb_permission_pb2

import permission_sdk.api.permission.validate_ops_automation_permission_pb2

import permission_sdk.utils.http_util
import google.protobuf.json_format


class PermissionClient(object):
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

    
    def batch_validate_cmdb_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.batch_validate_cmdb_permission_pb2.BatchValidateCmdbPermissionRequest, int, str, int) -> permission_sdk.api.permission.batch_validate_cmdb_permission_pb2.BatchValidateCmdbPermissionResponse
        """
        批量校验cmdb权限
        :param request: batch_validate_cmdb_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.batch_validate_cmdb_permission_pb2.BatchValidateCmdbPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.BatchValidateCmdbPermission"
        uri = "/api/v1/permission/validate"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.batch_validate_cmdb_permission_pb2.BatchValidateCmdbPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.delete_permission_pb2.DeletePermissionRequest, int, str, int) -> permission_sdk.api.permission.delete_permission_pb2.DeletePermissionResponse
        """
        根据action删除权限点
        :param request: delete_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.delete_permission_pb2.DeletePermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.DeletePermission"
        uri = "/api/v1/permission"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.delete_permission_pb2.DeletePermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_permission_detail(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.get_permission_detail_pb2.GetPermissionDetailRequest, int, str, int) -> permission_sdk.api.permission.get_permission_detail_pb2.GetPermissionDetailResponse
        """
        获取权限点详情信息
        :param request: get_permission_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.get_permission_detail_pb2.GetPermissionDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.GetPermissionDetail"
        uri = "/api/v1/permission/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.get_permission_detail_pb2.GetPermissionDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_permission_list(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.get_permission_list_pb2.GetPermissionListRequest, int, str, int) -> permission_sdk.api.permission.get_permission_list_pb2.GetPermissionListResponse
        """
        获取权限点列表
        :param request: get_permission_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.get_permission_list_pb2.GetPermissionListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.GetPermissionList"
        uri = "/api/v1/permission"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.get_permission_list_pb2.GetPermissionListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def org_register(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        org注册permission
        :param request: org_register请求
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
            route_name = "easyops.api.permission.permission.OrgRegister"
        uri = "/api/v1/org/register"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.permission_sdk",
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
    
    def put_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.put_permission_pb2.PutPermissionRequest, int, str, int) -> permission_sdk.api.permission.put_permission_pb2.PutPermissionResponse
        """
        修改权限配置
        :param request: put_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.put_permission_pb2.PutPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.PutPermission"
        uri = "/api/v1/permission/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.put_permission_pb2.PutPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def save_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.model.permission.permission_pb2.Permission, int, str, int) -> permission_sdk.api.permission.save_permission_pb2.SavePermissionResponse
        """
        保存权限配置(已存在权限点则更新)
        :param request: save_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.save_permission_pb2.SavePermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.SavePermission"
        uri = "/api/v1/permission/save"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.save_permission_pb2.SavePermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def user_register(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.user_register_pb2.UserRegisterRequest, int, str, int) -> permission_sdk.api.permission.user_register_pb2.UserRegisterResponse
        """
        user注册接口
        :param request: user_register请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.user_register_pb2.UserRegisterResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.UserRegister"
        uri = "/api/v2/permission/register_user"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.user_register_pb2.UserRegisterResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def validate_artifact_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.validate_artifact_permission_pb2.ValidateArtifactPermissionRequest, int, str, int) -> permission_sdk.api.permission.validate_artifact_permission_pb2.ValidateArtifactPermissionResponse
        """
        校验制品包系统权限
        :param request: validate_artifact_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.validate_artifact_permission_pb2.ValidateArtifactPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.ValidateArtifactPermission"
        uri = "/api/v1/permission/validate"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.validate_artifact_permission_pb2.ValidateArtifactPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def validate_cmdb_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.validate_cmdb_permission_pb2.ValidateCmdbPermissionRequest, int, str, int) -> permission_sdk.api.permission.validate_cmdb_permission_pb2.ValidateCmdbPermissionResponse
        """
        校验cmdb权限
        :param request: validate_cmdb_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.validate_cmdb_permission_pb2.ValidateCmdbPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.ValidateCmdbPermission"
        uri = "/api/v1/permission/validate"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.validate_cmdb_permission_pb2.ValidateCmdbPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def validate_ops_automation_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.permission.validate_ops_automation_permission_pb2.ValidateOpsAutomationPermissionRequest, int, str, int) -> permission_sdk.api.permission.validate_ops_automation_permission_pb2.ValidateOpsAutomationPermissionResponse
        """
        校验运维自动化系统权限
        :param request: validate_ops_automation_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.permission.validate_ops_automation_permission_pb2.ValidateOpsAutomationPermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.permission.ValidateOpsAutomationPermission"
        uri = "/api/v1/permission/validate"
        
        requestParam = request
        
        rsp_obj = permission_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.permission_sdk",
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
        rsp = permission_sdk.api.permission.validate_ops_automation_permission_pb2.ValidateOpsAutomationPermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
