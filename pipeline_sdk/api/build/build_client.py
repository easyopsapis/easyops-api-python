# -*- coding: utf-8 -*-
import os
import sys


import pipeline_sdk.model.pipeline.progress_log_pb2

import pipeline_sdk.api.build.approval_pb2

import google.protobuf.empty_pb2

import pipeline_sdk.api.build.cancel_build_pb2

import pipeline_sdk.api.build.create_pb2

import pipeline_sdk.model.pipeline.build_pb2

import pipeline_sdk.api.build.create_stage_status_pb2

import pipeline_sdk.model.pipeline.stage_status_pb2

import pipeline_sdk.api.build.failed_retry_pb2

import pipeline_sdk.api.build.get_pb2

import pipeline_sdk.api.build.get_progress_log_pb2

import pipeline_sdk.api.build.list_pb2

import pipeline_sdk.api.build.record_events_pb2

import pipeline_sdk.api.build.retry_pb2

import pipeline_sdk.api.build.update_build_artifact_pb2

import pipeline_sdk.api.build.update_build_status_pb2

import pipeline_sdk.api.build.update_events_pb2

import pipeline_sdk.utils.http_util
import google.protobuf.json_format


class BuildClient(object):
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

    
    def append_progress_log(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog, int, str, int) -> pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        追加实时日志
        :param request: append_progress_log请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.AppendProgressLog"
        uri = "/api/pipeline/v1/progress_log/{id}/append".format(
            id=request.id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def approval(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.approval_pb2.ApprovalRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        人工审批
        :param request: approval请求
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
            route_name = "easyops.api.pipeline.build.Approval"
        uri = "/api/pipeline/v1/builds/{build_id}/approval/{step_id}".format(
            build_id=request.build_id,
            step_id=request.step_id,
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def cancel(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.cancel_build_pb2.CancelRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        终止构建
        :param request: cancel请求
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
            route_name = "easyops.api.pipeline.build.Cancel"
        uri = "/api/pipeline/v1/builds/{build_id}/cancel".format(
            build_id=request.build_id,
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.create_pb2.CreateRequest, int, str, int) -> pipeline_sdk.model.pipeline.build_pb2.Build
        """
        创建构建任务记录
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.build_pb2.Build
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.Create"
        uri = "/api/pipeline/v1/builds"
        
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
        rsp = pipeline_sdk.model.pipeline.build_pb2.Build()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_progress_log(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog, int, str, int) -> pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        创建实时日志
        :param request: create_progress_log请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.CreateProgressLog"
        uri = "/api/pipeline/v1/progress_log"
        
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
        rsp = pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_stage_status(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.create_stage_status_pb2.CreateStageStatusRequest, int, str, int) -> pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus
        """
        创建构建stage记录
        :param request: create_stage_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.CreateStageStatus"
        uri = "/api/pipeline/v1/stage_status"
        
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
        rsp = pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def failed_retry(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.failed_retry_pb2.FailedRetryRequest, int, str, int) -> pipeline_sdk.api.build.failed_retry_pb2.FailedRetryResponse
        """
        从失败处重试
        :param request: failed_retry请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.build.failed_retry_pb2.FailedRetryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.FailedRetry"
        uri = "/api/pipeline/v1/builds/{build_id}/retry".format(
            build_id=request.build_id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.api.build.failed_retry_pb2.FailedRetryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.get_pb2.GetRequest, int, str, int) -> pipeline_sdk.api.build.get_pb2.GetResponse
        """
        获取单个流水线任务详情
        :param request: get请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.build.get_pb2.GetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.Get"
        uri = "/api/pipeline/v1/builds/{build_id}".format(
            build_id=request.build_id,
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
        rsp = pipeline_sdk.api.build.get_pb2.GetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_progress_log(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.get_progress_log_pb2.GetProgressLogRequest, int, str, int) -> pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        获取实时日志
        :param request: get_progress_log请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.GetProgressLog"
        uri = "/api/pipeline/v1/progress_log/{id}".format(
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
        rsp = pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.list_pb2.ListRequest, int, str, int) -> pipeline_sdk.api.build.list_pb2.ListResponse
        """
        获取流水线任务列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.build.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.List"
        uri = "/api/pipeline/v1/buildlist"
        
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
        rsp = pipeline_sdk.api.build.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def record_events(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.record_events_pb2.RecordEventsRequest, int, str, int) -> pipeline_sdk.model.pipeline.build_pb2.Build
        """
        追加构建任务事件日志
        :param request: record_events请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.build_pb2.Build
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.RecordEvents"
        uri = "/api/pipeline/v1/builds/{build_id}/events".format(
            build_id=request.build_id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.build_pb2.Build()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def retry(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.retry_pb2.RetryRequest, int, str, int) -> pipeline_sdk.api.build.retry_pb2.RetryResponse
        """
        重试
        :param request: retry请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.build.retry_pb2.RetryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.Retry"
        uri = "/api/pipeline/v1/builds/{build_id}/retry".format(
            build_id=request.build_id,
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
        rsp = pipeline_sdk.api.build.retry_pb2.RetryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_artifact(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.update_build_artifact_pb2.UpdateArtifactRequest, int, str, int) -> pipeline_sdk.api.build.update_build_artifact_pb2.UpdateArtifactResponse
        """
        更新制品包信息
        :param request: update_artifact请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.api.build.update_build_artifact_pb2.UpdateArtifactResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.UpdateArtifact"
        uri = "/api/pipeline/v1/builds/{build_id}/update_artifact".format(
            build_id=request.build_id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.api.build.update_build_artifact_pb2.UpdateArtifactResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_build_status(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.update_build_status_pb2.UpdateBuildStatusRequest, int, str, int) -> pipeline_sdk.model.pipeline.build_pb2.Build
        """
        修改构建任务记录
        :param request: update_build_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.build_pb2.Build
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.UpdateBuildStatus"
        uri = "/api/pipeline/v1/builds/{build_id}".format(
            build_id=request.build_id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.build_pb2.Build()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_events(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.api.build.update_events_pb2.UpdateEventsRequest, int, str, int) -> pipeline_sdk.model.pipeline.build_pb2.Build
        """
        更新构建任务事件日志
        :param request: update_events请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.build_pb2.Build
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.UpdateEvents"
        uri = "/api/pipeline/v2/builds/{build_id}/events".format(
            build_id=request.build_id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.build_pb2.Build()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_progress_log(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog, int, str, int) -> pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        修改实时日志
        :param request: update_progress_log请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.UpdateProgressLog"
        uri = "/api/pipeline/v1/progress_log/{id}".format(
            id=request.id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.progress_log_pb2.ProgressLog()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_stage_status(self, request, org, user, timeout=10):
        # type: (pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus, int, str, int) -> pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus
        """
        创建构建stage记录
        :param request: update_stage_status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.pipeline.build.UpdateStageStatus"
        uri = "/api/pipeline/v1/stage_status/{id}".format(
            id=request.id,
        )
        requestParam = request
        
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
        rsp = pipeline_sdk.model.pipeline.stage_status_pb2.StageStatus()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
