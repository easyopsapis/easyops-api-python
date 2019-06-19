# -*- coding: utf-8 -*-

import model.pipeline.pipeline_pb2

import google.protobuf.empty_pb2

import execute_pb2

import list_pb2

import trigger_pb2

import utils.http_util
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
        # type: (create_pb2.CreateRequest, int, str, int) -> model.pipeline.pipeline_pb2.Pipeline
        """
        创建流水线
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.pipeline.pipeline_pb2.Pipeline
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
        requestParam = request.pipeline
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_pipeline(self, request, org, user, timeout=10):
        # type: (delete_pb2.DeletePipelineRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        # type: (execute_pb2.ExecuteRequest, int, str, int) -> execute_pb2.ExecuteResponse
        """
        手动触发执行流水线
        :param request: execute请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: execute_pb2.ExecuteResponse
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = execute_pb2.ExecuteResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get(self, request, org, user, timeout=10):
        # type: (get_pb2.GetRequest, int, str, int) -> model.pipeline.pipeline_pb2.Pipeline
        """
        获取流水线详情
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.pipeline.pipeline_pb2.Pipeline
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (list_pb2.ListRequest, int, str, int) -> list_pb2.ListResponse
        """
        流水线列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_pb2.ListResponse
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def trigger(self, request, org, user, timeout=10):
        # type: (trigger_pb2.TriggerRequest, int, str, int) -> trigger_pb2.TriggerResponse
        """
        webhook触发执行流水线
        :param request: trigger请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: trigger_pb2.TriggerResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.pipeline.Trigger"
        uri = "/api/pipeline/v1/project/{project_id}/pipelines/{pipeline_id}/hook".format(
            project_id=request.project_id,
            pipeline_id=request.pipeline_id,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = trigger_pb2.TriggerResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (update_pb2.UpdateRequest, int, str, int) -> model.pipeline.pipeline_pb2.Pipeline
        """
        修改流水线
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.pipeline.pipeline_pb2.Pipeline
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
        
        rsp_obj = utils.http_util.do_api_request(
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
        rsp = model.pipeline.pipeline_pb2.Pipeline()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
