# -*- coding: utf-8 -*-
import os
import sys


import patch_manager_sdk.api.patch.create_win_patch_pb2

import patch_manager_sdk.api.patch.delete_win_patch_pb2

import google.protobuf.empty_pb2

import patch_manager_sdk.api.patch.get_host_pb2

import patch_manager_sdk.api.patch.get_os_versions_pb2

import patch_manager_sdk.api.patch.get_win_patch_pb2

import patch_manager_sdk.api.patch.list_host_pb2

import patch_manager_sdk.api.patch.list_win_patch_pb2

import patch_manager_sdk.api.patch.search_host_pb2

import patch_manager_sdk.api.patch.search_win_patch_pb2

import patch_manager_sdk.model.easy_command.task_detail_pb2

import patch_manager_sdk.api.patch.update_os_version_pb2

import patch_manager_sdk.api.patch.update_win_patch_pb2

import patch_manager_sdk.utils.http_util
import google.protobuf.json_format


class PatchClient(object):
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

    
    def create_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.create_win_patch_pb2.CreateWinPatchRequest, int, str, int) -> patch_manager_sdk.api.patch.create_win_patch_pb2.CreateWinPatchResponse
        """
        新建windows补丁
        :param request: create_win_patch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.create_win_patch_pb2.CreateWinPatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.CreateWinPatch"
        uri = "/api/patch_manager/v1/patch"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.create_win_patch_pb2.CreateWinPatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.delete_win_patch_pb2.DeleteWinPatchRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除windows补丁
        :param request: delete_win_patch请求
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
            route_name = "easyops.api.patch_manager.patch.DeleteWinPatch"
        uri = "/api/patch_manager/v1/patch/{patchId}".format(
            patchId=request.patchId,
        )
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.patch_manager_sdk",
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
    
    def get_host(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.get_host_pb2.GetHostRequest, int, str, int) -> patch_manager_sdk.api.patch.get_host_pb2.GetHostResponse
        """
        获取主机详情
        :param request: get_host请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.get_host_pb2.GetHostResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.GetHost"
        uri = "/api/patch_manager/v1/host/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.get_host_pb2.GetHostResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_os_versions(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> patch_manager_sdk.api.patch.get_os_versions_pb2.GetOsVersionsResponse
        """
        获取 Windows 补丁适用的操作系统版本
        :param request: get_os_versions请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.get_os_versions_pb2.GetOsVersionsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.GetOsVersions"
        uri = "/api/patch_manager/v1/win_patch_os_versions"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.get_os_versions_pb2.GetOsVersionsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.get_win_patch_pb2.GetWinPatchRequest, int, str, int) -> patch_manager_sdk.api.patch.get_win_patch_pb2.GetWinPatchResponse
        """
        获取windows补丁详情
        :param request: get_win_patch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.get_win_patch_pb2.GetWinPatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.GetWinPatch"
        uri = "/api/patch_manager/v1/win_patch/{patchId}".format(
            patchId=request.patchId,
        )
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.get_win_patch_pb2.GetWinPatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_host(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.list_host_pb2.ListHostRequest, int, str, int) -> patch_manager_sdk.api.patch.list_host_pb2.ListHostResponse
        """
        获取指定的实例ID获取主机列表
        :param request: list_host请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.list_host_pb2.ListHostResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.ListHost"
        uri = "/api/patch_manager/v1/host_list"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.list_host_pb2.ListHostResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.list_win_patch_pb2.ListWinPatchRequest, int, str, int) -> patch_manager_sdk.api.patch.list_win_patch_pb2.ListWinPatchResponse
        """
        获取指定的实例ID获取windows补丁列表
        :param request: list_win_patch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.list_win_patch_pb2.ListWinPatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.ListWinPatch"
        uri = "/api/patch_manager/v1/patch_list"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.list_win_patch_pb2.ListWinPatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_host(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.search_host_pb2.SearchHostRequest, int, str, int) -> patch_manager_sdk.api.patch.search_host_pb2.SearchHostResponse
        """
        获取主机列表
        :param request: search_host请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.search_host_pb2.SearchHostResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.SearchHost"
        uri = "/api/patch_manager/v1/host"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.search_host_pb2.SearchHostResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.search_win_patch_pb2.SearchWinPatchRequest, int, str, int) -> patch_manager_sdk.api.patch.search_win_patch_pb2.SearchWinPatchResponse
        """
        搜索windows补丁列表
        :param request: search_win_patch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.search_win_patch_pb2.SearchWinPatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.SearchWinPatch"
        uri = "/api/patch_manager/v1/patch"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.search_win_patch_pb2.SearchWinPatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_host_patch_callback(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.model.easy_command.task_detail_pb2.TaskDetail, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        同步主机已安装的补丁的回调
        :param request: update_host_patch_callback请求
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
            route_name = "easyops.api.patch_manager.patch.UpdateHostPatchCallback"
        uri = "/api/patch_manager/v1/host_patch_sync_task"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.patch_manager_sdk",
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
    
    def update_os_versions(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.update_os_version_pb2.UpdateOsVersionsRequest, int, str, int) -> patch_manager_sdk.api.patch.update_os_version_pb2.UpdateOsVersionsResponse
        """
        更新 Windows 补丁适用的操作系统版本
        :param request: update_os_versions请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.update_os_version_pb2.UpdateOsVersionsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.UpdateOsVersions"
        uri = "/api/patch_manager/v1/win_patch_os_versions"
        
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.update_os_version_pb2.UpdateOsVersionsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_win_patch(self, request, org, user, timeout=10):
        # type: (patch_manager_sdk.api.patch.update_win_patch_pb2.UpdateWinPatchRequest, int, str, int) -> patch_manager_sdk.api.patch.update_win_patch_pb2.UpdateWinPatchResponse
        """
        更新windows补丁
        :param request: update_win_patch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: patch_manager_sdk.api.patch.update_win_patch_pb2.UpdateWinPatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.patch_manager.patch.UpdateWinPatch"
        uri = "/api/patch_manager/v1/patch/{patchId}".format(
            patchId=request.patchId,
        )
        requestParam = request
        
        rsp_obj = patch_manager_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.patch_manager_sdk",
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
        rsp = patch_manager_sdk.api.patch.update_win_patch_pb2.UpdateWinPatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
