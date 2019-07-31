# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import create_pb2

import delete_pb2

import google.protobuf.empty_pb2

import list_pb2

import update_pb2

import utils.http_util
import google.protobuf.json_format


class SubscriberManagerClient(object):
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

    
    def pub_subscriber_create(self, request, org, user, timeout=10):
        # type: (create_pb2.PubSubscriberCreateRequest, int, str, int) -> create_pb2.PubSubscriberCreateResponse
        """
        添加订阅
        :param request: pub_subscriber_create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_pb2.PubSubscriberCreateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.notify.subscriber_manager.PubSubscriberCreate"
        uri = "/api/subscriber_manager/v1/subscribers"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.notify_sdk",
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
        rsp = create_pb2.PubSubscriberCreateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def pub_subscriber_delete(self, request, org, user, timeout=10):
        # type: (delete_pb2.PubSubscriberDeleteRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除订阅
        :param request: pub_subscriber_delete请求
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
            route_name = "easyops.api.notify.subscriber_manager.PubSubscriberDelete"
        uri = "/api/subscriber_manager/v1/subscribers/{subscriberId}".format(
            subscriberId=request.subscriberId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.notify_sdk",
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
    
    def pub_subscriber_list(self, request, org, user, timeout=10):
        # type: (list_pb2.PubSubscriberListRequest, int, str, int) -> list_pb2.PubSubscriberListResponse
        """
        获取订阅列表
        :param request: pub_subscriber_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.PubSubscriberListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.notify.subscriber_manager.PubSubscriberList"
        uri = "/api/subscriber_manager/v1/subscribers"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.notify_sdk",
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
        rsp = list_pb2.PubSubscriberListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def pub_subscriber_update(self, request, org, user, timeout=10):
        # type: (update_pb2.PubSubscriberUpdateRequest, int, str, int) -> update_pb2.PubSubscriberUpdateResponse
        """
        更新订阅
        :param request: pub_subscriber_update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_pb2.PubSubscriberUpdateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.notify.subscriber_manager.PubSubscriberUpdate"
        uri = "/api/subscriber_manager/v1/subscribers/{subscriberId}".format(
            subscriberId=request.subscriberId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.notify_sdk",
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
        rsp = update_pb2.PubSubscriberUpdateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
