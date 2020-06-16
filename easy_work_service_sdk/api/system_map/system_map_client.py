# -*- coding: utf-8 -*-
import os
import sys


import easy_work_service_sdk.api.system_map.collect_system_pb2

import easy_work_service_sdk.model.easy_work_service.app_system_pb2

import easy_work_service_sdk.api.system_map.create_system_pb2

import easy_work_service_sdk.api.system_map.delete_system_pb2

import google.protobuf.empty_pb2

import easy_work_service_sdk.api.system_map.get_my_collection_pb2

import easy_work_service_sdk.api.system_map.get_system_pb2

import easy_work_service_sdk.api.system_map.get_system_categories_pb2

import easy_work_service_sdk.api.system_map.list_system_pb2

import easy_work_service_sdk.api.system_map.update_system_pb2

import easy_work_service_sdk.utils.http_util
import google.protobuf.json_format


class SystemMapClient(object):
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

    
    def collect_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.system_map.collect_system_pb2.CollectSystemRequest, int, str, int) -> easy_work_service_sdk.api.system_map.collect_system_pb2.CollectSystemResponse
        """
        收藏/取消收藏应用系统
        :param request: collect_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.collect_system_pb2.CollectSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.CollectSystem"
        uri = "/api/easy_work_service/v1/collections"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.collect_system_pb2.CollectSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.model.easy_work_service.app_system_pb2.AppSystem, int, str, int) -> easy_work_service_sdk.api.system_map.create_system_pb2.CreateSystemResponse
        """
        创建应用系统
        :param request: create_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.create_system_pb2.CreateSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.CreateSystem"
        uri = "/api/easy_work_service/v1/systems"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.create_system_pb2.CreateSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.system_map.delete_system_pb2.DeleteSystemRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除应用系统
        :param request: delete_system请求
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
            route_name = "easyops.api.easy_work_service.system_map.DeleteSystem"
        uri = "/api/easy_work_service/v1/systems/{systemId}".format(
            systemId=request.systemId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.easy_work_service_sdk",
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
    
    def get_collection(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> easy_work_service_sdk.api.system_map.get_my_collection_pb2.GetCollectionResponse
        """
        获取我的收藏
        :param request: get_collection请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.get_my_collection_pb2.GetCollectionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.GetCollection"
        uri = "/api/easy_work_service/v1/collections"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.get_my_collection_pb2.GetCollectionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.system_map.get_system_pb2.GetSystemRequest, int, str, int) -> easy_work_service_sdk.api.system_map.get_system_pb2.GetSystemResponse
        """
        获取应用系统详情
        :param request: get_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.get_system_pb2.GetSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.GetSystem"
        uri = "/api/easy_work_service/v1/systems/{systemId}".format(
            systemId=request.systemId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.get_system_pb2.GetSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_system_categories(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> easy_work_service_sdk.api.system_map.get_system_categories_pb2.GetSystemCategoriesResponse
        """
        获取应用系统类型列表
        :param request: get_system_categories请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.get_system_categories_pb2.GetSystemCategoriesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.GetSystemCategories"
        uri = "/api/easy_work_service/v1/system_categories"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.get_system_categories_pb2.GetSystemCategoriesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.system_map.list_system_pb2.ListSystemRequest, int, str, int) -> easy_work_service_sdk.api.system_map.list_system_pb2.ListSystemResponse
        """
        获取应用系统列表
        :param request: list_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.list_system_pb2.ListSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.ListSystem"
        uri = "/api/easy_work_service/v1/systems"
        
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.list_system_pb2.ListSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_system(self, request, org, user, timeout=10):
        # type: (easy_work_service_sdk.api.system_map.update_system_pb2.UpdateSystemRequest, int, str, int) -> easy_work_service_sdk.api.system_map.update_system_pb2.UpdateSystemResponse
        """
        更新应用系统
        :param request: update_system请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_work_service_sdk.api.system_map.update_system_pb2.UpdateSystemResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_work_service.system_map.UpdateSystem"
        uri = "/api/easy_work_service/v1/systems/{systemId}".format(
            systemId=request.systemId,
        )
        requestParam = request
        
        rsp_obj = easy_work_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.easy_work_service_sdk",
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
        rsp = easy_work_service_sdk.api.system_map.update_system_pb2.UpdateSystemResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
