# -*- coding: utf-8 -*-
import os
import sys


import user_service_sdk.api.user_admin.alter_password_pb2

import google.protobuf.empty_pb2

import user_service_sdk.api.user_admin.alter_self_password_pb2

import user_service_sdk.api.user_admin.forgot_password_pb2

import user_service_sdk.api.user_admin.get_password_conf_pb2

import user_service_sdk.api.user_admin.get_user_info_pb2

import google.protobuf.struct_pb2

import user_service_sdk.api.user_admin.list_groups_id_name_pb2

import user_service_sdk.api.user_admin.list_users_pb2

import user_service_sdk.api.user_admin.list_users_id_nick_pb2

import user_service_sdk.api.user_admin.reset_password_pb2

import user_service_sdk.api.user_admin.search_all_user_group_pb2

import user_service_sdk.api.user_admin.search_all_users_pb2

import user_service_sdk.api.user_admin.user_delete_pb2

import user_service_sdk.api.user_admin.user_login_info_pb2

import user_service_sdk.api.user_admin.user_register_pb2

import user_service_sdk.utils.http_util
import google.protobuf.json_format


class UserAdminClient(object):
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

    
    def alter_password(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.alter_password_pb2.AlterPasswordRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改密码[内部]
        :param request: alter_password请求
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
            route_name = "easyops.api.user_service.user_admin.AlterPassword"
        uri = "/api/v1/users/alter_password"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
    
    def alter_self_password(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.alter_self_password_pb2.AlterSelfPasswordRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改自己密码
        :param request: alter_self_password请求
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
            route_name = "easyops.api.user_service.user_admin.AlterSelfPassword"
        uri = "/api/v1/users/password"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
    
    def forgot_password(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.forgot_password_pb2.ForgotPasswordRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        用户忘记密码
        :param request: forgot_password请求
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
            route_name = "easyops.api.user_service.user_admin.ForgotPassword"
        uri = "/api/v1/users/password/forgot"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
    
    def get_password_config(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> user_service_sdk.api.user_admin.get_password_conf_pb2.GetPasswordConfigResponse
        """
        获取密码配置
        :param request: get_password_config请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.get_password_conf_pb2.GetPasswordConfigResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.GetPasswordConfig"
        uri = "/api/v1/users/passconf"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.get_password_conf_pb2.GetPasswordConfigResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_user_info(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.get_user_info_pb2.GetUserInfoRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取用户信息
        :param request: get_user_info请求
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
            route_name = "easyops.api.user_service.user_admin.GetUserInfo"
        uri = "/api/v1/users/detail/{username}".format(
            username=request.username,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
    
    def list_groups_id_name(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.list_groups_id_name_pb2.ListGroupsIdNameRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取用户Id与name映射
        :param request: list_groups_id_name请求
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
            route_name = "easyops.api.user_service.user_admin.ListGroupsIdName"
        uri = "/api/v1/groups/id_map_name"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
    
    def list_users_info(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.list_users_pb2.ListUsersInfoRequest, int, str, int) -> user_service_sdk.api.user_admin.list_users_pb2.ListUsersInfoResponse
        """
        获取用户信息列表
        :param request: list_users_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.list_users_pb2.ListUsersInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.ListUsersInfo"
        uri = "/api/v1/users"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.list_users_pb2.ListUsersInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_users_id_nick(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.list_users_id_nick_pb2.ListUsersIdNickRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取用户name与昵称映射
        :param request: list_users_id_nick请求
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
            route_name = "easyops.api.user_service.user_admin.ListUsersIdNick"
        uri = "/api/v1/users/id_map_nickname"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
    
    def reset_password(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.reset_password_pb2.ResetPasswordRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        用户重置密码
        :param request: reset_password请求
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
            route_name = "easyops.api.user_service.user_admin.ResetPassword"
        uri = "/api/v1/users/password/reset"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
    
    def search_all_user_group(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.search_all_user_group_pb2.SearchAllUserGroupRequest, int, str, int) -> user_service_sdk.api.user_admin.search_all_user_group_pb2.SearchAllUserGroupResponse
        """
        搜索所有用户组列表
        :param request: search_all_user_group请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.search_all_user_group_pb2.SearchAllUserGroupResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.SearchAllUserGroup"
        uri = "/api/v1/users/group/all"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.search_all_user_group_pb2.SearchAllUserGroupResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_all_users_info(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.search_all_users_pb2.SearchAllUsersInfoRequest, int, str, int) -> user_service_sdk.api.user_admin.search_all_users_pb2.SearchAllUsersInfoResponse
        """
        搜索所有用户信息列表
        :param request: search_all_users_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.search_all_users_pb2.SearchAllUsersInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.SearchAllUsersInfo"
        uri = "/api/v1/users/all"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.search_all_users_pb2.SearchAllUsersInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def user_delete(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.user_delete_pb2.UserDeleteRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        用户删除[内部]
        :param request: user_delete请求
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
            route_name = "easyops.api.user_service.user_admin.UserDelete"
        uri = "/api/v1/users/{username}".format(
            username=request.username,
        )
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.user_service_sdk",
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
    
    def get_user_login_info(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.user_login_info_pb2.GetUserLoginInfoRequest, int, str, int) -> user_service_sdk.api.user_admin.user_login_info_pb2.GetUserLoginInfoResponse
        """
        查询用户登录信息
        :param request: get_user_login_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.user_login_info_pb2.GetUserLoginInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.GetUserLoginInfo"
        uri = "/api/v1/user/login_info"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.user_login_info_pb2.GetUserLoginInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def user_register(self, request, org, user, timeout=10):
        # type: (user_service_sdk.api.user_admin.user_register_pb2.UserRegisterRequest, int, str, int) -> user_service_sdk.api.user_admin.user_register_pb2.UserRegisterResponse
        """
        用户注册[内部]
        :param request: user_register请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: user_service_sdk.api.user_admin.user_register_pb2.UserRegisterResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.user_service.user_admin.UserRegister"
        uri = "/api/v1/users/register"
        
        requestParam = request
        
        rsp_obj = user_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.user_service_sdk",
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
        rsp = user_service_sdk.api.user_admin.user_register_pb2.UserRegisterResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
