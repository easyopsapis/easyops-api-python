# -*- coding: utf-8 -*-

import add_str_to_array_pb2

import add_str_to_set_pb2

import aggregate_total_pb2

import aggregate_total_v2_pb2

import google.protobuf.struct_pb2

import delete_instance_batch_pb2

import import_instance_pb2

import post_search_pb2

import search_total_pb2

import update_permission_batch_pb2

import utils.http_util
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

    
    def add_str_to_array(self, request, org, user, host="", timeout=10):
        """
        append数据到实例arr属性内
        :param request: add_str_to_array请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: add_str_to_array_pb2.AddStrToArrayResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AddStrToArray"
        uri = "/object/:objectId/instance/add_str_to_array".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = add_str_to_array_pb2.AddStrToArrayResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def add_str_to_set(self, request, org, user, host="", timeout=10):
        """
        append数据到实例arr属性内(set)
        :param request: add_str_to_set请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: add_str_to_set_pb2.AddStrToSetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AddStrToSet"
        uri = "/object/:objectId/instance/add_str_to_set".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = add_str_to_set_pb2.AddStrToSetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def aggregate_count(self, request, org, user, host="", timeout=10):
        """
        实例计数统计
        :param request: aggregate_count请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: aggregate_total_pb2.AggregateCountResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AggregateCount"
        uri = "/object/:objectId/instance/aggregate/count/:attrId".format(
            objectId=request.objectId,
            attrId=request.attrId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = aggregate_total_pb2.AggregateCountResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def aggregate_count_v_2(self, request, org, user, host="", timeout=10):
        """
        实例计数统计接口v2
        :param request: aggregate_count_v_2请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: aggregate_total_v2_pb2.AggregateCountV2Response
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.AggregateCountV2"
        uri = "/v2/object/:objectId/instance_aggregate/count/:attrId".format(
            objectId=request.objectId,
            attrId=request.attrId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = aggregate_total_v2_pb2.AggregateCountV2Response()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_instance(self, request, org, user, host="", timeout=10):
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
        uri = "/v2/object/:objectId/instance".format(
            objectId=request.objectId,
        )
        requestParam = request.instance
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_instance(self, request, org, user, host="", timeout=10):
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
        uri = "/object/:objectId/instance/:instanceId".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_instance_batch(self, request, org, user, host="", timeout=10):
        """
        批量删除实例
        :param request: delete_instance_batch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: delete_instance_batch_pb2.DeleteInstanceBatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.DeleteInstanceBatch"
        uri = "/object/:objectId/instance/_batch".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = delete_instance_batch_pb2.DeleteInstanceBatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_default_value_template(self, request, org, user, host="", timeout=10):
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
        uri = "/object/:objectId/instance_default_value_template".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_detail(self, request, org, user, host="", timeout=10):
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
        uri = "/object/:objectId/instance/:instanceId".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def import_instance(self, request, org, user, host="", timeout=10):
        """
        批量编辑/新增实例
        :param request: import_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: import_instance_pb2.ImportInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.ImportInstance"
        uri = "/object/:objectId/instance/_import".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = import_instance_pb2.ImportInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def post_search(self, request, org, user, host="", timeout=10):
        """
        搜索实例
        :param request: post_search请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: post_search_pb2.PostSearchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.PostSearch"
        uri = "/object/:objectId/instance/_search".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = post_search_pb2.PostSearchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def search_total(self, request, org, user, host="", timeout=10):
        """
        搜索总数
        :param request: search_total请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: search_total_pb2.SearchTotalResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.SearchTotal"
        uri = "/object/:objectId/instance/_search_total".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = search_total_pb2.SearchTotalResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_instance(self, request, org, user, host="", timeout=10):
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
        uri = "/object/:objectId/instance/:instanceId".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request.instance
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = google.protobuf.struct_pb2.Struct()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def update_permission_batch(self, request, org, user, host="", timeout=10):
        """
        批量修改实例权限
        :param request: update_permission_batch请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: update_permission_batch_pb2.UpdatePermissionBatchResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb.instance.UpdatePermissionBatch"
        uri = "/permission/:objectId/instances/_batch".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_sdk",
            dst_name=route_name,
            server_ip=server_ip,
            server_port=self._server_port,
            host=host,
            uri=uri,
            params=google.protobuf.json_format.MessageToDict(
                requestParam, preserving_proto_field_name=True),
            headers=headers,
            timeout=timeout,
        )
        rsp = update_permission_batch_pb2.UpdatePermissionBatchResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
