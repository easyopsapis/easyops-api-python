# -*- coding: utf-8 -*-
import os
import sys


import flowable_sdk.api.deployment.delete_deployment_pb2

import google.protobuf.empty_pb2

import flowable_sdk.api.deployment.get_deployment_pb2

import flowable_sdk.model.flowable.deployment_pb2

import flowable_sdk.api.deployment.get_deployment_resource_pb2

import flowable_sdk.model.flowable.deployment_resource_pb2

import flowable_sdk.api.deployment.list_deployment_pb2

import flowable_sdk.utils.http_util
import google.protobuf.json_format


class DeploymentClient(object):
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

    
    def delete_deployment(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.deployment.delete_deployment_pb2.DeleteDeploymentRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除部署
        :param request: delete_deployment请求
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
            route_name = "easyops.api.flowable.deployment.DeleteDeployment"
        uri = "/flowable-rest/service/repository/deployments/{deploymentId}".format(
            deploymentId=request.deploymentId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.flowable_sdk",
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
    
    def get_deployment(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.deployment.get_deployment_pb2.GetDeploymentRequest, int, str, int) -> flowable_sdk.model.flowable.deployment_pb2.FlowableDeployment
        """
        获取部署详情
        :param request: get_deployment请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.model.flowable.deployment_pb2.FlowableDeployment
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.deployment.GetDeployment"
        uri = "/flowable-rest/service/repository/deployments/{deploymentId}".format(
            deploymentId=request.deploymentId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.model.flowable.deployment_pb2.FlowableDeployment()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_deployment_resource(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.deployment.get_deployment_resource_pb2.GetDeploymentResourceRequest, int, str, int) -> flowable_sdk.model.flowable.deployment_resource_pb2.FlowableDeploymentResource
        """
        获取部署资源
        :param request: get_deployment_resource请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.model.flowable.deployment_resource_pb2.FlowableDeploymentResource
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.deployment.GetDeploymentResource"
        uri = "/flowable-rest/service/repository/deployments/{deploymentId}/resources".format(
            deploymentId=request.deploymentId,
        )
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.model.flowable.deployment_resource_pb2.FlowableDeploymentResource()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_deployment(self, request, org, user, timeout=10):
        # type: (flowable_sdk.api.deployment.list_deployment_pb2.ListDeploymentRequest, int, str, int) -> flowable_sdk.api.deployment.list_deployment_pb2.ListDeploymentResponse
        """
        部署列表
        :param request: list_deployment请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: flowable_sdk.api.deployment.list_deployment_pb2.ListDeploymentResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.flowable.deployment.ListDeployment"
        uri = "/flowable-rest/service/repository/deployments"
        
        requestParam = request
        
        rsp_obj = flowable_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.flowable_sdk",
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
        rsp = flowable_sdk.api.deployment.list_deployment_pb2.ListDeploymentResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
