# -*- coding: utf-8 -*-
import os
import sys


import cmdb_sdk.api.instance_relation.append_pb2

import google.protobuf.empty_pb2

import cmdb_sdk.api.instance_relation.count_relation_instance_pb2

import cmdb_sdk.api.instance_relation.discovery_pb2

import cmdb_sdk.api.instance_relation.discovery_v2_pb2

import cmdb_sdk.api.instance_relation.get_instance_relation_snapshot_pb2

import cmdb_sdk.api.instance_relation.remove_pb2

import cmdb_sdk.api.instance_relation.set_pb2

import cmdb_sdk.utils.http_util
import google.protobuf.json_format


class InstanceRelationClient(object):
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

    
    def append(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.append_pb2.AppendRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量添加关系
        :param request: append请求
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
            route_name = "easyops.api.cmdb.instance_relation.Append"
        uri = "/object/{objectId}/relation/{relationSideId}/append".format(
            objectId=request.objectId,
            relationSideId=request.relationSideId,
        )
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def count_relation_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.count_relation_instance_pb2.CountRelationInstanceRequest, int, str, int) -> cmdb_sdk.api.instance_relation.count_relation_instance_pb2.CountRelationInstanceResponse
        """
        统计关系实例数量
        :param request: count_relation_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance_relation.count_relation_instance_pb2.CountRelationInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance_relation.CountRelationInstance"
        uri = "/object_relation/{relationId}/relation_instance/_count_relation_instance".format(
            relationId=request.relationId,
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
        rsp = cmdb_sdk.api.instance_relation.count_relation_instance_pb2.CountRelationInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def discovery(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.discovery_pb2.DiscoveryRequest, int, str, int) -> cmdb_sdk.api.instance_relation.discovery_pb2.DiscoveryResponse
        """
        实例关系发现
        :param request: discovery请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance_relation.discovery_pb2.DiscoveryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance_relation.Discovery"
        uri = "/object_relation/{relationId}/_autodiscovery/multi".format(
            relationId=request.relationId,
        )
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
        rsp = cmdb_sdk.api.instance_relation.discovery_pb2.DiscoveryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def discovery_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.discovery_v2_pb2.DiscoveryV2Request, int, str, int) -> cmdb_sdk.api.instance_relation.discovery_v2_pb2.DiscoveryV2Response
        """
        实例关系发现V2(支持set关系)
        :param request: discovery_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance_relation.discovery_v2_pb2.DiscoveryV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance_relation.DiscoveryV2"
        uri = "/v2/object_relation/{relationId}/_autodiscovery/multi".format(
            relationId=request.relationId,
        )
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
        rsp = cmdb_sdk.api.instance_relation.discovery_v2_pb2.DiscoveryV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_relation_snapshot(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.get_instance_relation_snapshot_pb2.InstanceRelationSnapshotRequest, int, str, int) -> cmdb_sdk.api.instance_relation.get_instance_relation_snapshot_pb2.InstanceRelationSnapshotResponse
        """
        查询历史实例关系快照
        :param request: instance_relation_snapshot请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance_relation.get_instance_relation_snapshot_pb2.InstanceRelationSnapshotResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance_relation.InstanceRelationSnapshot"
        uri = "/history/object_relation/{relation_id}/relation_instance/{relation_instance_id}".format(
            relation_id=request.relation_id,
            relation_instance_id=request.relation_instance_id,
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
        rsp = cmdb_sdk.api.instance_relation.get_instance_relation_snapshot_pb2.InstanceRelationSnapshotResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def remove(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.remove_pb2.RemoveRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量移除关系
        :param request: remove请求
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
            route_name = "easyops.api.cmdb.instance_relation.Remove"
        uri = "/object/{objectId}/relation/{relationSideId}/remove".format(
            objectId=request.objectId,
            relationSideId=request.relationSideId,
        )
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def set(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance_relation.set_pb2.SetRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        批量设置关系
        :param request: set请求
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
            route_name = "easyops.api.cmdb.instance_relation.Set"
        uri = "/object/{objectId}/relation/{relationSideId}/set".format(
            objectId=request.objectId,
            relationSideId=request.relationSideId,
        )
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
        rsp = google.protobuf.empty_pb2.Empty()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
