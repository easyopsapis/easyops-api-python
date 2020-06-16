# -*- coding: utf-8 -*-
import os
import sys


import easy_flow_sdk.model.easy_flow.task_ret_pb2

import easy_flow_sdk.api.deploy.callback_pb2

import easy_flow_sdk.api.deploy.create_pb2

import easy_flow_sdk.api.deploy.get_pb2

import easy_flow_sdk.api.deploy.list_pb2

import easy_flow_sdk.utils.http_util
import google.protobuf.json_format


class DeployClient(object):
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

    
    def callback(self, request, org, user, timeout=10):
        # type: (easy_flow_sdk.model.easy_flow.task_ret_pb2.TaskRet, int, str, int) -> easy_flow_sdk.api.deploy.callback_pb2.CallbackResponse
        """
        部署任务回调
        :param request: callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_flow_sdk.api.deploy.callback_pb2.CallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_flow.deploy.Callback"
        uri = "/deployTask/callback"
        
        requestParam = request
        
        rsp_obj = easy_flow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_flow_sdk",
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
        rsp = easy_flow_sdk.api.deploy.callback_pb2.CallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create(self, request, org, user, timeout=10):
        # type: (easy_flow_sdk.api.deploy.create_pb2.CreateRequest, int, str, int) -> easy_flow_sdk.api.deploy.create_pb2.CreateResponse
        """
        启动装包任务
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_flow_sdk.api.deploy.create_pb2.CreateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_flow.deploy.Create"
        uri = "/deployTask"
        
        requestParam = request
        
        rsp_obj = easy_flow_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.easy_flow_sdk",
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
        rsp = easy_flow_sdk.api.deploy.create_pb2.CreateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get(self, request, org, user, timeout=10):
        # type: (easy_flow_sdk.api.deploy.get_pb2.GetRequest, int, str, int) -> easy_flow_sdk.api.deploy.get_pb2.GetResponse
        """
        查询装包任务
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_flow_sdk.api.deploy.get_pb2.GetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_flow.deploy.Get"
        uri = "/deployTask/{taskId}".format(
            taskId=request.taskId,
        )
        requestParam = request
        
        rsp_obj = easy_flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_flow_sdk",
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
        rsp = easy_flow_sdk.api.deploy.get_pb2.GetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (easy_flow_sdk.api.deploy.list_pb2.ListRequest, int, str, int) -> easy_flow_sdk.api.deploy.list_pb2.ListResponse
        """
        批量查询装包任务
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: easy_flow_sdk.api.deploy.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.easy_flow.deploy.List"
        uri = "/deployTaskList/{taskIdList}".format(
            taskIdList=request.taskIdList,
        )
        requestParam = request
        
        rsp_obj = easy_flow_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.easy_flow_sdk",
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
        rsp = easy_flow_sdk.api.deploy.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
