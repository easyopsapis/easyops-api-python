# -*- coding: utf-8 -*-
import os
import sys


import cmdb_sdk.api.cmdb_object.alter_word_index_pb2

import google.protobuf.empty_pb2

import cmdb_sdk.api.cmdb_object.batch_list_relation_query_strategy_v2_pb2

import cmdb_sdk.api.cmdb_object.batch_update_pb2

import cmdb_sdk.api.cmdb_object.create_pb2

import cmdb_sdk.model.cmdb.cmdb_object_pb2

import cmdb_sdk.api.cmdb_object.get_detail_pb2

import cmdb_sdk.api.cmdb_object.get_id_map_name_pb2

import google.protobuf.struct_pb2

import cmdb_sdk.api.cmdb_object.get_object_all_pb2

import cmdb_sdk.api.cmdb_object.get_object_basic_all_pb2

import cmdb_sdk.api.cmdb_object.get_object_relation_path_pb2

import cmdb_sdk.api.cmdb_object.get_object_relation_related_key_pb2

import cmdb_sdk.api.cmdb_object.get_object_snapshot_pb2

import cmdb_sdk.api.cmdb_object.import_check_pb2

import cmdb_sdk.api.cmdb_object.import_check_v2_pb2

import cmdb_sdk.api.cmdb_object.import_object_pb2

import cmdb_sdk.api.cmdb_object.import_v2_pb2

import cmdb_sdk.api.cmdb_object.list_pb2

import cmdb_sdk.api.cmdb_object.list_child_object_pb2

import cmdb_sdk.api.cmdb_object.list_relation_query_strategy_v2_pb2

import cmdb_sdk.api.cmdb_object.update_pb2

import cmdb_sdk.utils.http_util
import google.protobuf.json_format


