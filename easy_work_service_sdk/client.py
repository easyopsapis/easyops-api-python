# -*- coding: utf-8 -*-

import easy_work_service_sdk.api.backlog.backlog_client

import easy_work_service_sdk.api.calendar_events.calendar_events_client

import easy_work_service_sdk.api.system_map.system_map_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.backlog = easy_work_service_sdk.api.backlog.backlog_client.BacklogClient(server_ip, server_port, service_name)
        
        self.calendar_events = easy_work_service_sdk.api.calendar_events.calendar_events_client.CalendarEventsClient(server_ip, server_port, service_name)
        
        self.system_map = easy_work_service_sdk.api.system_map.system_map_client.SystemMapClient(server_ip, server_port, service_name)
        
