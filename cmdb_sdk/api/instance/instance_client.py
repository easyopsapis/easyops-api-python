# -*- coding: utf-8 -*-
import os
import sys


import cmdb_sdk.api.instance.add_str_to_array_pb2

import cmdb_sdk.api.instance.add_str_to_set_pb2

import cmdb_sdk.api.instance.aggregate_total_pb2

import cmdb_sdk.api.instance.aggregate_total_v2_pb2

import cmdb_sdk.api.instance.auto_discovery_pb2

import cmdb_sdk.api.instance.batch_list_instance_query_strategy_pb2

import cmdb_sdk.api.instance.batch_search_pb2

import cmdb_sdk.api.instance.create_instance_pb2

import google.protobuf.struct_pb2

import cmdb_sdk.api.instance.delete_instance_pb2

import cmdb_sdk.api.instance.delete_instance_batch_pb2

import cmdb_sdk.api.instance.fulltext_search_pb2

import cmdb_sdk.api.instance.get_default_value_template_pb2

import cmdb_sdk.api.instance.get_detail_pb2

import cmdb_sdk.api.instance.get_instance_query_strategy_pb2

import cmdb_sdk.model.cmdb.instance_query_strategy_pb2

import cmdb_sdk.api.instance.group_instance_pb2

import cmdb_sdk.api.instance.import_instance_pb2

import cmdb_sdk.api.instance.import_instance_with_csv_pb2

import cmdb_sdk.api.instance.import_instance_with_excel_pb2

import cmdb_sdk.api.instance.instance_relation_count_pb2

import cmdb_sdk.api.instance.instance_snapshot_pb2

import cmdb_sdk.api.instance.list_instance_pb2

import cmdb_sdk.api.instance.list_instance_query_strategy_pb2

import cmdb_sdk.api.instance.post_search_pb2

import cmdb_sdk.api.instance.post_search_v2_pb2

import cmdb_sdk.api.instance.relation_count_aggregate_pb2

import cmdb_sdk.api.instance.relation_max_check_pb2

import cmdb_sdk.api.instance.search_total_pb2

import cmdb_sdk.api.instance.update_instance_pb2

import cmdb_sdk.api.instance.update_instance_v2_pb2

import cmdb_sdk.api.instance.update_permission_batch_pb2

import cmdb_sdk.utils.http_util
import google.protobuf.json_format


