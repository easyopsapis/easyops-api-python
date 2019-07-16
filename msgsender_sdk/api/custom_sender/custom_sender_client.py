# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import google.protobuf.empty_pb2

import list_support_infom_pb2

import model.msgsender.send_message_request_pb2

import send_message_pb2

import model.msgsender.send_message_for_alert_request_pb2

import send_message_with_alert_pb2

import model.msgsender.send_message_with_appendix_request_pb2

import send_message_with_appendix_pb2

import utils.http_util
import google.protobuf.json_format


class CustomSenderClient(object):
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

    
    def list_support_inform(self, request, org, user, timeout=10):
        # type: (google.protobuf.empty_pb2.Empty, int, str, int) -> list_support_infom_pb2.ListSupportInformResponse
        """
        获取消息通道目前支持的通知方式
        :param request: list_support_inform请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_support_infom_pb2.ListSupportInformResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.msgsender.custom_sender.ListSupportInform"
        uri = "/api/v1/message_sender/method"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.msgsender_sdk",
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
        rsp = list_support_infom_pb2.ListSupportInformResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def send_message(self, request, org, user, timeout=10):
        # type: (model.msgsender.send_message_request_pb2.SendMessageRequest, int, str, int) -> send_message_pb2.SendMessageResponse
        """
        发送通知消息
        :param request: send_message请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: send_message_pb2.SendMessageResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.msgsender.custom_sender.SendMessage"
        uri = "/api/v1/message_sender/send_message"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.msgsender_sdk",
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
        rsp = send_message_pb2.SendMessageResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def send_message_for_alert(self, request, org, user, timeout=10):
        # type: (model.msgsender.send_message_for_alert_request_pb2.SendMessageForAlertRequest, int, str, int) -> send_message_with_alert_pb2.SendMessageForAlertResponse
        """
        处理告警通知消息
        :param request: send_message_for_alert请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: send_message_with_alert_pb2.SendMessageForAlertResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.msgsender.custom_sender.SendMessageForAlert"
        uri = "/api/v1/alert_adapter/receive"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.msgsender_sdk",
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
        rsp = send_message_with_alert_pb2.SendMessageForAlertResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def send_message_with_appendix(self, request, org, user, timeout=10):
        # type: (model.msgsender.send_message_with_appendix_request_pb2.SendMessageWithAppendixRequest, int, str, int) -> send_message_with_appendix_pb2.SendMessageWithAppendixResponse
        """
        处理带附件的通知消息
        :param request: send_message_with_appendix请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: send_message_with_appendix_pb2.SendMessageWithAppendixResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.msgsender.custom_sender.SendMessageWithAppendix"
        uri = "/api/v1/message_sender/mail_with_appendix"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.msgsender_sdk",
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
        rsp = send_message_with_appendix_pb2.SendMessageWithAppendixResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
