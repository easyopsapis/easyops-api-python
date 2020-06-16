# -*- coding: utf-8 -*-
import os
import sys


import micro_app_sdk.api.installed_micro_app.create_pb2

import micro_app_sdk.api.installed_micro_app.delete_pb2

import google.protobuf.empty_pb2

import micro_app_sdk.api.installed_micro_app.get_pb2

import micro_app_sdk.api.installed_micro_app.import_pb2

import micro_app_sdk.api.installed_micro_app.list_pb2

import micro_app_sdk.api.installed_micro_app.package_upload_pb2

import micro_app_sdk.api.installed_micro_app.search_pb2

import micro_app_sdk.api.installed_micro_app.search_with_uniq_key_pb2

import micro_app_sdk.api.installed_micro_app.update_pb2

import micro_app_sdk.api.installed_micro_app.update_status_pb2

import micro_app_sdk.model.micro_app.installed_micro_app_pb2

import micro_app_sdk.api.installed_micro_app.update_storyboardJson_pb2

import micro_app_sdk.utils.http_util
import google.protobuf.json_format


class InstalledMicroAppClient(object):
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
        # type: (micro_app_sdk.api.installed_micro_app.create_pb2.CreateRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.create_pb2.CreateResponse
        """
        创建小产品
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.create_pb2.CreateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.Create"
        uri = "/api/micro_app/v1/installed_micro_app"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.create_pb2.CreateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.delete_pb2.DeleteMicroAppRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除小产品
        :param request: delete_micro_app请求
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
            route_name = "easyops.api.micro_app.installed_micro_app.DeleteMicroApp"
        uri = "/api/micro_app/v1/installed_micro_app/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.micro_app_sdk",
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
    
    def get_installed_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.get_pb2.GetInstalledMicroAppRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.get_pb2.GetInstalledMicroAppResponse
        """
        获取已安装小产品信息
        :param request: get_installed_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.get_pb2.GetInstalledMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.GetInstalledMicroApp"
        uri = "/api/micro_app/v1/installed_micro_app/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.get_pb2.GetInstalledMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.import_pb2.ImportMicroAppRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        导入小产品（存在更新，不存在创建）
        :param request: import_micro_app请求
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
            route_name = "easyops.api.micro_app.installed_micro_app.ImportMicroApp"
        uri = "/api/micro_app/v1/import_installed_micro_app/{appId}".format(
            appId=request.appId,
        )
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
    
    def list_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.list_pb2.ListMicroAppRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.list_pb2.ListMicroAppResponse
        """
        获取已安装小产品列表
        :param request: list_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.list_pb2.ListMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.ListMicroApp"
        uri = "/api/micro_app/v1/installed_micro_app"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.list_pb2.ListMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def package_upload(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.package_upload_pb2.PackageUploadRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.package_upload_pb2.PackageUploadResponse
        """
        小产品生成打包文件并上传到r环境
        :param request: package_upload请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.package_upload_pb2.PackageUploadResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.PackageUpload"
        uri = "/api/micro_app/v1/package-upload"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.package_upload_pb2.PackageUploadResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_installed_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.search_pb2.SearchInstalledMicroAppRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.search_pb2.SearchInstalledMicroAppResponse
        """
        获取小产品列表
        :param request: search_installed_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.search_pb2.SearchInstalledMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.SearchInstalledMicroApp"
        uri = "/api/micro_app/v1/installed_micro_app/search"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.search_pb2.SearchInstalledMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_installed_micro_app_with_uniq_key(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.search_with_uniq_key_pb2.SearchInstalledMicroAppWithUniqKeyRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.search_with_uniq_key_pb2.SearchInstalledMicroAppWithUniqKeyResponse
        """
        按唯一key(name,appId,homepage)搜索小产品列表
        :param request: search_installed_micro_app_with_uniq_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.search_with_uniq_key_pb2.SearchInstalledMicroAppWithUniqKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.SearchInstalledMicroAppWithUniqKey"
        uri = "/api/micro_app/v1/installed_micro_app/search/uniq_key"
        
        requestParam = request
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.search_with_uniq_key_pb2.SearchInstalledMicroAppWithUniqKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_installed_micro_app(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.update_pb2.UpdateInstalledMicroAppRequest, int, str, int) -> micro_app_sdk.api.installed_micro_app.update_pb2.UpdateInstalledMicroAppResponse
        """
        更新小产品信息
        :param request: update_installed_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.api.installed_micro_app.update_pb2.UpdateInstalledMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.UpdateInstalledMicroApp"
        uri = "/api/micro_app/v1/installed_micro_app/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request.micro_app
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.api.installed_micro_app.update_pb2.UpdateInstalledMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_installed_micro_app_status(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.update_status_pb2.UpdateInstalledMicroAppStatusRequest, int, str, int) -> micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        更新小产品信息
        :param request: update_installed_micro_app_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.UpdateInstalledMicroAppStatus"
        uri = "/api/micro_app/v1/installed_micro_app/{app_id}/status".format(
            app_id=request.app_id,
        )
        requestParam = request.micro_app
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_installed_micro_app_storyboard_json(self, request, org, user, timeout=10):
        # type: (micro_app_sdk.api.installed_micro_app.update_storyboardJson_pb2.UpdateInstalledMicroAppStoryboardJsonRequest, int, str, int) -> micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        更新小产品配置信息
        :param request: update_installed_micro_app_storyboard_json请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.micro_app.installed_micro_app.UpdateInstalledMicroAppStoryboardJson"
        uri = "/api/micro_app/v1/installed_micro_app/{app_id}/storyboardJson".format(
            app_id=request.app_id,
        )
        requestParam = request.micro_app
        
        rsp_obj = micro_app_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.micro_app_sdk",
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
        rsp = micro_app_sdk.model.micro_app.installed_micro_app_pb2.InstalledMicroApp()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
