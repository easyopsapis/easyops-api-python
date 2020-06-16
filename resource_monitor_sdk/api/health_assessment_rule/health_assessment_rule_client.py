# -*- coding: utf-8 -*-
import os
import sys


import resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_pb2

import resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_by_object_id_pb2

import resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_pb2

import resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_object_id_pb2

import resource_monitor_sdk.api.health_assessment_rule.list_health_assessment_rule_pb2

import resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_pb2

import resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_by_related_resource_pb2

import resource_monitor_sdk.utils.http_util
import google.protobuf.json_format


class HealthAssessmentRuleClient(object):
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

    
    def create_health_assessment_rule(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_pb2.CreateHealthAssessmentRuleRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_pb2.CreateHealthAssessmentRuleResponse
        """
        创建健康评分规则 
        :param request: create_health_assessment_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_pb2.CreateHealthAssessmentRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.CreateHealthAssessmentRule"
        uri = "/api/v1/health-assessment/rule"
        
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_pb2.CreateHealthAssessmentRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_health_assessment_rule_by_object_id(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_by_object_id_pb2.CreateHealthAssessmentRuleByObjectIdRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_by_object_id_pb2.CreateHealthAssessmentRuleByObjectIdResponse
        """
        依据objectId初始化健康评分规则
        :param request: create_health_assessment_rule_by_object_id请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_by_object_id_pb2.CreateHealthAssessmentRuleByObjectIdResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.CreateHealthAssessmentRuleByObjectId"
        uri = "/api/v1/health-assessment/object_id/{objectId}/rule".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.create_health_assessment_rule_by_object_id_pb2.CreateHealthAssessmentRuleByObjectIdResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_health_assessment_rule(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_pb2.GetHealthAssessmentRuleRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_pb2.GetHealthAssessmentRuleResponse
        """
        查看健康评分规则详情
        :param request: get_health_assessment_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_pb2.GetHealthAssessmentRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.GetHealthAssessmentRule"
        uri = "/api/v1/health-assessment/rule/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_pb2.GetHealthAssessmentRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_health_assessment_rule_by_object_id(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_object_id_pb2.GetHealthAssessmentRuleByObjectIdRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_object_id_pb2.GetHealthAssessmentRuleByObjectIdResponse
        """
        通过ObjectId查看健康评分规则详情
        :param request: get_health_assessment_rule_by_object_id请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_object_id_pb2.GetHealthAssessmentRuleByObjectIdResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.GetHealthAssessmentRuleByObjectId"
        uri = "/api/v1/health-assessment/object_id/{objectId}/rule".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.get_health_assessment_rule_object_id_pb2.GetHealthAssessmentRuleByObjectIdResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_health_assessment_rule(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.list_health_assessment_rule_pb2.ListHealthAssessmentRuleRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.list_health_assessment_rule_pb2.ListHealthAssessmentRuleResponse
        """
        查看健康评分规则列表
        :param request: list_health_assessment_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.list_health_assessment_rule_pb2.ListHealthAssessmentRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.ListHealthAssessmentRule"
        uri = "/api/v1/health-assessment/rule"
        
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.list_health_assessment_rule_pb2.ListHealthAssessmentRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_health_assessment_rule(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_pb2.UpdateHealthAssessmentRuleRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_pb2.UpdateHealthAssessmentRuleResponse
        """
        更新健康评分规则
        :param request: update_health_assessment_rule请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_pb2.UpdateHealthAssessmentRuleResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.UpdateHealthAssessmentRule"
        uri = "/api/v1/health-assessment/rule/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_pb2.UpdateHealthAssessmentRuleResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_health_assessment_rule_by_related_resource(self, request, org, user, timeout=10):
        # type: (resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_by_related_resource_pb2.UpdateHealthAssessmentRuleByRelatedResourceRequest, int, str, int) -> resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_by_related_resource_pb2.UpdateHealthAssessmentRuleByRelatedResourceResponse
        """
        依据关联资源更新健康评分规则 
        :param request: update_health_assessment_rule_by_related_resource请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_by_related_resource_pb2.UpdateHealthAssessmentRuleByRelatedResourceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_monitor.health_assessment_rule.UpdateHealthAssessmentRuleByRelatedResource"
        uri = " /api/v1/health-assessment/object_id/{objectId}/rule_related_resource".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = resource_monitor_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.resource_monitor_sdk",
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
        rsp = resource_monitor_sdk.api.health_assessment_rule.update_health_assessment_rule_by_related_resource_pb2.UpdateHealthAssessmentRuleByRelatedResourceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
