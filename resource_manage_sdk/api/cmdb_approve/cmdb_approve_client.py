# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import model.notify.operation_log_with_meta_pb2

import google.protobuf.empty_pb2

import get_approve_count_pb2

import get_approve_object_list_pb2

import get_history_approver_list_pb2

import get_history_object_list_pb2

import instance_relation_edit_pb2

import utils.http_util
import google.protobuf.json_format


class CmdbApproveClient(object):
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

    
    def create_instance_apply_permission(self, request, org, user, timeout=10):
        # type: (model.notify.operation_log_with_meta_pb2.OperationLogWithMeta, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        创建模型提交变更权限
        :param request: create_instance_apply_permission请求
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
            route_name = "easyops.api.resource_manage.cmdb_approve.CreateInstanceApplyPermission"
        uri = "/instance/apply/permission/add"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
    
    def get_approve_count(self, request, org, user, timeout=10):
        # type: (get_approve_count_pb2.GetApproveCountRequest, int, str, int) -> get_approve_count_pb2.GetApproveCountResponse
        """
        获取待审批所有模型
        :param request: get_approve_count请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_approve_count_pb2.GetApproveCountResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.cmdb_approve.GetApproveCount"
        uri = "/api/v1/approve/count"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.resource_manage_sdk",
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
        rsp = get_approve_count_pb2.GetApproveCountResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_approve_object_list(self, request, org, user, timeout=10):
        # type: (get_approve_object_list_pb2.GetApproveObjectListRequest, int, str, int) -> get_approve_object_list_pb2.GetApproveObjectListResponse
        """
        获取待审批所有模型
        :param request: get_approve_object_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_approve_object_list_pb2.GetApproveObjectListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.cmdb_approve.GetApproveObjectList"
        uri = "/api/v1/approve/object/list"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = get_approve_object_list_pb2.GetApproveObjectListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_history_approver_list(self, request, org, user, timeout=10):
        # type: (get_history_approver_list_pb2.GetHistoryApproverListRequest, int, str, int) -> get_history_approver_list_pb2.GetHistoryApproverListResponse
        """
        获取审批历史所有审批人
        :param request: get_history_approver_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_history_approver_list_pb2.GetHistoryApproverListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.cmdb_approve.GetHistoryApproverList"
        uri = "/api/v1/history/approver/list"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = get_history_approver_list_pb2.GetHistoryApproverListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_history_object_list(self, request, org, user, timeout=10):
        # type: (get_history_object_list_pb2.GetHistoryObjectListRequest, int, str, int) -> get_history_object_list_pb2.GetHistoryObjectListResponse
        """
        获取审批历史所有模型
        :param request: get_history_object_list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_history_object_list_pb2.GetHistoryObjectListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.resource_manage.cmdb_approve.GetHistoryObjectList"
        uri = "/api/v1/history/object/list"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
        rsp = get_history_object_list_pb2.GetHistoryObjectListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_relation_edit(self, request, org, user, timeout=10):
        # type: (instance_relation_edit_pb2.InstanceRelationEditRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        实例关系变更
        :param request: instance_relation_edit请求
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
            route_name = "easyops.api.resource_manage.cmdb_approve.InstanceRelationEdit"
        uri = "/object/{object_id}/relation/{relation_side_id}/{operation}".format(
            object_id=request.object_id,
            relation_side_id=request.relation_side_id,
            operation=request.operation,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.resource_manage_sdk",
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
    
