# -*- coding: utf-8 -*-
import os
import sys


import console_gateway_sdk.api.cmdb_service_ctrl.archive_instance_list_all_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.get_object_upload_data_pb2

import google.protobuf.struct_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.instance_list_all_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.instance_search_all_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.relation_max_check_all_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.search_app_in_system_all_pb2

import console_gateway_sdk.api.cmdb_service_ctrl.search_subsystem_all_pb2

import console_gateway_sdk.utils.http_util
import google.protobuf.json_format


class CmdbServiceCtrlClient(object):
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

    
    def archive_instance_list_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.archive_instance_list_all_pb2.ArchiveInstanceListAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.archive_instance_list_all_pb2.ArchiveInstanceListAllResponse
        """
        归档实例列表查询,不分页
        :param request: archive_instance_list_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.archive_instance_list_all_pb2.ArchiveInstanceListAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.ArchiveInstanceListAll"
        uri = "/api/v1/cmdb/resource/{objectId}/instance/archive".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.archive_instance_list_all_pb2.ArchiveInstanceListAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_upload_data(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.get_object_upload_data_pb2.GetObjectUploadDataRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取模型导入文件内容
        :param request: get_object_upload_data请求
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
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.GetObjectUploadData"
        uri = "/api/abjectGetUploadData"
        
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_list_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.instance_list_all_pb2.InstanceListAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.instance_list_all_pb2.InstanceListAllResponse
        """
        实例列表查询,不分页
        :param request: instance_list_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.instance_list_all_pb2.InstanceListAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.InstanceListAll"
        uri = "/api/cmdb_resource/object/{objectId}/instance".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.instance_list_all_pb2.InstanceListAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_search_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.instance_search_all_pb2.InstanceSearchAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.instance_search_all_pb2.InstanceSearchAllResponse
        """
        搜索实例,不分页
        :param request: instance_search_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.instance_search_all_pb2.InstanceSearchAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.InstanceSearchAll"
        uri = "/api/cmdb_resource/object/{objectId}/instance/_search/all".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.instance_search_all_pb2.InstanceSearchAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def relation_max_check_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.relation_max_check_all_pb2.RelationMaxCheckAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.relation_max_check_all_pb2.RelationMaxCheckAllResponse
        """
        搜索实例列表指定关系是否大于等于max约束,不分页
        :param request: relation_max_check_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.relation_max_check_all_pb2.RelationMaxCheckAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.RelationMaxCheckAll"
        uri = "/api/cmdb_resource/object/{objectId}/instance/_search_relation_max_check/all".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.relation_max_check_all_pb2.RelationMaxCheckAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_app_in_system_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.search_app_in_system_all_pb2.SearchAppInSystemAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.search_app_in_system_all_pb2.SearchAppInSystemAllResponse
        """
        查询应用系统的所有子系统以及所有子系统的子系统所包含的应用,不分页
        :param request: search_app_in_system_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.search_app_in_system_all_pb2.SearchAppInSystemAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.SearchAppInSystemAll"
        uri = "/api/cmdb_resource/system/{systemInstanceId}/_search_apps/all".format(
            systemInstanceId=request.systemInstanceId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.search_app_in_system_all_pb2.SearchAppInSystemAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_sub_system_all(self, request, org, user, timeout=10):
        # type: (console_gateway_sdk.api.cmdb_service_ctrl.search_subsystem_all_pb2.SearchSubSystemAllRequest, int, str, int) -> console_gateway_sdk.api.cmdb_service_ctrl.search_subsystem_all_pb2.SearchSubSystemAllResponse
        """
        搜索系统的子系统以及，以及递归的获取子系统的子系统,不分页
        :param request: search_sub_system_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: console_gateway_sdk.api.cmdb_service_ctrl.search_subsystem_all_pb2.SearchSubSystemAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.console_gateway.cmdb_service_ctrl.SearchSubSystemAll"
        uri = "/api/cmdb_resource/system/{systemInstanceId}/_search_subsystem/all".format(
            systemInstanceId=request.systemInstanceId,
        )
        requestParam = request
        
        rsp_obj = console_gateway_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.console_gateway_sdk",
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
        rsp = console_gateway_sdk.api.cmdb_service_ctrl.search_subsystem_all_pb2.SearchSubSystemAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
