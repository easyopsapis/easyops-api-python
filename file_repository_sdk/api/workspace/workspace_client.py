# -*- coding: utf-8 -*-

import check_workspace_base_pb2

import google.protobuf.empty_pb2

import commit_worksapce_pb2

import compare_workspace_pb2

import compare_workspace_with_version_pb2

import get_file_info_pb2

import get_file_list_pb2

import model.file_repository.diff_pb2

import init_workspace_pb2

import safe_commit_workspace_pb2

import utils.http_util
import google.protobuf.json_format


class WorkspaceClient(object):
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

    
    def check_workspace_base(self, request, org, user, timeout=10):
        # type: (check_workspace_base_pb2.CheckWorkspaceBaseRequest, int, str, int) -> check_workspace_base_pb2.CheckWorkspaceBaseResponse
        """
        检查工作区baseId
        :param request: check_workspace_base请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: check_workspace_base_pb2.CheckWorkspaceBaseResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.CheckWorkspaceBase"
        uri = "/workspace/check/@packageId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
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
        rsp = check_workspace_base_pb2.CheckWorkspaceBaseResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def clear(self, request, org, user, timeout=10):
        # type: (clear_workspace_pb2.ClearRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        清空工作区
        :param request: clear请求
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
            route_name = "easyops.api.file_repository.workspace.Clear"
        uri = "/workspace/@packageId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.file_repository_sdk",
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
    
    def commit_workspace(self, request, org, user, timeout=10):
        # type: (commit_worksapce_pb2.CommitWorkspaceRequest, int, str, int) -> commit_worksapce_pb2.CommitWorkspaceResponse
        """
        提交工作区创建新归档版本
        :param request: commit_workspace请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: commit_worksapce_pb2.CommitWorkspaceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.CommitWorkspace"
        uri = "/workspace/{packageId}".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
        rsp = commit_worksapce_pb2.CommitWorkspaceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def file_compare(self, request, org, user, timeout=10):
        # type: (compare_workspace_pb2.FileCompareRequest, int, str, int) -> compare_workspace_pb2.FileCompareResponse
        """
        比较工作区文件
        :param request: file_compare请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: compare_workspace_pb2.FileCompareResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.FileCompare"
        uri = "/workspace/@packageId/file/compare"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
        rsp = compare_workspace_pb2.FileCompareResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def compare_workspace_with_version(self, request, org, user, timeout=10):
        # type: (compare_workspace_with_version_pb2.CompareWorkspaceWithVersionRequest, int, str, int) -> compare_workspace_with_version_pb2.CompareWorkspaceWithVersionResponse
        """
        工作区与版本比较
        :param request: compare_workspace_with_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: compare_workspace_with_version_pb2.CompareWorkspaceWithVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.CompareWorkspaceWithVersion"
        uri = "/workspace/@packageId/compareWithVersion"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
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
        rsp = compare_workspace_with_version_pb2.CompareWorkspaceWithVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_file_info(self, request, org, user, timeout=10):
        # type: (get_file_info_pb2.GetFileInfoRequest, int, str, int) -> get_file_info_pb2.GetFileInfoResponse
        """
        获取工作区文件信息
        :param request: get_file_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_file_info_pb2.GetFileInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.GetFileInfo"
        uri = "/v2/workspace/{packageId}/file".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
        rsp = get_file_info_pb2.GetFileInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_file_list(self, request, org, user, timeout=10):
        # type: (get_file_list_pb2.GetFileListRequest, int, str, int) -> get_file_list_pb2.GetFileListResponse
        """
        获取工作区文件列表
        :param request: get_file_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_file_list_pb2.GetFileListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.GetFileList"
        uri = "/v2/workspace/{packageId}/file".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
        rsp = get_file_list_pb2.GetFileListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def status(self, request, org, user, timeout=10):
        # type: (get_workspace_status_pb2.StatusRequest, int, str, int) -> model.file_repository.diff_pb2.Diff
        """
        查询工作区状态
        :param request: status请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: model.file_repository.diff_pb2.Diff
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.Status"
        uri = "/workspace/@packageId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.file_repository_sdk",
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
        rsp = model.file_repository.diff_pb2.Diff()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def init(self, request, org, user, timeout=10):
        # type: (init_workspace_pb2.InitRequest, int, str, int) -> init_workspace_pb2.InitResponse
        """
        初始化工作区
        :param request: init请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: init_workspace_pb2.InitResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.Init"
        uri = "/workspace/@packageId"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.file_repository_sdk",
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
        rsp = init_workspace_pb2.InitResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def safe_commit_workspace(self, request, org, user, timeout=10):
        # type: (safe_commit_workspace_pb2.SafeCommitWorkspaceRequest, int, str, int) -> safe_commit_workspace_pb2.SafeCommitWorkspaceResponse
        """
        提交工作区创建新归档版本v2
        :param request: safe_commit_workspace请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: safe_commit_workspace_pb2.SafeCommitWorkspaceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.file_repository.workspace.SafeCommitWorkspace"
        uri = "/v2/workspace/{packageId}".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
        rsp = safe_commit_workspace_pb2.SafeCommitWorkspaceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_file(self, request, org, user, timeout=10):
        # type: (update_file_pb2.UpdateFileRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        工作区文件修改
        :param request: update_file请求
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
            route_name = "easyops.api.file_repository.workspace.UpdateFile"
        uri = "/v2/workspace/{packageId}/file".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
    
    def upload_file(self, request, org, user, timeout=10):
        # type: (upload_file_pb2.UploadFileRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        上传文件
        :param request: upload_file请求
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
            route_name = "easyops.api.file_repository.workspace.UploadFile"
        uri = "/workspace/{packageId}/upload".format(
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.file_repository_sdk",
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
    
