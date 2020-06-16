# -*- coding: utf-8 -*-
import os
import sys


import assets_inventory_sdk.model.assets_inventory.user_setting_pb2

import google.protobuf.empty_pb2

import assets_inventory_sdk.api.idcrack.list_device_type_pb2

import assets_inventory_sdk.api.idcrack.list_user_setting_pb2

import assets_inventory_sdk.api.idcrack.list_v2_pb2

import assets_inventory_sdk.api.idcrack.update_layout_pb2

import assets_inventory_sdk.utils.http_util
import google.protobuf.json_format


class IdcrackClient(object):
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

    
    def create_user_setting(self, request, org, user, timeout=10):
        # type: (assets_inventory_sdk.model.assets_inventory.user_setting_pb2.InventoryUserSetting, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        创建展示字段用户设置
        :param request: create_user_setting请求
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
            route_name = "easyops.api.assets_inventory.idcrack.CreateUserSetting"
        uri = "/api/assets_inventory/v1/user_setting"
        
        requestParam = request
        
        rsp_obj = assets_inventory_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.assets_inventory_sdk",
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
    
    def list_device_type(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> assets_inventory_sdk.api.idcrack.list_device_type_pb2.ListDeviceTypeResponse
        """
        获取机柜上所有的设备列表
        :param request: list_device_type请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: assets_inventory_sdk.api.idcrack.list_device_type_pb2.ListDeviceTypeResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.assets_inventory.idcrack.ListDeviceType"
        uri = "/api/assets_inventory/v1/device_types"
        
        requestParam = request
        
        rsp_obj = assets_inventory_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.assets_inventory_sdk",
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
        rsp = assets_inventory_sdk.api.idcrack.list_device_type_pb2.ListDeviceTypeResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_user_setting(self, request, org, user, timeout=10):
        # type: (assets_inventory_sdk.api.idcrack.list_user_setting_pb2.ListUserSettingRequest, int, str, int) -> assets_inventory_sdk.api.idcrack.list_user_setting_pb2.ListUserSettingResponse
        """
        获取展示字段用户设置列表
        :param request: list_user_setting请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: assets_inventory_sdk.api.idcrack.list_user_setting_pb2.ListUserSettingResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.assets_inventory.idcrack.ListUserSetting"
        uri = "/api/assets_inventory/v1/user_setting"
        
        requestParam = request
        
        rsp_obj = assets_inventory_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.assets_inventory_sdk",
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
        rsp = assets_inventory_sdk.api.idcrack.list_user_setting_pb2.ListUserSettingResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_idc_rack_v_2(self, request, org, user, timeout=10):
        # type: (assets_inventory_sdk.api.idcrack.list_v2_pb2.ListIDCRackV2Request, int, str, int) -> assets_inventory_sdk.api.idcrack.list_v2_pb2.ListIDCRackV2Response
        """
        通过机柜ID列表获取机柜列表, 适用idc:1.1.x 以上版本
        :param request: list_idc_rack_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: assets_inventory_sdk.api.idcrack.list_v2_pb2.ListIDCRackV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.assets_inventory.idcrack.ListIDCRackV2"
        uri = "/api/assets_inventory/v2/idcracks"
        
        requestParam = request
        
        rsp_obj = assets_inventory_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.assets_inventory_sdk",
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
        rsp = assets_inventory_sdk.api.idcrack.list_v2_pb2.ListIDCRackV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_idc_rack_layout(self, request, org, user, timeout=10):
        # type: (assets_inventory_sdk.api.idcrack.update_layout_pb2.UpdateIDCRackLayoutRequest, int, str, int) -> assets_inventory_sdk.api.idcrack.update_layout_pb2.UpdateIDCRackLayoutResponse
        """
        更新机柜布局
        :param request: update_idc_rack_layout请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: assets_inventory_sdk.api.idcrack.update_layout_pb2.UpdateIDCRackLayoutResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.assets_inventory.idcrack.UpdateIDCRackLayout"
        uri = "/api/assets_inventory/v1/idcracks/{idcrackId}/layout".format(
            idcrackId=request.idcrackId,
        )
        requestParam = request
        
        rsp_obj = assets_inventory_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.assets_inventory_sdk",
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
        rsp = assets_inventory_sdk.api.idcrack.update_layout_pb2.UpdateIDCRackLayoutResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
