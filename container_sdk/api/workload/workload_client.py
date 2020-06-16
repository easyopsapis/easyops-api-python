# -*- coding: utf-8 -*-
import os
import sys


import container_sdk.api.workload.create_pb2

import container_sdk.model.container.workload_pb2

import container_sdk.api.workload.create_from_yaml_pb2

import container_sdk.api.workload.delete_workload_pb2

import google.protobuf.empty_pb2

import container_sdk.api.workload.get_pb2

import container_sdk.api.workload.get_status_pb2

import container_sdk.api.workload.get_summary_pb2

import container_sdk.api.workload.list_pb2

import container_sdk.api.workload.list_event_pb2

import container_sdk.api.workload.list_history_pb2

import container_sdk.api.workload.restart_pb2

import container_sdk.api.workload.rollback_pb2

import container_sdk.api.workload.update_pb2

import container_sdk.api.workload.update_resource_spec_pb2

import container_sdk.utils.http_util
import google.protobuf.json_format


class WorkloadClient(object):
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
        # type: (container_sdk.api.workload.create_pb2.CreateRequest, int, str, int) -> container_sdk.model.container.workload_pb2.Workload
        """
        创建工作负载
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.workload_pb2.Workload
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.Create"
        uri = "/api/container/v1/workloads"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.model.container.workload_pb2.Workload()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_from_yaml(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.create_from_yaml_pb2.CreateFromYamlRequest, int, str, int) -> container_sdk.model.container.workload_pb2.Workload
        """
        通过 yaml 创建工作负载
        :param request: create_from_yaml请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.workload_pb2.Workload
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.CreateFromYaml"
        uri = "/api/container/v1/workloads/yaml"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.model.container.workload_pb2.Workload()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_workload(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.delete_workload_pb2.DeleteWorkloadRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除工作负载
        :param request: delete_workload请求
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
            route_name = "easyops.api.container.workload.DeleteWorkload"
        uri = "/api/container/v1/workloads/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.container_sdk",
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
    
    def get(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.get_pb2.GetRequest, int, str, int) -> container_sdk.api.workload.get_pb2.GetResponse
        """
        获取工作负载配置, 数据来源于 CMDB
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.workload.get_pb2.GetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.Get"
        uri = "/api/container/v1/workloads/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.workload.get_pb2.GetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_status(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.get_status_pb2.GetStatusRequest, int, str, int) -> container_sdk.model.container.workload_pb2.Workload
        """
        获取工作负载, 数据来源于现网
        :param request: get_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.workload_pb2.Workload
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.GetStatus"
        uri = "/api/container/v1/workloads/{instanceId}/status".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.model.container.workload_pb2.Workload()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_summary(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.get_summary_pb2.GetSummaryRequest, int, str, int) -> container_sdk.api.workload.get_summary_pb2.GetSummaryResponse
        """
        获取Workload Summary
        :param request: get_summary请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.workload.get_summary_pb2.GetSummaryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.GetSummary"
        uri = "/api/container/v1/workloads/{instanceId}/summary".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.workload.get_summary_pb2.GetSummaryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.list_pb2.ListRequest, int, str, int) -> container_sdk.api.workload.list_pb2.ListResponse
        """
        获取工作负载
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.workload.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.List"
        uri = "/api/container/v1/workloads"
        
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.workload.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_event(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.list_event_pb2.ListEventRequest, int, str, int) -> container_sdk.api.workload.list_event_pb2.ListEventResponse
        """
        获取workload事件记录
        :param request: list_event请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.workload.list_event_pb2.ListEventResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.ListEvent"
        uri = "/api/container/v1/workloads/{instanceId}/events".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.workload.list_event_pb2.ListEventResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_history(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.list_history_pb2.ListHistoryRequest, int, str, int) -> container_sdk.api.workload.list_history_pb2.ListHistoryResponse
        """
        获取workload版本历史
        :param request: list_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.api.workload.list_history_pb2.ListHistoryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.ListHistory"
        uri = "/api/container/v1/workloads/{instanceId}/history".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.api.workload.list_history_pb2.ListHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def restart(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.restart_pb2.RestartRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        重启工作负载
        :param request: restart请求
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
            route_name = "easyops.api.container.workload.Restart"
        uri = "/api/container/v1/workloads/{instanceId}/restart".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
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
    
    def rollback(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.rollback_pb2.RollbackRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        回滚
        :param request: rollback请求
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
            route_name = "easyops.api.container.workload.Rollback"
        uri = "/api/container/v1/workloads/{instanceId}/rollback".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
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
    
    def update(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.update_pb2.UpdateRequest, int, str, int) -> container_sdk.model.container.workload_pb2.Workload
        """
        更新工作负载
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.workload_pb2.Workload
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.Update"
        uri = "/api/container/v1/workloads/{instanceId}".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.model.container.workload_pb2.Workload()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_resource_spec(self, request, org, user, timeout=10):
        # type: (container_sdk.api.workload.update_resource_spec_pb2.UpdateResourceSpecRequest, int, str, int) -> container_sdk.model.container.workload_pb2.Workload
        """
        更新 Workload yaml 文件定义
        :param request: update_resource_spec请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: container_sdk.model.container.workload_pb2.Workload
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.container.workload.UpdateResourceSpec"
        uri = "/api/container/v1/workloads/{instanceId}/yaml".format(
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = container_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.container_sdk",
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
        rsp = container_sdk.model.container.workload_pb2.Workload()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
