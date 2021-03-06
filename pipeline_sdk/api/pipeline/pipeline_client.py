# -*- coding: utf-8 -*-
import os
import sys


import pipeline_sdk.api.pipeline.create_pb2

import pipeline_sdk.model.pipeline.pipeline_pb2

import pipeline_sdk.api.pipeline.create_trigger_pb2

import pipeline_sdk.model.pipeline.trigger_pb2

import pipeline_sdk.api.pipeline.delete_pb2

import google.protobuf.empty_pb2

import pipeline_sdk.api.pipeline.delete_trigger_pb2

import pipeline_sdk.api.pipeline.delete_triggers_pb2

import pipeline_sdk.api.pipeline.execute_pb2

import pipeline_sdk.api.pipeline.get_pb2

import pipeline_sdk.api.pipeline.get_pipeline_v2_pb2

import pipeline_sdk.api.pipeline.get_trigger_pb2

import pipeline_sdk.api.pipeline.get_trigger_detail_pb2

import pipeline_sdk.api.pipeline.handle_hook_pb2

import pipeline_sdk.api.pipeline.list_pb2

import pipeline_sdk.api.pipeline.list_trigger_pb2

import pipeline_sdk.api.pipeline.list_v2_pb2

import pipeline_sdk.api.pipeline.update_pb2

import pipeline_sdk.api.pipeline.update_trigger_pb2

import pipeline_sdk.utils.http_util
import google.protobuf.json_format


class PipelineClient(object):
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
        # type: (pipeline_sdk.api.pipeline.create_pb2.CreateRequest, int, str, int) -> pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        创建流水线
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.Create"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines".format(
            project_id=request.project_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_trigger(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.create_trigger_pb2.CreateTriggerRequest, int, str, int) -> pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        创建流水线钩子
        :param request: create_trigger请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.CreateTrigger"
        uri = "/api/pipeline/v1/triggers"
        
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.trigger_pb2.Trigger()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_pipeline(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.delete_pb2.DeletePipelineRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除流水线
        :param request: delete_pipeline请求
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
            route_name = "easyops.api.pipeline.pipeline.DeletePipeline"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines/{pipeline_id}".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.pipeline_sdk",
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
    
    def delete_trigger(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.delete_trigger_pb2.DeleteTriggerRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除流水线钩子
        :param request: delete_trigger请求
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
            route_name = "easyops.api.pipeline.pipeline.DeleteTrigger"
        uri = "/api/pipeline/v1/triggers/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.pipeline_sdk",
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
    
    def delete_triggers(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.delete_triggers_pb2.DeleteTriggersRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除流水线所有钩子
        :param request: delete_triggers请求
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
            route_name = "easyops.api.pipeline.pipeline.DeleteTriggers"
        uri = "/api/pipeline/v1/triggers"
        
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.pipeline_sdk",
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
    
    def execute(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.execute_pb2.ExecuteRequest, int, str, int) -> pipeline_sdk.api.pipeline.execute_pb2.ExecuteResponse
        """
        手动触发执行流水线
        :param request: execute请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.execute_pb2.ExecuteResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.Execute"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines/{pipeline_id}/execute".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.execute_pb2.ExecuteResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.get_pb2.GetRequest, int, str, int) -> pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        获取流水线详情
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.Get"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines/{pipeline_id}".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_v_2(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.get_pipeline_v2_pb2.GetV2Request, int, str, int) -> pipeline_sdk.api.pipeline.get_pipeline_v2_pb2.GetV2Response
        """
        获取流水线详情
        :param request: get_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.get_pipeline_v2_pb2.GetV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.GetV2"
        uri = "/api/pipeline/v2/projects/{project_id}/pipelines/{pipeline_id}".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.get_pipeline_v2_pb2.GetV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_trigger(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.get_trigger_pb2.GetTriggerRequest, int, str, int) -> pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        获取钩子详情
        :param request: get_trigger请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.GetTrigger"
        uri = "/api/pipeline/v1/triggers/{id}".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.trigger_pb2.Trigger()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_trigger_detail(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.get_trigger_detail_pb2.GetTriggerDetailRequest, int, str, int) -> pipeline_sdk.api.pipeline.get_trigger_detail_pb2.GetTriggerDetailResponse
        """
        获取钩子相关信息
        :param request: get_trigger_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.get_trigger_detail_pb2.GetTriggerDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.GetTriggerDetail"
        uri = "/api/pipeline/v1/triggers/{id}/detail".format(
            id=request.id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.get_trigger_detail_pb2.GetTriggerDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def handle_hook(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.handle_hook_pb2.HandleHookRequest, int, str, int) -> pipeline_sdk.api.pipeline.handle_hook_pb2.HandleHookResponse
        """
        webhook触发执行流水线
        :param request: handle_hook请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.handle_hook_pb2.HandleHookResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.HandleHook"
        uri = "/api/pipeline/v1/webhook/{provider}/hook/{token}".format(
            provider=request.provider,
            token=request.token,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.handle_hook_pb2.HandleHookResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.list_pb2.ListRequest, int, str, int) -> pipeline_sdk.api.pipeline.list_pb2.ListResponse
        """
        流水线列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.List"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines".format(
            project_id=request.project_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_trigger(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.list_trigger_pb2.ListTriggerRequest, int, str, int) -> pipeline_sdk.api.pipeline.list_trigger_pb2.ListTriggerResponse
        """
        钩子列表
        :param request: list_trigger请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.list_trigger_pb2.ListTriggerResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.ListTrigger"
        uri = "/api/pipeline/v1/triggers"
        
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.list_trigger_pb2.ListTriggerResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_v_2(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.list_v2_pb2.ListV2Request, int, str, int) -> pipeline_sdk.api.pipeline.list_v2_pb2.ListV2Response
        """
        流水线列表
        :param request: list_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.pipeline.list_v2_pb2.ListV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.ListV2"
        uri = "/api/pipeline/v2/projects/{project_id}/pipelines".format(
            project_id=request.project_id,
        )
        requestParam = request
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.api.pipeline.list_v2_pb2.ListV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.update_pb2.UpdateRequest, int, str, int) -> pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        修改流水线
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.Update"
        uri = "/api/pipeline/v1/projects/{project_id}/pipelines/{pipeline_id}".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request.pipeline
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_trigger(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.pipeline.update_trigger_pb2.UpdateTriggerRequest, int, str, int) -> pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        更新流水线钩子
        :param request: update_trigger请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.trigger_pb2.Trigger
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.UpdateTrigger"
        uri = "/api/pipeline/v1/triggers/{id}".format(
            id=request.id,
        )
        requestParam = request.trigger
        
        rsp_obj = pipeline_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.pipeline_sdk",
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
        rsp = pipeline_sdk.model.pipeline.trigger_pb2.Trigger()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
