# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import creat_jobs_excution_pb2

import model.ops_automation.jobs_pb2

import create_jobs_pb2

import delete_jobs_pb2

import get_job_pb2

import model.ops_automation.job_details_pb2

import get_job_change_log_pb2

import list_jobs_pb2

import update_jobs_pb2

import utils.http_util
import google.protobuf.json_format


class JobsClient(object):
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

    
    def create_jobs_excution(self, request, org, user, timeout=10):
        # type: (creat_jobs_excution_pb2.CreateJobsExcutionRequest, int, str, int) -> creat_jobs_excution_pb2.CreateJobsExcutionResponse
        """
        创建作业执行
        :param request: create_jobs_excution请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: creat_jobs_excution_pb2.CreateJobsExcutionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.CreateJobsExcution"
        uri = "/api/ops_automation/v1/jobs/execution"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ops_automation_sdk",
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
        rsp = creat_jobs_excution_pb2.CreateJobsExcutionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_jobs(self, request, org, user, timeout=10):
        # type: (model.ops_automation.jobs_pb2.Jobs, int, str, int) -> create_jobs_pb2.CreateJobsResponse
        """
        创建作业
        :param request: create_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_jobs_pb2.CreateJobsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.CreateJobs"
        uri = "/api/ops_automation/v1/jobs"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.ops_automation_sdk",
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
        rsp = create_jobs_pb2.CreateJobsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_jobs(self, request, org, user, timeout=10):
        # type: (delete_jobs_pb2.DeleteJobsRequest, int, str, int) -> delete_jobs_pb2.DeleteJobsResponse
        """
        删除作业
        :param request: delete_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_jobs_pb2.DeleteJobsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.DeleteJobs"
        uri = "/api/ops_automation/v1/jobs/{jobId}".format(
            jobId=request.jobId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.ops_automation_sdk",
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
        rsp = delete_jobs_pb2.DeleteJobsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_jobs(self, request, org, user, timeout=10):
        # type: (get_job_pb2.GetJobsRequest, int, str, int) -> model.ops_automation.job_details_pb2.JobDetails
        """
        获取作业详情
        :param request: get_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.ops_automation.job_details_pb2.JobDetails
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.GetJobs"
        uri = "/api/ops_automation/v1/jobs/{jobId}".format(
            jobId=request.jobId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ops_automation_sdk",
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
        rsp = model.ops_automation.job_details_pb2.JobDetails()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_job_change_log(self, request, org, user, timeout=10):
        # type: (get_job_change_log_pb2.GetJobChangeLogRequest, int, str, int) -> get_job_change_log_pb2.GetJobChangeLogResponse
        """
        获取作业变更历史
        :param request: get_job_change_log请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_job_change_log_pb2.GetJobChangeLogResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.GetJobChangeLog"
        uri = "/api/ops_automation/v1/jobs/{jobId}/changeLog".format(
            jobId=request.jobId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ops_automation_sdk",
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
        rsp = get_job_change_log_pb2.GetJobChangeLogResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_jobs(self, request, org, user, timeout=10):
        # type: (list_jobs_pb2.ListJobsRequest, int, str, int) -> list_jobs_pb2.ListJobsResponse
        """
        获取作业列表
        :param request: list_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_jobs_pb2.ListJobsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.ListJobs"
        uri = "/api/ops_automation/v1/jobs"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.ops_automation_sdk",
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
        rsp = list_jobs_pb2.ListJobsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_jobs(self, request, org, user, timeout=10):
        # type: (update_jobs_pb2.UpdateJobsRequest, int, str, int) -> update_jobs_pb2.UpdateJobsResponse
        """
        更新作业
        :param request: update_jobs请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_jobs_pb2.UpdateJobsResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.ops_automation.jobs.UpdateJobs"
        uri = "/api/ops_automation/v1/jobs/{jobId}".format(
            jobId=request.jobId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.ops_automation_sdk",
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
        rsp = update_jobs_pb2.UpdateJobsResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
