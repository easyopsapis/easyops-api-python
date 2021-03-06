# -*- coding: utf-8 -*-
import os
import sys


import cmdb_extend_sdk.api.instance.add_cluster_device_pb2

import cmdb_extend_sdk.api.instance.app_add_packages_pb2

import google.protobuf.empty_pb2

import cmdb_extend_sdk.api.instance.app_delete_package_pb2

import cmdb_extend_sdk.api.instance.app_sort_packages_pb2

import cmdb_extend_sdk.api.instance.app_update_package_pb2

import cmdb_extend_sdk.api.instance.cluster_add_packages_pb2

import cmdb_extend_sdk.api.instance.cluster_delete_package_pb2

import cmdb_extend_sdk.api.instance.cluster_update_package_pb2

import cmdb_extend_sdk.api.instance.create_instances_pb2

import cmdb_extend_sdk.api.instance.delete_cluster_device_pb2

import cmdb_extend_sdk.api.instance.get_instance_pb2

import google.protobuf.struct_pb2

import cmdb_extend_sdk.api.instance.get_instances_pb2

import cmdb_extend_sdk.api.instance.list_instance_pb2

import cmdb_extend_sdk.utils.http_util
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

    
    def add_cluster_device(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.add_cluster_device_pb2.AddClusterDeviceRequest, int, str, int) -> cmdb_extend_sdk.api.instance.add_cluster_device_pb2.AddClusterDeviceResponse
        """
        集群添加设备
        :param request: add_cluster_device请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.instance.add_cluster_device_pb2.AddClusterDeviceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.instance.AddClusterDevice"
        uri = "/cluster/{instanceId}/device/{deviceIds}".format(
            instanceId=request.instanceId,
            deviceIds=request.deviceIds,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.instance.add_cluster_device_pb2.AddClusterDeviceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def app_add_packages(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.app_add_packages_pb2.AppAddPackagesRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        应用关联程序包
        :param request: app_add_packages请求
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
            route_name = "easyops.api.cmdb_extend.instance.AppAddPackages"
        uri = "/app/{instanceId}/package".format(
            instanceId=request.instanceId,
        )
        requestParam = request.packages
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
    
    def app_delete_package(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.app_delete_package_pb2.AppDeletePackageRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        应用解除关联包
        :param request: app_delete_package请求
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
            route_name = "easyops.api.cmdb_extend.instance.AppDeletePackage"
        uri = "/app/{instanceId}/package/{packageId}".format(
            instanceId=request.instanceId,
            packageId=request.packageId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_extend_sdk",
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
    
    def app_sort_packages(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.app_sort_packages_pb2.AppSortPackagesRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        应用关联程序包排序
        :param request: app_sort_packages请求
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
            route_name = "easyops.api.cmdb_extend.instance.AppSortPackages"
        uri = "/app/{instanceId}/package_list/_sort".format(
            instanceId=request.instanceId,
        )
        requestParam = request.packages
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
    def app_update_package(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.app_update_package_pb2.AppUpdatePackageRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改应用关联包
        :param request: app_update_package请求
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
            route_name = "easyops.api.cmdb_extend.instance.AppUpdatePackage"
        uri = "/app/{instanceId}/package".format(
            instanceId=request.instanceId,
        )
        requestParam = request.package
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
    def cluster_add_packages(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.cluster_add_packages_pb2.ClusterAddPackagesRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        集群添加程序包
        :param request: cluster_add_packages请求
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
            route_name = "easyops.api.cmdb_extend.instance.ClusterAddPackages"
        uri = "/cluster/{instanceId}/package".format(
            instanceId=request.instanceId,
        )
        requestParam = request.packages
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
    
    def cluster_delete_package(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.cluster_delete_package_pb2.ClusterDeletePackageRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        集群解除关联包
        :param request: cluster_delete_package请求
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
            route_name = "easyops.api.cmdb_extend.instance.ClusterDeletePackage"
        uri = "/cluster/{instanceId}/package/{packageIds}".format(
            instanceId=request.instanceId,
            packageIds=request.packageIds,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_extend_sdk",
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
    
    def cluster_update_package(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.cluster_update_package_pb2.ClusterUpdatePackageRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        修改集群关联包
        :param request: cluster_update_package请求
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
            route_name = "easyops.api.cmdb_extend.instance.ClusterUpdatePackage"
        uri = "/cluster/{instanceId}/package".format(
            instanceId=request.instanceId,
        )
        requestParam = request.package
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.cmdb_extend_sdk",
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
    
    def create_instances(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.create_instances_pb2.CreateInstancesRequest, int, str, int) -> cmdb_extend_sdk.api.instance.create_instances_pb2.CreateInstancesResponse
        """
        批量创建实例
        :param request: create_instances请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.instance.create_instances_pb2.CreateInstancesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.instance.CreateInstances"
        uri = "/object/instance/list/{objectId}".format(
            objectId=request.objectId,
        )
        requestParam = request.instances
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="POST",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.instance.create_instances_pb2.CreateInstancesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def delete_cluster_device(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.delete_cluster_device_pb2.DeleteClusterDeviceRequest, int, str, int) -> cmdb_extend_sdk.api.instance.delete_cluster_device_pb2.DeleteClusterDeviceResponse
        """
        集群删除设备
        :param request: delete_cluster_device请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.instance.delete_cluster_device_pb2.DeleteClusterDeviceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.instance.DeleteClusterDevice"
        uri = "/cluster/{instanceId}/device/{deviceIds}".format(
            instanceId=request.instanceId,
            deviceIds=request.deviceIds,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="DELETE",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.instance.delete_cluster_device_pb2.DeleteClusterDeviceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj, rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_instance(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.get_instance_pb2.GetInstanceRequest, int, str, int) -> google.protobuf.struct_pb2.Struct
        """
        获取实例
        :param request: get_instance请求
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
            route_name = "easyops.api.cmdb_extend.instance.GetInstance"
        uri = "/object_instance/{objectId}/{instanceId}".format(
            objectId=request.objectId,
            instanceId=request.instanceId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
    
    def get_instances(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.get_instances_pb2.GetInstancesRequest, int, str, int) -> cmdb_extend_sdk.api.instance.get_instances_pb2.GetInstancesResponse
        """
        获取指定实例Id实例列表
        :param request: get_instances请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.instance.get_instances_pb2.GetInstancesResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.instance.GetInstances"
        uri = "/object/instance/list/{objectId}/{instanceIds}".format(
            objectId=request.objectId,
            instanceIds=request.instanceIds,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.instance.get_instances_pb2.GetInstancesResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_instance(self, request, org, user, timeout=10):
        # type: (cmdb_extend_sdk.api.instance.list_instance_pb2.ListInstanceRequest, int, str, int) -> cmdb_extend_sdk.api.instance.list_instance_pb2.ListInstanceResponse
        """
        获取实例列表
        :param request: list_instance请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: cmdb_extend_sdk.api.instance.list_instance_pb2.ListInstanceResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.cmdb_extend.instance.ListInstance"
        uri = "/object/instance/list/{objectId}".format(
            objectId=request.objectId,
        )
        requestParam = request
        
        rsp_obj = cmdb_extend_sdk.utils.http_util.do_api_request(
            method="GET",
            src_name="logic.cmdb_extend_sdk",
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
        rsp = cmdb_extend_sdk.api.instance.list_instance_pb2.ListInstanceResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
