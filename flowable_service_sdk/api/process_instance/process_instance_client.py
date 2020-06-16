# -*- coding: utf-8 -*-
import os
import sys


import flowable_service_sdk.api.process_instance.assign_process_instance_pb2

import google.protobuf.empty_pb2

import flowable_service_sdk.api.process_instance.cc_process_instance_pb2

import flowable_service_sdk.api.process_instance.complete_process_instance_pb2

import flowable_service_sdk.api.process_instance.delete_process_instance_pb2

import flowable_service_sdk.api.process_instance.get_process_instance_pb2

import flowable_service_sdk.api.process_instance.list_process_instance_pb2

import flowable_service_sdk.api.process_instance.start_process_instance_pb2

import flowable_service_sdk.api.process_instance.update_process_instance_state_pb2

import flowable_service_sdk.utils.http_util
import google.protobuf.json_format


class ProcessInstanceClient(object):
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

    
    def assign_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.assign_process_instance_pb2.AssignProcessInstanceRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        指派流程实例
        :param request: assign_process_instance请求
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
            route_name = "easyops.api.flowable_service.process_instance.AssignProcessInstance"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}/assignee".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flowable_service_sdk",
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
    
    def carbon_copy_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.cc_process_instance_pb2.CarbonCopyProcessInstanceRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        分阅流程实例
        :param request: carbon_copy_process_instance请求
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
            route_name = "easyops.api.flowable_service.process_instance.CarbonCopyProcessInstance"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}/cc".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flowable_service_sdk",
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
    
    def complete_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.complete_process_instance_pb2.CompleteProcessInstanceRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        完成流程实例
        :param request: complete_process_instance请求
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
            route_name = "easyops.api.flowable_service.process_instance.CompleteProcessInstance"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}/task".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flowable_service_sdk",
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
    
    def delete_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.delete_process_instance_pb2.DeleteProcessInstanceRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除流程实例
        :param request: delete_process_instance请求
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
            route_name = "easyops.api.flowable_service.process_instance.DeleteProcessInstance"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.flowable_service_sdk",
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
    
    def get_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.get_process_instance_pb2.GetProcessInstanceRequest, int, str, int) -> flowable_service_sdk.api.process_instance.get_process_instance_pb2.GetProcessInstanceResponse
        """
        获取流程实例详情
        :param request: get_process_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.process_instance.get_process_instance_pb2.GetProcessInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.process_instance.GetProcessInstance"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.process_instance.get_process_instance_pb2.GetProcessInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.list_process_instance_pb2.ListProcessInstanceRequest, int, str, int) -> flowable_service_sdk.api.process_instance.list_process_instance_pb2.ListProcessInstanceResponse
        """
        获取流程实例列表
        :param request: list_process_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.process_instance.list_process_instance_pb2.ListProcessInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.process_instance.ListProcessInstance"
        uri = "/api/flowable_service/v1/process_instance"
        
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.process_instance.list_process_instance_pb2.ListProcessInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def start_process_instance(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.start_process_instance_pb2.StartProcessInstanceRequest, int, str, int) -> flowable_service_sdk.api.process_instance.start_process_instance_pb2.StartProcessInstanceResponse
        """
        发起流程实例
        :param request: start_process_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_service_sdk.api.process_instance.start_process_instance_pb2.StartProcessInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable_service.process_instance.StartProcessInstance"
        uri = "/api/flowable_service/v1/process_instance"
        
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.flowable_service_sdk",
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
        rsp = flowable_service_sdk.api.process_instance.start_process_instance_pb2.StartProcessInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_process_instance_state(self, request, org, user, timeout=10):
        # type: (flowable_service_sdk.api.process_instance.update_process_instance_state_pb2.UpdateProcessInstanceStateRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改流程实例状态
        :param request: update_process_instance_state请求
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
            route_name = "easyops.api.flowable_service.process_instance.UpdateProcessInstanceState"
        uri = "/api/flowable_service/v1/process_instance/{instanceId}/state".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = flowable_service_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.flowable_service_sdk",
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
    
