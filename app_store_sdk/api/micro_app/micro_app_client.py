# -*- coding: utf-8 -*-

import model.app_store.micro_app_pb2

import delete_pb2

import google.protobuf.empty_pb2

import get_pb2

import get_packages_pb2

import list_pb2

import utils.http_util
import google.protobuf.json_format


class MicroAppClient(object):
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
        # type: (model.app_store.micro_app_pb2.AppStoreMicroApp, int, str, int) -> model.app_store.micro_app_pb2.AppStoreMicroApp
        """
        发布新的小产品
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.app_store.micro_app_pb2.AppStoreMicroApp
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.app_store.micro_app.Create"
        uri = "/api/app_store/v1/micro_app"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.app_store_sdk",
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
        rsp = model.app_store.micro_app_pb2.AppStoreMicroApp()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_app_store_micro_app(self, request, org, user, timeout=10):
        # type: (delete_pb2.DeleteAppStoreMicroAppRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        下线小产品
        :param request: delete_app_store_micro_app请求
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
            route_name = "easyops.api.app_store.micro_app.DeleteAppStoreMicroApp"
        uri = "/api/app_store/v1/micro_app/app_id/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.app_store_sdk",
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
    
    def get_app_store_micro_app(self, request, org, user, timeout=10):
        # type: (get_pb2.GetAppStoreMicroAppRequest, int, str, int) -> get_pb2.GetAppStoreMicroAppResponse
        """
        根据id获取小产品信息
        :param request: get_app_store_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_pb2.GetAppStoreMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.app_store.micro_app.GetAppStoreMicroApp"
        uri = "/api/app_store/v1/micro_app/app_id/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.app_store_sdk",
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
        rsp = get_pb2.GetAppStoreMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_related_packages(self, request, org, user, timeout=10):
        # type: (get_packages_pb2.GetRelatedPackagesRequest, int, str, int) -> get_packages_pb2.GetRelatedPackagesResponse
        """
        根据app_id获取关联制品包
        :param request: get_related_packages请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_packages_pb2.GetRelatedPackagesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.app_store.micro_app.GetRelatedPackages"
        uri = "/api/app_store/v1/related_packages/app_id/{app_id}".format(
            app_id=request.app_id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.app_store_sdk",
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
        rsp = get_packages_pb2.GetRelatedPackagesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_app_store_micro_app(self, request, org, user, timeout=10):
        # type: (list_pb2.ListAppStoreMicroAppRequest, int, str, int) -> list_pb2.ListAppStoreMicroAppResponse
        """
        获取小产品列表
        :param request: list_app_store_micro_app请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.ListAppStoreMicroAppResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.app_store.micro_app.ListAppStoreMicroApp"
        uri = "/api/app_store/v1/micro_app/search"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.app_store_sdk",
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
        rsp = list_pb2.ListAppStoreMicroAppResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
