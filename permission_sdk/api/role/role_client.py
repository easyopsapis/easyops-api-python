# -*- coding: utf-8 -*-
import os
import sys


import permission_sdk.api.role.create_role_pb2

import permission_sdk.api.role.delete_role_permission_pb2

import google.protobuf.empty_pb2

import permission_sdk.api.role.get_permission_role_list_pb2

import permission_sdk.api.role.get_role_detail_pb2

import permission_sdk.api.role.get_user_role_pb2

import permission_sdk.api.role.put_role_permission_pb2

import permission_sdk.api.role.role_add_user_pb2

import permission_sdk.api.role.role_add_user_or_gorup_pb2

import permission_sdk.api.role.role_change_permission_pb2

import permission_sdk.api.role.role_delete_user_or_gorup_pb2

import permission_sdk.api.role.role_set_user_pb2

import permission_sdk.utils.http_util
import google.protobuf.json_format


class RoleClient(object):
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

    
    def create_role(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.create_role_pb2.CreateRoleRequest, int, str, int) -> permission_sdk.api.role.create_role_pb2.CreateRoleResponse
        """
        新增角色权限配置
        :param request: create_role请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.create_role_pb2.CreateRoleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.CreateRole"
        uri = "/api/v1/permission_role/config"
        
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
        rsp = permission_sdk.api.role.create_role_pb2.CreateRoleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_permission_role(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.delete_role_permission_pb2.DeletePermissionRoleRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除角色权限
        :param request: delete_permission_role请求
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
            route_name = "easyops.api.permission.role.DeletePermissionRole"
        uri = "/api/v1/permission_role/config/{id}".format(
            id=request.id,
        )
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_permission_role_list(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.get_permission_role_list_pb2.GetPermissionRoleListRequest, int, str, int) -> permission_sdk.api.role.get_permission_role_list_pb2.GetPermissionRoleListResponse
        """
        获取角色权限配置列表
        :param request: get_permission_role_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.get_permission_role_list_pb2.GetPermissionRoleListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.GetPermissionRoleList"
        uri = "/api/v1/permission_role/config"
        
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
        rsp = permission_sdk.api.role.get_permission_role_list_pb2.GetPermissionRoleListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_role_detail(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.get_role_detail_pb2.GetRoleDetailRequest, int, str, int) -> permission_sdk.api.role.get_role_detail_pb2.GetRoleDetailResponse
        """
        获取角色权限配置详情
        :param request: get_role_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.get_role_detail_pb2.GetRoleDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.GetRoleDetail"
        uri = "/api/v1/permission_role/config/{id}".format(
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
        rsp = permission_sdk.api.role.get_role_detail_pb2.GetRoleDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_user_role(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.get_user_role_pb2.GetUserRoleRequest, int, str, int) -> permission_sdk.api.role.get_user_role_pb2.GetUserRoleResponse
        """
        获取用户及用户所在用户组所属角色
        :param request: get_user_role请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.get_user_role_pb2.GetUserRoleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.GetUserRole"
        uri = "/api/v1/permission_role/user_role/{user}".format(
            user=request.user,
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
        rsp = permission_sdk.api.role.get_user_role_pb2.GetUserRoleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def put_permission_role(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.put_role_permission_pb2.PutPermissionRoleRequest, int, str, int) -> permission_sdk.api.role.put_role_permission_pb2.PutPermissionRoleResponse
        """
        修改角色名
        :param request: put_permission_role请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.put_role_permission_pb2.PutPermissionRoleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.PutPermissionRole"
        uri = "/api/v1/permission_role/rename_role/{id}".format(
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
        rsp = permission_sdk.api.role.put_role_permission_pb2.PutPermissionRoleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def role_add_user(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.role_add_user_pb2.RoleAddUserRequest, int, str, int) -> permission_sdk.api.role.role_add_user_pb2.RoleAddUserResponse
        """
        角色新加用户
        :param request: role_add_user请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.role_add_user_pb2.RoleAddUserResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.RoleAddUser"
        uri = "/api/v1/permission_role/role_add_user/{id}".format(
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
        rsp = permission_sdk.api.role.role_add_user_pb2.RoleAddUserResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def role_add_user_or_group(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.role_add_user_or_gorup_pb2.RoleAddUserOrGroupRequest, int, str, int) -> permission_sdk.api.role.role_add_user_or_gorup_pb2.RoleAddUserOrGroupResponse
        """
        角色添加用户(组)
        :param request: role_add_user_or_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.role_add_user_or_gorup_pb2.RoleAddUserOrGroupResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.RoleAddUserOrGroup"
        uri = "/api/v1/permission_role/role_add_user_or_group/{id}".format(
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
        rsp = permission_sdk.api.role.role_add_user_or_gorup_pb2.RoleAddUserOrGroupResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def role_change_permission(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.role_change_permission_pb2.RoleChangePermissionRequest, int, str, int) -> permission_sdk.api.role.role_change_permission_pb2.RoleChangePermissionResponse
        """
        角色修改权限
        :param request: role_change_permission请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.role_change_permission_pb2.RoleChangePermissionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.RoleChangePermission"
        uri = "/api/v1/permission_role/role_change_permission/{id}".format(
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
        rsp = permission_sdk.api.role.role_change_permission_pb2.RoleChangePermissionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def role_delete_user_or_group(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.role_delete_user_or_gorup_pb2.RoleDeleteUserOrGroupRequest, int, str, int) -> permission_sdk.api.role.role_delete_user_or_gorup_pb2.RoleDeleteUserOrGroupResponse
        """
        角色删除用户(组)
        :param request: role_delete_user_or_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.role_delete_user_or_gorup_pb2.RoleDeleteUserOrGroupResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.RoleDeleteUserOrGroup"
        uri = "/api/v1/permission_role/role_delete_user_or_group/{id}".format(
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
        rsp = permission_sdk.api.role.role_delete_user_or_gorup_pb2.RoleDeleteUserOrGroupResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def role_set_user(self, request, org, user, timeout=10):
        # type: (permission_sdk.api.role.role_set_user_pb2.RoleSetUserRequest, int, str, int) -> permission_sdk.api.role.role_set_user_pb2.RoleSetUserResponse
        """
        设置用户(组)所属角色
        :param request: role_set_user请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: permission_sdk.api.role.role_set_user_pb2.RoleSetUserResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.permission.role.RoleSetUser"
        uri = "/api/v1/permission_role/user_set_roles/{user}".format(
            user=request.user,
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
        rsp = permission_sdk.api.role.role_set_user_pb2.RoleSetUserResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
