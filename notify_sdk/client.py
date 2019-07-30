# -*- coding: utf-8 -*-

import api.oplog.oplog_client

import api.subscriber.subscriber_client

import api.subscriber_manager.subscriber_manager_client

import api.topic.topic_client



class Client(object):
    def __init__(self, server_ip="", server_port=0, service_name=""):
        
        self.oplog = api.oplog.oplog_client.OplogClient(server_ip, server_port, service_name)
        
        self.subscriber = api.subscriber.subscriber_client.SubscriberClient(server_ip, server_port, service_name)
        
        self.subscriber_manager = api.subscriber_manager.subscriber_manager_client.SubscriberManagerClient(server_ip, server_port, service_name)
        
        self.topic = api.topic.topic_client.TopicClient(server_ip, server_port, service_name)
        
