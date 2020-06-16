# -*- coding: utf-8 -*-
import os
import sys


import cmdb_sdk.api.object_relation.create_pb2

import cmdb_sdk.model.cmdb.object_relation_pb2

import cmdb_sdk.api.object_relation.delete_pb2

import google.protobuf.empty_pb2

import cmdb_sdk.api.object_relation.get_object_relation_snapshot_pb2

import cmdb_sdk.api.object_relation.get_relations_by_group_id_pb2

import cmdb_sdk.utils.http_util
import google.protobuf.json_format


class ObjectRelationClient(object):
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
        # type: (cmdb_sdk.api.object_relation.create_pb2.CreateRequest, int, str, int) -> cmdb_sdk.model.cmdb.object_relation_pb2.ObjectRelation
        """
        创建模型关系定义
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.model.cmdb.object_relation_pb2.ObjectRelation
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.object_relation.Create"
        uri = "/object_relation"
        
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.model.cmdb.object_relation_pb2.ObjectRelation()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_relation(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.object_relation.delete_pb2.DeleteRelationRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        删除模型关系定义
        :param request: delete_relation请求
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
            route_name = "easyops.api.cmdb.object_relation.DeleteRelation"
        uri = "/object_relation/{relation_id}".format(
            relation_id=request.relation_id,
        )
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_sdk",
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
    
    def object_relation_snapshot(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.object_relation.get_object_relation_snapshot_pb2.ObjectRelationSnapshotRequest, int, str, int) -> cmdb_sdk.api.object_relation.get_object_relation_snapshot_pb2.ObjectRelationSnapshotResponse
        """
        查询指定版本模型关系快照
        :param request: object_relation_snapshot请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.object_relation.get_object_relation_snapshot_pb2.ObjectRelationSnapshotResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.object_relation.ObjectRelationSnapshot"
        uri = "/history/object_relation/{relation_id}".format(
            relation_id=request.relation_id,
        )
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.api.object_relation.get_object_relation_snapshot_pb2.ObjectRelationSnapshotResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_relations_by_group_id(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.object_relation.get_relations_by_group_id_pb2.GetRelationsByGroupIdRequest, int, str, int) -> cmdb_sdk.api.object_relation.get_relations_by_group_id_pb2.GetRelationsByGroupIdResponse
        """
        根据关系分组查询关系列表
        :param request: get_relations_by_group_id请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.object_relation.get_relations_by_group_id_pb2.GetRelationsByGroupIdResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.object_relation.GetRelationsByGroupId"
        uri = "/object_relation/object/{object_id}/relation_group/{group_id}".format(
            object_id=request.object_id,
            group_id=request.group_id,
        )
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
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
        rsp = cmdb_sdk.api.object_relation.get_relations_by_group_id_pb2.GetRelationsByGroupIdResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