class InstanceClient(object):
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

    
    def add_str_to_array(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.add_str_to_array_pb2.AddStrToArrayRequest, int, str, int) -> cmdb_sdk.api.instance.add_str_to_array_pb2.AddStrToArrayResponse
        """
        append数据到实例arr属性内
        :param request: add_str_to_array请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.add_str_to_array_pb2.AddStrToArrayResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AddStrToArray"
        uri = "/object/{objectId}/instance/add_str_to_array".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.add_str_to_array_pb2.AddStrToArrayResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def add_str_to_set(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.add_str_to_set_pb2.AddStrToSetRequest, int, str, int) -> cmdb_sdk.api.instance.add_str_to_set_pb2.AddStrToSetResponse
        """
        append数据到实例arr属性内(set)
        :param request: add_str_to_set请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.add_str_to_set_pb2.AddStrToSetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AddStrToSet"
        uri = "/object/{objectId}/instance/add_str_to_set".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.add_str_to_set_pb2.AddStrToSetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def aggregate_count(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.aggregate_total_pb2.AggregateCountRequest, int, str, int) -> cmdb_sdk.api.instance.aggregate_total_pb2.AggregateCountResponse
        """
        实例计数统计
        :param request: aggregate_count请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.aggregate_total_pb2.AggregateCountResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AggregateCount"
        uri = "/object/{objectId}/instance/aggregate/count/{attrId}".format(
            objectId=request.objectId,
            attrId=request.attrId,
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
        rsp = cmdb_sdk.api.instance.aggregate_total_pb2.AggregateCountResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def aggregate_count_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.aggregate_total_v2_pb2.AggregateCountV2Request, int, str, int) -> cmdb_sdk.api.instance.aggregate_total_v2_pb2.AggregateCountV2Response
        """
        实例计数统计接口v2
        :param request: aggregate_count_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.aggregate_total_v2_pb2.AggregateCountV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AggregateCountV2"
        uri = "/v2/object/{objectId}/instance_aggregate/count/{attrId}".format(
            objectId=request.objectId,
            attrId=request.attrId,
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
        rsp = cmdb_sdk.api.instance.aggregate_total_v2_pb2.AggregateCountV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def auto_discovery(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.auto_discovery_pb2.AutoDiscoveryRequest, int, str, int) -> cmdb_sdk.api.instance.auto_discovery_pb2.AutoDiscoveryResponse
        """
        实例自动发现的接口
        :param request: auto_discovery请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.auto_discovery_pb2.AutoDiscoveryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AutoDiscovery"
        uri = "/object/{objectId}/instance/_import-json".format(
            objectId=request.objectId,
        )
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
        rsp = cmdb_sdk.api.instance.auto_discovery_pb2.AutoDiscoveryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def batch_list_instance_query_strategy(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.batch_list_instance_query_strategy_pb2.BatchListInstanceQueryStrategyRequest, int, str, int) -> cmdb_sdk.api.instance.batch_list_instance_query_strategy_pb2.BatchListInstanceQueryStrategyResponse
        """
        批量获取实例查询策略列表
        :param request: batch_list_instance_query_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.batch_list_instance_query_strategy_pb2.BatchListInstanceQueryStrategyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.BatchListInstanceQueryStrategy"
        uri = "batch/object/query/strategy"
        
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
        rsp = cmdb_sdk.api.instance.batch_list_instance_query_strategy_pb2.BatchListInstanceQueryStrategyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def batch_search(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.batch_search_pb2.BatchSearchRequest, int, str, int) -> cmdb_sdk.api.instance.batch_search_pb2.BatchSearchResponse
        """
        多模型批量搜索实例
        :param request: batch_search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.batch_search_pb2.BatchSearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.BatchSearch"
        uri = "/batch/object/instance/_search"
        
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
        rsp = cmdb_sdk.api.instance.batch_search_pb2.BatchSearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.create_instance_pb2.CreateInstanceRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        创建实例
        :param request: create_instance请求
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
            route_name = "easyops.api.cmdb.instance.CreateInstance"
        uri = "/v2/object/{objectId}/instance".format(
            objectId=request.objectId,
        )
        requestParam = request.instance
        
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.delete_instance_pb2.DeleteInstanceRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        删除实例
        :param request: delete_instance请求
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
            route_name = "easyops.api.cmdb.instance.DeleteInstance"
        uri = "/object/{objectId}/instance/{instanceId}".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_instance_batch(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.delete_instance_batch_pb2.DeleteInstanceBatchRequest, int, str, int) -> cmdb_sdk.api.instance.delete_instance_batch_pb2.DeleteInstanceBatchResponse
        """
        批量删除实例
        :param request: delete_instance_batch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.delete_instance_batch_pb2.DeleteInstanceBatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.DeleteInstanceBatch"
        uri = "/object/{objectId}/instance/_batch".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.delete_instance_batch_pb2.DeleteInstanceBatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def fulltext_search(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.fulltext_search_pb2.FulltextSearchRequest, int, str, int) -> cmdb_sdk.api.instance.fulltext_search_pb2.FulltextSearchResponse
        """
        全文搜索
        :param request: fulltext_search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.fulltext_search_pb2.FulltextSearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.FulltextSearch"
        uri = "/fulltext/_search"
        
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
        rsp = cmdb_sdk.api.instance.fulltext_search_pb2.FulltextSearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_default_value_template(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.get_default_value_template_pb2.GetDefaultValueTemplateRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取实例默认值模板
        :param request: get_default_value_template请求
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
            route_name = "easyops.api.cmdb.instance.GetDefaultValueTemplate"
        uri = "/object/{objectId}/instance_default_value_template".format(
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_detail(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.get_detail_pb2.GetDetailRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取实例详情
        :param request: get_detail请求
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
            route_name = "easyops.api.cmdb.instance.GetDetail"
        uri = "/object/{objectId}/instance/{instanceId}".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_instance_query_strategy(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.get_instance_query_strategy_pb2.GetInstanceQueryStrategyRequest, int, str, int) -> cmdb_sdk.model.cmdb.instance_query_strategy_pb2.InstanceQueryStrategy
        """
        获取实例查询策略
        :param request: get_instance_query_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.model.cmdb.instance_query_strategy_pb2.InstanceQueryStrategy
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.GetInstanceQueryStrategy"
        uri = "/object/{objectId}/query/strategy/{strategyId}".format(
            objectId=request.objectId,
            strategyId=request.strategyId,
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
        rsp = cmdb_sdk.model.cmdb.instance_query_strategy_pb2.InstanceQueryStrategy()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def group_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.group_instance_pb2.GroupInstanceRequest, int, str, int) -> cmdb_sdk.api.instance.group_instance_pb2.GroupInstanceResponse
        """
        实例聚合接口
        :param request: group_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.group_instance_pb2.GroupInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.GroupInstance"
        uri = "/object/{object_id}/instance/group".format(
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
        rsp = cmdb_sdk.api.instance.group_instance_pb2.GroupInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.import_instance_pb2.ImportInstanceRequest, int, str, int) -> cmdb_sdk.api.instance.import_instance_pb2.ImportInstanceResponse
        """
        批量编辑/新增实例
        :param request: import_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.import_instance_pb2.ImportInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ImportInstance"
        uri = "/object/{objectId}/instance/_import".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.import_instance_pb2.ImportInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_instance_with_csv(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.import_instance_with_csv_pb2.ImportInstanceWithCsvRequest, int, str, int) -> cmdb_sdk.api.instance.import_instance_with_csv_pb2.ImportInstanceWithCsvResponse
        """
        使用csv文件导入实例
        :param request: import_instance_with_csv请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.import_instance_with_csv_pb2.ImportInstanceWithCsvResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ImportInstanceWithCsv"
        uri = "/import/object/{object_id}/instance/csv".format(
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
        rsp = cmdb_sdk.api.instance.import_instance_with_csv_pb2.ImportInstanceWithCsvResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_instance_with_excel(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.import_instance_with_excel_pb2.ImportInstanceWithExcelRequest, int, str, int) -> cmdb_sdk.api.instance.import_instance_with_excel_pb2.ImportInstanceWithExcelResponse
        """
        使用excel文件导入实例
        :param request: import_instance_with_excel请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.import_instance_with_excel_pb2.ImportInstanceWithExcelResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ImportInstanceWithExcel"
        uri = "/import/object/{object_id}/instance/excel".format(
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
        rsp = cmdb_sdk.api.instance.import_instance_with_excel_pb2.ImportInstanceWithExcelResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_relations_count(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.instance_relation_count_pb2.InstanceRelationsCountRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        单个实例关系统计
        :param request: instance_relations_count请求
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
            route_name = "easyops.api.cmdb.instance.InstanceRelationsCount"
        uri = "/object/{object_id}/instance/{instance_id}/_relation_count".format(
            object_id=request.object_id,
            instance_id=request.instance_id,
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def instance_snapshot(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.instance_snapshot_pb2.InstanceSnapshotRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        查询指定版本实例快照
        :param request: instance_snapshot请求
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
            route_name = "easyops.api.cmdb.instance.InstanceSnapshot"
        uri = "/history/object/{object_id}/instance/{instance_id}".format(
            object_id=request.object_id,
            instance_id=request.instance_id,
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.list_instance_pb2.ListInstanceRequest, int, str, int) -> cmdb_sdk.api.instance.list_instance_pb2.ListInstanceResponse
        """
        实例分页列表查询
        :param request: list_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.list_instance_pb2.ListInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ListInstance"
        uri = "/object/{object_id}/instance".format(
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
        rsp = cmdb_sdk.api.instance.list_instance_pb2.ListInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_instance_query_strategy(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.list_instance_query_strategy_pb2.ListInstanceQueryStrategyRequest, int, str, int) -> cmdb_sdk.api.instance.list_instance_query_strategy_pb2.ListInstanceQueryStrategyResponse
        """
        获取实例查询策略列表
        :param request: list_instance_query_strategy请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.list_instance_query_strategy_pb2.ListInstanceQueryStrategyResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ListInstanceQueryStrategy"
        uri = "/object/{object_id}/query/strategy".format(
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
        rsp = cmdb_sdk.api.instance.list_instance_query_strategy_pb2.ListInstanceQueryStrategyResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def post_search(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.post_search_pb2.PostSearchRequest, int, str, int) -> cmdb_sdk.api.instance.post_search_pb2.PostSearchResponse
        """
        搜索实例
        :param request: post_search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.post_search_pb2.PostSearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.PostSearch"
        uri = "/object/{objectId}/instance/_search".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.post_search_pb2.PostSearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def post_search_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.post_search_v2_pb2.PostSearchV2Request, int, str, int) -> cmdb_sdk.api.instance.post_search_v2_pb2.PostSearchV2Response
        """
        搜索实例V2
        :param request: post_search_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.post_search_v2_pb2.PostSearchV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.PostSearchV2"
        uri = "/v2/object/{objectId}/instance/_search".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.post_search_v2_pb2.PostSearchV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def relation_count_aggregate(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.relation_count_aggregate_pb2.RelationCountAggregateRequest, int, str, int) -> cmdb_sdk.api.instance.relation_count_aggregate_pb2.RelationCountAggregateResponse
        """
        实例关系数量统计
        :param request: relation_count_aggregate请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.relation_count_aggregate_pb2.RelationCountAggregateResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.RelationCountAggregate"
        uri = "/object/{objectId}/instance/_relation_count_aggregate".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.relation_count_aggregate_pb2.RelationCountAggregateResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def relation_max_check(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.relation_max_check_pb2.RelationMaxCheckRequest, int, str, int) -> cmdb_sdk.api.instance.relation_max_check_pb2.RelationMaxCheckResponse
        """
        搜索实例列表指定关系是否大于等于max约束
        :param request: relation_max_check请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.relation_max_check_pb2.RelationMaxCheckResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.RelationMaxCheck"
        uri = "/object/{objectId}/instance/_search_relation_max_check".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.relation_max_check_pb2.RelationMaxCheckResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_total(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.search_total_pb2.SearchTotalRequest, int, str, int) -> cmdb_sdk.api.instance.search_total_pb2.SearchTotalResponse
        """
        搜索总数
        :param request: search_total请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.search_total_pb2.SearchTotalResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.SearchTotal"
        uri = "/object/{objectId}/instance/_search_total".format(
            objectId=request.objectId,
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
        rsp = cmdb_sdk.api.instance.search_total_pb2.SearchTotalResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_instance(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.update_instance_pb2.UpdateInstanceRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        更新实例
        :param request: update_instance请求
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
            route_name = "easyops.api.cmdb.instance.UpdateInstance"
        uri = "/object/{objectId}/instance/{instanceId}".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request.instance
        
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_instance_v_2(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.update_instance_v2_pb2.UpdateInstanceV2Request, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        更新实例V2
        :param request: update_instance_v_2请求
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
            route_name = "easyops.api.cmdb.instance.UpdateInstanceV2"
        uri = "/v2/object/{objectId}/instance/{instanceId}".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request.instance
        
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
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_permission_batch(self, request, org, user, timeout=10):
        # type: (cmdb_sdk.api.instance.update_permission_batch_pb2.UpdatePermissionBatchRequest, int, str, int) -> cmdb_sdk.api.instance.update_permission_batch_pb2.UpdatePermissionBatchResponse
        """
        批量修改实例权限
        :param request: update_permission_batch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_sdk.api.instance.update_permission_batch_pb2.UpdatePermissionBatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.UpdatePermissionBatch"
        uri = "/permission/{objectId}/instances/_batch".format(
            objectId=request.objectId,
        )
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
        rsp = cmdb_sdk.api.instance.update_permission_batch_pb2.UpdatePermissionBatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