class CmdbObjectClient(object):
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

    
    def alert_word_index(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.alter_word_index_pb2.AlertWordIndexRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        模型及属性全文索引配置
        :param request: alert_word_index请求
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
            route_name = "easyops.api.cmdb.cmdb_object.AlertWordIndex"
        uri = "/object_word_index/{object_id}".format(
            object_id=request.object_id,
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
    
    def batch_list_relation_query_strategy_v_2_request(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.batch_list_relation_query_strategy_v2_pb2.BatchListRelationQueryStrategyV2RequestRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.batch_list_relation_query_strategy_v2_pb2.BatchListRelationQueryStrategyV2RequestResponse
        """
        批量获取模型查询策略v2
        :param request: batch_list_relation_query_strategy_v_2_request请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.batch_list_relation_query_strategy_v2_pb2.BatchListRelationQueryStrategyV2RequestResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.BatchListRelationQueryStrategyV2Request"
        uri = "/v2/batch/object/relation_query_strategy"
        
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
        rsp = cmdb_sdk.api.cmdb_object.batch_list_relation_query_strategy_v2_pb2.BatchListRelationQueryStrategyV2RequestResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def batch_update(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.batch_update_pb2.BatchUpdateRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.batch_update_pb2.BatchUpdateResponse
        """
        批量更新模型
        :param request: batch_update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.batch_update_pb2.BatchUpdateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.BatchUpdate"
        uri = "/batch/object"
        
        requestParam = request
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="PUT",
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
        rsp = cmdb_sdk.api.cmdb_object.batch_update_pb2.BatchUpdateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.create_pb2.CreateRequest, int, str, int) -> cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        创建模型
        :param request: create请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.Create"
        uri = "/object"
        
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
        rsp = cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_detail(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_detail_pb2.GetDetailRequest, int, str, int) -> cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        获取模型详情
        :param request: get_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetDetail"
        uri = "/object/{objectId}".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_id_map_name(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_id_map_name_pb2.GetIdMapNameRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取模型id和name映射
        :param request: get_id_map_name请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: google.protobuf.struct_pb2.Struct
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetIdMapName"
        uri = "/object_id_map_name"
        
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_all(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_object_all_pb2.GetObjectAllRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.get_object_all_pb2.GetObjectAllResponse
        """
        获取所有模型
        :param request: get_object_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.get_object_all_pb2.GetObjectAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetObjectAll"
        uri = "/object_all"
        
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
        rsp = cmdb_sdk.api.cmdb_object.get_object_all_pb2.GetObjectAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_basic_all(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_object_basic_all_pb2.GetObjectBasicAllRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.get_object_basic_all_pb2.GetObjectBasicAllResponse
        """
        获取所有模型基本信息
        :param request: get_object_basic_all请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.get_object_basic_all_pb2.GetObjectBasicAllResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetObjectBasicAll"
        uri = "/object_basic_all"
        
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
        rsp = cmdb_sdk.api.cmdb_object.get_object_basic_all_pb2.GetObjectBasicAllResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_relation_path(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_object_relation_path_pb2.GetObjectRelationPathRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.get_object_relation_path_pb2.GetObjectRelationPathResponse
        """
        获取资源模型路径列表
        :param request: get_object_relation_path请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.get_object_relation_path_pb2.GetObjectRelationPathResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetObjectRelationPath"
        uri = "/object_relation_path"
        
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
        rsp = cmdb_sdk.api.cmdb_object.get_object_relation_path_pb2.GetObjectRelationPathResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_object_relation_related_key(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_object_relation_related_key_pb2.GetObjectRelationRelatedKeyRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.get_object_relation_related_key_pb2.GetObjectRelationRelatedKeyResponse
        """
        获取资源模型路径实例查询key
        :param request: get_object_relation_related_key请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.get_object_relation_related_key_pb2.GetObjectRelationRelatedKeyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.GetObjectRelationRelatedKey"
        uri = "/object_relation_related_key"
        
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
        rsp = cmdb_sdk.api.cmdb_object.get_object_relation_related_key_pb2.GetObjectRelationRelatedKeyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def object_snapshot(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.get_object_snapshot_pb2.ObjectSnapshotRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.get_object_snapshot_pb2.ObjectSnapshotResponse
        """
        查询指定版本模型快照
        :param request: object_snapshot请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.get_object_snapshot_pb2.ObjectSnapshotResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ObjectSnapshot"
        uri = "/history/object/{object_id}".format(
            object_id=request.object_id,
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
        rsp = cmdb_sdk.api.cmdb_object.get_object_snapshot_pb2.ObjectSnapshotResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_check(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.import_check_pb2.ImportCheckRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.import_check_pb2.ImportCheckResponse
        """
        import objects check
        :param request: import_check请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.import_check_pb2.ImportCheckResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ImportCheck"
        uri = "/object_import_check"
        
        requestParam = request.body
        
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
        rsp = cmdb_sdk.api.cmdb_object.import_check_pb2.ImportCheckResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_check_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.import_check_v2_pb2.ImportCheckV2Request, int, str, int) -> cmdb_sdk.api.cmdb_object.import_check_v2_pb2.ImportCheckV2Response
        """
        批量导入模型检查v2
        :param request: import_check_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.import_check_v2_pb2.ImportCheckV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ImportCheckV2"
        uri = "/v2/object_import_check"
        
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
        rsp = cmdb_sdk.api.cmdb_object.import_check_v2_pb2.ImportCheckV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_object(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.import_object_pb2.ImportObjectRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.import_object_pb2.ImportObjectResponse
        """
        批量导入模型
        :param request: import_object请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.import_object_pb2.ImportObjectResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ImportObject"
        uri = "/object_import"
        
        requestParam = request.body
        
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
        rsp = cmdb_sdk.api.cmdb_object.import_object_pb2.ImportObjectResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.import_v2_pb2.ImportV2Request, int, str, int) -> cmdb_sdk.api.cmdb_object.import_v2_pb2.ImportV2Response
        """
        批量导入模型v2
        :param request: import_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.import_v2_pb2.ImportV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ImportV2"
        uri = "/v2/object_import"
        
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
        rsp = cmdb_sdk.api.cmdb_object.import_v2_pb2.ImportV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.list_pb2.ListRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.list_pb2.ListResponse
        """
        获取模型列表
        :param request: list请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.list_pb2.ListResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.List"
        uri = "/object"
        
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
        rsp = cmdb_sdk.api.cmdb_object.list_pb2.ListResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_child_object(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.list_child_object_pb2.ListChildObjectRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.list_child_object_pb2.ListChildObjectResponse
        """
        获取某个模型所有关联子模型
        :param request: list_child_object请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.list_child_object_pb2.ListChildObjectResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ListChildObject"
        uri = "/object/{objectId}/child".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.cmdb_object.list_child_object_pb2.ListChildObjectResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_relation_query_strategy_v_2_request(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.list_relation_query_strategy_v2_pb2.ListRelationQueryStrategyV2RequestRequest, int, str, int) -> cmdb_sdk.api.cmdb_object.list_relation_query_strategy_v2_pb2.ListRelationQueryStrategyV2RequestResponse
        """
        获取查询策略v2
        :param request: list_relation_query_strategy_v_2_request请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.cmdb_object.list_relation_query_strategy_v2_pb2.ListRelationQueryStrategyV2RequestResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.ListRelationQueryStrategyV2Request"
        uri = "/v2/object/{object_id}/relation_query_strategy".format(
            object_id=request.object_id,
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
        rsp = cmdb_sdk.api.cmdb_object.list_relation_query_strategy_v2_pb2.ListRelationQueryStrategyV2RequestResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.cmdb_object.update_pb2.UpdateRequest, int, str, int) -> cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        更新模型
        :param request: update请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.cmdb_object.Update"
        uri = "/object/{objectId}".format(
            objectId=request.objectId,
        )
        requestParam = request.body
        
        rsp_obj = cmdb_sdk.utils.http_util.do_api_request(
            method="PUT",
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
        rsp = cmdb_sdk.model.cmdb.cmdb_object_pb2.CmdbObject()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
