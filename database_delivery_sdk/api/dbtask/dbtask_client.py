# -*- coding: utf-8 -*-
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(current_path))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)


import backup_task_callback_pb2

import check_task_callback_pb2

import convert_changeset_pb2

import convert_sql_pb2

import create_custom_dbtask_pb2

import create_sqlpkg_dbtask_pb2

import edit_custom_dbtask_rollbacksql_pb2

import google.protobuf.empty_pb2

import get_custom_dbtask_detail_pb2

import get_custom_dbtask_rollbackinfo_pb2

import get_sqlpkg_dbtask_detail_pb2

import get_sqlpkg_dbtask_rollbackinfo_pb2

import liquibase_task_callback_pb2

import list_custom_dbtask_changehistory_pb2

import list_dbversions_pb2

import list_sqlpkg_changehistory_pb2

import list_sqlpkg_dbtask_changehistory_pb2

import retry_custom_dbtask_pb2

import retry_sqlpkg_dbtask_pb2

import rollback_custom_dbtask_pb2

import rollback_sqlpkg_dbtask_pb2

import utils.http_util
import google.protobuf.json_format


class DbtaskClient(object):
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

    
    def backup_task_callback(self, request, org, user, timeout=10):
        # type: (backup_task_callback_pb2.BackupTaskCallbackRequest, int, str, int) -> backup_task_callback_pb2.BackupTaskCallbackResponse
        """
        备份任务结果回调
        :param request: backup_task_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: backup_task_callback_pb2.BackupTaskCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.BackupTaskCallback"
        uri = "/api/v1/backup-tasks/callback"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = backup_task_callback_pb2.BackupTaskCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def check_task_callback(self, request, org, user, timeout=10):
        # type: (check_task_callback_pb2.CheckTaskCallbackRequest, int, str, int) -> check_task_callback_pb2.CheckTaskCallbackResponse
        """
        检查任务结果回调
        :param request: check_task_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: check_task_callback_pb2.CheckTaskCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.CheckTaskCallback"
        uri = "/api/v1/check-tasks/callback"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = check_task_callback_pb2.CheckTaskCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def convert_changeset_to_sql(self, request, org, user, timeout=10):
        # type: (convert_changeset_pb2.ConvertChangesetToSQLRequest, int, str, int) -> convert_changeset_pb2.ConvertChangesetToSQLResponse
        """
        将变更集列表转换为SQL
        :param request: convert_changeset_to_sql请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: convert_changeset_pb2.ConvertChangesetToSQLResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ConvertChangesetToSQL"
        uri = "/api/v1/changeset/convert"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = convert_changeset_pb2.ConvertChangesetToSQLResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def convert_sql_to_changeset(self, request, org, user, timeout=10):
        # type: (convert_sql_pb2.ConvertSQLToChangesetRequest, int, str, int) -> convert_sql_pb2.ConvertSQLToChangesetResponse
        """
        将SQL文本转换为变更集列表
        :param request: convert_sql_to_changeset请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: convert_sql_pb2.ConvertSQLToChangesetResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ConvertSQLToChangeset"
        uri = "/api/v1/sql/convert"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = convert_sql_pb2.ConvertSQLToChangesetResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_custom_db_task(self, request, org, user, timeout=10):
        # type: (create_custom_dbtask_pb2.CreateCustomDBTaskRequest, int, str, int) -> create_custom_dbtask_pb2.CreateCustomDBTaskResponse
        """
        创建自定义SQL变更任务
        :param request: create_custom_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_custom_dbtask_pb2.CreateCustomDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.CreateCustomDBTask"
        uri = "/api/v1/dbtasks"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = create_custom_dbtask_pb2.CreateCustomDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def create_sql_package_db_task(self, request, org, user, timeout=10):
        # type: (create_sqlpkg_dbtask_pb2.CreateSQLPackageDBTaskRequest, int, str, int) -> create_sqlpkg_dbtask_pb2.CreateSQLPackageDBTaskResponse
        """
        创建SQL包变更任务
        :param request: create_sql_package_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: create_sqlpkg_dbtask_pb2.CreateSQLPackageDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.CreateSQLPackageDBTask"
        uri = "/api/v1/sqlpkgs/{pkgId}/versions/{versionId}/dbtasks".format(
            pkgId=request.pkgId,
            versionId=request.versionId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = create_sqlpkg_dbtask_pb2.CreateSQLPackageDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def edit_custom_db_task_rollback_sql(self, request, org, user, timeout=10):
        # type: (edit_custom_dbtask_rollbacksql_pb2.EditCustomDBTaskRollbackSQLRequest, int, str, int) -> google.protobuf.empty_pb2.Empty
        """
        编辑自定义SQL任务的回退SQL
        :param request: edit_custom_db_task_rollback_sql请求
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
            route_name = "easyops.api.database_delivery.dbtask.EditCustomDBTaskRollbackSQL"
        uri = "/api/v1/dbtasks/{dbTaskId}/rollbaskSql".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="PUT",
            src_name="logic.database_delivery_sdk",
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
    
    def get_custom_db_task_detail(self, request, org, user, timeout=10):
        # type: (get_custom_dbtask_detail_pb2.GetCustomDBTaskDetailRequest, int, str, int) -> get_custom_dbtask_detail_pb2.GetCustomDBTaskDetailResponse
        """
        获取自SQL变更任务详情
        :param request: get_custom_db_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_custom_dbtask_detail_pb2.GetCustomDBTaskDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.GetCustomDBTaskDetail"
        uri = "/api/v1/dbtasks/{dbTaskId}".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = get_custom_dbtask_detail_pb2.GetCustomDBTaskDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_custom_db_task_rollback_info(self, request, org, user, timeout=10):
        # type: (get_custom_dbtask_rollbackinfo_pb2.GetCustomDBTaskRollbackInfoRequest, int, str, int) -> get_custom_dbtask_rollbackinfo_pb2.GetCustomDBTaskRollbackInfoResponse
        """
        获取自定义SQL变更任务的可回退信息
        :param request: get_custom_db_task_rollback_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_custom_dbtask_rollbackinfo_pb2.GetCustomDBTaskRollbackInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.GetCustomDBTaskRollbackInfo"
        uri = "/api/v1/dbtasks/{dbTaskId}/rollbackInfo".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = get_custom_dbtask_rollbackinfo_pb2.GetCustomDBTaskRollbackInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_sql_package_db_task_detail(self, request, org, user, timeout=10):
        # type: (get_sqlpkg_dbtask_detail_pb2.GetSQLPackageDBTaskDetailRequest, int, str, int) -> get_sqlpkg_dbtask_detail_pb2.GetSQLPackageDBTaskDetailResponse
        """
        获取SQL包变更任务详情
        :param request: get_sql_package_db_task_detail请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_sqlpkg_dbtask_detail_pb2.GetSQLPackageDBTaskDetailResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.GetSQLPackageDBTaskDetail"
        uri = "/api/v1/sqlpkg-dbtasks/{dbTaskId}".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = get_sqlpkg_dbtask_detail_pb2.GetSQLPackageDBTaskDetailResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def get_sql_package_db_task_rollback_info(self, request, org, user, timeout=10):
        # type: (get_sqlpkg_dbtask_rollbackinfo_pb2.GetSQLPackageDBTaskRollbackInfoRequest, int, str, int) -> get_sqlpkg_dbtask_rollbackinfo_pb2.GetSQLPackageDBTaskRollbackInfoResponse
        """
        获取SQL包变更任务的可回退信息
        :param request: get_sql_package_db_task_rollback_info请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: get_sqlpkg_dbtask_rollbackinfo_pb2.GetSQLPackageDBTaskRollbackInfoResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.GetSQLPackageDBTaskRollbackInfo"
        uri = "/api/v1/sqlpkg-dbtasks/{dbTaskId}/rollbackInfo".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = get_sqlpkg_dbtask_rollbackinfo_pb2.GetSQLPackageDBTaskRollbackInfoResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def liquibase_task_callback(self, request, org, user, timeout=10):
        # type: (liquibase_task_callback_pb2.LiquibaseTaskCallbackRequest, int, str, int) -> liquibase_task_callback_pb2.LiquibaseTaskCallbackResponse
        """
        变更任务结果回调
        :param request: liquibase_task_callback请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: liquibase_task_callback_pb2.LiquibaseTaskCallbackResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.LiquibaseTaskCallback"
        uri = "/api/v1/liquibase-tasks/callback"
        
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = liquibase_task_callback_pb2.LiquibaseTaskCallbackResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_custom_db_task_change_history(self, request, org, user, timeout=10):
        # type: (list_custom_dbtask_changehistory_pb2.ListCustomDBTaskChangeHistoryRequest, int, str, int) -> list_custom_dbtask_changehistory_pb2.ListCustomDBTaskChangeHistoryResponse
        """
        获取数据库服务下的自定义SQL任务的变更历史
        :param request: list_custom_db_task_change_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_custom_dbtask_changehistory_pb2.ListCustomDBTaskChangeHistoryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ListCustomDBTaskChangeHistory"
        uri = "/api/v1/dbservices/{dbServiceId}/custom/history".format(
            dbServiceId=request.dbServiceId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = list_custom_dbtask_changehistory_pb2.ListCustomDBTaskChangeHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_db_version(self, request, org, user, timeout=10):
        # type: (list_dbversions_pb2.ListDBVersionRequest, int, str, int) -> list_dbversions_pb2.ListDBVersionResponse
        """
        获取变更版本列表
        :param request: list_db_version请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_dbversions_pb2.ListDBVersionResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ListDBVersion"
        uri = "/api/v1/dbservices/{dbServiceId}/versions".format(
            dbServiceId=request.dbServiceId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = list_dbversions_pb2.ListDBVersionResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_sql_package_change_history(self, request, org, user, timeout=10):
        # type: (list_sqlpkg_changehistory_pb2.ListSQLPackageChangeHistoryRequest, int, str, int) -> list_sqlpkg_changehistory_pb2.ListSQLPackageChangeHistoryResponse
        """
        获取SQL包的变更历史
        :param request: list_sql_package_change_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_sqlpkg_changehistory_pb2.ListSQLPackageChangeHistoryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ListSQLPackageChangeHistory"
        uri = "/api/v1/sqlpkgs/{pkgId}/history".format(
            pkgId=request.pkgId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = list_sqlpkg_changehistory_pb2.ListSQLPackageChangeHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def list_sql_package_db_task_change_history(self, request, org, user, timeout=10):
        # type: (list_sqlpkg_dbtask_changehistory_pb2.ListSQLPackageDBTaskChangeHistoryRequest, int, str, int) -> list_sqlpkg_dbtask_changehistory_pb2.ListSQLPackageDBTaskChangeHistoryResponse
        """
        获取数据库服务下的SQL包任务的变更历史
        :param request: list_sql_package_db_task_change_history请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: list_sqlpkg_dbtask_changehistory_pb2.ListSQLPackageDBTaskChangeHistoryResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.ListSQLPackageDBTaskChangeHistory"
        uri = "/api/v1/dbservices/{dbServiceId}/sqlpkg/history".format(
            dbServiceId=request.dbServiceId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="GET",
            src_name="logic.database_delivery_sdk",
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
        rsp = list_sqlpkg_dbtask_changehistory_pb2.ListSQLPackageDBTaskChangeHistoryResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def retry_custom_db_task(self, request, org, user, timeout=10):
        # type: (retry_custom_dbtask_pb2.RetryCustomDBTaskRequest, int, str, int) -> retry_custom_dbtask_pb2.RetryCustomDBTaskResponse
        """
        重试自定义SQL变更任务
        :param request: retry_custom_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: retry_custom_dbtask_pb2.RetryCustomDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.RetryCustomDBTask"
        uri = "/api/v1/dbtasks/{dbTaskId}/retry".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = retry_custom_dbtask_pb2.RetryCustomDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def retry_sql_package_db_task(self, request, org, user, timeout=10):
        # type: (retry_sqlpkg_dbtask_pb2.RetrySQLPackageDBTaskRequest, int, str, int) -> retry_sqlpkg_dbtask_pb2.RetrySQLPackageDBTaskResponse
        """
        重试SQL包变更任务
        :param request: retry_sql_package_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: retry_sqlpkg_dbtask_pb2.RetrySQLPackageDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.RetrySQLPackageDBTask"
        uri = "/api/v1/sqlpkg-dbtasks/{dbTaskId}/retry".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = retry_sqlpkg_dbtask_pb2.RetrySQLPackageDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def rollback_custom_db_task(self, request, org, user, timeout=10):
        # type: (rollback_custom_dbtask_pb2.RollbackCustomDBTaskRequest, int, str, int) -> rollback_custom_dbtask_pb2.RollbackCustomDBTaskResponse
        """
        回退自定义SQL变更任务
        :param request: rollback_custom_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: rollback_custom_dbtask_pb2.RollbackCustomDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.RollbackCustomDBTask"
        uri = "/api/v1/dbtasks/{dbTaskId}/rollback".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = rollback_custom_dbtask_pb2.RollbackCustomDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
    def rollback_sql_package_db_task(self, request, org, user, timeout=10):
        # type: (rollback_sqlpkg_dbtask_pb2.RollbackSQLPackageDBTaskRequest, int, str, int) -> rollback_sqlpkg_dbtask_pb2.RollbackSQLPackageDBTaskResponse
        """
        回退SQL包变更任务
        :param request: rollback_sql_package_db_task请求
        :param org: 客户的org编号，为数字
        :param user: 调用api使用的用户名
        :param timeout: 调用超时时间，单位秒
        :return: rollback_sqlpkg_dbtask_pb2.RollbackSQLPackageDBTaskResponse
        """
        headers = {"org": org, "user": user}
        route_name = ""
        server_ip = self._server_ip
        if self._service_name != "":
            route_name = self._service_name
        elif self._server_ip != "":
            route_name = "easyops.api.database_delivery.dbtask.RollbackSQLPackageDBTask"
        uri = "/api/v1/sqlpkg-dbtasks/{dbTaskId}/rollback".format(
            dbTaskId=request.dbTaskId,
        )
        requestParam = request
        
        rsp_obj = utils.http_util.do_api_request(
            method="POST",
            src_name="logic.database_delivery_sdk",
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
        rsp = rollback_sqlpkg_dbtask_pb2.RollbackSQLPackageDBTaskResponse()
        
        google.protobuf.json_format.ParseDict(rsp_obj["data"], rsp, ignore_unknown_fields=True)
        
        return rsp
    
