# -*- coding: utf-8 -*-
import os
import sys


import google.protobuf.empty_pb2

import cmdb_extend_sdk.api.custom.get_all_system_tree_pb2

import cmdb_extend_sdk.api.custom.get_component_architecture_pb2

import cmdb_extend_sdk.model.cmdb_extend.app_dependency_pb2

import cmdb_extend_sdk.api.custom.get_idc_all_rack_unit_pb2

import google.protobuf.struct_pb2

import cmdb_extend_sdk.api.custom.get_idcrack_unit_pb2

import cmdb_extend_sdk.model.cmdb_extend.idcrack_unit_info_pb2

import cmdb_extend_sdk.api.custom.get_one_subsystem_tree_pb2

import cmdb_extend_sdk.model.cmdb_extend.subsystem_dependency_pb2

import cmdb_extend_sdk.api.custom.get_one_system_tree_pb2

import cmdb_extend_sdk.model.cmdb_extend.system_dependency_pb2

import cmdb_extend_sdk.api.custom.modify_idc_rack_unit_pb2

import cmdb_extend_sdk.api.custom.modify_idc_rack_unit_check_pb2

import cmdb_extend_sdk.api.custom.release_idc_rack_unit_pb2

import cmdb_extend_sdk.utils.http_util
import google.protobuf.json_format


class CustomClient(object):
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

    
    def get_all_system_tree(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> cmdb_extend_sdk.api.custom.get_all_system_tree_pb2.GetAllSystemTreeResponse
        """
        获取应用架构树
        :param request: get_all_system_tree请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.custom.get_all_system_tree_pb2.GetAllSystemTreeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.custom.GetAllSystemTree"
        uri = "/application-tree"
        
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.custom.get_all_system_tree_pb2.GetAllSystemTreeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_component_architecture(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.get_component_architecture_pb2.GetComponentArchitectureRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.app_dependency_pb2.AppDependency
        """
        获取应用组件的服务依赖
        :param request: get_component_architecture请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.app_dependency_pb2.AppDependency
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.custom.GetComponentArchitecture"
        uri = "/component-architecture/{abbreviation}".format(
            abbreviation=request.abbreviation,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.app_dependency_pb2.AppDependency()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_idc_all_rack_unit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.get_idc_all_rack_unit_pb2.GetIdcAllRackUnitRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取某机房下所有机柜U位信息
        :param request: get_idc_all_rack_unit请求
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
            route_name = "easyops.api.cmdb_extend.custom.GetIdcAllRackUnit"
        uri = "/object/_IDC/instance/{instance_id}/unit".format(
            instance_id=request.instance_id,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
    
    def get_idcrack_unit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.get_idcrack_unit_pb2.GetIdcrackUnitRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.idcrack_unit_info_pb2.IdcrackUnitInfo
        """
        获取机柜U位信息
        :param request: get_idcrack_unit请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.idcrack_unit_info_pb2.IdcrackUnitInfo
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.custom.GetIdcrackUnit"
        uri = "/object/_IDCRACK/instance/{instance_id}/unit".format(
            instance_id=request.instance_id,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.idcrack_unit_info_pb2.IdcrackUnitInfo()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_one_sub_system_tree(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.get_one_subsystem_tree_pb2.GetOneSubSystemTreeRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.subsystem_dependency_pb2.SubsystemDependency
        """
        获取应用系统架构
        :param request: get_one_sub_system_tree请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.subsystem_dependency_pb2.SubsystemDependency
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.custom.GetOneSubSystemTree"
        uri = "/subsystem-architecture/{abbreviation}".format(
            abbreviation=request.abbreviation,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.subsystem_dependency_pb2.SubsystemDependency()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_one_system_tree(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.get_one_system_tree_pb2.GetOneSystemTreeRequest, int, str, int) -> cmdb_extend_sdk.model.cmdb_extend.system_dependency_pb2.SystemDependency
        """
        获取应用系统架构
        :param request: get_one_system_tree请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.model.cmdb_extend.system_dependency_pb2.SystemDependency
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.custom.GetOneSystemTree"
        uri = "/system-architecture/{abbreviation}".format(
            abbreviation=request.abbreviation,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.model.cmdb_extend.system_dependency_pb2.SystemDependency()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def modify_idc_rack_unit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.modify_idc_rack_unit_pb2.ModifyIdcRackUnitRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量更新机柜U位占用接口
        :param request: modify_idc_rack_unit请求
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
            route_name = "easyops.api.cmdb_extend.custom.ModifyIdcRackUnit"
        uri = "/object/_IDCRACK/instance/unit/device"
        
        requestParam = request.deviceList
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
    def modify_idc_rack_unit_check(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.modify_idc_rack_unit_check_pb2.ModifyIdcRackUnitCheckRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量检查机柜U位占用接口
        :param request: modify_idc_rack_unit_check请求
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
            route_name = "easyops.api.cmdb_extend.custom.ModifyIdcRackUnitCheck"
        uri = "/object/_IDCRACK/instance/unit/device/check"
        
        requestParam = request.deviceList
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
    
    def release_idc_rack_unit(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.custom.release_idc_rack_unit_pb2.ReleaseIdcRackUnitRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量更新机柜U位释放
        :param request: release_idc_rack_unit请求
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
            route_name = "easyops.api.cmdb_extend.custom.ReleaseIdcRackUnit"
        uri = "/object/_IDCRACK/instance/unit/device/release"
        
        requestParam = request.deviceList
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
