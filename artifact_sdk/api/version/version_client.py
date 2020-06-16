# -*- coding: utf-8 -*-
import os
import sys


import artifact_sdk.api.version.batch_delete_versions_pb2

import google.protobuf.empty_pb2

import artifact_sdk.api.version.create_version_with_sign_pb2

import artifact_sdk.model.artifact.version_pb2

import artifact_sdk.api.version.delete_version_pb2

import artifact_sdk.api.version.get_clean_version_list_pb2

import artifact_sdk.api.version.get_version_detail_pb2

import artifact_sdk.api.version.get_version_list_pb2

import artifact_sdk.api.version.get_version_permission_by_ids_pb2

import artifact_sdk.api.version.get_version_permission_info_pb2

import artifact_sdk.model.artifact.white_permission_user_pb2

import artifact_sdk.api.version.update_pb2

import artifact_sdk.api.version.update_version_env_type_pb2

import artifact_sdk.api.version.update_version_permission_users_pb2

import artifact_sdk.utils.http_util
import google.protobuf.json_format


class VersionClient(object):
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

    
    def batch_delete_versions(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.batch_delete_versions_pb2.BatchDeleteVersionsRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量删除版本
        :param request: batch_delete_versions请求
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
            route_name = "easyops.api.artifact.version.BatchDeleteVersions"
        uri = "/versions/{packageId}".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.artifact_sdk",
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
    
    def create_version_with_sign(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.create_version_with_sign_pb2.CreateVersionWithSignRequest, int, str, int) -> artifact_sdk.model.artifact.version_pb2.Version
        """
        创建版本
        :param request: create_version_with_sign请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.model.artifact.version_pb2.Version
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.CreateVersionWithSign"
        uri = "/version/sign"
        
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.model.artifact.version_pb2.Version()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_version(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.delete_version_pb2.DeleteVersionRequest, int, str, int) -> artifact_sdk.api.version.delete_version_pb2.DeleteVersionResponse
        """
        删除版本
        :param request: delete_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.api.version.delete_version_pb2.DeleteVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.DeleteVersion"
        uri = "/v2/version/{packageId}/{versionId}".format(
            packageId=request.packageId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.api.version.delete_version_pb2.DeleteVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_clean_version_list(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.get_clean_version_list_pb2.GetCleanVersionListRequest, int, str, int) -> artifact_sdk.api.version.get_clean_version_list_pb2.GetCleanVersionListResponse
        """
        获取可清理的版本列表
        :param request: get_clean_version_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.api.version.get_clean_version_list_pb2.GetCleanVersionListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.GetCleanVersionList"
        uri = "version/clean/list"
        
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.api.version.get_clean_version_list_pb2.GetCleanVersionListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_version_detail(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.get_version_detail_pb2.GetVersionDetailRequest, int, str, int) -> artifact_sdk.api.version.get_version_detail_pb2.GetVersionDetailResponse
        """
        获取版本详情
        :param request: get_version_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.api.version.get_version_detail_pb2.GetVersionDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.GetVersionDetail"
        uri = "/version/{versionId}".format(
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.api.version.get_version_detail_pb2.GetVersionDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_version_list(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.get_version_list_pb2.GetVersionListRequest, int, str, int) -> artifact_sdk.api.version.get_version_list_pb2.GetVersionListResponse
        """
        获取版本列表
        :param request: get_version_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.api.version.get_version_list_pb2.GetVersionListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.GetVersionList"
        uri = "/version/list"
        
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.api.version.get_version_list_pb2.GetVersionListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_version_permission_by_ids(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.get_version_permission_by_ids_pb2.GetVersionPermissionByIdsRequest, int, str, int) -> artifact_sdk.api.version.get_version_permission_by_ids_pb2.GetVersionPermissionByIdsResponse
        """
        通过版本id列表获取版本权限
        :param request: get_version_permission_by_ids请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.api.version.get_version_permission_by_ids_pb2.GetVersionPermissionByIdsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.GetVersionPermissionByIds"
        uri = "/permission/versions/{packageId}".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.api.version.get_version_permission_by_ids_pb2.GetVersionPermissionByIdsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_version_permission_info(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.get_version_permission_info_pb2.GetVersionPermissionInfoRequest, int, str, int) -> artifact_sdk.model.artifact.white_permission_user_pb2.WhitePermissionUser
        """
        获取版本权限
        :param request: get_version_permission_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.model.artifact.white_permission_user_pb2.WhitePermissionUser
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.GetVersionPermissionInfo"
        uri = "/permission/version/{packageId}/{versionId}".format(
            packageId=request.packageId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.model.artifact.white_permission_user_pb2.WhitePermissionUser()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.update_pb2.UpdateRequest, int, str, int) -> artifact_sdk.model.artifact.version_pb2.Version
        """
        修改版本信息
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.model.artifact.version_pb2.Version
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.Update"
        uri = "/version/{versionId}".format(
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.model.artifact.version_pb2.Version()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_version_env_type(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.update_version_env_type_pb2.UpdateVersionEnvTypeRequest, int, str, int) -> artifact_sdk.model.artifact.version_pb2.Version
        """
        更新版本的环境号
        :param request: update_version_env_type请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: artifact_sdk.model.artifact.version_pb2.Version
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.artifact.version.UpdateVersionEnvType"
        uri = "/version_env_type"
        
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.artifact_sdk",
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
        rsp = artifact_sdk.model.artifact.version_pb2.Version()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_version_permission_users(self, request, org, user, timeout=10):
        # type: (artifact_sdk.api.version.update_version_permission_users_pb2.UpdateVersionPermissionUsersRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        创建版本权限
        :param request: update_version_permission_users请求
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
            route_name = "easyops.api.artifact.version.UpdateVersionPermissionUsers"
        uri = "/permission/version"
        
        requestParam = request
        
        rsp_obj = artifact_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.artifact_sdk",
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
    
